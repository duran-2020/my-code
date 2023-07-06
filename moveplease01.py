#!/usr/bin/env python3

import shutil
import os

# Change directory using the argument path as current working directory
os.chdir('/home/student/mycode/')

# Take raynor object and move to directory 'ceph_storage'
shutil.move('raynor.obj', 'ceph_storage/')

# Rename 'kerrigan.obj' with the user's input
xname = input('What is the new name for kerrigan.obj? ')

# Take name entered by user, concatinate it to destination argument
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



