#!/usr/bin/env python3

import re

with open('holmes.txt') as handle:
    text = handle.read()

hero = r'Sherlock'
villain = r'Moriarity'

hit = re.search(hero, text)

#print(re.findall(r'(\d[,\d]+\d)', text))

p = r'(\d[,\d]+\d)'

total = sum([int(m.replace(',', '')) for m in re.findall(p, text)])

print(total)
