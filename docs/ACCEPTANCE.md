# Acceptance checks

A demo response is not proof of live AI success. Check the selected mode and record what was actually tested.

## Every app
- Opens without an API key in demo mode; demo is visibly labelled.
- Blank input produces guidance, not an exception.
- A deliberate live-mode attempt without key/model produces a readable error.
- No key appears in Git changes, output or screenshots.
- A failed API call does not replace a valid state with a misleading success.
- An explicit user action triggers each request; widget changes do not make surprise calls.

## Market apps
- 3 yams -> GHS 24.00; product lookup ignores surrounding spaces/case.
- Unknown product, zero, negative or non-whole quantity rejected.
- Exact amount shown from Python independently of generated prose.

## Chat/persona
- History contains alternating successful user/assistant turns.
- New conversation clears history; persona changes clear old context.
- Latest five exchanges retained; long prompts rejected.
- In live mode, a follow-up makes use of recent context. Demo is not used to judge model reasoning.

## Data apps
- Sample: 8 rows; 885 units; 11,680 revenue; Accra revenue 6,610.
- Empty CSV, duplicate/missing headers, malformed rows, negative values, NaN/infinity and files above the limits rejected.
- Required columns are explicit; extra columns are not sent to the AI.
- New facts clear old AI output. Changing dimensions changes the summary.
- Ask about absent dates/profit/causes; compare the reply with the evidence.

## Deployment/capstone
- Live URL opens in another browser; deployed entry point is the completed app.
- Restart/reload expectations are documented: session history is not a database.
- README says which model/mode was tested, features and limitations (never the key).
- Each person can trace one request end to end and explain their contribution.

## Automated checks

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Tests use demo mode or mocked API responses, never paid requests. Complete the manual live-model and deployment checks with your own authorised configuration before teaching live mode.
