#!/usr/bin/python
#Filename: backup_ver5.py

import zipfile
import time
import os

#Naming the files that will be backed up
#Look at os.path documentation for fuction called walk?
archive_list = [ ] 

#Inserting a comment so the reason for the backup can be tracked
comment = raw_input('Insert comment here -->')


underscore = ' '
if not len(comment) == 0:
    underscore = '_'

zlocation = '/Users/Zach'


#using os.walk to make a list (zlocation) of all of the files that will be zipped
for root, dirs, files in os.walk("/Users/Zach/zachs_code"):
    for f in files:
        archive_list.append(os.path.join(root, f))

#Recording the date and time of the backup
dt = time.strftime('%Y%m%d')
today = zlocation + os.sep + dt

if not os.path.exists(today) == True:
    os.mkdir(today)

#Setting the location for storing the archived file
zfilename = zlocation + os.sep + dt + os.sep + time.strftime('%H%M%S') + underscore + comment.replace(' ', '_') + '.zip'


#Archiving the file
zout = zipfile.ZipFile(zfilename, "w")
for fname in archive_list:
    zout.write(fname)
zout.close()
