#!/usr/bin/env python3

import os
import re
import sys

def find_ssn(inputfile):
    pattern = r'\d\d\d-\d\d-\d\d\d\d'
    with open(inputfile, encoding='windows-1252') as handle:
        text = handle.read()
    matches = re.findall(pattern, text)
    return matches

for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        path = os.path.join(root, file)
        matches = find_ssn(path)
        if matches:
            print(path)
