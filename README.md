🎧 Spotify → Last.fm Scrobbler (V1)

Import your complete Spotify listening history into Last.fm using batch scrobbling.

This project converts Spotify privacy export JSON files → CSV → batches → uploads to Last.fm safely.

✨ Features

🎵 Scrobbles Artist + Track + Album

📦 Batch upload (Last.fm safe limit)

▶️ Command-line menu (simple CMD GUI)

🔄 Resume support (continues from last file)

🧹 Works with large Spotify history exports

📁 Project Structure

spotify-to-lastfm/
│
├── spotify_json/                 # Put Spotify JSON files here
├── MusicCSV/                     # Auto-generated CSV parts
│
├── scripts/
│   ├── json_to_csv.py            # Convert JSON → CSV
│   └── split_csv.py              # Split into parts
│
├── lastfm_scrobbler_v1.py        # Main scrobbler
├── requirements.txt
├── .env                          # Last.fm credentials (PRIVATE)
└── .gitignore

🧰 Requirements

Python 3.9+

Last.fm account

Spotify privacy data export

Install dependencies:

pip install -r requirements.txt

🔑 Get Last.fm API Keys

Go to: https://www.last.fm/api/account/create

Create an API application

Copy:

API Key

API Secret

⚙️ Setup .env

Create a file in the root folder:

.env


Add:

LASTFM_API_KEY=your_api_key
LASTFM_API_SECRET=your_api_secret
LASTFM_USERNAME=your_lastfm_username
LASTFM_PASSWORD=your_lastfm_password

⚠️ Important

No quotes

No spaces

.env is ignored by GitHub for security

📥 Export Spotify Data

Request your data from:

https://www.spotify.com/account/privacy/

Download the archive and copy all streaming history JSON files into:

spotify_json/


Example files:

Streaming_History_Audio_0.json
Streaming_History_Audio_1.json

🚀 Step-by-Step Usage
1️⃣ Convert JSON → CSV
cd scripts
python json_to_csv.py


Creates:

spotify_all.csv

2️⃣ Split CSV into batches
python split_csv.py


Creates:

MusicCSV/
  part1.csv
  part2.csv
  part3.csv
  ...


Each file contains about 2800 songs.

3️⃣ Start Scrobbling

Go back to root:

cd ..
python scrobbler.py


You’ll see:

Available: [1,2,3...]
Remaining: [1,2,3...]
Process next file? (yes):


Type:

yes

🎧 How It Works

Each batch sends:

Artist

Track

Album

Timestamp

Last.fm limit = 50 tracks per request, so the script uploads safely in batches.

🔄 Resume Support

Progress is saved automatically in:

scrobble_progress.json


If the script stops or crashes, just run it again — it continues from the next file.

⚠️ Notes

Do NOT upload .env

Do NOT upload Spotify data

Keep API keys private

Album play counts are included

🧹 .gitignore (Recommended)
.env
venv/
spotify_json/
MusicCSV/
spotify_all.csv
scrobble_progress.json
__pycache__/
*.pyc

🧑‍💻 Author

Built for importing Spotify history into Last.fm safely.

⭐ Future Ideas (Not in V1)

Backdated timestamps

GUI window version

Progress bar

Auto installer

🎉 Done!

After running everything, your old Spotify history will appear in:

Last.fm → Profile → Recent Tracks
