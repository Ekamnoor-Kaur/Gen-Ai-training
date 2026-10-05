import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression,LogisticRegression 

df=pd.read_csv("house_prce.csv")
print(df)
print("shape",df.shape)
print("columns",df.columns)
print("info",df.info)

nullvalues=df.isnull().sum()
print(nullvalues)

plt.figure(figsize=(25,25))
sns.heatmap(df.isnull())
plt.show()

nullvalue_per=df.isnull().sum()/df.shape[0]*100
print("null values percentage:",nullvalue_per)

finalnullcol=nullvalue_per[nullvalue_per>5].keys()
df_cols=df.drop(columns=finalnullcol)

plt.figure(figsize=(25,25))
sns.heatmap(df_cols.isnull())
plt.show()

df_rows=df_cols.dropna()
plt.figure(figsize=(25,25))
sns.heatmap(df_rows.isnull())
plt.show()

df=df_rows
print(df)

text_content=list(df.select_dtypes(str).columns)
print("text content",text_content)

X=df.drop(columns=['House_ID','Location','Price'])
y=df["Price"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("X_train",X_train.shape)
print("X_test",X_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)

model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("model prediction is ",y_pred)
model_score=model.score(X_test,y_test)
print('model score is',model_score)