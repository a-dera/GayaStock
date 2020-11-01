import sqlite3
import os
import platform
import subprocess
from fpdf import FPDF

class BalancePDF(FPDF):
	
	pdf = FPDF('P', 'cm', 'A4')
	pdf.add_page()
	pdf.image('logo3.png', 0, 0, 4, 4)
	pdf.set_font('Arial', 'B', 35)
	pdf.set_text_color(13, 61, 84)
	pdf.cell(8)
	pdf.cell(5, 3, 'Balance', 'B', 1, 'C')
	pdf.set_font('Arial', 'B', 12)
	pdf.cell(8)
	#pdf.cell(5, 1.5, date, 0, 1, 'C')
	pdf.ln(1)
	pdf.set_font('Arial', 'I', 12)
	pdf.set_text_color(0, 0, 0)
	pdf.cell(2, 2, 'Numero', 1, 0, 'C')
	pdf.cell(5, 2, 'Intitulé', 1, 0, 'C')
	pdf.cell(6, 1, 'Totaux', 1, 0, 'C')
	pdf.cell(6, 1, 'Solde de cloture', 1, 1, 'C')
	pdf.cell(7)
	pdf.cell(3, 1, 'Debit', 1, 0, 'C')
	pdf.cell(3, 1, 'Credit', 1, 0, 'C')
	pdf.cell(3, 1, 'Debit', 1, 0, 'C')
	pdf.cell(3, 1, 'Credit', 1, 1, 'C')



	mydb = sqlite3.connect("smartcompta.db")
	cur = mydb.cursor()
	cur.execute("SELECT * FROM compte WHERE debit !=0 or credit!=0")
	print(" Compte     \tIntitulé   \tT Debit        \tT Credit      \tSC Debit      \tSC Cloture")
	print("-------------------------------------------------------------------------------------------------")
	for row in cur:
		compte= row[0]
		intitulé= row[1]
		debit= row[2]
		credit= row[3]
		solde = debit - credit
		s_debit = 0
		s_credit = 0

		if solde <0:
			s_debit = "--"
			s_credit = abs(solde)
			

		elif solde >0:
			s_debit = solde
			s_credit = "--"
			

		else :
			s_debit = solde
			s_credit = solde
		print("{}      {}          {}     {}       {}      {}".format(compte,intitulé,debit,credit,s_debit,s_credit))

		pdf.cell(2, 1, str(compte), 1, 0, 'C')
		pdf.cell(5, 1, str(intitulé), 1, 0, 'C')
		pdf.cell(3, 1, str(debit), 1, 0, 'C')
		pdf.cell(3, 1, str(credit), 1, 0, 'C')
		pdf.cell(3, 1, str(s_debit), 1, 0, 'C')
		pdf.cell(3, 1, str(s_credit), 1, 1, 'C')
	pdf.output('Balance.pdf', 'F')
	os.startfile('Balance.pdf')

	mydb.close()