'''

Système de cryptographie avancée
    Génértion de code d'activation

        Decodage
'''

from datetime import datetime

def decode(x,y,z,p,s):
    temps = datetime.today()

    a = temps.year
    b = temps.hour
    c = temps.minute

    a = int(a)

    if a == 2021:
        t = 4
    elif a == 2022:
        t = 5
    elif a == 2023:
        t = 6
    elif a == 2024:
        t = 7
    else:
        t = 100
        


    b_hash = str(b)
    c_hash = str(c)

    l_hash = b_hash + c_hash

    l_int = int(l_hash)

    l_test = l_int +100

    l_test2 = l_int -100


    table = ['DE', 'DR', 'DA','DD', 'ER', 'ED','EA', 'EE', 'RE','RA', 'RD', 'RR','AD', 'AE', 'AR','AA']
    table2 = ['ki', 'mp', 'nh','jd', 'sd']

    if x != t:
        return False
    elif  l_int> y:
        return False 
    elif y>l_test:
        return False
    elif y<l_test2:
        return False
    elif z not in table:
            return False
    elif s not in table2:
        return False
    else: 
        return True
    
