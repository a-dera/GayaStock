'''
Tests de la table user
'''

import sqlite3


def sql_select():
    con = sqlite3.connect('db_user.db')
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM user ')
  
    [print(row) for row in cursorObj.fetchall()]#equivalent des 3 lignes d'en haut

    con.close()

# sql_select()

def test():
    identifiant_saisie = 'roo'
    mdp_saisie = '1234'

    c = (mdp_saisie,)#échange
    mdp_saisie=c

    con = sqlite3.connect('db_user.db')
    
    cursorObj = con.cursor()

    select = cursorObj.execute("SELECT mdp FROM user WHERE identifiant =  ? ",(identifiant_saisie,))
    row = cursorObj.fetchone()
    if row:

        if row == mdp_saisie: #si le mdp match
            print("Vous êtes connectés")
        else:
            print("Mot de passe incorrect")
    else:
        print("identifiant incorrect")


test()
