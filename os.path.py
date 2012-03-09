#!/usr/bin/python
#Filename: os.path.py

tobackup = []


import os
for root, dirs, files in os.walk("/Users/Zach/zachs_code"):
    for f in files:
        tobackup.append(os.path.join(root, f))

print(tobackup)
