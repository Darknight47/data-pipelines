import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("RAPIDAPI_HOST")

url = "https://nfl-api-data.p.rapidapi.com/nfl-team-listing/v1/data"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": API_HOST,
    "x-rapidapi-key": API_KEY
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

# timestamped filename
timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")

# saving the RAW data.
output_dir = Path("project02/data/bronze/nfl_teams")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / f"{timestamp}.json"

with open(output_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved raw data to {output_file}")