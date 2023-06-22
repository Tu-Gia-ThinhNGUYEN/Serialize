import json

# Opening JSON file
stations = []
index = 0
with open('pathArray.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
for i in range(0, len(json_object)):
    stations.append(json_object["p"])
while index < 5:
    print(stations[0][0][index][0])
    index = index + 1
# try:
#     with open('pathArray.json', 'r') as openfile:

#         # Reading from json file
#         json_object = json.load(openfile)
#     for i in range(0, len(json_object)):
#         stations.append(json_object["p"])
#     while index < 5:
#         print(stations[0][0][index][0])
#         index = index + 1
# except:
#     print('Error reading')
# print(type(json_object['p1']))
