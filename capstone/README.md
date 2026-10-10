# Level 1 group capstone

Work in groups of **three** after completing the guided apps individually. Form teams around Meeting 5. Each person writes code, opens a pull request, reviews a teammate's change and explains their contribution.

## Choose one small problem

- Assistant: a study planner, interview-practice helper or a bounded business-enquiry assistant.
- Data analyst: validated sales data, verified calculations/charts and an AI explanation or bounded Q&A.

Document-search/knowledge-bot projects need an additional guided retrieval lesson and mentor approval of scope; they are not assumed to be covered by the current labs.

**Project name:**
**Members and GitHub usernames:**
**User:**
**Problem in one sentence:**
**Live URL:**

| Planning question | Our answer |
|---|---|
| What goes in? | |
| What comes out? | |
| Which part is exact Python logic? | |
| Which part benefits from AI? | |
| What context is sent outside the app? | |
| What can the app NOT do? | |
| Core feature and at most two extras | |
| How will we prove it works? | |

## Collaboration

Use one group repository. Agree small issues, work on branches and review pull requests. Rotate logic/AI, interface, and testing/deployment responsibilities rather than permanently assigning one person to slides. Each person owns an identifiable coded feature and reviews another feature. Evaluate actual work and explanations, not commit or line counts.

Suggested branch workflow (example name):

```bash
git switch main
git pull
git switch -c feature/input-validation
# edit and test
git status
git diff
git add path/to/changed_file.py
git commit -m "Validate user input"
git push -u origin feature/input-validation
```

Replace the example file path. Open a pull request on GitHub, request a teammate review and merge after resolving feedback. Pull the updated main before starting the next feature.

## Assessment

| Component | Marks |
|---|---:|
| Team: useful, scoped core workflow | 20 |
| Team: correct calculations and responsible AI use | 15 |
| Team: validation and understandable failures | 10 |
| Team: working deployment | 10 |
| Team: README and demonstration | 5 |
| Individual: identifiable implementation contribution | 15 |
| Individual: explanation of code and design | 10 |
| Individual: debugging and checking evidence | 10 |
| Individual: peer review and collaboration | 5 |
| Total | 100 |

Team work contributes 60%; individual evidence contributes 40%.

## Submission and presentation

- Working app URL, group repository and completed README.
- Acceptance checklist with test results and remaining limitations.
- Contribution table linking each member's feature and reviewed PR.
- A 60-second backup demo recording.
- A seven-minute group presentation: each member explains a contribution and the team demonstrates the core workflow.

The instructor example `instructor/capstone/app.py` demonstrates a small study-planning app. Choose and implement your own variation; merely renaming it is not an independent capstone.
