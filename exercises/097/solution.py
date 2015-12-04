def love_meet(amant1, amant2):
    rencontre = []
    for i in amant1:
        for j in amant2:
            if i == j:
                rencontre.append(i)
    rencontre = set(rencontre)
    return(rencontre)


def affair_meet(amant1, amant2, amant3):
    dispute = set(amant2) & set(amant1)
    amour = set(amant2) & set(amant3)
    rencontre = amour - dispute
    return(rencontre)
