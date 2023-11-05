from flask import Flask, render_template, request, jsonify
import data_algorithms
import data_analysis

app = Flask(__name__)

@app.route('/calculation', methods=['POST'])
def calculation():
    # Array of information to pass back with 11 values
    # LTV value, PMI required (True/False), monthly debt value, DTI value, FEDTI value, credit score enum, LTV enum, DTI enum, FEDTI enum, approval status (True/False), total score value
    #    0                  1                        2              3           4              5              6          7          8                   9                       10 
    return_list = []
    
    # This data would have to be passed in from the jsx form
    #ID = 1 (not relevant to calculation)
    gross_monthly_income = request.form.get("Credit Payment")
    credit_card_payment = request.form.get("Credit Payment")
    car_payment = request.form.get("Car Payment")
    student_loan_payments = request.form.get("Student Loan Payment")
    appraised_value = request.form.get("House Appraisal")
    down_payment = request.form.get("Down Payment")
    loan_amount = request.form.get("Loan Amount")
    LTV = data_algorithms.get_LTV(appraised_value, down_payment)
    return_list.append(LTV) # Index @ 0 = LTV
    # Make sure to access monthly_mortgage_payment after the if statement to get accurate value
    monthly_mortgage_payment = request.form.get("Monthly Mortgage")
    if data_algorithms.PMI_required(LTV):
        monthly_mortgage_payment *= 1.01
        return_list.append(True) 
    else:
        return_list.append(False)

    credit_score = request.form.get("Credit Score")

    # Additional calculations based on input
    monthly_debt = data_algorithms.get_total_debt(credit_card_payment, car_payment, student_loan_payments, monthly_mortgage_payment)
    DTI = data_algorithms.get_DTI(monthly_debt, gross_monthly_income)
    FEDTI = data_algorithms.get_FEDTI(monthly_mortgage_payment, gross_monthly_income)

    return_list.append(monthly_debt)
    return_list.append(DTI)
    return_list.append(FEDTI)
    
    # Inputted data's "GOOD"s "OKAY"s "BAD"s etc
    evaluated_credit_score = data_algorithms.evaluate_credit_score(credit_score)
    evaluated_LTV = data_algorithms.evaluate_LTV(LTV)
    evaluated_DTI = data_algorithms.evaluate_DTI(DTI, monthly_mortgage_payment, monthly_debt)
    evaluated_FEDTI = data_algorithms.evaluate_FEDTI(FEDTI)

    return_list.append(evaluated_credit_score)
    return_list.append(evaluated_LTV)
    return_list.append(evaluated_DTI)
    return_list.append(evaluated_FEDTI)

    # Approval status
    approval_status = data_algorithms.approval_status(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)
    return_list.append(approval_status)

    # Total score
    total_score = data_algorithms.total_score(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)
    return_list.append(total_score)

    return jsonify(return_list)

@app.route('/analysis')
def analysis():
    data_analysis.main()