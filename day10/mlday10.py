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
print(df.shape)
print(df.columns)
print(df.info())
print(df.corr())

plt.plot(df["study-hour"],df["marks"],color="r",linestyle="--")
# Numerical vs Numerical scatter plot
sns.scatterplot(data=df,x="study-hour",y="marks")
plt.xlabel("Study Hours")
plt.ylabel("marks")
plt.show()

X=df[["study-hour"]] #input
y=df["marks"] #output

#model build
model=LinearRegression()
print(model)

# model training
model.fit(X,y)
# fit() is used for training purpose
# if X and y are categorical then must be convert into numerical
# is called feature engineering 
#  we need to provide X in 2 dimension
c=model.intercept_
print(round(c,2))

# y=mx+c
m=model.coef_[0]
print(round(m,2))

#  formula apply y=mx+c
study_hours=float(input("Enter study hours"))
y=m*study_hours+c
print("predicted value is ",round(y,2))