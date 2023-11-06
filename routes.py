from flask import Blueprint, request, jsonify
import data_algorithms
import data_analysis

input_bp = Blueprint('input', __name__)
calc_bp = Blueprint('calc', __name__)
analyze_bp = Blueprint('analyze', __name__)

# Global variables to remember
LTV = 0.0
monthly_debt = 0.0
DTI = 0.0
FEDTI = 0.0
evaluated_credit_score = ""
evaluated_LTV = ""
evaluated_DTI = ""
evaluated_FEDTI = ""
approval_status = False
total_score = 0.0

# From input
gross_monthly_income = 0.0
credit_card_payment = 0.0
car_payment = 0.0
student_loan_payments = 0.0
appraised_value = 0.0
down_payment = 0.0
loan_amount = 0.0
monthly_mortgage_payment = 0.0
credit_score = 0.0

# Read in all variables to update global variables
@input_bp.route('/input', methods=['POST'])
def input_variables():
    
    # Read input from POST
    data = request.get_json()
    gross_monthly_income = float(data["GMI"])
    credit_card_payment = float(data["creditP"])
    car_payment = float(data["carP"])
    student_loan_payments = float(data["studentP"])
    appraised_value = float(data["house"])
    down_payment = float(data["downP"])
    loan_amount = float(data["loan"])
    monthly_mortgage_payment = float(data["monthly"])
    credit_score = float(data["credit"])

# Return LTV
@calc_bp.route('/LTV', methods=['POST'])
def calculate_LTV():
    
    # Return LTV value in json format by creating dictionary with the float variable
    LTV = data_algorithms.get_LTV(appraised_value, down_payment)
    LTV_dict = {'LTV': LTV}

    return jsonify(LTV_dict)

# Return updated monthly mortgage payment (either unchanged or changed for PMI)
@calc_bp.route('/update-monthly-mortgage-payment-with-PMI', methods=['GET'])
def update_monthly_with_PMI():

    if data_algorithms.PMI_required(LTV):
        monthly_mortgage_payment *= 1.01
    
    # Return monthly_mortgage_payment value in json format by creating dictionary with the float variable
    updated_monthly_dict = {'updated_monthly': monthly_mortgage_payment}
    
    return jsonify(updated_monthly_dict)

# Return monthly debt (added credit card payment, car payment, student loan payments, and monthly mortgage payment)
@calc_bp.route('/monthlydebt', methods=['GET'])
def get_monthlydebt():

    monthly_debt = data_algorithms.get_total_debt(credit_card_payment, car_payment, student_loan_payments, monthly_mortgage_payment)
    
    # Return monthly debt in json format by creating dictionary with the float variable
    monthly_debt_dict = {'monthly_debt': monthly_debt}
    
    return jsonify(monthly_debt_dict)

# Return DTI
@calc_bp.route('/DTI', methods=['GET'])
def get_DTI():

    DTI = data_algorithms.get_DTI(monthly_debt, gross_monthly_income)
    
    # Return DTI in json format by creating dictionary with the float variable
    DTI_dict = {'DTI': DTI}
    
    return jsonify(DTI_dict)

# Return FEDTI
@calc_bp.route('/FEDTI', methods=['GET'])
def get_FEDTI():

    FEDTI = data_algorithms.get_FEDTI(monthly_mortgage_payment, gross_monthly_income)
    
    # Return FEDTI in json format by creating dictionary with the float variable
    FEDTI_dict = {'FEDTI': FEDTI}
    
    return jsonify(FEDTI_dict)

# Return evaluated credit score ("GOOD", "OKAY", "BAD")
@calc_bp.route('/evaluated-creditscore', methods=['GET'])
def get_evaluated_creditscore():

    evaluated_credit_score = data_algorithms.evaluate_credit_score(credit_score)
    
    # Return in json format by creating dictionary with the string variable
    eval_credit_score_dict = {'eval_credit_score': evaluated_credit_score}
    
    return jsonify(eval_credit_score_dict)

# Return evaluated LTV ("GOOD", "OKAY", "BAD")
@calc_bp.route('/evaluated-LTV', methods=['GET'])
def get_evaluated_LTV():

    evaluated_LTV = data_algorithms.evaluate_LTV(LTV)
    
    # Return in json format by creating dictionary with the string variable
    eval_LTV_dict = {'eval_LTV': evaluated_LTV}
    
    return jsonify(eval_LTV_dict)

# Return evaluated DTI ("GOOD", "GOOD-MD", "OKAY", "OKAY-MD", "BAD")
@calc_bp.route('/evaluated-DTI', methods=['GET'])
def get_evaluated_DTI():

    evaluated_DTI = data_algorithms.evaluate_DTI(DTI, monthly_mortgage_payment, monthly_debt)
    
    # Return in json format by creating dictionary with the string variable
    eval_DTI_dict = {'eval_DTI': evaluated_DTI}
    
    return jsonify(eval_DTI_dict)

# Return evaluated FEDTI ("GOOD", "OKAY", "BAD")
@calc_bp.route('/evaluated-FEDTI', methods=['GET'])
def get_evaluated_FEDTI():

    evaluated_FEDTI = data_algorithms.evaluate_FEDTI(FEDTI)
    
    # Return in json format by creating dictionary with the string variable
    eval_FEDTI_dict = {'eval_FEDTI': evaluated_FEDTI}
    
    return jsonify(eval_FEDTI_dict)

# Return approval status (True/False)
@calc_bp.route('/approval-status', methods=['GET'])
def get_approval_status():

    approval_status = data_algorithms.approval_status(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)
    
    # Return in json format by creating dictionary with the boolean variable
    approval_status_dict = {'approval_status': approval_status}
    
    return jsonify(approval_status_dict)

# Return total score
@calc_bp.route('/total-score', methods=['GET'])
def get_total_score():

    total_score = data_algorithms.total_score(evaluated_credit_score, evaluated_LTV, evaluated_DTI, evaluated_FEDTI)
    
    # Return in json format by creating dictionary with the float variable
    total_score_dict = {'total_score': total_score}
    
    return jsonify(total_score_dict)

# returns an array of the values we need to create a graph for approved factors.
@analyze_bp.route('/approvedgraph', methods=['GET'])
def approvedgraph():
    approval=True
    approvedarray = data_analysis.main(approval)
    data = {'array_data': approvedarray}
    return jsonify(data)

# returns an array of the values we need to create a graph for notapproved factors.
@analyze_bp.route('/notapprovedgraph', methods=['GET'])
def notapprovedgraph():
    approval=False
    notapprovedarray = data_analysis.main(approval)
    data = {'array_data': notapprovedarray}
    return jsonify(data)