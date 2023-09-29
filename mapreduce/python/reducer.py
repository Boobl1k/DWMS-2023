#!/usr/bin/env python3

import sys

stars = {}

i = 0

for line in sys.stdin:
    i+=1
    try:
        line = line.strip()
        star, year = line.split("\t", 1)
        star = int(star)
        year = int(year)
        if year in stars:
            stars[year][0]+=star
            stars[year][1]+=1
        else:
            stars[year] = [star,1]
    except Exception as e:
        continue

print(i)

try:
    for year in stars:
        print("%s\t%s" % (year, stars[year][0]/stars[year][1]))
except Exception as e:
    pass

