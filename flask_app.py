from flask import Flask, render_template
import data_algorithms
import data_analysis

app = Flask(__name__)

@app.route('/')
def homepage():
    
    #output = str(test_input())
    #return output
    # ^ DK Comments
    return data_analysis.data_analysis()


def test_input():
    ID = 1
    gross_monthly_income = 3103.00
    credit_card_payment = 317.00
    car_payment = 374.00
    student_loan_payments = 250.00
    appraised_value = 268468.00
    down_payment = 32216.16
    loan_amount = 236251.84
    LTV = data_algorithms.get_LTV(appraised_value, down_payment)
    # Make sure to access monthly_mortgage_payment after the if statement to get accurate value
    monthly_mortgage_payment = 1127.90
    if data_algorithms.PMI_required(LTV):
        monthly_mortgage_payment *= 1.01
    credit_score = 778

    
    return LTV

    #DTI = ''
    #FEDTI = ''