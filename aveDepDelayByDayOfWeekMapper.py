#!/usr/bin/env python
import sys

# Iterate over each line of input
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    unpacked = line.split(",")  # Split the line into fields using comma as the delimiter
    
    # Extract relevant columns
    DayOfWeek = unpacked[3]  # Index of "DayOfWeek" column
    DepDelay = unpacked[16]  # Index of "DepDelay" column

    # Emit key-value pair (DayOfWeek as key, DepDelay as value)
    print(f"{DayOfWeek}\t{DepDelay}")
