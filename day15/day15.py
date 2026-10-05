import pandas as pd 
import numpy as np

data={
    "age":[23,22,np.nan,15,25,np.nan],
    "marks":[30,45,np.nan,np.nan,49,23]
}
df=pd.DataFrame(data)
print(df)
print(df.info())

# df["age"]=df["age"].fillna(df["age"].mean())
# df["marks"]=df["marks"].fillna(df["marks"].mean())
# print(df)

print(df.isnull().sum())
print(df.isnull().any(axis=1))
# filling null values
df["age"]=df["age"].fillna(df["age"].median())
df["marks"]=df["marks"].fillna(df["marks"].median())
print(df)
print(df.isnull().sum())

df1=pd.read_csv("student_marks.csv")
print(df1)
print(df1.isnull().sum())

# filling null values
df1["physics"]=df1["physics"].fillna(df1["physics"].median())
df1["chemistry"]=df1["chemistry"].fillna(df1["chemistry"].median())
df1["math"]=df1["math"].fillna(df1["math"].median())
df1["biology"]=df1["biology"].fillna(df1["biology"].median())
df1["english"]=df1["english"].fillna(df1["english"].median())

print(df1)
print(df1.isnull().sum())