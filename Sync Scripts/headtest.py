import win32com.client
import os
import pandas as pd
import time
######THIS IS FOR HEADCOUNT########
##Open and refresh PowerPivot Data
xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.Workbooks.Open("C:/Users/pkubier/Desktop/PY/Headcount-Pivot.xlsx")
wb.RefreshAll()
time.sleep(5)
wb.Save()
xl.Quit()
os.system("taskkill /f /im excel.exe")

##Read Excel Sheet
df = pd.read_excel('../PY/Headcount-Pivot.xlsx', sheet_name=None)
##Save to CSV
df['Sheet1'].to_csv('headcount3.csv')

##Read CSV
df2 = pd.read_csv("../PY/headcount3.csv")
##If blank rows, fill with above
df2=df2.fillna(method='ffill')


##Resave due to paranoia
df2.to_csv('headcount3.csv')
df3 = pd.read_csv("../PY/headcount3.csv")
##Rename colums to something readable

df3 = df3.drop(df3.columns[[0,1]], axis=1)
df3 = df3.iloc[0:]

df3.to_csv('headcount3.csv', index=False, date_format='%m-%d-%Y')

##other random shit to make the date right
parse_dates = [0]
date_cols = [0]

df = pd.read_csv("headcount3.csv", index_col=0, header = None, parse_dates=date_cols)
df = df.iloc[0:]

##customer_calls.index = pd.to_datetime(customer_calls.index).strftime("%m-%d-%Y")
df.to_csv("hc.csv", date_format='%m-%d-%Y')

##Start combo time
import csv

with open('../PY/hc.csv', 'r') as f1:
    next(f1)
    original = f1.read()

with open('X:/UCO/data/headcount.csv', 'a') as f2:
##    f2.write('\n')
    f2.write(original)
    

df = pd.read_csv("X:/UCO/data/headcount.csv", index_col=0, header=None)
df.drop(df.head(1).index, inplace=True)
df.to_csv("X:/UCO/data/headcount.csv", header=None)
    
####THIS IS FOR CREDIT HOURS ENROLLED########
##Open and refresh PowerPivot Data
xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.Workbooks.Open("C:/Users/pkubier/Desktop/PY/Credithour-Pivot.xlsx")
wb.RefreshAll()
time.sleep(5)
wb.Save()
xl.Quit()
os.system("taskkill /f /im excel.exe")

##Read Excel Sheet
df = pd.read_excel('../PY/Credithour-Pivot.xlsx', sheet_name=None)
##Save to CSV
df['Sheet1'].to_csv('credithour3.csv')

##Read CSV
df2 = pd.read_csv("../PY/credithour3.csv")
##If blank rows, fill with above
df2=df2.fillna(method='ffill')


##Resave due to paranoia
df2.to_csv('headcount3.csv')
df3 = pd.read_csv("../PY/credithour3.csv")
##Rename colums to something readable

df3 = df3.drop(df3.columns[[0]], axis=1)
df3 = df3.iloc[0:]

df3.to_csv('credithour3.csv', index=False, date_format='%m-%d-%Y')

##other random shit to make the date right
parse_dates = [0]
date_cols = [0]

df = pd.read_csv("credithour3.csv", index_col=0, header = None, parse_dates=date_cols)
df = df.iloc[0:]

##customer_calls.index = pd.to_datetime(customer_calls.index).strftime("%m-%d-%Y")
df.to_csv("ch.csv", date_format='%m-%d-%Y')
##Start combo time
import csv

with open('../PY/ch.csv', 'r') as f1:
    next(f1)
    original = f1.read()

with open('X:/UCO/data/credithour.csv', 'a') as f2:
##    f2.write('\n')
    f2.write(original)

df = pd.read_csv("X:/UCO/data/credithour.csv", index_col=0, header=None)
df.drop(df.head(1).index, inplace=True)
df.to_csv("X:/UCO/data/credithour.csv", header=None)

