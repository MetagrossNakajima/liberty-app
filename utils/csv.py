import csv


def read(path: str):
    with open(path, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        # 最初の行（ヘッダー行）をスキップ
        next(csvreader)
        content = [row for row in csvreader]
        return content
