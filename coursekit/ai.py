"""One API boundary, explicit demo mode, no calls during import.

OPENAI_MODEL is configured by the instructor, not silently selected here.
Demo output is deliberately labelled and is NOT model-generated.
"""
import os
from collections.abc import Mapping


class AIError(Exception):
    """A readable error suitable for the classroom UI; never contains a key."""


def settings(overrides: Mapping | None = None) -> dict:
    values = overrides or {}
    return {name: str(values.get(name, os.getenv(name, default))).strip()
            for name, default in (("APP_MODE", "demo"), ("OPENAI_API_KEY", ""),
                                  ("OPENAI_MODEL", ""))}


def reply(messages: list[dict], instructions: str, config=None, client=None) -> str:
    config = settings(config)
    if not messages or messages[-1].get("role") != "user":
        raise AIError("Enter a question first.")
    for message in messages:
        if (message.get("role") not in {"user", "assistant"}
                or not isinstance(message.get("content"), str)
                or not message['content'].strip()):
            raise AIError("Messages need a role and non-empty text.")
    if len(messages[-1]['content']) > 1000:
        raise AIError("Keep your question to 1,000 characters or fewer.")
    # Last five complete exchanges plus this question: bounded teaching context.
    context = messages[-11:]
    if config['APP_MODE'] == 'demo':
        turns = sum(m['role'] == 'user' for m in context)
        return (f"[DEMO - no AI request] Received your question: "
                f"{context[-1]['content'][:200]}\n\n"
                f"The request contains {turns} user message(s). "
                "This is a fixed practice response, not an AI answer.")
    if config['APP_MODE'] != 'openai':
        raise AIError("APP_MODE must be demo or openai.")
    if not config['OPENAI_API_KEY'] or not config['OPENAI_MODEL']:
        raise AIError("Live mode needs OPENAI_API_KEY and OPENAI_MODEL. See SETUP.md.")
    from openai import OpenAI, APIConnectionError, APIStatusError, AuthenticationError, RateLimitError
    owned_client = client is None
    try:
        if owned_client:
            client = OpenAI(api_key=config['OPENAI_API_KEY'], timeout=25.0, max_retries=0)
        response = client.responses.create(
            model=config['OPENAI_MODEL'], instructions=instructions,
            input=context, max_output_tokens=600, store=False,
        )
        if getattr(response, 'status', None) == 'incomplete':
            raise AIError("The response reached its limit. Ask a shorter question or ask your mentor to review the model configuration.")
        answer = response.output_text.strip()
        if not answer:
            raise AIError("The service returned no text. Try another question.")
        return answer
    except AuthenticationError:
        raise AIError("Authentication failed. Check your key privately.") from None
    except RateLimitError:
        raise AIError("The request was limited. Check account usage and try later.") from None
    except APIConnectionError:
        raise AIError("Could not reach the AI service. Check your connection and try again.") from None
    except APIStatusError:
        raise AIError("The AI request failed. Check model access and provider status; ask your mentor if it continues.") from None
    finally:
        if owned_client and client is not None:
            client.close()
