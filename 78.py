"""
Problème 78

Quel est le seul nombre ayant le motif suivant : abcd = ab x cd ? 

Précision (1.5.2014) : ce n'est pas un cryptarithme. 
Deux lettres différentes peuvent désigner le même chiffre.
"""

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a*1000+b*100+c*10+d == a**b*c**d:
                    print(str(a)+str(b)+str(c)+str(d))
