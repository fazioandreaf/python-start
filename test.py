import pandas as pd
file = pd.ExcelFile('sales.xlsx')
# print(file.sheet_names)
sheet = file.parse('sales')
# print(sheet)
# type(sheet)
# print(sheet.Date)
sheet.Amount.sum()

# locate, search
sheet.loc[0, 'Amount']
sheet.set_index('Customer', inplace=True)
sheet.loc['MMC Inc.']
sheet = sheet.reset_index()

type(sheet['Invoice'])
sheet.loc[sheet['Invoice'] == 99]
sheet.loc[sheet['Amount'] > 2000]
sheet.loc[sheet['Amount'].idxmax()]
for customer in sheet.loc[sheet['Amount'] > 1800]["Customer"].unique():
    print(customer)