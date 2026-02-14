import json
import csv
import glob

INPUT = "../spotify_json/*.json"
OUTPUT = "../spotify_all.csv"

rows = []

for file in glob.glob(INPUT):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

        for d in data:
            artist = d.get("master_metadata_album_artist_name")
            track = d.get("master_metadata_track_name")
            album = d.get("master_metadata_album_album_name")

            if artist and track:
                rows.append({
                    "artist": artist,
                    "track": track,
                    "album": album or ""
                })

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["artist","track","album"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {OUTPUT} with {len(rows)} rows")
