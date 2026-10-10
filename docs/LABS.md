# Guided build guide

Use SETUP.md first. All commands run from the repository root, with the environment selected. Student files contain TODOs; completed references are under the same path inside `instructor/` in the instructor package.

## Meeting 1 - from notebooks to scripts

Open `week2/market_basics.py`. Predict `calculate_total(8, 3)`, then implement it. A positive whole quantity is required. Print a result, run the file, and intentionally try zero and a string. Read the final traceback line, find the failing code and correct it.

```bash
python week2/market_basics.py
```

Next create a price dictionary and a function that checks the product name. Use familiar functions first. Then read `coursekit/market.py`: `strip().lower()` normalises the product; `Decimal` keeps money arithmetic exact; `quote()` returns a dictionary; `receipt()` formats it. Explain why calculation and display are separate.

Checkpoint: three yams at GHS 8 each cost GHS 24. Unknown products and zero quantity are rejected. Student changes one value and can predict the result. Commit only the intended files.

## Meeting 2 - one AI request

Implement `week2/assistant.py`. The input is a string. The request uses a list of dictionaries, such as `[{"role": "user", "content": question}]`. Read `coursekit/ai.py` together: configuration -> validation -> optional demo response -> client -> request -> output -> handled failure.

The implementation uses `client.responses.create(...)`. `instructions` describes the assistant's job; `input` is the conversation; `output_text` holds returned text. This replaces the older Chat Completions TODO in the original starter. Keep the reusable function; do not introduce multiple API styles during this first build.

```bash
python week2/assistant.py
```

Start in demo mode and identify the fixed-response label. Enable live mode only after setup. The model explains a quote calculated by Python; it must not be treated as the calculator or as evidence of real inventory.

Checkpoint: blank question handled, key/model configuration understood, no raw key printed, failure message readable.

## Meeting 3 - give the assistant a web interface

```bash
python -m streamlit run week2/app.py
```

Build title -> form -> selectbox/number_input/text_input -> submit button -> result. Use `quote()` for the exact amount. Call AI only after submission and a non-empty question. Save results in `st.session_state` so another rerun does not erase them.

Demonstrate that changing a widget can rerun a Streamlit script. Ask why a paid API call should not sit unconditionally at top level. A form batches input until submission.

Checkpoint: changing a widget does not make an unsolicited AI call. The result and empty-input behaviour are understandable to another learner.

## Meeting 4 - memory

Before the chat loop, make a tiny counter. First use `count = 0`, observe the reset, then initialise `st.session_state.count` only if it does not exist. This establishes the reason for the guard.

Build `week3/chatbot.py`: initialise history -> replay messages -> capture input -> request using history -> append successful user and assistant messages. Keep five recent exchanges. Explain that this is bounded session history, not permanent storage or model training. On failure, do not save an incomplete turn. Add a reset button; it should not reset the request counter.

Checkpoint: ask a follow-up in live mode; show the history structure in class; start a new conversation. Demo mode can show message counts but cannot answer as a real model.

## Meeting 5 - controls and first deployment

Build a persona dictionary and sidebar controls in `week3/persona_bot.py`. Show the constructed instructions. Reset conversation when persona/tone/detail changes so old context does not silently conflict with the new choices. We use answer-detail instructions, not a temperature slider that some models may reject.

Deploy the basic chatbot first using week5/DEPLOY.md. Persona changes can follow after the simple app is live. Form capstone groups and select a narrow problem.

## Meeting 6 - verified data before AI

Teach `week4/dashboard.py` **before** `data_chat.py`. The supplied sales schema is product, region, units, revenue. Uploading a random spreadsheet is outside this first exercise.

Read `coursekit/sales.py`: decode -> parse -> check headers/rows -> validate numbers -> group -> summarise. Explain every rejection. The sample has 8 rows, 885 units and revenue 11,680. No currency is inferred from the CSV. Chart by product or region; choose units or revenue. Check totals manually before adding AI.

Then add an explicit Explain button. Only the computed totals and up to 20 grouped values are sent. Display those facts. Clear an old explanation when source facts or chart selections change.

## Meeting 7 - questions about bounded facts

Build `week4/data_chat.py` using the same validated data and summary. Show the facts first. Ask for the largest shown group, then ask about a date or cause that is absent. The instruction asks the model to admit insufficient evidence. This is helpful guidance, not a mathematical guarantee that a model will comply: compare its claims with the displayed facts.

Do not send arbitrary full files, claim unlimited spreadsheet analysis or execute model-generated Python. The bounded lesson prepares students to understand later retrieval/tool workflows without adding them now.

## Meetings 8-10 - group application

Use the capstone brief. Start with one complete workflow and then add at most two extras. Use branches and reviewed pull requests. During the clinic, run docs/ACCEPTANCE.md on a teammate's machine/browser. Every member presents a contribution, an error they solved and a remaining limitation.
