# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object').shape
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number').shape
print(numerical_var)

banks=bank.drop(['Loan_ID'],axis=1)
print(type(banks))
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
print(bank_mode)
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum().values.sum())

banks.head(20)
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)


loan_approved_se=banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),['LoanAmount']] .count()
print(int(loan_approved_se))

loan_approved_nse=banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),['LoanAmount']] .count()
print(int(loan_approved_nse))

percentage_se=round(float(loan_approved_se)*100/len(banks['Loan_Status']),2)

percentage_nse=round(float(loan_approved_nse)*100/len(banks['Loan_Status']),2)

print(percentage_se,"\n",percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

mean_values=loan_groupby.agg([np.mean])
print(mean_values)





