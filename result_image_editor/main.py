import csv


def main(image_path: str, csv_path: str):
    print("hi")
    result = read(csv_path)
    print(result)


def read(path: str):
    with open(path, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        content = [row for row in csvreader]
        return content


if __name__ == "__main__":
    image_path = "image.png"
    csv_path = "ResultTemplate.csv"
    main(image_path, csv_path)
