'''
Test SQLite3
'''

import sqlite3

from sqlite3 import Error

def test():
    if sqlite3.connect('database.db'):
        print("Base de donnée déjà crée")
    else:#création de la table
        def sql_connection():

            try:

                con = sqlite3.connect('database.db')

                print("Connection établie: Base de données crée avec succès!")

            except Error:

                print(Error)

            finally:

                con.close()

        sql_connection()
test()
def sql_table():
    con = sqlite3.connect('database.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE if not exists employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()

# con = sql_connection()

sql_table()

# def insert_data():
#     con = sqlite3.connect('database.db')
    
#     cursorObj = con.cursor()

#     cursorObj.execute("INSERT INTO employees VALUES(3, 'Joe', 800, 'HR', 'Manager', '2001-11-03')")

#     con.commit()

# insert_data()

def sql_update():
    con = sqlite3.connect('database.db')
    
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 3')

    con.commit()

sql_update()

def sql_select():
    con = sqlite3.connect('database.db')
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees ')

    # rows = cursorObj.fetchall()
    # for row in rows:
    #     print(row)
  
    [print(row) for row in cursorObj.fetchall()]#equivalent des 3 lignes d'en haut

    # con.commit()

sql_select()