import os
import subprocess

folder_path = input("Enter your folder path with .mkv files: ")
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".mkv"):
            if file.replace(".mkv", ".mp4") in files:
                continue
            else:
                subprocess.run(["ffmpeg", "-i", root+"/"+file, root+"/"+file.replace(".mkv", ".mp4")])
