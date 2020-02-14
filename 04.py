"""
Problème 4

Un nombre palindrome se lit de la même façon de gauche à droite et de droite à gauche.
Le plus grand palindrome que l'on peut obtenir en multipliant deux nombres de deux chiffres est 9009 = 99 x 91. 

Quel est le plus grand palindrome que l'on peut obtenir en multipliant un nombre de 4 chiffres avec un nombre de 3 chiffres ?
"""

meilleur = 0
for a in range(1000, 10000):
    for b in range(100, 1000):
        mul = a*b
        if str(mul) == str(mul)[::-1]:
            if mul > meilleur:
                meilleur = mul
print(meilleur)
