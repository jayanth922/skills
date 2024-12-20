from fetch_jobs import fetch_jobs
from extract_skills import extract_skills_from_jobs
from write_to_docs import write_to_google_docs
from collections import Counter

def main():
    # Step 1: Fetch job descriptions
    print("Fetching job descriptions...")
    jobs = fetch_jobs()

    if not jobs:
        print("No jobs fetched.")
        return

    # Step 2: Extract skills
    print("Extracting skills from job descriptions...")
    skills = extract_skills_from_jobs(jobs)

    # Step 3: Count and rank skills
    skill_counts = Counter(skills)
    top_skills = skill_counts.most_common(10)
    formatted_skills = "\n".join([f"{skill}: {count}" for skill, count in top_skills])

    # Step 4: Write to Google Docs
    print("Writing top skills to Google Docs...")
    write_to_google_docs(f"Top Skills:\n{formatted_skills}")

if __name__ == "__main__":
    main()
