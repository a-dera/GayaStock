from fpdf import FPDF 
#generate a receipt

def generate_receipt(date, amount):
    x = FPDF(orientation='P', unit='pt', format='A4')
    x.add_page()
    x.set_font("Times","B",24)
    x.cell(0,80, "Facture d'Achat", 0,1, "C")
    x.set_font("Times","B",14)
    x.cell(100,25, "Date de paiement: ")
    x.set_font("Times","",12)
    x.cell(0,25, "{}".format(date), 0,1)
    x.cell(0,5,"",0,1)
    x.set_font("Times","B",14)
    x.cell(100,25, "Montant total: ",)
    x.set_font("Times","",12)
    x.cell(0,25, "{} franc CFA".format(amount), 0,1)

    return x.output("test_fpdf.pdf")


generate_receipt('30/04/2020', 10000 )
