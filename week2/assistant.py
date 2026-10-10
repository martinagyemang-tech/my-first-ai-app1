"""Meeting 2 starter. python week2/assistant.py. See docs/LABS.md."""
from coursekit.ai import reply, AIError
from coursekit.market import quote, receipt


def ask_assistant(question):
    # TODO: reject blank input; build a list with one user message.
    # TODO: call reply(messages, instructions), then return its text.
    # Demo mode is the default: it does not call AI.
    raise NotImplementedError('Complete ask_assistant in Meeting 2.')


if __name__ == '__main__':
    try:
        print(ask_assistant(input('Your question: ')))
    except (NotImplementedError, AIError) as exc:
        print(exc)
