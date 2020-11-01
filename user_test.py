'''
test pour la connexion, si ok passage au main screen

'''

import sqlite3

def test_user(x,y):

    con = sqlite3.connect('base.db')
    
    cursorObj = con.cursor()
    x = str(x)
    y= str(y)
    cursorObj.execute("SELECT mdp FROM utilisateurs WHERE identifiant =  ? ",(x,))

    row = cursorObj.fetchone()
    con.close()

    if row:#si l'id existe

        for item in row:
            if item == y: #si le mdp match
                # return True
                z = 'True'
            else:
                # return False
                z = 'False'
    else:
        # return False
        z = 'False'

    return z
