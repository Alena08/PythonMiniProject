# pip install pandas

import pandas as pd

# Series (1D Array)

s = pd.Series([10,20,30,40])
print(s)
print(type(s))

data = {
    'Name':["Alena","Ali","Rayen","Maria",None,"Alena","Ali","Rayen","Maria","Daria"],
    'Age': [34,43,26,None,32,45,66,43,23,45]
}

df = pd.DataFrame(data)
print(df)
print(type(df))

# CSV File
df_1 = pd.read_csv("my_dataFrame.csv")
print(df_1)

# Excel File
df_2 = pd.read_excel("my_dataFrame.xlsx")
print(df_2)

# Select Column
print(df['Age'])

# Select multiple Columns
print(df[['Age','Name']])

# Filter
print(df[df['Age']>=35])

# loc, iloc Select rows by index
print(df.iloc[0])
print(df.loc[1])

# Daten Ändern / Modifying data

## Add new Column / neue Splate einfügen
df['AgePlus10'] = df['Age']+10
print(df)

# Rename column
#df_n = df.rename(columns={'Age':'Years'}, inplace=False)
df.rename(columns={'Age':'Years'}, inplace=True)
print(df)
#print(df_n)

# Drop Columns / Spalte löschen
df.drop('AgePlus10',axis=1, inplace=True)
print(df)

# Handling missing Data

# Find missing value
print(df.isnull().sum())

# Fill missing values
df_rn = df.fillna(0)
print(df_rn)

# Remove rows with missing values
df_rr=df.dropna()
print(df_rr)

# Grouping & Aggregating

# Group by a column

print(df.groupby('Name')['Years'].mean())

# Multiple Aggs.

df_gp=df.groupby('Name').agg({'Years':['mean','max','min']}) 
print(df_gp)

# Saving Data

# CSV
df.to_csv("names.csv", index=False)

# Excel
df.to_excel("names.xlsx", index=False)