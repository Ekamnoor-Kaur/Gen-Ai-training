s1={"sun","mon","tue","wed"}
print(s1)
s1.add("jan")
print(s1)
s1.add("mar")
print(s1)

s3={1,4,8,7}
s3.add(5)
s3.update([3,10])
s3.remove(8)
s3.discard(9)
s3.pop()
s4=s3.copy()
s3.clear()
print(s3)
print(s4)

#adding by converting to list
li=list(s1)
li.remove("jan")
li.append("april")
s2=set(li)
print(s2)

#removing by converting to list
lis=list(s1)
lis.remove("mon")
s3=set(lis)
print(s3)

# dictionary
print("dictionary")
d={"id":1, "name":"sunil","course":"cse","age":21,"city":"chandigarh"}
print(d)

k=[1,2,3,4]
v=["pitter","david","warner","parker"]
d1=dict(zip(k,v))
print(d1)
print(d1.keys())
print(d1.values())

k1=["id","name","post","salary"]
v1=[101,"arsh","developer",39000]
d2=dict(zip(k1,v1))
print(d2)
print(d2.keys())
print(d2.values())

#add, remove, and update
d2["Course"]="java developer"
d2["experience"]="2 years"
print(d2)
d2.pop("Course")
print(d2)
