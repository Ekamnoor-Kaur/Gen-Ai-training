import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression,LogisticRegression

df=pd.read_csv("housetrain.csv")
print(df)
print("shape: ",df.shape)
print("columns: ",df.columns)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# removing null values
missing_val=df.isnull().sum()
print(missing_val)

plt.figure(figsize=(15,15))
sns.heatmap(df.isnull())
plt.show()

missing_val_per=df.isnull().sum()/df.shape[0]*100
print("missing values percentage: ",missing_val_per)

final_miss_val=missing_val_per[missing_val_per>15].keys()
print(final_miss_val)

drop_cols=df.drop(columns=final_miss_val)

plt.figure(figsize=(15,15))
sns.heatmap(drop_cols.isnull())
plt.show()

drop_rows=drop_cols.dropna()

plt.figure(figsize=(15,15))
sns.heatmap(drop_rows.isnull())
plt.show()

df=drop_rows
print(df.shape)

# replacing and removeing columns containing string
text_content=list(df.select_dtypes(str).columns)
print(text_content)
# text content: 'MSZoning', 'Utilities', 'HouseStyle', 'ExterQual', 'Foundation','BsmtQual', 'CentralAir', 'Electrical', 'GarageType', 'PavedDrive',
# print(df["SaleCondition"].unique())

df["HouseStyle"] = df["HouseStyle"].replace({"1Story": 1, "1.5Story": 1.5, "2Story": 2,"2.5Story":2.5})
df["ExterQual"] = df["ExterQual"].replace({"Fa": 0, "TA": 1, "Gd": 2, "Ex": 3})
df["BsmtQual"] = df["BsmtQual"].replace({"Fa": 0, "TA": 1, "Gd": 2, "Ex": 3})
df["CentralAir"] = df["CentralAir"].replace({"N": 0, "Y": 1})
df["GarageType"] = df["GarageType"].replace({"NoGarage": 0, "Detchd": 1, "Attchd": 2, "BuiltIn": 3})
df["PavedDrive"] = df["PavedDrive"].replace({"N": 0, "P": 1, "Y": 2})
print(df.shape)

X=df.drop(columns=["MSZoning","Utilities","Foundation","Electrical","SaleType","SaleCondition","SalePrice"])
y=df["SalePrice"]
print("shape of X",X.shape)
print("shape of y",y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model=LinearRegression()

model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("model prediction ",y_pred)
model_score=model.score(X_test,y_test)
print("model score:",model_score)
