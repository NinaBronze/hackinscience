import json


def load_json(fichier):
    op = open(fichier, 'r')
    lire = op.read()
    my_json = json.loads(lire)
    return(my_json)
