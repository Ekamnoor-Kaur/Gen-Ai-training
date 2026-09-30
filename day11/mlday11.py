import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
# linear regression is a class 
# model name is linear

data={
    "study-hour":[1,2,3,4,5,6,7,8,9],
    "marks":[35,45,52,64,73,80,88,92,98]
}
df=pd.DataFrame(data)
print(df)

X=df[["study-hour"]] #input
y=df["marks"] #output

#model build
model=LinearRegression()
print(model)

# model training
model.fit(X,y)

# using formulas
# c=model.intercept_
# print(round(c,2))
# m=model.coef_[0]
# print(round(m,2))
# #  formula apply y=mx+c
# study_hours=float(input("Enter study hours"))
# marks=m*study_hours+c
# if 0<=marks<=100:
#     print("predicted Value is ",round(marks,2))
# elif marks<0:
#     marks=0
#     print("predicted value is ",round(marks,2))
# else:
#     marks=100
#     print("predicted value is ",round(marks,2))


# without formals
# hour=float(input("enter study hours"))
# mrks=model.predict([[hour]])
# print("Model predicted value is ",mrks)

y_pred=model.predict(X)
print(y_pred)

compare_md=pd.DataFrame({
    "Actual X":X.values.flatten(),
    "Actual y":y.values,
    "Model predicted value":y_pred
})
print(compare_md)

plt.plot(compare_md["Actual X"],compare_md["Model predicted value"],color="g",marker="o", label="best line")
plt.scatter(compare_md["Actual X"],compare_md["Actual y"],color="r", label="original data")
plt.title("Linear regression model")
plt.xlabel("study hour")
plt.ylabel("Marks")
plt.legend() #to show label
# plt.show()

MAE=(compare_md["Actual y"]-compare_md["Model predicted value"]).abs().mean()
print("Mean Absolue Error: ",round(MAE,2))

MSE=((compare_md["Actual y"]-compare_md["Model predicted value"])**2).abs().mean()
print("Mean Squared Error: ",round(MSE,2))

import math
RMSE=math.sqrt(MSE)
print("Root Mean Squared Error: ",round(RMSE,2))

model_score=round(model.score(X,y),2)
print("After training model score is ",model_score)

c=model.intercept_
print(round(c,2))
m=model.coef_[0]
print(round(m,2))
#  formula apply y=mx+c
study_hours=float(input("Enter study hours"))
marks=m*study_hours+c
if 0<=marks<=100:
    print("predicted Value is ",round(marks,2))
elif marks<0:
    marks=0
    print("predicted value is ",round(marks,2))
else:
    marks=100
    print("predicted value is ",round(marks,2))

print(f"Model giving prediction with {model_score}% score")