import csv


def read(path: str):
    with open(path, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        content = [row for row in csvreader]
        return content
