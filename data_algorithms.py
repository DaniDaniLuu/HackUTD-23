
def evaluate_credit_score(credit_score):
    if credit_score >= 670 and credit_score <= 850:
        return "GOOD"
    if credit_score >= 640 and credit_score < 670:
        return "OKAY"
    if credit_score < 640:
        return "BAD"

def get_LTV(appraised_value, down_payment):
    return (appraised_value - down_payment) / appraised_value

def PMI_required(LTV):
    if LTV < 0.8:
        return True

def get_DTI(monthly_debt, gross_income):
    return monthly_debt / gross_income

def get_FEDTI(monthly_mortgage_payment, gross_income):
    return monthly_mortgage_payment / gross_income
    
def get_total_debt(credit_card_payment, car_payment, student_loans_payments, monthly_mortgage_payment):
    return credit_card_payment + car_payment + student_loans_payments + monthly_mortgage_payment

def evaluate_LTV(LTV):
    if LTV < .8:
        return "GOOD"
    elif LTV >= .8 and LTV <= .95:
        return "OKAY"
    else:
        return "BAD"

def evaluate_DTI(DTI, monthly_mortgage_payment, total_debt):
    if DTI > .43:
        # These text statements can be replaced with any numbers that we prefer to determine
        # levels of acceptability.
        return "BAD" # This DTI is not acceptable. Lowering a DTI can involve transferring high interest loans to a low interest credit card, but also consider having too many credit cards can negatively impact home buying power.
    elif DTI <= .43 and DTI > .36:
        if monthly_mortgage_payment / total_debt > .28:
             return "OKAY-MD" # This DTI is acceptable, but too high to be preferred by lenders, also more than 28% of your monthly debt is going to servicing a mortgage which lenders do not prefer.
        else:
            return "OKAY" # This DTI is acceptable, but too high to be preferred by lenders.
    elif DTI <= .36:
        if monthly_mortgage_payment / total_debt > .28:
            return "GOOD-MD" # This DTI is acceptable, however more than 28% of your monthly debt is going to servicing a mortgage which lenders do not prefer.
        else:
            return "GOOD" # This DTI is acceptable.

def evaluate_FEDTI(FEDTI):
    # These strings can also be replaced with any sort of input validation necessary.
    if FEDTI <= .25:
        return "GOOD" # Your FEDTI is acceptable.
    elif FEDTI < .25 and FEDTI <= .28:
        return "OKAY" # Your FEDTI is acceptable, but could be lower.
    else:
        return "BAD" # Your FEDTI needs to be lower than 28%.
    
def approval_status(enum_credit_score, enum_LTV, enum_DTI, enum_FEDTI):
    if enum_credit_score != "BAD":
        if enum_LTV != "BAD":
            if enum_DTI != "BAD":
                if enum_FEDTI != "BAD":
                    return True #approved
                else:
                    return False
            else: 
                return False
        else:
            return False
    else:
        return False
    
def total_score(enum_credit_score, enum_LTV, enum_DTI, enum_FEDTI):
    points_credit_score = 0
    points_LTV = 0
    points_DTI = 0
    points_FEDTI = 0
    total_points = 0
    if enum_credit_score == "GOOD":
        points_credit_score = 3.5
    elif enum_credit_score == "OKAY":
        points_credit_score = 2.6
    else:
        points_credit_score = 1.1
    if enum_LTV == "GOOD":
        points_LTV = 2
    elif enum_LTV == "OKAY":
        points_LTV = 1.4
    else:
        points_LTV = .8
    if enum_DTI == "GOOD":
        points_DTI = 2.5
    elif enum_DTI == "GOOD-MD":
        points_DTI = 2.1
    elif enum_DTI == "OKAY":
        points_DTI = 1.8
    elif enum_DTI == "OKAY-MD":
        points_DTI = 1.4
    else:
        points_DTI = .6
    if enum_FEDTI == "GOOD":
        points_FEDTI = 2
    elif enum_FEDTI == "OKAY":
        points_FEDTI = 1.3
    else:
        points_FEDTI = .9

    total_points = points_credit_score + points_LTV + points_DTI + points_FEDTI
    return total_points