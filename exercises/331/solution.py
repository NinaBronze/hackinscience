import json
from aide import *

station = open("velib.json", 'r')
velib = json.load(station)


for i in velib:
    NAME = i["name"].split(" - ")
    i["name"] = " ".join(NAME[1::])
    ADDRESS = sans_tiret_sans_espace(i["address"])
    for d in ADDRESS:
        if len(d) == 5:
            try:
                numero = ADDRESS.index(d)
                d = int(d)
                i["zip_code"] = str(d)
                i["city"] = ' '.join(ADDRESS[(numero + 1)::])
                i["address"] = ' '.join(ADDRESS[0:(numero)])
            except ValueError:
                None

solution = open("solution.json", 'w')
json.dump(velib, solution)
solution.close()
station.close()
