
def good_credit_score(credit_score):
    if credit_score >= 640 and credit_score <= 850:
        return True

def debt_income_ratio(monthly_debt, gross_income):
    return monthly_debt / gross_income

def get_FEDTI(monthly_mortgage_payment, gross_income):
    return monthly_mortgage_payment / gross_income
    
def get_total_debt(credit_card_payment, car_payment, student_loans_payments, monthly_mortgage_payment):
    return credit_card_payment + car_payment + student_loans_payments + monthly_mortgage_payment