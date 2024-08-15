#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_size = 0
status_code_counts = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

def print_statistics():
    """Prints the file size and the number of lines per status code."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signum, frame):
    """Handles keyboard interrupt to print statistics before exiting."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        # Ensure the line format is valid before processing
        if len(parts) >= 7 and parts[5] == '"GET' and parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
            try:
                # Extract file size and status code
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Accumulate file size
                total_size += file_size

                # Count the status code occurrences
                if status_code in valid_status_codes:
                    if status_code not in status_code_counts:
                        status_code_counts[status_code] = 0
                    status_code_counts[status_code] += 1

            except ValueError:
                # If conversion to int fails, skip the line
                continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle interrupt during normal processing
    print_statistics()
    sys.exit(0)

# Final statistics printout (if script ends normally)
print_statistics()
