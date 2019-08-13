"""
Problème 10

La somme des nombres premiers entre 1 et 10 vaut 2 + 3 + 5 + 7 = 17. 

Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
"""

nombres = list(range(3, 10000000, 2))
for a in range(3, 4000, 2):
    if a in nombres:
        for b in nombres:
            if a != b and b % a == 0:
                nombres.remove(b)
print(sum(nombres)+2)
