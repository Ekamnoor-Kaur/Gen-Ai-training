t1=()
t2=(1,2,3,4)
t3=11,22,33
t4=(11,22,[101,102])
t5=((1,2,3),("sun","mon","tue"))

t=(1,2,3,5,4,6,8,7)
#count,index,reverse,sort
#sum, max, min, len
t=(4,6,3,2,5,7,4,2,3)
print(t.count(2))
print(t.index(4))

print(sorted(t))
print(reversed(t))
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
tu=tuple([3,5,3,2,5])
print(tu)

#not allowed in tuple
# print(t.pop(2))
# print(t.extend(2))
# print(t.append(9))
# print(t.reverse())
# print(t.remove(8))

t6=[1,2,3]
t7=[11,22,33]
# t1.append(t2)
# t1.append([101,102])

# deleting a element in tuple
t8=(1,2,5,6)
t9=list(t8)
t9.remove(5)
t11=tuple(t9)
print(t11)

#adding a element in tuple
t12=(4,6,4,3,5,7,5,4)
li1=list(t12)
li1.insert(4,56)
t13=tuple(li1)
print(t13)

t10=(1,2,3,4,5)
t10[2]=222
print(t1)
# TypeError: 'tuple' object does not support item assignment