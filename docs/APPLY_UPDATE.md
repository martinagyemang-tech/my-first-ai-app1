# Apply this prepared update

This package has not been pushed to GitHub. It contains no `.git` directory, credentials or virtual environment.

1. Save/commit unfinished changes in your existing clone.
2. Create a review branch: `git switch -c course/level1-build-stage`.
3. Extract this package elsewhere. Copy its contents into that clone, including `.gitignore`, `.github/` and `.streamlit/`. Never replace the clone's `.git` directory. This updates starters/docs, so preserve any local learner changes before copying.
4. Follow SETUP.md and run the acceptance checks.
5. Review `git status`, `git diff --stat` and `git diff`.
6. Decide whether to publish full instructor files or a student-only version. Run `python tools/export_students.py` for the latter. If a repo already tracks solutions, omitting them from a ZIP does not delete tracked copies or erase history.
7. Stage reviewed files only, commit, push the branch, and open a pull request. Do not stage real secrets.

Source revision: `5343a610a4da2c6f3e3ed8c28bc365c2ad04742a`.

Original Week 1 material and the sample CSV remain. Assignment checks now safely handle unanswered placeholders; question prompts are unchanged. Other notebooks distributed separately were not in the source repository and have not been fabricated.
