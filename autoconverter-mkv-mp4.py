import os
import subprocess

folder_path = input("Enter your folder path with .mkv files: ")
language = input("Enter your language (Example: eng, ita): ")
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".mkv"):
            if file.replace(".mkv", ".mp4") in files:
                continue
            else:
                subprocess.run(["ffmpeg", "-i", root+"/"+file, "-metadata:s:a:0", "language="+l
anguage, root+"/"+file.replace(".mkv", ".mp4")])
