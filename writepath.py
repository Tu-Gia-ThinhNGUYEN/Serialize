import json

# Data to be written
dictionary = {
	"p1": [1.9366612434387207, -3.053391933441162, -3.0622968673706055, 0.30975770950317383, 2.032531261444092],
	"p2": [1.9366612434387207, -3.053391933441162, -3.0622968673706055, 0.30975770950317383]
}

# Serializing json
json_object = json.dumps(dictionary, indent=2)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)
