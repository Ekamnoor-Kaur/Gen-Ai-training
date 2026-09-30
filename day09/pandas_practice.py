import numpy as np
import pandas as pd
import openpyxl as op
# emp={
#     "id":[1,2,3,4,5],
#     "name":["ram","shyam","nikhil","david","pitter"],
#     "post":["developer","hr","clerk","programmer","trainee"],
#     "salary":[23000,34000,12000,32000,17000],
#     "city":["noida","delhi","gurgaon","faridabad","mohali"]  
# }

# df=pd.DataFrame(emp)
# print(df.loc[2])
# print(df.loc[3]) #get row number 3 not index

# print(df.loc[2,"city"])#get city of second row
# print(df.loc[:,"name"])
# print(df.loc[:,["name","salary"]])

# # get multipple rows
# print(df.loc[[1,2,4]])
# print(df.loc[[1,2,4],["name","salary"]])
# print(df.loc[df["salary"]>30000])
# print(df.loc[df["city"]=="delhi"])
# print(df.loc[(df["city"]=="delhi")&(df["salary"]>3000)])


# data = {
#     "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     "Name": ["Aarav", "Simran", "Rohan", "Ananya", "Harsh",
#             "Mehak", "Arjun", "Navya", "Karan", "Isha"],
#     "Gender": ["Male", "Female", "Male", "Female", "Male",
#                "Female", "Male", "Female", "Male", "Female"],
#     "Age": [20, 21, 20, 19, 22, 20, 21, 19, 22, 20],
#     "Department": ["CSE", "IT", "CSE", "ECE", "IT","CSE", "ME", "ECE", "CSE", "IT"],
#     "Marks": [85, 78, 92, 74, 65, 88, 59, 81, 73, 95],
#     "Attendance": [92, 88, 95, 82, 76, 91, 68, 89, 85, 97],
#     "City": ["Chandigarh", "Ludhiana", "Mohali", "Delhi", "Amritsar", "Patiala", "Ludhiana", "Chandigarh", "Mohali", "Delhi"]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.loc[2:6,["Student_ID","Name"]])
# print(df.loc[df["Gender"]=="Female"])
# print(df.loc[(df["Marks"]>80)&(df["Attendance"]>80)])

# print(df.iloc[2:3])
# print(df.iloc[0:5])
# print(df.iloc[[2,4,5]]) # 2,4,5 record
# print(df.iloc[0:3])#first four rows
# print(df.iloc[-1]) #last row
# print(df.iloc[:,-1]) #last column
# print(df.iloc[0:3,0:2])#first 3 rows 2 columns

# data = {
#     "ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     "Name": [
#         "Rahul", "Priya", "Aman", "Neha", "Arjun",
#         "Rahul", "Simran", "Vikas", None, "Priya"
#     ],
#     "Post": [
#         "Manager", "Developer", "Accountant", "HR", "Designer",
#         "Developer", "Manager", None, "Accountant", "Developer"
#     ],
#     "Salary": [
#         60000, 50000, 45000, 40000, None,
#         50000, 65000, 42000, 45000, 50000
#     ],
#     "City": [
#         "Delhi", "Mumbai", "Chandigarh", "Ludhiana", "Amritsar",
#         "Mumbai", None, "Delhi", "Chandigarh", "Mumbai"
#     ],
#     "Age": [
#         35, 28, 32, 30, 27,
#         None, 38, 29, 32, 28
#     ]
# } 
# df=pd.DataFrame(data)
# print(df)
# print(df.info(),"\n")
# print(df.isnull(),"\n")
# print(df.notnull(),"\n")
# print(df.isnull().sum(),"\n")
# print(df.count(),"\n")
# df=df.fillna(0)
# print(df)
# df=df.dropna(0)
# print(df)

df = pd.read_excel(r"C:\Users\harry\OneDrive\Desktop\Gen AI training\day9\code\employee.xlsx")
print(df)

exp=[2,3,5,4,3,4,6,7,5,8]
df["Experience"]=exp

print(df.loc[df["Age"]>30])
print(df.loc[:,["Name","Post"]])
print(df.loc[df["Salary"]>50000])
print(df.loc[(df["Gender"]=="Male")&(df["Experience"]>2)])
print(df.loc[df["ID"]==101])
print(df.loc[::-1])

print(df.iloc[0:5])
print(df.iloc[:,0:3])

print(df.info())
print(df.isnull().count())
