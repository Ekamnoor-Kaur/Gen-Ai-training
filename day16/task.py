import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
print("done")

# df=pd.read_csv("IRIS.csv")
# print(df)

dataset=load_iris()
print(dataset)
print(type(dataset))
print(dataset.keys())
# dict_keys(['data', 'target', 'target_names',  'feature_names', 'filename', 'data_module' 'frame','DESCR',])
print("desc",dataset['DESCR'])
print("data",dataset['data'])
print("target",dataset['target'])
print("target names",dataset['target_names'])

columns=dataset['feature_names']
print(columns)

df=pd.DataFrame(dataset['data'],columns=columns)
df['result']=dataset['target']
print(df)
print("shape ",df.shape)

# EDA
print(df.isnull().sum().sum())

# separate X and y
X=df.iloc[:,:-1]
y=df['result']
print("X shape ",X.shape)
print("y shape ",y.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print("model prediction ",y_pred)
score=model.score(X_test,y_test)
print("model score  is ",score)

new_score=[[5.1,3.5,1.4,0.2]]
new_pred=model.predict(new_score)
print("model prediction value ",new_pred)

res=[]
for var in y_pred:
    if var==0:
         res.append("Iris-setosa")
    elif var==1:
        res.append("Iris-versicolor") 
    else:
        res.append("Iris-virginica")
print(res)

plt.figure(figsize=(6, 5))
sns.heatmap(df[dataset['feature_names']].corr())
plt.title("Iris feature correlation")
plt.show()

sns.pairplot(df, hue='result')
plt.show()
