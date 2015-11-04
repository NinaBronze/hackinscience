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
            for k in amant1:
                if i != k:
                    if i == j:
                        rencontre.append(i)
    rencontre = set(rencontre)
    return(rencontre)
