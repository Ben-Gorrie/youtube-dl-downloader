#!/usr/bin/python3

import os
#enter song urls in the list as strings
songs = [""]
commands = []
for i in songs:
    string = "youtube-dl -o '~/Music/%(title)s.%(ext)s' --extract-audio --audio-format mp3 " + i
    commands.append(string)
    
for i in commands:
    os.system(i)

