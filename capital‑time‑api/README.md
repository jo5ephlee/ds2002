Capital-Time API
A simple Flask API that returns the current local time and UTC offset for a given capital city, protected by a Bearer token.

Prerequisites
Python 3.8+
pip
A GitHub account (for your repo)
A GCP VM with port 5000 opened to the public

Setup
Clone the repo
git clone https://github.com/jo5ephlee/ds2002.git
cd ds2002/capital-time-api

Create a virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure your token
Copy .env.example to .env:
cp .env.example .env
Edit .env and replace your_token_here with your actual secret token (e.g. supersecrettoken123).

Running the API
source venv/bin/activate
python3 app.py

The server listens on 0.0.0.0:5000.

Endpoint
GET /api/time/<capital>
Headers:
  Authorization: Bearer <YOUR_TOKEN>
Responses:
  200 OK
    {
      "capital": "Paris",
      "local_time": "2025-04-21T22:15:30",
      "utc_offset": "+02:00"
    }
  401 Unauthorized
    { "error": "Unauthorized" }
  404 Not Found
    { "error": "Atlantis not in our database" }

Testing with curl
Unauthorized
curl http://35.199.37.173:5000/api/time/Paris

Not found
curl -H "Authorization: Bearer supersecrettoken123" http://35.199.37.173:5000/api/time/Atlantis

Success
curl -H "Authorization: Bearer supersecrettoken123" http://35.199.37.173:5000/api/time/Paris
