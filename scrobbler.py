import pylast
import time
import os
import glob
import re
import json
import csv
from dotenv import load_dotenv

load_dotenv()

BATCH = 50
DELAY = 3
CSV_DIR = "MusicCSV"
PROGRESS = "scrobble_progress.json"


class Scrobbler:

    def __init__(self):
        self.net = pylast.LastFMNetwork(
            api_key=os.getenv("LASTFM_API_KEY"),
            api_secret=os.getenv("LASTFM_API_SECRET"),
            username=os.getenv("LASTFM_USERNAME"),
            password_hash=pylast.md5(os.getenv("LASTFM_PASSWORD"))
        )
        print("Connected to Last.fm")

    def list_parts(self):
        files = glob.glob(f"{CSV_DIR}/part*.csv")
        nums = []
        for f in files:
            m = re.search(r"part(\d+)", f)
            if m:
                nums.append(int(m.group(1)))
        return sorted(nums)

    def read_csv(self, path):
        songs = []
        with open(path,"r",encoding="utf-8",errors="ignore") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if len(r) >= 3:
                    songs.append({
                        "artist": r[0],
                        "track": r[1],
                        "album": r[2]
                    })
        return songs

    def scrobble_batch(self, batch, n, total):
        now = int(time.time())
        payload = []

        for i,s in enumerate(batch):
            payload.append({
                "artist": s["artist"],
                "title": s["track"],
                "album": s["album"],
                "timestamp": now - (i*180) - n
            })

        self.net.scrobble_many(payload)
        print(f"Batch {n}/{total} done")

    def process(self, num):
        path = f"{CSV_DIR}/part{num}.csv"
        songs = self.read_csv(path)

        total = (len(songs)+BATCH-1)//BATCH

        if input(f"Scrobble {len(songs)} songs? (yes): ")!="yes":
            return

        for i in range(total):
            chunk = songs[i*BATCH:(i+1)*BATCH]
            self.scrobble_batch(chunk,i+1,total)
            if i<total-1:
                time.sleep(DELAY)

        self.save(num)

    def save(self,num):
        if os.path.exists(PROGRESS):
            with open(PROGRESS) as f:
                data=json.load(f)
        else:
            data={"done":[]}

        if num not in data["done"]:
            data["done"].append(num)

        with open(PROGRESS,"w") as f:
            json.dump(data,f,indent=2)


def main():
    s = Scrobbler()

    parts = s.list_parts()

    if os.path.exists(PROGRESS):
        with open(PROGRESS) as f:
            done=json.load(f).get("done",[])
    else:
        done=[]

    remain=[p for p in parts if p not in done]

    print("Available:", parts)
    print("Remaining:", remain)

    if not remain:
        print("All done")
        return

    choice=input("Process next file? (yes): ")
    if choice=="yes":
        s.process(remain[0])

if __name__ == "__main__":
    main()
