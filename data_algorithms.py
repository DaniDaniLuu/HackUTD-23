
def good_credit_score(credit_score):
    if credit_score >= 640 and credit_score <= 850:
        return True
"""
# Please evaluate if code is necessary. -> INPUT VALIDATION FOR ALL VALUES AFTER INPUT???

def evaluate_credit_score(credit_score):
    if credit_score >= 640 and credit_score <= 850:
        return True
    elif credit_score > 640 and credit_score <= 0:
        return False
    else:
        return "Invalid credit score."
"""

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
        return ("This DTI is not acceptable. Lowering a DTI can involve transferring high interest loans to a "
                "low interest credit card, but also consider having too many credit cards can negatively impact home buying power.")
    elif DTI <= .43 and DTI > .36:
        return "This DTI is acceptable, but too high to be preferred by lenders."
    elif DTI <= .36:
        if monthly_mortgage_payment / total_debt > .28:
            return "This DTI is acceptable, however more than 28% of your monthly debt is going to servicing a mortgage which lenders do not prefer."
        else:
            return "This DTI is acceptable."

def evaluate_FEDTI(FEDTI):
    # These strings can also be replaced with any sort of input validation necessary.
    if FEDTI <= .28:
        return "Your FEDTI is acceptable."
    else:
        return "Your FEDTI needs to be lower than 28%."