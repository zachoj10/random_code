#!/usr/bin/python
#Filename: backup_ver4.py

import os
import time

source = ["/Users/Zach/zachs_code"]

target_dir = '/Users/Zach'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'

else:
    target = today + os.sep + now + '_'\
        + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Sucessfully created directory', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Sucessful backup to', target)

else:
    print('Backup FAILED')
