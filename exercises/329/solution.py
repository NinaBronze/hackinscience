from aide import *

fichier = open('test.txt', 'r')
suite_nb = fichier.read()
le_plus_grand = 0
for i in range(0, len(suite_nb) - 13):
    a = multi(suite_nb[i:(i + 13)])
    if a > le_plus_grand:
        le_plus_grand = a
print(le_plus_grand)
