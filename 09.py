"""
Problème 9

Le triplet d'entiers naturels non nuls (a,b,c) est pythagoricien si a2 + b2 = c2. Par exemple, (3,4,5) est un triplet pythagoricien.
Parmi les triplets pythagoriciens (a,b,c) tels que a + b + c = 3600, donner le produit a x b x c le plus grand.
"""

produits=[]
for a in range(3601):
    for b in range(3601-a):
        c=3600-a-b
        if a**2+b**2==c**2:
            produits.append(a*b*c)
print(max(produits))