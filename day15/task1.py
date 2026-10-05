import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df=pd.read_csv("housetrain.csv")
print(df)
print("shape",df.shape)

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

miss_val=df.isnull().sum()
print("missing values sum",miss_val)

miss_val_per=df.isnull().sum()/df.shape[0]*100
print("missing value percentage",miss_val_per)

final_mvalue=miss_val_per[miss_val_per>15].keys()
print("final missing values",final_mvalue)

plt.figure(figsize=(25,25))
sns.heatmap(df.isnull())
plt.show()

drop_cols=df.drop(columns=final_mvalue)
print(drop_cols.shape)

plt.figure(figsize=(25,25))
sns.heatmap(drop_cols.isnull())
plt.show()

df3=drop_cols.select_dtypes(include=['int64','float64'])
print(df3.shape)

print(df3[df3.isnull().any(axis=1)])
print(df3.isnull().sum())

missing_values=[var for var in df3.columns if df3[var].isnull().sum()>0]
print("missing value",missing_values)

df4=df3.fillna(df3.mean())
print(df4.isnull().sum().sum())
df5=df3.fillna(df3.mean())
print(df5.isnull().sum().sum())