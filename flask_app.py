from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return 'HELLO WORLD'

def test_input():
    ID = 1
    GrossMonthlyIncome = 3103.00
    CreditCardPayment = 317.00
    CarPayment = 374.00
    StudentLoanPayments = 250.00
    AppraisedValue = 268468.00
    DownPayment = 32216.16
    LoanAmount = 236251.84
    MonthlyMortgagePayment = 1127.90
    CreditScore = 778

    #LTV = functionfromdata_algor()
    #DTI = ''
    #FEDTI = ''