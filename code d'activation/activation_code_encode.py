'''

Système de cryptographie avancée
    Génértion de code d'activation

        Encodage
'''

from datetime import datetime
from random import choice


def encode():
    temps = datetime.today()

    a = temps.year
    a = int(a)

    if a == 2020:
        b = 4
    elif a == 2021:
        b = 5
    elif a == 2022:
        b = 6
    elif a == 2023:
        b = 7
    else:
        b = 100

    c = temps.hour
    c = int(c)
    c = c + 1#ajout de la validité qui de l'ordre de 1 heure
    if c ==0 or c==1 or c==2 or c==3 or c==4 or c==5 or c==6 or c==7 or c==8 or c==9:#pour avoir les 2 chiffres
        c = str(c)
        c = '0' + c

    d = temps.minute
    
    if d ==0 or d==1 or d==2 or d==3 or d==4 or d==5 or d==6 or d==7 or d==8 or d==9:#pour avoir les 2 chiffres
        d = str(d)
        d = '0' + d

    c_hash = str(c)
    d_hash = str(d)
    time_hash = c_hash + d_hash#concatenation heure+minute

    g = temps.minute
    g = int(g)
    g = g - 13

    if g <0:
        g = g*(-1)

    b_hash = str(b)
    g_hash = str(g)

    j_hash = choice(['DE', 'DR', 'DA','DD', 'ER', 'ED','EA', 'EE', 'RE','RA', 'RD', 'RR','AD', 'AE', 'AR','AA'])

    k_hash = choice(['ki', 'mp', 'nh','jd', 'sd'])

    output = b_hash +'-'+ time_hash +'-'+ j_hash+'-' + g_hash +'-'+ k_hash
    
    return output
