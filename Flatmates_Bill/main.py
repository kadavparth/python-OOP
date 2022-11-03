import webbrowser
import os

from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        topay = bill.amount * weight
        return topay


class PdfReport:
    """
    Create a pdf file that contains data about the flatmates
    and their names, amount and period
    """
    def __init__(self, filename):
        self.filename = filename

    def generatepdf(self, flatmate1,flatmate2,bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4',)
        pdf.add_page()
        # add some text to the pdf)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w = 0, h = 80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.cell(w=100,h=40,txt="Period",border=1)
        pdf.cell(w=150,h=40,txt=bill.period,border=1,ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=1,ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1),2)), border=1, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://' + '/home/parth/Desktop/python_udemy_oop/Flatmates_Bill/{}'.format(self.filename))

a = float(input("Hey User, enter the bill amount"))
p = input("Input Bill period")
rm1 = input("Enter name of 1st roommate")
days1 = float(input("Enter number of days lived in the house: "))
rm2 = input("Enter name of 2nd roommate")
days2 = float(input("Enter number of days lived in the house: "))

bill1 = Bill(a, p)
rm1 = Flatmate(rm1, days1)
rm2 = Flatmate(rm2, days2)

pdfrep = PdfReport('{}'.format(p))
pdfrep.generatepdf(flatmate1=rm1, flatmate2=rm2, bill=bill1)
print(rm1.pays(bill1, rm2))
print(rm2.pays(bill1, rm1))

