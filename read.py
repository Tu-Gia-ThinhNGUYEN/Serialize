import csv

fieldnames = ['country_name', 'area', 'code2', 'code3']

with open('countries.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")
