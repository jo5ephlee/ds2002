from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os

# Load secret token from .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Mapping of capitals to IANA time zones
TZ = {
    "Washington":  "America/New_York",
    "Austin":      "America/Chicago",
    "Denver":      "America/Denver",
    "Sacramento":  "America/Los_Angeles",
    "Juneau":      "America/Juneau",
    "Honolulu":    "Pacific/Honolulu",
    "London":      "Europe/London",
    "Paris":       "Europe/Paris",
    "Tokyo":       "Asia/Tokyo",
    "Canberra":    "Australia/Sydney",
    "Seoul":       "Asia/Seoul",
    "New Delhi":   "Asia/Kolkata",
    "Brasilia":    "America/Sao_Paulo"
}

app = Flask(__name__)

# Token authentication decorator
def token_required(f):
    def decorator(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth.split()[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

# Time endpoint
@app.route("/api/time/<capital>", methods=["GET"])
@token_required
def capital_time(capital):
    tz_name = TZ.get(capital)
    if not tz_name:
        return jsonify({"error": f"{capital} not in our database"}), 404

    now = datetime.now(ZoneInfo(tz_name))
    offset = now.utcoffset()
    hh = int(offset.total_seconds() // 3600)
    mm = int((abs(offset.total_seconds()) % 3600) // 60)
    utc_offset = f"{hh:+03d}:{mm:02d}"

    return jsonify({
        "capital":    capital,
        "local_time": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "utc_offset": utc_offset
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)