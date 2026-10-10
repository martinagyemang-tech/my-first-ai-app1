# Validation record

Prepared 10 October 2026 from source revision `5343a610a4da2c6f3e3ed8c28bc365c2ad04742a`.

## Passed locally

- Python 3.12 isolated virtual environment; editable local package installation.
- Dependency compatibility check (`python -m pip check`).
- **44 pytest checks passed**: exact quote maths, invalid inputs, sales validation and totals, demo mode, configuration errors, bounded context, empty/incomplete replies, connection failures, and provider 401/429/500 errors.
- Real installed OpenAI SDK exercised using an in-memory HTTP transport; request shape and response extraction verified without contacting the provider.
- Streamlit AppTest checks: all six web starters open without a key; completed market app, chatbot, persona app, dashboard, data Q&A and capstone interactions; reset and invalidation behaviour; session attempt limit.
- Terminal Market Assistant run with 3 yams: GHS 24.00 and labelled demo response.
- Original assignment notebook's unfilled code/check cells executed without crashing.

## Not claimed

No live paid model request, account/model access verification, semantic AI evaluation, Windows execution, GitHub Actions run or Streamlit Cloud deployment was performed. The included Windows instructions and CI/deployment configuration require confirmation in your teaching environment. A mentor should complete the short live-mode and deployment acceptance checks before class.

Direct versions tested: Streamlit 1.65.0, OpenAI 3.28.0, pandas 3.0.6, pytest 9.1.1. Python 3.12 is the documented runtime.
