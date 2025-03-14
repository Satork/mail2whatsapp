import os
import pickle
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authenticates the Gmail API and saves the token."""
    creds = None

    # Load token if exists
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If no valid credentials, authenticate user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

# Authenticate and test
if __name__ == "__main__":
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)
    print("Authentication successful!")
