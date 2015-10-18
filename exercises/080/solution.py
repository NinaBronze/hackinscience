list = "abcdefghijklmnopqrstuvwxyz"

for lettre1 in list:
    for lettre2 in list:
        if lettre1 != lettre2:
            print(lettre1 + lettre2)
    list = list[1::]
    
