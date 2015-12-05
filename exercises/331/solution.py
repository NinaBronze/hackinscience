import json

velib = open("velib.json", 'r')
solution = open("solution.json", 'w')

station = json.load(velib)
a = 0

for i in station:
    NAME = i["name"].split(" - ")
    ADDRESS = i["address"].split("- ")
    VILLE = ADDRESS[1].split(" ")
    i["zip_code"] = VILLE[0]
    i["name"] = NAME[1]
    i["address"] = ADDRESS[0]
    i["city"] = VILLE[1]
station = str(station)
solution.write(station)
