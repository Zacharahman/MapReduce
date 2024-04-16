#!/usr/bin/env python

import sys

last_day = None
total_delay = 0
count = 0

# Iterate over each key-value pair from the mapper
for line in sys.stdin:
    line = line.strip()
    day, delay = line.split("\t")

    # Handle missing values (NA)
    if delay == "NA":
        continue

    delay = int(delay)

    # If this is the first iteration
    if not last_day:
        last_day = day
        total_delay = delay
        count = 1
    # If the day is the same as the last one
    elif day == last_day:
        total_delay += delay
        count += 1
    # If the day changes, output the result for the previous day
    else:
        avg_delay = total_delay / count
        print(f"{last_day}\t{avg_delay}")

        # Reset variables for the new day
        last_day = day
        total_delay = delay
        count = 1

# Output the result for the last day
if last_day:
    avg_delay = total_delay / count
    print(f"{last_day}\t{avg_delay}")
