#!/usr/bin/env python3
import sys

current_country = None
count = 0
total = 0
min_qty = None
max_qty = None

for line in sys.stdin:
    try:
        country, qty = line.strip().split('\t')
        qty = int(qty)

        if current_country == country:
            total += qty
            count += 1
            min_qty = min(min_qty, qty)
            max_qty = max(max_qty, qty)
        else:
            if current_country:
                avg = total / count
                print(f"{current_country}\tMin: {min_qty}, Max: {max_qty}, Avg: {avg:.2f}")
            current_country = country
            total = qty
            count = 1
            min_qty = qty
            max_qty = qty
    except:
        continue

if current_country:
    avg = total / count
    print(f"{current_country}\tMin: {min_qty}, Max: {max_qty}, Avg: {avg:.2f}")
