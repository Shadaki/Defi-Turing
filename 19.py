"""
Problème 19

Des petits hommes verts rencontrent des petits hommes bleus.
A leur grand étonnement, ils constatent que leurs mains ne comportent pas le même nombre de doigts :
7 pour les bleus et 8 pour les verts.
Mais les savants des deux peuples remarquent que si l'on compte sur les doigts comme indiqué sur la figure,
en faisant des allers-retours de l'auriculaire vers le pouce, puis du pouce vers l'auriculaire,
certains nombres se comptent à la fois sur l'annulaire des mains bleues et sur celui des mains vertes (le 2 et le 14 par exemple).
Ces nombres ont été qualifiés d'"annulaires" par les savants.

Calculer la somme des nombres annulaires compris entre 1 et 2013.
"""

vert,bleu=0,0
verts,bleus=[],[]
for x in range(500):
    if x%2==0:
        vert+=2
        bleu+=2
    else:
        vert+=12
        bleu+=10
    verts.append(vert)
    bleus.append(bleu)
verts=set(n for n in verts if n<2013)
bleus=set(n for n in bleus if n<2013)
print(sum(verts&bleus))