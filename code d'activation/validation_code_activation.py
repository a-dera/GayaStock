
'''
Csript exécutable pour avoir unencodage rapide
'''
import os
from  activation_code_decode import decode

x = input("Entrer le premier caractère (c'est un chiffre):--> ")
y = input("Entrer les 4 chiffres suivants:--> ")
z = input("Entrer les deux lettres:--> ")
p = input("Entrer les 2 chiffres suivants:--> ")
s = input("Entrer les deux lettres::--> ")

x = int(x)
y = int(y)
z = str(z)
p = int(p)
s = str(s)



print(decode(x,y,z,p,s))

os.system('pause')