from flask import Flask, render_template
import data_algorithms
import data_analysis

app = Flask(__name__)

@app.route('/calculation')
def calculation():
    # This data would have to be passed in from the jsx form
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

    monthly_debt = data_algorithms.get_total_debt(credit_card_payment, car_payment, student_loan_payments, monthly_mortgage_payment)
    DTI = data_algorithms.get_DTI(monthly_debt, gross_monthly_income)
    FEDTI = data_algorithms.get_FEDTI(monthly_mortgage_payment, gross_monthly_income)
    
    # Inputted data's "GOOD"s "OKAY"s "BAD"s etc
    evaluated_credit_score = data_algorithms.evaluate_credit_score(credit_score)
    evaluated_LTV = data_algorithms.evaluate_LTV(LTV)
    evaluated_DTI = data_algorithms.evaluate_DTI(DTI, monthly_mortgage_payment, monthly_debt)
    evaluated_FEDTI = data_algorithms.evaluate_FEDTI(FEDTI)

    # Approval status
    approval_status = data_algorithms.approval_status(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)

    # Total score
    total_score = data_algorithms.total_score(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)
