import csv
import json


def parse():
    data = []

    with open('wheater.csv', encoding='utf-8') as cs:
        reader = csv.DictReader(cs)
        for row in reader:
            data.append(row)

    with open('wheater.json', 'w', encoding='utf-8') as js:
        js_data = json.dumps(data, indent=4)
        js.write(js_data)


parse()



