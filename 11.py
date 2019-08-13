"""
Problème 11

On appellera "miroir d'un nombre n" le nombre n écrit de droite à gauche.
Par exemple, miroir(7423) = 3247. 

Quel est le grand grand nombre inférieur à 10 millions ayant la propriété :
miroir(n) = 4 x n ?
"""

for n in range(10000000, 0, -1):
    if int(str(n)[::-1]) == 4*n:
        print(n)
        break
