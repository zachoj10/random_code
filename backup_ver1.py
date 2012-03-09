#!/usr/bin/python
#Filename: backup_ver1.py

import os
import time

source = ['/Users/Zach/zachs_code', '/Users/Zach/Documents/iChats']

target_dir = "/Volumes/USB\ DISK/backup"

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('Sucessful backup to', target)

else:
    print('Backup FAILED')
