#!/usr/bin/python3

import os
#enter songs in the list as strings
songs = [""]
commands = []
os.system("mkdir ~/Songs")
for i in songs:
    string = "youtube-dl -o '~/Songs/%(title)s.%(ext)s' --extract-audio --audio-format mp3 " + i
    commands.append(string)
    
for i in commands:
    os.system(i)

