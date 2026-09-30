import numpy as np
import pandas as pd

print("Series")
# s1=pd.Series()
# print(s1)
# s2=np.array([1,2,3,4,5])
# s3=pd.Series(s2)
# print(s3)
# s4=pd.Series([11,22,33,44])
# print(s4)

# customize indexing is very important for ML
# print("Customized indexing")
# s5=pd.Series(["aman","chaman","sonu","monu"], index=["A","B","C","D"])
# print(s5)

# s6=pd.Series([10,20,30,40,50])
# print(s6.size)
# print(s6.index)
# print(s6.values)
# print(s6.shape) #dimension
# print(s6.dtype)

# i way 2D dataset

# print("Dataframe")
# print("Using 2D array")
# data=[
#     [1,"david","developer",23000,"noida"],
#     [2,"pitter","programmer",45000,"delhi"],
#     [3,"kumar","hr",32000,"bangalore"],
#     [4,"sahil","trainee",16000,"chennai"],
#     [5,"hari","manager",50000,"delhi"]
# ]
# df=pd.DataFrame(data,columns=["id","Name","post","salary","city"])
# print(df)

# 2 way dataset
print("using dictionary")
emp={
    "id":[1,2,3,4,5],
    "name":["ram","shyam","nikhil","david","pitter"],
    "post":["developer","hr","clerk","programmer","trainee"],
    "salary":[23000,34000,12000,32000,17000],
    "city":["noida","delhi","gurgaon","faridabad","mohali"]  
}
df1=pd.DataFrame(emp)
print(df1)

# print("get only name")
# print(df1["name"])

# print("top 2")
# print(df1.head(2))

# print("last 2")
# print(df1.tail(2))

# print("salary greater than 20000")
# print(df1[df1["salary"]>2000])

# print("salary between 35000 to 25000")
# print(df1[(df1["salary"]>25000) & (df1["salary"]<35000)])

# print("max and min salary")
# print(df1["salary"].max())
# print(df1["salary"].min())

# print("get name post and salary")
# print(df1[["name","post","salary"]])

# print("add column")
# df1["age"]=[23,21,17,19,22]
# print(df1)

# client mostly ask each nd every months
# give me 10 pandas dataset like id, name, post salary,city,age
# 1 add column bonus salary >=40000 5% bonus
# 2 add column hra 10%
# 3 ad column 5%
# 4 calculate gross salary
# 5 calculate net salary

# emp={
#     "id":[1,2,3,4,5],
#     "name":["ram","shyam","nikhil","david","pitter"],
#     "post":["developer","hr","clerk","programmer","trainee"],
#     "salary":[23000,34000,12000,32000,17000],
#     "city":["noida","delhi","gurgaon","faridabad","mohali"]  
# }

# print(emp)
# df2=pd.DataFrame(emp)
# print(df2)

# df2["bonus"]=np.where(df2["salary"]>4000 , df2["salary"]*0.05,0)
# df2["hra"]=df2["salary"]*0.1
# df2["da"]=df2["salary"]*0.05
# df2["gross salary"]=df2["salary"]+df2["bonus"]+df2["hra"]+df2["da"]
# df2["net salary"]=df2["gross salary"]*12
# print(df2)

# give data productid ,namen price,quantity
# add column total price
# add col free delivery if total price 2000
# add col discount if total price 5000
# add col gst apply on total price

import numpy as np
import pandas as pd

# product={
#     "product id":[1,2,3,4,5,6],
#     "name":["shoes","bottle","bag","jeans","glasses","headphone"],
#     "price":[2500,500,800,1500,300,700],
#     "quantity":[4,3,5,7,5,3]
# }

# df=pd.DataFrame(product)
# df["product price"]=df["price"]*df["quantity"]
# df["discount"]=np.where(df["product price"]>5000, df["product price"]*0.10,0)
# df["delivery"]=np.where(df["product price"]>2000,0, 150)
# df["gst"]=df["product price"]*0.08
# df["final price"]=df["product price"]-df["discount"]+df["delivery"]+df["gst"]

# print(df)