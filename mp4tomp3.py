import os
import subprocess

files = os.listdir("videos")
for file in files:
    print(file)
    filename, _ = os.path.splitext(file) 
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{filename}.mp3"])