'''
Linear Regression 2nd project
emp_exp=[1,.....................,20]
emp_salary=[................]
final prediction
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data={
    "emp_exp":[1,2,4,5,7,8,9,11,13,14,16,17,19,20],
    "emp_sal":[15000,17000,20000,25000,29000,31000,34000,38000,42000,45000,49000,51000,55000,59000]
}
df=pd.DataFrame(data)
print(df)

X=df[["emp_exp"]]
y=df["emp_sal"]

model=LinearRegression()
print(model)

model.fit(X,y)

exp=int(input("Enter experience"))
sal_pred=model.predict([[exp]])
print(sal_pred)

all_sal_predict=model.predict(X)
print(all_sal_predict)

compare_df=pd.DataFrame({
   "Actual exp":X.values.flatten(),
   "Actual sal":y.values,
   "Predicted values of y":all_sal_predict
})
print(compare_df)

plt.plot(compare_df["Actual exp"],compare_df["Actual sal"], color="r", marker="o")
plt.scatter(compare_df["Actual exp"],compare_df["Predicted values of y"])
plt.title("Linear Regression")
plt.show()

MAE=(compare_df["Actual sal"]-compare_df["Predicted values of y"]).abs().mean()
print("Mean absolute Salary",  round(MAE,2))

MSE=((compare_df["Actual sal"]-compare_df["Predicted values of y"])**2).abs().mean()
print("Mean squared value",round(MSE,2))

import math
RMSE=math.sqrt(MSE)
print("root mean squared value",round(RMSE,2))

model_score=round(model.score(X,y),2)
print("After training model score is ",model_score)