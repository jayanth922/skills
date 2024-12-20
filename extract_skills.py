import spacy
from spacy.matcher import PhraseMatcher
from skillNer.skill_extractor_class import SkillExtractor
from skillNer.general_params import SKILL_DB

# Initialize SkillNER
nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

def extract_skills_from_job(job):
    """Extract skills from a single job description."""
    description = job.get("description", "")
    if not description.strip():
        print("DEBUG: Empty job description found!")
        return []

    try:
        annotations = skill_extractor.annotate(description)
        full_matches = annotations.get("results", {}).get("full_matches", [])
        extracted_skills = [match["doc_node_value"] for match in full_matches]
        return extracted_skills
    except Exception as e:
        print(f"DEBUG: Error processing job description: {e}")
        return []

def extract_skills_from_jobs(jobs):
    """Extract skills from a list of job descriptions."""
    all_skills = []
    for job in jobs:
        description = job.get("description", "")
        if not description.strip():
            print("DEBUG: Skipping job with empty description.")
            continue
        all_skills.extend(extract_skills_from_job(job))
    return all_skills
