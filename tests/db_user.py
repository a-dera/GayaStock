'''
Création de la table user
'''

import sqlite3
from datetime import datetime

from sqlite3 import Error

def test():
    if sqlite3.connect('db_user.db'):
        print("Base de donnée déjà crée")
    else:#création de la table
        def sql_connection():

            try:

                con = sqlite3.connect('db_user.db')

                print("Connection établie: Base de données crée avec succès!")

            except Error:

                print(Error)

            finally:

                con.close()

        sql_connection()
test()
def sql_table():
    con = sqlite3.connect('db_user.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE if not exists user (id integer PRIMARY KEY , nom text, prenom text, identifiant text, mdp text, date_inscription text)")

    con.commit()

# con = sql_connection()

sql_table()

def insert_data():
    con = sqlite3.connect('db_user.db')
    
    cursorObj = con.cursor()

    dt = datetime.now()
    # dtx = x.day,'/',x.month,'/',x.year, ' --- ',x.hour,':',x.minute,':',x.second
    dtx = dt.strftime("%d/%m/%Y %H:%M:%S")
    dtx = str(dtx)

    cursorObj.execute("INSERT INTO user VALUES(1, 'admin', 'admin', 'root', '1234', ?) ", (dtx,))

    con.commit()

insert_data()


def sql_select():
    con = sqlite3.connect('db_user.db')
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM user ')

    # rows = cursorObj.fetchall()
    # for row in rows:
    #     print(row)
  
    [print(row) for row in cursorObj.fetchall()]#equivalent des 3 lignes d'en haut

    con.close()

sql_select()