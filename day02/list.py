t1 = []
print(t1, type(t1))

t2 = [1, 2, 3, 4]
t3 = [11, 22, [101, 102, 103]]
t4 = [111, "ram", 't', 23.5, 111]

t5 = "techlive"
t6 = list(t5)

t7 = "techlive solutions pvt limited"
t8 = t7.split()

t9 = input("Enter elements: ")
t10 = list(map(int, input("Enter elements: ").split()))

print(t2, t3, t4, t5, t6, t7, t8, t9, t10, sep="\n")

# List of lists using loop
n = int(input("Enter number of elements: "))
t12 = []
for i in range(n):
    t = list(map(int, input("Enter elements: ").split()))
    t12.append(t)
print(t12)

# List methods
t = [1, 2, 3, 6, 2, 5, 8, 9, 2]
nums=[10,20,30]
nums.append(40)
nums.append([50,60])
nums.extend([70,90])
nums.insert(0,5)

print(nums)
nums.pop(6)
nums.remove(40)
# nums.clear()
print(nums)

n1=[4,7,3,5,7,4,3]
n1.sort()
n1.reverse()
print(n1)

print(n1.index(3))
print(n1.count(3))

print(len(n1))
n2=n1.copy()
print(n2)

if len(t) > 5:
    t.pop(5)             # remove element at index 5
print(t)

print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print(sum(t) / len(t))

# minor project
students=[]
while True:
    print("1. Add element")
    print("2. view student")
    print("3. Searh Student")
    print("4. Find max marks with Name")
    print("5. Exit")
    ch=int(input("Enter your choice"))
    productprice=0
    if ch==1:
        name=input("enter student name")
        marks=int(input("enter student marks"))
        students.append([name,marks])
        print("Student added successfully")
    elif ch==2:
        if len(students)==0:
            print("no student found")
        else:
            for student in students:
                print("Name : ",student[0], "Marks : ",student[1])
    elif ch==3:
        searchname=input("enter name")
        for student in students:
            if student[0]==searchname:
                print("Name : ",student[0], "Marks : ",student[1])
    elif ch==4:
        max=0
        for student in students:
            if student[1]>max:
                max=student[1]
        for student in students:
            if(student[1]==max):
                print("Name : ",student[0], "Marks : ",student[1])
    elif ch==5:
     print("exited")
     break
    else:
     print("invalid choice")
