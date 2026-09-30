'''
class Test:
    def __init__(self):
        print(id(self))
t=Test()
print(id(t))

class Test:
    def __init__(self):
        # instance variable
        self.a=10
        self.b=20
t=Test()
print(t.a)
print(t.__dict__) #is a keyword which is used to access 

class Test:
    def __init__(self):
        # instance variable
        self.a=10
        self.b=20
        #instance method can access instance variable 
    def add(self): #why do we pass self ?
        print(self.a+self.b)
        
t=Test()
t.add()

class User:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def login(self):
        if self.name=='Techlive' and self.password==123:
            print("valid user")
        else:
            print("Invalid user")
name=input("Enter name")
password=int(input("Enter password"))
u=User(name,password)
u.login()

class Customer:
    bname="HDFC Bank Mohali"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("After Deposit Balance is",self.balance)
    def withdraw(self,amt):
        if self.balance<amt:
            print("Insufficient balance")
        else:
           self.balance=self.balance-amt
        print("After withdraw balance is ",self.balance)
name=input("enter customer name")
c=Customer(name)
print("Welcome to ", Customer.bname,"Mr.",name)
while True:
    print("d-Deposit")
    print("w-Withdraw")
    print("e-Exit")
    ch=input("Enter your choice")
    if ch=='d' or ch=="D":
        amt=int(input("Enter anount for deposit"))
        c.deposit(amt)
    elif ch=='w' or ch=="W":
        amt=int(input("Enter anount for withdraw"))
        c.withdraw(amt)
    elif ch=='e' or ch=="E":
        print("Thank you for using HDFC ATM Mohali")
        break
    else:
        print("Invalid choice")

how to delete a variable
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
    def m2(self):
        self.d=40
        self.e=50
        del self.a
        del self.b
t=Test()
t.m1()
print(t.__dict__)
t.m2()
print(t.__dict__)
'''