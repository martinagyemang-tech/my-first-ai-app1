
# Python for Everybody with AI - Level 1
=======
# 🚀 My First AI App 


**CloudWithShad | Get Skills Network | Shadrack Darku**

From Python notebooks to a working, deployed AI application.
=======
**👤 Name:** Shadrack Darku
**📅 Cohort:** July 2026
**🔗 My live app:** _(paste your .streamlit.app link here when you deploy in Week 5!)_


**Student:** add your name. **Cohort:** add your cohort. **Live app:** add your URL.

## Start here

1. Follow [SETUP.md](SETUP.md). Use Python 3.12 and a virtual environment.
2. Read the [10-meeting roadmap](docs/ROADMAP.md).
3. Follow [the lab guide](docs/LABS.md), one small feature at a time.
4. Complete the guided apps individually; form capstone groups of three around Meeting 5.
5. Read [the capstone brief](capstone/README.md) before planning your group project.

The existing `week2`, `week3` and `week4` paths are retained to preserve course links. They now represent **build milestones**, not a restart of the notebook timetable. Only the three original Week 1 notebooks are present here. Additional course notebooks remain separately distributed; they have not been invented or silently replaced.

## Student starters versus instructor solutions

- `week2/`, `week3/`, `week4/`, `capstone/`: intentionally unfinished student starters. They open without a key and tell you what to implement.
- `instructor/`: complete runnable reference apps and facilitator notes. Do your attempt before consulting a solution.
- `coursekit/`: small, readable helpers for exact calculations, validated CSVs, AI calls and shared UI. Read these as the course progresses.
- `tests/`: checks for calculations, invalid inputs and the AI boundary. Full instructor copies also check UI behaviour.

An instructor folder in a public GitHub repo is **not private**. To distribute a student-only copy, use `python tools/export_students.py`; see [instructor/README.md](instructor/README.md).

## Launch after setup

Student starter:

```bash
python -m streamlit run week2/app.py
```

Complete reference (full instructor copy):

```bash
python instructor/week2/market_basics.py
python instructor/week2/assistant.py
python -m streamlit run instructor/week2/app.py
```

Run commands separately. Stop a running web app with Ctrl+C before starting another.

Default **demo mode** returns clearly labelled fixed responses. It makes no API requests and is not real AI. Live mode requires an instructor-approved model ID and your own configured API key. See SETUP.md.

## Progress

- [ ] M1: local script, environment and Git checkpoint
- [ ] M2: terminal assistant and first AI request
- [ ] M3: first Streamlit app
- [ ] M4: chatbot memory and reset
- [ ] M5: persona controls, first deployment, group formation
- [ ] M6: validated data dashboard
- [ ] M7: questions about calculated data facts
- [ ] M8: capstone skeleton and reviewed pull request
- [ ] M9: working capstone, tests and deployment
- [ ] M10: demo and individual explanation

## What counts as finished?

A useful app, a readable repository, checked inputs and failure states, a working deployment, and an explanation of your own contribution. See [acceptance checks](docs/ACCEPTANCE.md).

The stack is Python, Streamlit, OpenAI, pandas and Git/GitHub. This is a learning app, not a hardened public AI service. Read the deployment guide before enabling billable AI for visitors.
