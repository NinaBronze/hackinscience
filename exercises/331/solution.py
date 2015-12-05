import json

velib = json.load(open("velib.json", 'r'))
mon_rendu = open("solution.json", 'w')

for i in velib:
    NAME = i["name"].split(" - ")
    ADDRESS = i["address"].split("- ")
    VILLE = ADDRESS[-1].split(" ")
    i["zip_code"] = VILLE[0]
    i["name"] = NAME[1]
    i["address"] = ADDRESS[0]
    i["city"] = VILLE[-1]

json.dump(velib, mon_rendu)
