#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)  # Skip header
for row in reader:
    if len(row) >= 8:
        country = row[7].strip()
        quantity = row[3].strip()
        if country and quantity:
            try:
                quantity = int(float(quantity))
                print(f"{country}\t{quantity}")
            except:
                continue
