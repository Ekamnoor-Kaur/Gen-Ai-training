# binary classification
# X_test, y_pred : simple model score
# X_test, y_test :X_test value internally test  then trai and then gicvee score
# y_test, y_pred: compare behvave score generates 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
x=np.random.random(30)
print(x)

plt.plot(x)
# plt.show()

# create sigmoid function
def sigmoid_func(x):
    return 1/(1+2.71**(-x))

sigmoid_x=sigmoid_func(x)
plt.plot(sigmoid_x)
# plt.show()

new_x=np.linspace(-10,10,20)
sigmoid_x_new=sigmoid_func(new_x)
plt.plot(sigmoid_x_new)
# plt.show()

df=pd.read_csv("myinsurance.csv")
print(df)

# start EDA
print(df.shape)
print(df.columns)
print(df.info())
print(df.corr(numeric_only=True))

text_data=list[df.select_dtypes(str).columns]
print(text_data)

df.sample()
for i in text_data:
    print(f"Analysis Data {i}")
    print(df[i].value_counts)

df["Gender"]=df["Gender"].replace({'Male':0,'Female':1})
df["Buy_Insurance"]=df["Buy_Insurance"].replace({'No':0,'Yes':1})
df["Marital_Status"]=df["Marital_Status"].replace({'Single':0,'Married':1})
print(df)
df.corr().round(2)

X=df.drop(columns=["Buy_Insurance","Customer_ID"])
y=df["Buy_Insurance"]
print(X)
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("model prediction is ",y_pred)

res=sigmoid_func(y_pred)
print(res)

final_ypred=[round(i) for i in sigmoid_func(y_pred)]
print(final_ypred)
score=model.score(X_test,y_test)
print("Model score is ",score)

model_logistic=LogisticRegression()
print(y_train.dtype)
y_train=y_train.astype(int)
print(y_train.dtype)

model_logistic.fit(X_train,y_train)
y_predict=model_logistic.predict(X_test)
print("prdiction of y is",y_predict)
score_log=model.score(X_test,y_test)
print("model score",score_log)

age=int(input("Enter age"))
gender=int(input("Enter gender male:0 female:1"))
income=int(input("Enter  income"))
status=int(input("Enter employee status"))
maritial=int(input("Enter maritial status single:0 married:1"))
married=int(input("enter married status"))
prev_ins=int(input("enter previous insurance"))
f_size=int(input("Enter family size"))

new_data=[[age,gender,income,status,maritial,married,prev_ins,f_size]]
prediction1=model_logistic.predict(new_data)[0]
answer = "Yes" if prediction1 >= 0.5 else "No"

print("Predicted Buy Insurance:" ,answer)
print("Calculated Score/Probability:", prediction1)
print("Model Accuracy Score: ",score * 100,"%")