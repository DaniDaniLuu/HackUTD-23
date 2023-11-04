from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return 'HELLO WORLD'

def test_input():
    ID = 1
    gross_monthly_income = 3103.00
    credit_card_payment = 317.00
    car_payment = 374.00
    student_loan_payments = 250.00
    appraised_value = 268468.00
    down_payment = 32216.16
    loan_amount = 236251.84
    monthly_mortgage_payment = 1127.90
    credit_score = 778

    #LTV = functionfromdata_algor()
    #DTI = ''
    #FEDTI = ''