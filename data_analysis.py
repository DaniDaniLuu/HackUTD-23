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
        if row['LTV'] < .8:
            return "GOOD"
        elif row['LTV'] >= .8 and row['LTV'] < .9500001:
            return "OKAY"
        else:
            return "BAD"

    df['EVAL_LTV'] = df.apply(eval_rows_LTV, axis=1)
    #df['Approval'] = 






    print(df.iloc[0])
    print(df.iloc[1])
    print(df.iloc[2])
    print(df.iloc[3])
    print(df.iloc[4])
    print(df.iloc[5])
    print(df.iloc[6])
    print(df.iloc[7])

    
    return 'meow'
    #df['Approval'] = df.apply(filler_func, axis=0, raw=False, result_type=broadcast, args=())

    #df['negative_credit_score_impact'] = ''
    #df['negative_credit_card_payment_impact'] = ''
    #df['negative_mortgage_payment_impact'] = ''

    # super simple, if credit score is lower than a certain value, make true
    

    # not as simple, if LTV is <80%, make true
    #df['negative_credit_card_payment_impact'] = np.where(df.['CreditCardPayment'])

