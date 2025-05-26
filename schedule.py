from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def create_study_events(service):
    schedule = [
        ("English Listening", 7, 0, 1),
        ("English Speaking & Grammar", 8, 0, 1),
        ("Chinese Reading & Writing", 9, 0, 1),
        ("Networking Fundamentals", 10, 0, 1),
        ("Cybersecurity Theory", 11, 0, 1),
        ("Lunch & Break", 12, 0, 1),
        ("Hacking Tools Practice", 13, 0, 1),
        ("Chinese Listening", 14, 0, 1),
        ("English Reading", 15, 0, 1),
        ("Practical Lab (TryHackMe)", 16, 0, 1),
        ("Flashcards Review", 17, 0, 1),
        ("Dinner & Rest", 18, 0, 1),
        ("Quiz or Recap Session", 19, 0, 1),
        ("YouTube Learning", 20, 0, 1),
        ("Journal Writing", 21, 0, 1),
    ]

    today = datetime.date.today()
    for title, hour, minute, duration in schedule:
        start = datetime.datetime(today.year, today.month, today.day, hour, minute).isoformat()
        end = (datetime.datetime(today.year, today.month, today.day, hour, minute) + datetime.timedelta(hours=duration)).isoformat()

        event = {
            'summary': title,
            'start': {'dateTime': start, 'timeZone': 'Asia/Yangon'},
            'end': {'dateTime': end, 'timeZone': 'Asia/Yangon'},
            'recurrence': ['RRULE:FREQ=DAILY'],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Created event: {title} at {start}")

if __name__ == '__main__':
    service = authenticate_google()
    create_study_events(service)
