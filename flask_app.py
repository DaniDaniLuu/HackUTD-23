from flask import Flask, render_template
import data_algorithms
app = Flask(__name__)

@app.route('/')
def homepage():
    
    output = str(test_input())
    return output

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
    # return data_algorithms.debt_income_ratio(monthly_mortgage_payment, gross_monthly_income)

    LTV = data_algorithms.get_LTV(appraised_value, down_payment)
    return LTV

    #DTI = ''
    #FEDTI = ''