#!/usr/bin/env python3
import sys

current_country = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    country, count = line.split('\t')
    count = int(count)

    if current_country == country:
        current_count += count
    else:
        if current_country:
            print(f"{current_country}\t{current_count}")
        current_country = country
        current_count = count

if current_country:
    print(f"{current_country}\t{current_count}")
