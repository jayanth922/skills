from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
GOOGLE_DOC_ID = os.getenv("GOOGLE_DOC_ID")

def write_to_google_docs(text):
    """Write the aggregated skills to a Google Docs document."""
    SCOPES = ['https://www.googleapis.com/auth/documents']
    creds = Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_JSON, scopes=SCOPES)
    service = build("docs", "v1", credentials=creds)

    # Update document content
    requests = [{"insertText": {"location": {"index": 1}, "text": text}}]
    service.documents().batchUpdate(documentId=GOOGLE_DOC_ID, body={"requests": requests}).execute()
