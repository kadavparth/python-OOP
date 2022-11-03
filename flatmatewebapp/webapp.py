from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from main import Bill, Flatmate, PdfReport
from fpdf import FPDF

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("index.html", billform = bill_form)

class BillFormPage(MethodView):

    def get(self):
        bill_form1 = BillForm()
        return render_template('bill_form_page.html', billform=bill_form1)

class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = int(billform.amount.data)

        bill1 = Bill(amount, billform.period.data)
        fl1 = Flatmate(billform.name1.data, billform.days1.data)
        fl2 = Flatmate(billform.name2.data, billform.days2.data)
        return render_template('results_page.html',name1 = fl1.name,amount1 = fl1.pays(bill1,fl2),name2 = fl2.name,amount2 = fl2.pays(bill1,fl1))


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    name1 = StringField("Enter name of first roommate: ")
    days1 = StringField("Enter number of days lived: ")
    name2 = StringField("Enter name of second roommate: ")
    days2 = StringField("Enter number of days lived: ")

    button = SubmitField("Calculate")
    button1 = SubmitField("Go to Bill Form Page")

app.add_url_rule('/',view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill',view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)