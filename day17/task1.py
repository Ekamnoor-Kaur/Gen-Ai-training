import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,classification_report
import warnings
warnings.filterwarnings("ignore")

data=np.arange(0,256)
print(data)
# black - 0
# white - 1
print(data.shape)

image_data=data.reshape((16,16))
print(image_data)
print(image_data.shape)

plt.gray()
plt.imshow(image_data)
# plt.show()

doraemon_array=plt.imread('doraemon.jpg')
final_arr=doraemon_array.copy()
print(final_arr)
print(final_arr.shape)

plt.imshow(final_arr)
# plt.show()

# final_arr=final_arr[80:450,100:400]
final_arr=final_arr[25:140,10:140]
plt.imshow(final_arr)
plt.show()

dataset=load_digits()
print(dataset)
print(type(dataset))
print(dataset.keys())
# print(dataset['DESCR'])
print("target",dataset["target"])
print("target names",dataset["target_names"])

df=pd.DataFrame(dataset['data'],columns=dataset['feature_names'])
df["resullt"]=dataset["target"]
# print(df)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print("df.head",df.head())
print("df shape",df.shape)

df.sample()
temp_data=df.sample().values.ravel() 
print("temp data",temp_data)
print("temp data shape",temp_data.shape)

features=temp_data[:-1]  #Features/independent variable/label all input values
print("features",features)
print(features.shape)

digit_arr = features.reshape((8, 8))
print("dgit arr",digit_arr)
plt.imshow(digit_arr)
plt.show()

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=30)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("model prediction is ",y_pred)
score_train=model.score(X_train,y_train)
print("model score",score_train)
score_test=model.score(X_test,y_test)
print("model score",score_test)

from sklearn.metrics import confusion_matrix

# model prediction vs actual values
cm=confusion_matrix(y_test,y_pred)
print(cm)

sns.heatmap(cm,annot=True)
plt.xlabel("Predicted digit")
plt.ylabel("Actual digit")
plt.show()

print(accuracy_score(y_test,y_pred))
print(precision_score(y_test,y_pred,average='weighted'))
print(recall_score(y_test,y_pred,average='weighted'))
print(f1_score(y_test,y_pred,average='weighted'))
print(classification_report(y_test,y_pred))

