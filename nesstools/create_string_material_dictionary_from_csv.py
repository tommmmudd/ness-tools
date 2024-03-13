import csv
import json

# material database for Python Ness Guitar scripts

inputfile = open("materials.csv", 'r')
reader = csv.reader(inputfile)

materials = {}

for i, line in enumerate(reader):
	if i > 0:
		mName = line[0]
		mDensity = float(line[1])
		mYM = float(line[2])
		mPoisson = float(line[3])
		materials[mName] = [mDensity, mYM, mPoisson] #(print (line)

json = json.dumps(materials)
f = open("material_dictionary.json","w")
f.write(json)
f.close()