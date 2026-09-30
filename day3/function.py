def show():
    print("hello")
show()

def sum(a,b):
    print(a+b)
sum(4,6)

a=int(input("Enter number1"))
b=int(input("enter number2"))
def add():
    print(a+b)
    mul()
def sub():
    print(a-b)
    add()
def mul():
    print(a*b)
    div()
def div():
    print(a/b)
sub(a,b)