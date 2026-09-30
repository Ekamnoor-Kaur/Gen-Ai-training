
# try:
#     a=int(input("Enter first number"))
#     b=int(input("Enter second number"))
#     c=a/b
#     print(c)
# except Exception as e:
#     print("Exception Generates")
#     print(e)
# finally:
#     print("always execute")

# def vote():
#     try:
#         age=int(input("enter age"))
#         if(age<=10):
#             raise ValueError
#         else:print("you are eligible to vote")
#     except ValueError:
#         print("You are not elligible for vote")
# vote()

# def practice():
#     try:
#         a1=int(input("enter number"))
#         b1=int(input("enter number"))
#         c=a1/b1
#         print(c)
#     except Exception as e:
#         print(e)
#     try:
#         age1=int(input("enter age"))
#         if age1<=0 or age1>100:
#             raise ValueError
#     except ValueError:
#         print("enter a valie age")
# practice()

# class Test:
#     def show(self):
#         try:
#             li=[3,6,3,6,8,5,4]
#             print(li[10])
#         except Exception as e:
#             print(e)    
#     def div(self):
#          try:
#              a1=int(input("enter number"))
#              b1=int(input("enter number"))
#              c=a1/b1
#              print(c)
#          except Exception as e:
#              print(e)  
                 
# t=Test()
# t.show()
# t.div()

from abc import ABC,abstractmethod
class InsufficientException(Exception):
    pass

class BankAccount(ABC):
    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amt):
        if amt<=0:
            raise ValueError("please enter a valid amount")
        self.balance=self.balance+amt
        print("After Deposit Balance is",self.balance)

    @abstractmethod
    def withdraw(self,amt):
        pass

    def showdetails(self):
        print("Customer name",self.name)
        print("Your Balance is ",self.balance)
        print("Your account no is",self.account_no)

class Customer(BankAccount):
    def withdraw(self,amt):
        if amt <= 0:
            raise ValueError("Please enter a valid amount")
        if amt>self.balance:
            raise InsufficientException("Insufficient funds")
        self.balance=self.balance-amt
        print("Withdrawl successful")
        print("After Withdrawl, remaining balance is ", self.balance)

name = input("enter name: ")
account_no = int(input("enter account no: "))
c = Customer(name, account_no, 0)

while(True):
    print("d- deposit")
    print("w- withdraw")
    print("s- show details")
    print("e- exit")
    
    ch=input("enter choice: ").lower()    
    try:
        if ch == 'd':
            amt = int(input("enter amount you want to deposit: "))
            c.deposit(amt)
        elif ch == 'w':
            amt = int(input("enter amount you want to withdraw: "))
            c.withdraw(amt)
        elif ch == 's':
            c.showdetails()
        elif ch == 'e':
            print("Exiting...")
            break
        else:
            print("invalid choice")
    except ValueError as e:
        print("Error:", e)
    except InsufficientException as e:
        print("Error:", e)