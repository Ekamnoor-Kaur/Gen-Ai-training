import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Loading dataset
dataset=load_wine()
print(dataset)
print("type of datset",type(dataset))
print("dataset keys",dataset.keys())

# ['data', 'target', 'target_names', 'feature_names']
print("data",dataset["data"],end="\n")
print("target",dataset["target"],end="\n")
print("target name",dataset["target_names"],end="\n")
print("columns",dataset["feature_names"],end="\n")

# coverting to dataframe
df=pd.DataFrame(dataset['data'],columns=dataset['feature_names'])
df["result"]=dataset["target"]

# see all rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print(df.head())

# EDA
print("null values",df.isnull().sum().sum())

# plotting
sns.pairplot(df, hue='result')
plt.show()

# separate X ans y
X=df.iloc[:,:-1]
y=df["result"]
print("Shape of X",X.shape)
print("Shape of y",y.shape)

# Training and testing data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=12)
print("Shape of X_train",X_train.shape)
print("Shape of X_test",X_test.shape)
print("Shape of y_train",y_train.shape)
print("Shape of y_test",y_test.shape)

# model training
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("model prediction value",y_pred)
score=model.score(X_test,y_test)
print("model score is ",score)

# getting actual values
res=[]
res = dataset['target_names'][y_pred]
print("final result",res)

