"""
Problème 7

La somme des nombres premiers entre 1 et 10 vaut 2 + 3 + 5 + 7 = 17. 

Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
"""

premiers = [2]
n = 3
while len(premiers) < 23456:
    ok = True
    for p in premiers:
        if n % p == 0:
            ok = False
    if ok:
        premiers.append(n)
    n += 2
print(premiers[-1])
