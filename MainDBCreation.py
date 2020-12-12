'''
Création de toutes les autres tables, dans une base de donnée à part entière
'''

import sqlite3
from datetime import datetime
from time_fill import dtx

from sqlite3 import Error

def createdatabase():
    if sqlite3.connect('DataBase.db'):
        print("Base de donnée déjà crée")
    else:#création de la table
        def sql_connection():

            try:

                con = sqlite3.connect('DataBase.db')

                # print("Connection établie: DataBase de données crée avec succès!")

            except Error:
                # pass

                print(Error)

            finally:

                con.close()

        sql_connection()
createdatabase()
def sql_table():
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    #user
    cursorObj.execute('''CREATE TABLE if not exists utilisateurs (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        nom text, 
        prenom text, 
        identifiant text, 
        mdp text, 
        tel text, 
        mail text, 
        date_inscription text
    )''')

    cursorObj.execute('''CREATE TABLE if not exists caisse (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        date_opération datetime, 
        lib_prod text, 
        débit float,
        crédit float  /*débit ou crédit*/
    )''')

    cursorObj.execute('''CREATE TABLE if not exists ventes (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        li_prod text, 
        quant float, 
        prix text, 
        nom_client text, 
        code_facture text,
        date_opération datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists mouvements (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        type_mouv text, 
        quant integer, 
        lib_prod text, 
        montant float, 
        date_opération datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists catégories (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        lib_catégorie text, 
        description_catégorie text, 
        date_enregistrement datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists livraisons (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        lib_prod text, 
        nom_fournisseur integer, 
        quant float, 
        montant float, 
        code_facture text,
        date_opération datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists factures (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        code_facture integer, 
        type_facture text, /*acaht/vente*/
        montant float, 
        nom_prod text,
        nom_client text,/* si c'est vente*/
        nom_fournissuer text,/* si c'est achat*/
        date_émission datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists fournisseurs (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        nom text, 
        prenom text, 
        type_fournisseur text, /*entreprise/particulier*/ 
        nom_entreprise text, 
        adresse text, 
        code_factures text, 
        nombre_articles_total integer, 
        date_enregistrement datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists clients (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        identité text, 
        type_client text, 
        nombre_achat integer, 
        montant_total_dep float, 
        frequence integer, 
        date_enregistrement datetime
    )''')

    cursorObj.execute('''CREATE TABLE if not exists produits (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE, 
        lib_prod text,
        code_prod integer,
        quant_seuil integer, 
        quant integer, 
        /*localisation text, 
        /*code_fournisseurs integer,*/
        prix_unitaire float, 
        unité_mesure text, 
        description_prod text, 
        catégorie_prod text,
        date_dernière_modif datetime,  
        date_enregistrement datetime
    )''')

    con.commit()

sql_table()

def super_user():
    con = sqlite3.connect('DataBase.db')
    
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO utilisateurs VALUES(null,'admin', 'admin', 'dera.amedee@gmail.com', '13Kona$JuopY%', '56833675','dera.amedee@gmail.com', ?) ", (dtx,))


    con.commit()

super_user()


