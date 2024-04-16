#!/usr/bin/env python
import sys

last_key = None
total_delay = 0
count = 0

# Iterate over each line of input
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")

    # Skip lines with non-numeric values
    if not value.isdigit():
        continue

    # Convert the value to an integer
    value = int(value)

    # If this is the first iteration or key has changed
    if last_key != key:
        # Output the average delay for the previous key
        if last_key:
            average_delay = total_delay / count
            print(f"{last_key}\t{average_delay}")

        # Reset count and total_delay for the new key
        last_key = key
        count = 0
        total_delay = 0

    # Accumulate delay and count
    total_delay += value
    count += 1

# Output the average delay for the last key
if last_key:
    average_delay = total_delay / count
    print(f"{last_key}\t{average_delay}")
