import sqlite3
def insert(a,b,c,d,e,f,g):
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO utilisateurs VALUES(null,?,?,?,?,?,?,?) ", (a,b,c,d,e,f,g,))

    con.commit()
    con.close()

    t = 'True'
    # return True #pour dire que tout est ok
    return True





