import pandas as pd

df_new = pd.read_csv('result.csv')

# Write to excel file
GFG = pd.ExcelWriter('products.xls')
df_new.to_excel(GFG, index=False)

GFG.save()
