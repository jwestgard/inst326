#!/usr/bin/env python

# this program samples the enron email dataset while looking for social security
# numbers. it is intended to create a smaller dataset for students to use to 
# try to identify pii. you can download the full dataset that this program works
# on from https://www.cs.cmu.edu/~./enron/

import os
import re
import csv
import glob
import shutil

from os.path import join
from random import randint

def sample(person):
    for dirname, dirs, files in os.walk(join('maildir/', person)):
        for filename in files:
            path = join(dirname, filename)
            has_pii = inspect(path)
            if has_pii is not None:
                print("{},{}".format(path, has_pii.group(0)))
            if randint(0, 100) <= 2:
                new_path = re.sub('^maildir', 'sample', path + 'txt')
                new_dir = os.path.dirname(new_path)
                if not os.path.isdir(new_dir):
                    os.makedirs(new_dir)
                shutil.copyfile(path, new_path)

def inspect(path):
    text = open(path).read()
    m = re.search('.{10}\d\d\d-\d\d-\d\d\d\d .{10}', text)
    return m

for person in os.listdir('maildir'):
    sample(person)
