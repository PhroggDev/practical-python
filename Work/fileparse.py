"""fileparse.py for Exercise3.1"""
# fileparse.py
#
# Exercise 3.4
import csv


def parse_csv(filename, select=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # if a column selector was given, find indices of the specified columns,
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip empty rows
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Make a dictionary out of records returned
            record = dict(zip(headers, row))
            records.append(record)
    return records
