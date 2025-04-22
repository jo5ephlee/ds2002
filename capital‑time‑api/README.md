# Capital-Time API

A simple Flask API that returns the current local time and UTC offset for a given capital city, protected by a Bearer token.

## Prerequisites

- Python 3.8+  
- pip  
- A GitHub account (for your repo)  
- A GCP VM with port 5000 opened to the public  

## Setup

1. Clone the repo  
   git clone https://github.com/your-username/capital-time-api.git  
   cd capital-time-api

2. Create a virtual environment & install dependencies  
   python3 -m venv venv  
   source venv/bin/activate  
   pip install -r requirements.txt

3. Configure your token  
   Copy .env.example to .env:  
     cp .env.example .env  
   Edit .env and replace your_token_here with your actual secret token.

## Running the API

source venv/bin/activate  
python3 app.py

The server listens on 0.0.0.0:5000.

## Endpoint

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

## Testing with curl

# Unauthorized  
curl http://<IP>:5000/api/time/Paris

# Not found  
curl -H "Authorization: Bearer YOUR_TOKEN" http://<IP>:5000/api/time/Atlantis

# Success  
curl -H "Authorization: Bearer YOUR_TOKEN" http://<IP>:5000/api/time/Paris
