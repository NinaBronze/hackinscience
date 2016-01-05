import random

# Fonctions

def gen_colors(nombre):
    couleurs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if nombre > 26:
        return(couleurs)
    else:
        return(couleurs[0:nombre])


def gen_code(taille, couleurs):
    a = 0
    code = ''
    while a < taille:
        num = random.randint(0, (len(couleurs) - 1))
        code = code + couleurs[num]
        a += 1
    return(code)


def check_guess(guess, nombre, code):
    if len(guess) != nombre:
        return(False)
    for i in guess:
        if code.find(i) < 0:
            return(False)
    return(True)


def score_guess(guess, code):
    score_1 = 0
    score_2 = 0
    for i in range(0, len(guess)):
        if guess[i] == code[i]:
            score_1 += 1
            guess = guess.replace(guess[i], '0', 1)
            code = code.replace(code[i], '0', 1)
        elif code.find(guess[i]) > -1:
            score_2 += 1
            code = code.replace(guess[i], '0', 1)      
            guess = guess.replace(guess[i], '0', 1)
    return((score_1, score_2))


def comparaison(str1, str2):
    for i in str1:
        if str2.find(i) < 0:
            return(False)
    return(True)

 
def play_cli(taille, nombre):
   
    couleurs_possibles = gen_colors(nombre)
    solution_jeu = gen_code(taille, couleurs_possibles)
    print('Le code est :', solution_jeu)
    print('Possible colors are', couleurs_possibles)
    print('Code is size', str(taille) + '.')
    nb_essais = 0
    print(nb_essais, end=' ')
    test = input('--> ')
    while test != solution_jeu:
        if comparaison(test, couleurs_possibles) is False or len(test) != len(solution_jeu):
            print('Wrong size or color !')
        else:
            print(score_guess(test, solution_jeu))
        print(nb_essais, end=' ')
        test = input('--> ')
    nb_essais += 1
    print('Congrats, you won after', nb_essais, 'attempts !')
    return()


# Main

nombre = 6
taille = 4
play_cli(taille, nombre)




