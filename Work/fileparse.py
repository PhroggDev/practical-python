"""fileparse.py for Exercise3.1"""
# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename):
    """
    Parse a CSV file into a list of records
    """
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:  # Skip empty rows
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records
