import pandas as pd


# Reading the csv file
df_new = pd.read_csv('file.csv')

# Write to excel file
GFG = pd.ExcelWriter('quotes.xls')
df_new.to_excel(GFG, index=False)

GFG.save()
