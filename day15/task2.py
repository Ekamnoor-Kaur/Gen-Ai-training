import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#1 read csv file
df=pd.read_csv("houseprice_with_nulls.csv")
print(df)
print("shape",df.shape)

# display all rows and columns 
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

#2 checking missing values
null_val=df.isnull().sum()
null_val_per=df.isnull().sum()/df.shape[0]*100
final_null_val=null_val_per[null_val_per>15].keys()
print("null values",null_val)
print("null values per",null_val_per)
print("final null values",final_null_val)

plt.figure(figsize=(12,12))
sns.heatmap(df.isnull())
plt.show()

# drop column containing large number of nan values
df_clean=df.drop(columns=final_null_val)
print("df_clean shape",df_clean.shape)

plt.figure(figsize=(12,12))
sns.heatmap(df_clean.isnull())
plt.show()

# include only those columns which have int or float values
df2=df_clean.select_dtypes(include=['int64','float64'])
print(df2.shape)
print(df2.head())

# rows which contain nan values
print("rows containing nan values")
print(df2[df2.isnull().any(axis=1)])

# getting column which contain nan values
missingvalues=[var for var in df2.columns if df2[var].isnull().sum()>0]
print("columns containing nan values",missingvalues)

#3 filling missing values with mean and median
# Fill missing value using mean 
df3=df2.fillna(df2.mean())
#4 check missing values
print(df3.isnull().sum().sum())

plt.figure(figsize=(12,12))
sns.heatmap(df3.isnull())
# plt.show()

# fill missing value using median
df4=df2.fillna(df2.median())
#4 check missing values
print(df4.isnull().sum().sum())

#5 separate X and y
X=df3.drop(columns='SalePrice')
y=df3['SalePrice']

#6 Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)
print("size of X train",X_train.shape)
print("size of X test",X_test.shape)
print("shape of y train",y_train.shape)
print("shape of y test",y_test.shape)

#7 create linear model
model=LinearRegression()

#8 train model
model.fit(X_train,y_train)

#9 prediction
y_pred=model.predict(X_test)
print("model predicted value",y_pred)
score=model.score(X_test,y_test)
print("model score",score)

# comparison between actual and predicted
compare_md={
    "Actual price":y_test,
    "Predicted value":y_pred
}
compare_md_df=pd.DataFrame(compare_md)
print("comparision between actual and model predicted price",compare_md_df)

# coef and intercept
for col, coef in zip(X_train.columns, model.coef_):
    print(col, ":", round(coef, 4))

# actual vs predicted chart
plt.scatter(y_test, y_pred)
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.title("Actual vs Predicted")
plt.show()