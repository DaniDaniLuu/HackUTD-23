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

    # add empty columns Populate an entire column with values of True or False, depending on if they are approved or not
    # calculateApproval(CreditScore)
    # calculate LTV, DTI, and FEDTI
    df['LIV'] = df['AppraisedValue'] - df['DownPayment']
    df['DTI'] = df['MonthlyDebt']/df['GrossMonthlyIncome']
    df['FEDTI'] = df['MonthlyMortgagePayment']/df['GrossMonthlyIncome']
    return df.head(5)
    #df['Approval'] = df.apply(filler_func, axis=0, raw=False, result_type=broadcast, args=())

    #df['negative_credit_score_impact'] = ''
    #df['negative_credit_card_payment_impact'] = ''
    #df['negative_mortgage_payment_impact'] = ''

    # super simple, if credit score is lower than a certain value, make true
    

    # not as simple, if LTV is <80%, make true
    #df['negative_credit_card_payment_impact'] = np.where(df.['CreditCardPayment'])

