import sqlite3
def sql_select():
    con = sqlite3.connect('base.db')
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM utilisateurs ')

    rows = cursorObj.fetchall()
    for row in rows:
        yes = row
  
    # yes = [print(row) for row in cursorObj.fetchall()]#equivalent des 3 lignes d'en haut

    con.close()
    yes=str(yes)
    return yes



'''def insert7():
    con = sqlite3.connect('base.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("DELETE FROM utilisateurs where id between 6 and 19")

    con.commit()'''


