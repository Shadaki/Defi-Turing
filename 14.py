"""
Problème 14

En mathématiques, on appelle "suite de Syracuse"
une suite d'entiers naturels définie de la manière suivante :

On part d'un nombre entier plus grand que zéro ;
s’il est pair, on le divise par 2 ;
s’il est impair, on le multiplie par 3 et on ajoute 1.

En répétant l’opération, on obtient une suite d'entiers positifs,
dont chacun ne dépend que de son prédécesseur.

Il existe une conjecture qui dit que :
la suite de Syracuse de n'importe quel entier strictement positif atteint 1. 

Par exemple, à partir de 14, on construit la suite des nombres :
14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
C'est ce qu'on appelle la suite de Syracuse du nombre 14.
Elle a ici une longueur de 18. 

Pour quel nombre de départ inférieur à 1'500'000 obtient-on la plus longue suite de Syracuse?
Il y a deux solutions, donner la plus petite.
"""

longueur = 0
nombre = 0
for num in range(1, 1500000):
    n = num
    lon = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1
        lon += 1
    if lon > longueur:
        nombre = num
print(num)
