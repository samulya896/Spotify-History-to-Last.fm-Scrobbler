import csv
import os

INPUT = "../spotify_all.csv"
OUT_DIR = "../MusicCSV"
SIZE = 2800

os.makedirs(OUT_DIR, exist_ok=True)

with open(INPUT, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    part = 1
    buf = []

    for i, row in enumerate(reader, 1):
        buf.append(row)

        if i % SIZE == 0:
            with open(f"{OUT_DIR}/part{part}.csv","w",newline="",encoding="utf-8") as out:
                w = csv.writer(out)
                w.writerow(header)
                w.writerows(buf)
            print(f"Created part{part}.csv")
            buf = []
            part += 1

    if buf:
        with open(f"{OUT_DIR}/part{part}.csv","w",newline="",encoding="utf-8") as out:
            w = csv.writer(out)
            w.writerow(header)
            w.writerows(buf)
        print(f"Created part{part}.csv")
