"""
Problème 13

Le plus petit carré palindrome ayant un nombre pair de chiffres est 698896 = 8362. 
Quel est le carré palindrome suivant ?
"""

n = 837
while True:
    carre = n**2
    if int(str(carre)[::-1]) == carre and len(str(carre)) % 2 == 0:
        break
    n += 1
print(n)
