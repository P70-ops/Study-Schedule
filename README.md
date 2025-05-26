# Study-Schedule

🔧 1. Install Required Python Packages:
        pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


🔐 2. Enable Google Calendar API

        Go to: https://console.cloud.google.com/

        Create a new project (or use existing one)

        Go to APIs & Services > Library

        Search for Google Calendar API and click Enable

        Go to Credentials > Create Credentials > OAuth client ID

        Choose: Desktop App

        Download the credentials.json file

        Place credentials.json in the same folder as your Python script

🟩 Result:

      After running this:
      
      Your Google Calendar will be filled with daily study blocks
      
      Each will repeat daily
      
      You can customize times, durations, and titles
