# a=int(input("enter a number"))
# b=int(input("enter a number"))

# #swap
# temp=a
# a=b
# b=temp
# print("a",a)
# print("b",b)

#2
# c=int(input("enter a number"))
# d=int(input("enter a number"))
# c=c+d
# d=c-d
# c=c-d
# print("c",c)
# print("d",d)

# e=float(input("enter marks"))
# f=float(input("enter marks"))
# g=float(input("enter marks"))
# h=float(input("enter marks"))
# avg=(e+f+g+h)/4;
# if avg>80:
#     print("Grade A")
# elif avg>70:
#     print("Grade B")
# elif avg>55:
#     print("Grade C")
# elif avg>45:
#     print("Grade D")
# else:
#     print("Grade E")

for i in range(5):
    print(i)

roll=[1,2,3,4]
name=["armaan","gurman","arsh","sahil"]
course=["java","c++","python","java"]
for r,n,c in zip(roll,name,course):
    print(r,n,c)

sum=0
product=1
for i in range(1,6):
    sum+=i
    product*=i
    print(i)
print("sum: ",sum)
print("product",product)

for i in range(1,22):
    if i%2==0:
        print(i)

a=0
b=1
print(a)
print(b)
for i in range(5):
    c=a+b
    print(c)
    a=b
    b=c

