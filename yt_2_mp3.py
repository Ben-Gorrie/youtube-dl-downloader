#!/usr/bin/python3

import os

songs = ["https://www.youtube.com/watch?v=ETEg-SB01QY", "https://www.youtube.com/watch?v=3jTjBt0Enyw"]
commands = []
os.system("mkdir ~/Songs")
for i in songs:
    string = "youtube-dl -o '~/Songs/%(title)s.%(ext)s' --extract-audio --audio-format mp3 " + i
    commands.append(string)
    
for i in commands:
    os.system(i)

