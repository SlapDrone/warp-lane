"""
client.py

Sends an audio file over HTTP to a given server
"""
from pathlib import Path

import requests

# http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
PORT = 8000
SERVER_URL = f"http://localhost:{PORT}/upload"
FILE_PATH = Path("./media/clip.wav")

if __name__ == "__main__":
    fin = open(FILE_PATH, "rb")
    files = {"file": (FILE_PATH.parts[-1], fin, "audio/x-wav")}
    try:
        r = requests.post(SERVER_URL, files=files)
        print(r.text)
    finally:
        fin.close()
