def insert():
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    dt = datetime.now()
    dtx = dt.strftime("%d/%m/%Y %H:%M:%S")
    dtx = str(dtx)

    cursorObj.execute("INSERT INTO utilisateurs VALUES(null,'admin', 'admin', 'dera.amedee@gmail.com', 'Franck2013', '56833675','dera.amedee@gmail.com', ?) ", (dtx,))


    con.commit()

insert()