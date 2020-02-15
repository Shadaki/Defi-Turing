"""
Problème 34

145 est un nombre curieux. En effet, 1! + 4! + 5! = 1 + 24 + 120 = 145.
Trouver le produit de tous les nombres qui sont égaux à la somme de la factorielle de leurs chiffres.

Remarques:
1! = 1 et 2! = 2 ne sont pas des sommes et ne seront pas incluses dans le produit.

Rappelons que 0! = 1
"""

import math
nombres=[n for n in range(10,1000000) if sum([math.factorial(ch) for ch in map(int,list(str(n)))])==n]
print(nombres)
produit=1
for n in nombres:
    produit*=n
print(produit)