#!/usr/bin/env python3

import sys

for line in sys.stdin:
        words = line.strip().split(',')
        if(len(words) < 3):
                continue
        stars = words[1]
        year = words[2].split('-')[0]
        print("%s\t%s" % (stars, year))
