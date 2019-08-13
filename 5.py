"""
Problème 5

2^15 = 32768 et la somme de ses chiffres vaut 3 + 2 + 7 + 6 + 8 = 26. 
Que vaut la somme des chiffres composant le nombre 2^2222 ?
"""

chiffres = list(str(2**2222))
chiffres = [int(n) for n in chiffres]
print(sum(chiffres))
