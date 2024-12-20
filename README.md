# Job Skills Extractor & Analysis

Want to know the latest skills being asked by job recruiters? Here is the place!, This is a Python-based project to extract, analyze, and aggregate key skills and technologies from job descriptions in the tech domain. The extracted skills are written to a Google Docs document for easy reference. This project runs daily using GitHub Actions as a cron job.

---

## Features
- Fetches job descriptions using the [TheirStack API](https://api.theirstack.com/).
- Extracts relevant skills and technologies from job descriptions using **SkillNER**.
- Aggregates top skills and writes them to Google Docs using the **Google Docs API**.
- Automates the process with GitHub Actions.

---
