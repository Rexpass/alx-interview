#!/usr/bin/env python3

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1

        # Parse the line
        try:
            parts = line.split()
            ip_address = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Check if the line format is valid
            if len(parts) < 12 or parts[5] != '"GET' or parts[6] != '/projects/260' or parts[8] != 'HTTP/1.1"':
                continue

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

        except (ValueError, IndexError):
            # Ignore lines with invalid format
            continue

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_statistics()
    sys.exit(0)
