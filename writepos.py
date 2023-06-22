import csv

# csv header
fieldnames = ['x', 'y', 'z']
x = [1.9366612434387207, -3.053391933441162, -3.0622968673706055, 0.30975770950317383, 2.032531261444092]
y = [3.9708738327026367, 3.220120429992676, -2.63504695892334, -2.9622130393981934, -1.0816521644592285]
# csv data
rows = []
for i in range(0,len(x)):
    rows.append({'x': x[i], 'y': y[i], 'z': 0})
with open('pos.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
