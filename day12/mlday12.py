import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df=pd.read_csv("Advertising.csv")
print(df)

print(df.shape)
print(df.columns)
print(df.info())
print(df.isna().sum())

print(df.corr())

# with the help of heatmap we can describe the correlation
sns.heatmap(df.corr(),annot=True)
plt.show()
# numerical vs numerical
sns.scatter(data=df)
plt.show()

# pair plot
sns.pairplot(data=df)
plt.show()


# data is divided into two parts
X=df.iloc[:,:3]
y=df.iloc[:,-1]
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print("predicted values")
print(y_pred)

score=model.score(X_test,y_pred)
print("Model tained score",score)

df.sample()
tv=float(input("Enter tv advertising cost"))
radio=float(input("Enter radio advertising cost"))
news=float(input("Enter newspapaer advertising cost"))

user_data=[[tv,radio,news]]
prediction=model.predict(user_data)
print("Model predicted value is",prediction)
print(f"Model Giving Price with {score}% accurate score prediction {prediction}")