#!/usr/bin/env python3
import sys
import csv
import traceback

def safe_input():
    for line in sys.stdin:
        try:
            yield line.encode("utf-8").decode("utf-8", errors="ignore")
        except Exception as e:
            sys.stderr.write("Failed to decode line: {}\n".format(str(e)))
            continue

try:
    reader = csv.reader(safe_input())
    header = next(reader, None)  # Skip header
    for row in reader:
        try:
            if len(row) < 8:
                continue
            country = row[7].strip()
            if country:
                print(f"{country}\t1")
        except Exception as e:
            sys.stderr.write("Row error: {}\n".format(str(e)))
            traceback.print_exc(file=sys.stderr)
            continue
except Exception as e:
    sys.stderr.write("Mapper fatal error: {}\n".format(str(e)))
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)



