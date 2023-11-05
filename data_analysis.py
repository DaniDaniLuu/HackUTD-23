# Need to check data inputs to determine which of the 3 negatively impact their loan acceptance odds
import pandas as pd
import numpy as np
import data_algorithms
import json
# input into df the csv file of HomeBuyerInfo
file_path = 'HackUTD-2023-HomeBuyerInfo.csv'
df = pd.read_csv(file_path)

def main(approve):   
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 100)  # Set a width of 100 characters for columns
    pd.set_option('display.width', 120)  # Set the console display width to 120 characters

    # Expand the columns of our csv to include new EVAL and Totals information
    expand_tabular(df)
    # Create 2 new separate dataframes that total in 10000 entries, but with separate Approval statuses.
    a_df = approved_rows_dataframe(df)
    na_df = not_approved_rows_dataframe(df)
    count = a_df['APPROVAL'].value_counts().get("Approved", 0)
    nacount = na_df['APPROVAL'].value_counts().get("Not Approved", 0)
    # Derive the count of different comparison factors for approved dataframe.
    good_credit_score_count = a_df['EVAL_CS'].value_counts().get("GOOD", 0)
    okay_credit_score_count = a_df['EVAL_CS'].value_counts().get("OKAY", 0)
    good_ltv_count = a_df['EVAL_LTV'].value_counts().get("GOOD", 0)
    okay_ltv_count = a_df['EVAL_LTV'].value_counts().get("OKAY", 0)

    good_dti_count = a_df['EVAL_DTI'].value_counts().get("GOOD", 0)
    good_md_dti_count = a_df['EVAL_DTI'].value_counts().get("GOOD-MD", 0)
    okay_dti_count = a_df['EVAL_DTI'].value_counts().get("OKAY", 0)
    okay_md_dti_count = a_df['EVAL_DTI'].value_counts().get("OKAY-MD", 0)

    good_fedti_count = a_df['EVAL_FEDTI'].value_counts().get("GOOD", 0)
    okay_fedti_count = a_df['EVAL_FEDTI'].value_counts().get("OKAY", 0)

    # Derive the count of different comparison factors for not approved dataframe.
    ngood_credit_score_count = na_df['EVAL_CS'].value_counts().get("GOOD", 0)
    nokay_credit_score_count = na_df['EVAL_CS'].value_counts().get("OKAY", 0)
    nbad_credit_score_count = na_df['EVAL_CS'].value_counts().get("BAD", 0)


    ngood_ltv_count = na_df['EVAL_LTV'].value_counts().get("GOOD", 0)
    nokay_ltv_count = na_df['EVAL_LTV'].value_counts().get("OKAY", 0)
    nbad_ltv_count = na_df['EVAL_LTV'].value_counts().get("BAD", 0)

    ngood_dti_count = na_df['EVAL_DTI'].value_counts().get("GOOD", 0)
    ngood_md_dti_count = na_df['EVAL_DTI'].value_counts().get("GOOD-MD", 0)
    nokay_dti_count = na_df['EVAL_DTI'].value_counts().get("OKAY", 0)
    nokay_md_dti_count = na_df['EVAL_DTI'].value_counts().get("OKAY-MD", 0)
    nbad_dti_count = na_df['EVAL_DTI'].value_counts().get("BAD", 0)

    ngood_fedti_count = na_df['EVAL_FEDTI'].value_counts().get("GOOD", 0)
    nokay_fedti_count = na_df['EVAL_FEDTI'].value_counts().get("OKAY", 0)
    nbad_fedti_count = na_df['EVAL_FEDTI'].value_counts().get("BAD", 0)

    # what does the barchart look like. We have for Non-approved. 
    #barchartdict = {'impactcs': [ngood_credit_score_count, nokay_credit_score_count, nbad_credit_score_count], 'impactltv': [good_ltv_count, okay_ltv_count, bad_ltv_count], 'impactdti': [good_dti_count, good_md_dti_count, okay_dti_count, okay_md_dti_count, bad_dti_count], 'impactfedti': [good_fedti_count, okay_fedti_count, bad_fedti_count]}
    
    approved_array = [good_credit_score_count/count, okay_credit_score_count/count, good_ltv_count/count, okay_ltv_count/count, good_dti_count/count, good_md_dti_count/count, okay_dti_count/count, okay_md_dti_count/count, good_fedti_count/count, okay_fedti_count/count]
    
    notapproved_array = [ngood_credit_score_count/nacount, nokay_credit_score_count/nacount, nbad_credit_score_count/nacount, ngood_ltv_count/nacount, nokay_ltv_count/nacount, nbad_ltv_count/nacount, ngood_dti_count/nacount, ngood_md_dti_count/nacount, nokay_dti_count/nacount, nokay_md_dti_count/nacount, nbad_dti_count/nacount, ngood_fedti_count/nacount, nokay_fedti_count/nacount, nbad_fedti_count/nacount]
    if (approve == True):
        return approved_array
    else:
        return notapproved_array

def return_dataframe():
        return df.to_json()

def expand_tabular(df):    

    # add empty columns and populate with respective values from columns.
    # calculate LTV, DTI, and FEDTI
    df['LTV'] = (df['AppraisedValue'] - df['DownPayment'])/df['AppraisedValue']
    df['DTI'] = (df['CreditCardPayment'] + df['CarPayment'] + df['StudentLoanPayments'] + df['MonthlyMortgagePayment'])/df['GrossMonthlyIncome']
    df['FEDTI'] = df['MonthlyMortgagePayment']/df['GrossMonthlyIncome']


    def eval_rows_CS(row):
        if (row['CreditScore'] >= 670 and row['CreditScore'] <= 850):
            return "GOOD"
        if (row['CreditScore'] >= 640 and row['CreditScore'] < 670):
            return "OKAY"
        if (row['CreditScore'] < 640):
            return "BAD"

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




    # populate 3 new columns to evaluate the conditions of these values.
    df['EVAL_CS'] = df.apply(eval_rows_CS, axis=1)
    df['EVAL_LTV'] = df.apply(eval_rows_LTV, axis=1)
    df['EVAL_DTI'] = df.apply(eval_rows_DTI, axis=1)
    df['EVAL_FEDTI'] = df.apply(eval_rows_FEDTI, axis=1)
    

    def approval_rows_status(row):
        if (row['EVAL_CS'] != "BAD" and row['EVAL_LTV'] != "BAD" and row['EVAL_DTI'] != "BAD" and row['EVAL_FEDTI'] != "BAD"):
            return "Approved"
        else:
            return "Not Approved"

    df['APPROVAL'] = df.apply(approval_rows_status, axis=1)


    # acquire total score and store as value in last column.
    def rows_total_score(row):
        if row['EVAL_CS'] == "GOOD":
            points_credit_score = 3.5
        elif row['EVAL_CS'] == "OKAY":
            points_credit_score = 2.6
        else:
            points_credit_score = 1.1

        if row['EVAL_LTV'] == "GOOD":
            points_LTV = 2
        elif row['EVAL_LTV'] == "OKAY":
            points_LTV = 1.4
        else:
            points_LTV = .8

        if row['EVAL_DTI'] == "GOOD":
            points_DTI = 2.5
        elif row['EVAL_DTI'] == "GOOD-MD":
            points_DTI = 2.1
        elif row['EVAL_DTI'] == "OKAY":
            points_DTI = 1.8
        elif row['EVAL_DTI'] == "OKAY-MD":
            points_DTI = 1.4
        else:
            points_DTI = .6

        if row['EVAL_FEDTI'] == "GOOD":
            points_FEDTI = 2
        elif row['EVAL_FEDTI'] == "OKAY":
            points_FEDTI = 1.3
        else:
            points_FEDTI = .9

        total_points = points_credit_score + points_LTV + points_DTI + points_FEDTI
        return total_points

    df['TOTAL_SCORE'] = df.apply(rows_total_score, axis = 1)   


def approved_rows_dataframe(df):
    a_df = df[df['APPROVAL'] == 'Approved']
    return a_df

def not_approved_rows_dataframe(df):
    not_a_df = df[df['APPROVAL'] == 'Not Approved']
    return not_a_df
