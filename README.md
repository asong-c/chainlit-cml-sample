# Sample Chainlit in CML

## Instuctions

- Import this github repo as a CML project
- Create a CML Application within that project
  - Set a reasonable subdomain
  - Select start-app.py as launch script
  - Select a PBJ / Workbench Python Kernel as runtime
  - Launch!

> Note: in this mini example the pip install of chainlit happens directly in the start-app.py script, this not good practice. It would be better to use a requirements.txt file with pinned versions and install dependencies only once for a project in a CML session.
