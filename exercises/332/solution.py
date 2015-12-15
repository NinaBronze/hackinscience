import folium
import json

#Fonctions
#####################################


def sans_tiret_sans_espace(phrase):
    sans_tiret = phrase.split("- ")
    if len(sans_tiret) > 2:
        sans_tiret[0] = "- ".join(sans_tiret[0:2])
        del sans_tiret[1]
    phrase_2_0 = " ".join(sans_tiret)
    sans_espace = phrase_2_0.split(" ")
    for i in sans_espace:
        if i == '':
            sans_espace.remove(i)
    return(sans_espace)


def propre(fichier):
    station = open(fichier, 'r')
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

    station.close()
    return(velib)


#Script
##################################

map_osm = folium.Map(location=[48.8682170167744, 2.330493511399173])


station = propre("velib.json")


for i in station:
    map_osm.simple_marker(
        [i["latitude"], i["longitude"]],
        popup='zip_code: '+i["zip_code"]+'; address: '+i["address"])


map_osm.create_map(path='velib.html')
