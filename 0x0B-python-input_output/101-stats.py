#!/usr/bin/python3
"""file handling"""
import sys
from collections import defaultdict


STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

total_size = 0
status_counts = defaultdict(int)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[8]
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in STATUS_CODES:
                status_counts[status_code] += 1
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(STATUS_CODES):
                if status_counts[code] > 0:
                    print(f"{code}: {status_counts[code]}")
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(STATUS_CODES):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
