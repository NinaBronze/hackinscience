from aide import *

fichier = open('test.txt', 'r')
suite_nb = fichier.read()
le_plus_grand = 0
for i in range(0, len(suite_nb)):
    a = multi(suite_nb[i:(i + 13)])
    b = multi(suite_nb[(i + 1):(i + 14)])
    if a * b != 0 and a < b:
        le_plus_grand = multi(suite_nb[(i + 1):(i + 14)])
    else:
        le_plus_grand = multi(suite_nb[i:(i + 13)])
print(le_plus_grand)
