#!/usr/bin/env python3

import re

with open('holmes.txt') as handle:
    text = handle.read()

pattern = r'\w+? Sherlock.{5}'

hits = re.finditer(pattern, text)

for hit in hits: print(hit[0])
