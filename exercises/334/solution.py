import json


def distance(a, b):
    m = 0
    for i in range(0, len(a)):
        m = m + (b[i] - a[i]) ** 2
    d = m ** 0.5
    return(d)


def locate(lat, lon):

    station = open("solution.json", 'r')
    velib = json.load(station)
    le_plus_petit = 100000
    le_plus_proche = {}

    for i in velib:
        a = [i["latitude"], i["longitude"]]
        b = [lat, lon]
        d = distance(a, b)
        if d < le_plus_petit:
            le_plus_petit = d
            le_plus_proche = i

    return(le_plus_proche)
