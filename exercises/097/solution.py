def love_meet(amant1, amant2):
    rencontre = []
    for i in amant1:
        for j in amant2:
            if i == j:
                rencontre.append(i)
    rencontre = set(rencontre)
    return(rencontre)


def affair_meet(amant1, amant2, amant3):
    rencontre = []
    for i in amant2:
        for j in amant3:
            if i == j:
                rencontre.append(i)
    for k in rencontre:
        for l in amant1:
            if k == l:
                rencontre.remove(k)
    rencontre = set(rencontre)
    return(rencontre)
