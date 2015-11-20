from is_prime import *

for i in range(222281, 222381):
    binaire = bin(i)
    if is_prime(binaire.count('1')):
        print(i)
