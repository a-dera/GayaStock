import sqlite3
from datetime import datetime
def insert():
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    dt = datetime.now()
    dtx = dt.strftime("%d/%m/%Y %H:%M:%S")
    dtx = str(dtx)

 

    cursorObj.execute("INSERT INTO catégories VALUES(null,'Smartphone', 'Les téléphones intelligents', ?) ", (dtx,))

    cursorObj.execute("INSERT INTO produits VALUES(null,'Tecno Camon 15', '001','20','100','140000','élément','Un téléphone performant pour vous','Smartphone',?, ?) ", (dtx,dtx,))
    


    con.commit()

insert()