import sqlite3
from time_fill import dtx
def insert_livraison(lib_prod,nom_four,quant,montant,code_facture,dtx):
    con = sqlite3.connect('DataBase.db')

    cursorObj.execute("INSERT INTO livraisons VALUES(null,?,?,?,?,?,?,?) ", (lib_prod,nom_four,quant,montant,code_facture,dtx,))

    con.commit()
    con.close()

    return True

def insert_produits(prod,quant):
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("UPDATE produits SET quant = ? WHERE lib_prod = ? ", (prod, quant,))

    con.commit()
    con.close()

    return True

def insert_mouvement(a,b,c,d,e,f,g):
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()
 
    cursorObj.execute("INSERT INTO mouvements VALUES(null,'Livraison',?,?,?,?,) ", (quant, lib_pod,montant,dtx,))

    con.commit()
    con.close()

    return True

def insert_four(a,b,c,d,e,f,g):#a revoir en profondeur
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO fournisseurs VALUES(null,?,?,?,?,?,?,?) ", (nom,prenom,type_four,nom_entreprise,adresse,code_facture,))

    con.commit()
    con.close()

    return True

def insert_fact(a,b,c,d,e,f,g):
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO utilisateurs VALUES(null,?,?,?,?,?,?,?) ", (a,b,c,d,e,f,g,))

    con.commit()
    con.close()

    return True

def insert_caisse(a,b,c,d,e,f,g):
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO utilisateurs VALUES(null,?,?,?,?,?,?,?) ", (a,b,c,d,e,f,g,))

    con.commit()
    con.close()

    return True