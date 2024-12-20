import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
THEIRSTACK_API_KEY = os.getenv("THEIRSTACK_API_KEY")

def fetch_jobs():
    """Fetch job descriptions from TheirStack API."""
    url = "https://api.theirstack.com/v1/jobs/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {THEIRSTACK_API_KEY}",
    }
    payload = {
        "page": 0,
        "limit": 5,
        "order_by": [{"desc": True, "field": "date_posted"}],
        "include_total_results": False,
        "blur_company_data": False,
        "job_title_pattern_or": [
            "Data Science Intern",
            "Software Engineer Intern",
            "AI Intern",
            "Machine Learning Intern",
            "Backend Intern",
            "Full Stack Intern"
        ],
        "job_country_code_or": ["US"],
        "posted_at_max_age_days": 1
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Jobs fetched successfully!")
        return response.json().get("data", [])
    else:
        print(f"Error fetching jobs: {response.status_code} - {response.text}")
        return []
