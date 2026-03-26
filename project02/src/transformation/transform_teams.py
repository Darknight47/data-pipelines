import json
import pandas as pd
from pathlib import Path

# Paths
bronze_path = Path("project02/data/bronze/nfl_teams")
silver_base = Path("project02/data/silver")

teams_out = silver_base / "teams"
logos_out = silver_base / "team_logos"
links_out = silver_base / "team_links"

teams_out.mkdir(parents=True, exist_ok=True)
logos_out.mkdir(parents=True, exist_ok=True)
links_out.mkdir(parents=True, exist_ok=True)

# Read latest bronze file
latest_file = sorted(bronze_path.glob("*.json"))[-1]

with open(latest_file, "r") as f:
    raw_data = json.load(f)

teams_list = []
logos_list = []
links_list = []

for item in raw_data:
    team = item["team"]

    # -------- teams table --------
    teams_list.append({
        "team_id": team.get("id"),
        "slug": team.get("slug"),
        "abbreviation": team.get("abbreviation"),
        "display_name": team.get("displayName"),
        "nickname": team.get("nickname"),
        "location": team.get("location"),
        "color": team.get("color"),
        "alternate_color": team.get("alternateColor"),
        "is_active": team.get("isActive"),
        "is_all_star": team.get("isAllStar")
    })

    # -------- logos table --------
    for logo in team.get("logos", []):
        logos_list.append({
            "team_id": team.get("id"),
            "href": logo.get("href"),
            "width": logo.get("width"),
            "height": logo.get("height"),
            "rel": ",".join(logo.get("rel", []))
        })

    # -------- links table --------
    for link in team.get("links", []):
        links_list.append({
            "team_id": team.get("id"),
            "href": link.get("href"),
            "text": link.get("text"),
            "short_text": link.get("shortText"),
            "language": link.get("language"),
            "is_external": link.get("isExternal")
        })

# Convert to DataFrames
teams_df = pd.DataFrame(teams_list)
logos_df = pd.DataFrame(logos_list)
links_df = pd.DataFrame(links_list)

# Write CSVs
teams_df.to_csv(teams_out / "teams.csv", index=False)
logos_df.to_csv(logos_out / "team_logos.csv", index=False)
links_df.to_csv(links_out / "team_links.csv", index=False)

print("Silver layer tables created.")