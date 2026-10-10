# Set up once; understand every step

Use **Python 3.12**, Git and VS Code. This release is tested on Python 3.12; use that version for a consistent cohort environment.

## 1. Your own repository

On the course GitHub page use **Use this template** if available. If it is not shown, use **Fork**. Name your copy `my-first-ai-app`. Clone **your copy**, not the instructor's repository:

```bash
git clone https://github.com/YOUR-USERNAME/my-first-ai-app.git
cd my-first-ai-app
code .
```

Replace YOUR-USERNAME. If you received a ZIP, extract it and open the folder containing README.md in VS Code. See docs/APPLY_UPDATE.md for applying this package to an existing repository without losing its Git history.

## 2. Create an isolated Python environment

An environment gives this project its own installed libraries. Run these commands in the VS Code terminal, from the repo root.

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If activation is blocked by your computer's policy, do not change the policy just for this lesson. Use the interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run week2/app.py
```

Windows Git Bash (after creating `.venv`):

```bash
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

macOS/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

In VS Code choose **Python: Select Interpreter** and select the interpreter inside `.venv`. `-e .` in requirements installs this repository's `coursekit` helpers so imports work from different lab folders. Re-run installation when you move the repository to a new location.

Check the actual interpreter and packages:

```bash
python --version
python -c "import sys; print(sys.executable)"
python -c "import streamlit, openai, pandas, coursekit; print('Imports OK')"
```

## 3. Run without a key first

```bash
python week2/market_basics.py
python -m streamlit run week2/app.py
```

The first starter asks you to finish a function. The second opens a checklist in your browser. That is intentional, not a failed installation. In the instructor copy, use `instructor/week2/market_basics.py` or `instructor/week2/app.py` to see finished versions.

`python file.py` runs a script. `python -m streamlit run file.py` starts a web app server. Keep the terminal running; Ctrl+C stops it.

## 4. Enable real AI deliberately

The mentor chooses a currently accessible, text-capable **Responses API** model and verifies its cost and account access before class. No model ID is silently selected. The app uses a 600-token output limit; some reasoning models may need a different setting. Review this with the mentor, not by removing all limits.

For web apps, copy `.streamlit/secrets.example.toml` to `.streamlit/secrets.toml` using VS Code. Edit the private file:

```toml
APP_MODE = "openai"
OPENAI_API_KEY = "YOUR_PRIVATE_KEY"
OPENAI_MODEL = "YOUR_INSTRUCTOR_APPROVED_MODEL_ID"
```

Restart the app. Do not paste the real values into source code, chat, screenshots or commits.

For terminal scripts, set environment variables in the same terminal. These are placeholders:

PowerShell:

```powershell
$env:APP_MODE="openai"
$env:OPENAI_API_KEY="YOUR_PRIVATE_KEY"
$env:OPENAI_MODEL="YOUR_INSTRUCTOR_APPROVED_MODEL_ID"
```

macOS/Linux/Git Bash:

```bash
export APP_MODE="openai"
export OPENAI_API_KEY="YOUR_PRIVATE_KEY"
export OPENAI_MODEL="YOUR_INSTRUCTOR_APPROVED_MODEL_ID"
```

Check only whether configuration exists, never print the key:

```bash
python -c "import os; print('Key configured:', bool(os.getenv('OPENAI_API_KEY'))); print('Model configured:', bool(os.getenv('OPENAI_MODEL')))"
```

Terminal scripts read environment variables, **not** Streamlit secrets. Web apps prefer Streamlit secrets, then environment variables. `.env` files are ignored by Git but are **not automatically loaded** by this application. Demo mode is selected when APP_MODE is absent or set to `demo`.

## 5. Save a meaningful checkpoint

```bash
git status
git diff
git add README.md
git commit -m "Personalise my learning repository"
git push
```

Review file names and changes before staging. `.gitignore` excludes matching untracked files; it does not remove files already tracked and cannot protect a key pasted into `.py` code. If a key is exposed, revoke it at the provider, create a replacement and tell the mentor. Removing a line alone does not erase Git history.

## Troubleshooting

| Symptom | Check |
|---|---|
| Python not found | Confirm Python 3.12 installation; reopen the terminal. On Windows try `py -3.12`. |
| `No module named coursekit` | Run the requirements install from the repo root using the same interpreter you use to launch. |
| Streamlit cannot find the file | Use the repo root as your working directory; check spelling. |
| Starter shows TODOs | Expected. Implement the lab, or launch the instructor reference. |
| Demo message instead of AI | Demo is intentional. Configure both key/model and APP_MODE for live mode. |
| Key works in CLI but not web | Check whether a local secrets file overrides environment values. |
| Authentication/model error | Check key and model access privately; never paste credentials into an issue. |
| Git push asks for login | Use your supported GitHub sign-in/credential flow; do not use your account password as a Git token. |

[Official Python venv guidance](https://docs.python.org/3/library/venv.html)
