import numpy as np
# n1=np.array([1,2,3,4,5]) #1D array
# print(n1)
# print(n1.size)
# print(type(n1))
# print(n1.ndim)

# #Model always accept 2D array
# n2=np.array([[1,2,3,4],[5,6,7,8]])
# print(n2)
# print(n2.size)
# print(type(n2))
# print(n2.ndim)

# n3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(n3)
# print(n3.size)
# print(type(n3))
# print(n3.ndim)
# in case of 3D array then must be converted into 2D array
# then train model 

# n4=np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]])
# print(n4)
# print(n4.size)
# print(type(n4))
# print(n4.ndim)

# n5=np.array(list(map(int,input("enter elements").split())))
# print(n5)

# n=int(input("Enter number of elements"))
# n6=np.array([(int(input())) for i in range(n)])
# print(n6)

# rows=int(input("Enter number of rows"))
# cols=int(input("Enter number of cols"))
# t=[]
# for row in range(0,rows):
#     li=[]
#     for col in range(cols):
#         l=int(input())
#         li.append(l)
#     t.append(li)
# n7=np.array(t)
# print(n7)

# z=np.zeros(4)
# print(z)
# z2=np.zeros((4,4))
# print(z2)

#is used to availability like product, loan, email
#0 and 1 is mostly used in Binary classification 
# o=np.ones(4)
# o2=np.ones((4,4))
# print(o,o2,sep="\n")

# identity matrix used ofr corelation
# in ML eye replaces with t3.corr() method
# t3=np.eye(3)
# print(t3)

# slicing or indexing in numpy
# a1=np.array([1,2,3,4,5,6,7,8,9])
# a2=np.array([[1,2,3,4],[5,6,7,8],[3,6,3,3]])
# a3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# slicing
# print("1D")
# print(a1[0:2])
# print(a1[2:7])
# print(a1[:-4:])
# print("\n")

# print("2D")
# print(a2[0:2])
# print(a2[1:2])
# print(a2[-1::])
# print("\n")

# print("3D")
# print(a3[0:2])
# print(a3[1:1])
# print(a3[2:0])
# print("\n")

# print("\n")
# print(a1[2:7:2])
# print(a1[3:6])

# shaping and reshaping
# a1=np.array([1,2,3,4,5])
# print(a1.shape)
# a2=np.array([1,2,3,4,5,6,7,8,9])
# print(a2.shape)
# s=a2.reshape(3,3)
# print(s)

# x=np.arange(1,9)
# y=x.reshape(2,2,2)
# print(y)
# print(y.ndim)

# next is age and salary (inc or dec)
# in product, if purchase 10000 then free delivery
# in product, if purchase 5000 then 5% discount
# is used for (inc or dec)
# a=np.array([1,2,3,4,5,6])
# x=a+2
# y=a*2
# print(x)
# print(y)

# a1=np.array([[1,2,3,4],[5,6,7,8]])
# a2=np.array([11,22,33,44])
# z1=a1+a2
# z2=a1*a2
# z3=a1/a2
# print(z1) 
# print(z2)
# print(z3)

stu_name=["arsh","mehak","ansh","harman","aman"]
stu_attendance=[70,80,78,68,74]
stu_mst_marks=[17,28,10,20,18]

name=np.array(stu_name)
attendance=np.array(stu_attendance)
marks=np.array(stu_mst_marks)

status=[]
reason=[]
for att,mark in zip(attendance,marks):
    if att<75 and mark<12:
        status.append("Not Allowed")
        reason.append("Low attendance and low marks")
    elif att<75:
        status.append("Not Allowed")
        reason.append("Low attendance")
    elif mark<12:
        status.append("Not Allowed")
        reason.append("Low marks")
    else:
        status.append("Allowed")
        reason.append("-")

print("===== FINAL EXAM ELIGIBILITY LIST =====\n")
for n,a,m,s,r in zip(name,attendance,marks,status,reason):
    print("Name:",n," Attendance:",a," Marks:",m," Status:",s," Reason:",r)