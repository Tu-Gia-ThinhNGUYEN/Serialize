import csv

fieldnames = ['x', 'y', 'z']
x = []
y = []

with open('pos.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        x.extend({line['x']})
        y.extend({line['y']})
    # convert string list to float list
    x = [float(x) for x in x]
    y = [float(y) for y in y]
    print(type(x[0]))
    print(y)
