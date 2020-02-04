import pandas as pd


df = pd.read_excel('201912list.xlsx', sheet_name='Sheet1')

print("Column headings: ")
print(df.columns)
count = 0
for row in df.itertuples():
    if getattr(row, "_5") != '가격문의':
        count +=1
        print(row)

print(count)