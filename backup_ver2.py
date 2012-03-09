#!/usr/bin/python
#Filename: backup_ver2.py

import os
import time

source = ['/Users/Zach/zachs_code', '/Users/Zach/Desktop/beg_python']

target_dir = "/Volumes/USB\ DISK/backup"

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Sucessful backup to', target)

else:
    print('Backup FAILED')
