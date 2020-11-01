'''
Tests de la table user
'''

import sqlite3

def test_user(x,y):

    con = sqlite3.connect('base.db')
    
    cursorObj = con.cursor()

    select = cursorObj.execute("SELECT mdp FROM user WHERE identifiant =  ? ",(x,))
    row = cursorObj.fetchone()

    if row:#tester si l'identifiant existe dans la base
        if row == y: #si le mdp match
            return True
        else:
            # error = "Mot de passe incorrect"
            return False
    else:
        # error = "Identifiant incorrect"
        return False
