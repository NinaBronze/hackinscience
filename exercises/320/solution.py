f = open("words.txt", 'r')
text = f.read()
cara = len(text)
alpha = 'abcdefghijklmnopqrstuvwxyz'
for lettre in alpha:
    frequence = text.count(lettre) / cara
    print("%s: %0.2f" % (lettre, frequence))
f.close()
