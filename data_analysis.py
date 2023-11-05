# Need to check data inputs to determine which of the 3 negatively impact their loan acceptance odds
import pandas as pd
import numpy as np
import data_algorithms

def data_analysis():    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 100)  # Set a width of 100 characters for columns
    pd.set_option('display.width', 120)  # Set the console display width to 120 characters

    file_path = 'HackUTD-2023-HomeBuyerInfo.csv'
    df = pd.read_csv(file_path)

    # add empty columns and populate with respective values from columns.
    # calculate LTV, DTI, and FEDTI
    df['LTV'] = (df['AppraisedValue'] - df['DownPayment'])/df['AppraisedValue']
    df['DTI'] = (df['CreditCardPayment'] + df['CarPayment'] + df['StudentLoanPayments'] + df['MonthlyMortgagePayment'])/df['GrossMonthlyIncome']
    df['FEDTI'] = df['MonthlyMortgagePayment']/df['GrossMonthlyIncome']

    # definte function to evaluate LTV condition
    def eval_rows_LTV(row):
        if (row['LTV'] < .8):
            return "GOOD"
        elif (row['LTV'] >= .8 and row['LTV'] < .9500001):
            return "OKAY"
        else:
            return "BAD"

    def eval_rows_DTI(row):
        if (row['DTI'] > .43):
            # These text statements can be replaced with any numbers that we prefer to determine
            # levels of acceptability.
            return "BAD" # This DTI is not acceptable. Lowering a DTI can involve transferring high interest loans to a low interest credit card, but also consider having too many credit cards can negatively impact home buying power.
        elif (row['DTI'] <= .43 and row['DTI'] > .36):
            if (row['MonthlyMortgagePayment'] / (row['CreditCardPayment'] + row['CarPayment'] + row['StudentLoanPayments'] + row['MonthlyMortgagePayment']) > .28):
                return "OKAY-MD" # This DTI is acceptable, but too high to be preferred by lenders, also more than 28% of your monthly debt is going to servicing a mortgage which lenders do not prefer.
            else:
                return "OKAY" # This DTI is acceptable, but too high to be preferred by lenders.
        elif (row['DTI'] <= .36):
            if (row['MonthlyMortgagePayment'] / (row['CreditCardPayment'] + row['CarPayment'] + row['StudentLoanPayments'] + row['MonthlyMortgagePayment']) > .28):
                return "GOOD-MD" # This DTI is acceptable, however more than 28% of your monthly debt is going to servicing a mortgage which lenders do not prefer.
            else:
                return "GOOD" # This DTI is acceptable.

    def eval_rows_FEDTI(row):
          # These strings can also be replaced with any sort of input validation necessary.
        if (row['FEDTI'] <= .25):
            return "GOOD" # Your FEDTI is acceptable.
        elif (row['FEDTI'] < .25 and row['FEDTI'] <= .28):
            return "OKAY" # Your FEDTI is acceptable, but could be lower.
        else:
            return "BAD" # Your FEDTI needs to be lower than 28%.

    def eval_rows_CS(row):
        if (row['CreditScore'] >= 670 and row['CreditScore'] <= 850):
            return "GOOD"
        if (row['CreditScore'] >= 640 and row['CreditScore'] < 670):
            return "OKAY"
        if (row['CreditScore'] < 640):
            return "BAD"



    # populate 3 new columns to evaluate the conditions of these values.
    df['EVAL_LTV'] = df.apply(eval_rows_LTV, axis=1)
    df['EVAL_DTI'] = df.apply(eval_rows_DTI, axis=1)
    df['EVAL_FEDTI'] = df.apply(eval_rows_FEDTI, axis=1)
    df['EVAL_CS'] = df.apply(eval_rows_CS, axis=1)

    def approval_rows_status(row):
        if (row['EVAL_CS'] != "BAD" and row['EVAL_LTV'] != "BAD" and row['EVAL_DTI'] != "BAD" and row['EVAL_FEDTI'] != "BAD"):
            return "Approved"
        else:
            return "Not Approved"

    df['APPROVAL'] = df.apply(approval_rows_status, axis=1)

    print(df.iloc[0])
    print(df.iloc[1])
    print(df.iloc[2])

    
    return 'meow'