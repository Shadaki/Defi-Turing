"""
Problème 10

La somme des nombres premiers entre 1 et 10 vaut 2 + 3 + 5 + 7 = 17.
Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
"""

restants=list(range(2,10000000))
premiers=[2]
while premiers[-1]<lim**0.5:
    restants=[num for num in restants if not num%premiers[-1]==0]
    premiers.append(restants[0])
del restants[0]
premiers.extend(restants)
print(sum(premiers))