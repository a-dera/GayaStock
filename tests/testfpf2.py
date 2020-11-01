import sqlite3
import os
from fpdf import FPDF

class BalancePDF(FPDF):
	
	pdf = FPDF('P', 'cm', 'A4')
	pdf.add_page()
	pdf.image('img/github.png', 0, 0, 6, 4)
	pdf.set_font('Arial', 'B', 35)
	pdf.set_text_color(13, 61, 84)
	pdf.cell(8)
	pdf.cell(5, 3, 'Fiche utilisateur', 'B', 1, 'C')
	pdf.set_font('Arial', 'B', 12)
	pdf.cell(8)
	#pdf.cell(5, 1.5, date, 0, 1, 'C')
	pdf.ln(1)
	pdf.set_font('Arial', 'I', 12)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(6, 1, 'Numero', 1, 0, 'C')
	pdf.cell(6, 1, 'Nom', 1, 0, 'C')
	pdf.cell(6, 1, 'Identifiant', 1, 0, 'C')

	


	mydb = sqlite3.connect("base.db")
	cur = mydb.cursor()
	cur.execute("SELECT * FROM utilisateurs")
	print(" Id     \tNom         \tT Identifiant  ")
	print("--------------------------------------------------")
	for row in cur:
		Id= row[0]
		nom= row[1]
		identifiant= row[3]

	
		print("{}      {}              {}      ".format(Id,nom,identifiant))

		pdf.cell(2, 1, str(Id), 1, 0, 'C')
		pdf.cell(5, 1, str(nom), 1, 0, 'C')
		pdf.cell(3, 1, str(identifiant), 1, 0, 'C')
	pdf.output('test10.pdf', 'F')
	os.startfile('test10.pdf')

	mydb.close()