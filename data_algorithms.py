
def valid_credit_score(credit_score):
    if credit_score >= 640 and credit_score <= 850:
        return True

def debt_income_ratio(monthly_debt, gross_income):
    return monthly_debt / gross_income

def get_total_debt(credit_card_payment, car_payment, student_loans_payments, monthly_mortgage_payment):
    return total_debt = credit_card_payment + car_payment + student_loans_payments + monthly_mortgage_payment