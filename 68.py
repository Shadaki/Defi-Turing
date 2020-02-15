"""
Problème 68

Un cryptarithme est un casse-tête numérique et logique qui consiste
en une équation mathématique où les lettres représentent des chiffres à trouver.

SIX^2 = TROIS 

Que vaut TROIS ?
"""

for s in range(1, 10):
    for i in range(10):
        for x in range(10):
            for t in range(1, 10):
                for r in range(10):
                    for o in range(10):
                        six = s*100+i*10+x
                        trois = t*10000+r*1000+o*100+i*10+s
                        if six**2 == trois and s!=i!=x!=t!=r!=o:
                            print(trois)
                            break
