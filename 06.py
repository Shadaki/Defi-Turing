
"""
Problème 6

n! signifie n x (n-1) x ... x 3 x 2 x 1 
Par exemple, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800. 
La somme des chiffres du nombre 10! vaut 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 

Trouver la somme des chiffres du nombre 2013!
"""

import math
chiffres = list(str(math.factorial(2013)))
chiffres = [int(n) for n in chiffres]
print(sum(chiffres))
