# First deployment at Meeting 5; final deployment at Meeting 9

Deploy your **completed student app**. If demonstrating the full instructor copy, its entry point can be `instructor/week3/chatbot.py`. A TODO starter is not a completed app.

1. Run and verify locally using docs/ACCEPTANCE.md.
2. Push reviewed code to your GitHub repository. Include `requirements.txt`, `pyproject.toml`, `coursekit/` and sample data. Never commit real secrets.
3. In Streamlit Community Cloud, choose your repository, branch and exact entry file (for example `week3/chatbot.py`). Select Python **3.12** to match this course.
4. In deployment advanced settings / app secrets, start with:

```toml
APP_MODE = "demo"
```

5. Deploy. Open the URL on another device and check the demo label.
6. For real AI, configure APP_MODE, OPENAI_API_KEY and OPENAI_MODEL in the platform's secrets settings using SETUP.md. The deployed app does not inherit the variables on your laptop.
7. Test one short request, a follow-up and reset. Check application logs without exposing secrets.
8. Push a small change and verify the deployed app updates. This demonstrates automatic deployment; it is not proof of a complete production CI/CD process.

## Cost and access

Public visitors can spend the configured account's API credit in live mode. The example bounds question length, history, output tokens and attempts per session. A session limit can be bypassed by opening a new session: it is not authentication, an account-wide quota or a hard spending cap. Before sharing live mode widely, add suitable access controls and provider-side usage controls, and monitor usage. Otherwise publish the demo version for class review. No API key is accepted from visitors in this implementation.

## Deployment failures

- Missing `coursekit`: ensure root requirements include `-e .`, pyproject.toml is committed and the repo root is used.
- Missing dependency: compare Python and package versions with the tested setup.
- No useful answer: check mode, model access and service errors; consult the mentor.
- Upload schema error: use the documented sales CSV or sample toggle.

**My live URL:**
**Entry file:**
**Mode tested:**
**Date and reviewer:**

[Streamlit deployment documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
[Secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
