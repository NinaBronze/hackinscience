def perfect_shuffle(deck):
    newdeck = []
    num = len(deck)
    milieu = num // 2
    deck1 = deck[0:milieu]
    deck2 = deck[milieu::]
    for i in range(0, milieu):
        a = deck1[i]
        b = deck2[i]
        newdeck.append(a)
        newdeck.append(b)
    if len(deck1) != len(deck2):
        newdeck.append(deck2[-1])
    return(newdeck)
