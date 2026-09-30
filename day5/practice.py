# class Test:
#     #class level variable
#     a=10
#     def __init__(self):
#         #instance variable
#         self.b=20
# t=Test()
# print(t.a,t.b) #10 20
# t.a=11 # this does not change te static variable a it create a new instance variable for t 
# t.b=22
# print(t.a,t.b) #11 22
# t1=Test()
# print(t1.a,t1.b) #a.b are instance variable 10 20
# Test.a=11
# print(t1.a) #11
#instance variable is varied from object

# class Demo:
#     def msg(self):
#         print("bye")
#     @classmethod
#     def show(cls):
#         print("hello")
#     @staticmethod
#     def disp():
#         print("hi")
# d=Demo()
#we can access instance method by using object reference
# d.msg()
#we can access classmethod by using object reference as well as classname
# Demo.show()
# d.show()
#we can access static method by using only class name
# Demo.disp()


#when used instance, class method, static method
# self can get object information
# cls can get class information
# static method can only get logic and calculation

# we can declare static/class level variables inside class and constructor but by using class name

# class Test:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Test.count+=1
# t1=Test("Ravi")
# t2=Test("Mukesh")
# t3=Test("Rahul")
# print("Number of employees ",Test.count)

#difference instance, static/class and local variable
# instance variable - inside constructor
# class variable - inside class
# local variable - inside function

# class Prac:
#     count=0 #static variable
#     def __init__(self):
#         Prac.count+=1
#         self.i1=4 #instance variable
#         self.i2=8 #instance variable
#     def add(a,b):
#         c=a+b #local variable
#         print(c)
# p=Prac()
# print(p.i1,p.i2)
# # p.greet()
# p1=Prac()
# p2=Prac()
# print(Prac.count)

'''
inheritance
The process of acquiring poperties and behaviour from one class to another class
There are five types of inheritance
1 single level inheritance - when a class inherits the properties of another known as single level inheritance
2 Multilevel inheritance - when a class inherits the properties of another class but that class is already inherited by another class
3 Multiple inheritance - when a class inherits properties from more than one class
4 Hierarchial inheritance - when a class is inheritance by more than one class
5 Hybrid inheritance - it is a combination of hierarchial and multiple inheritance
'''

# class A:
#     def m1(self):
#         print("hello")
#     def m2(self,a,b):
#         print(self.a+self.b)
# class B(A):
#     pass
# b=B()
# b.m1()
# b.m2()

# class A:
#     def __init__(self):
#         print("hello")
# class B(A):
#     def m1(self):
#         print("hi")

# class C(B):
#     def m2(self):
#         print("hey")
# c=C()
# c.m1()
# c.m2()

# hierarchial inheritance
class Animal:
    def __init__(self,name):
        self.name=name
        print(self.name)
    def eats(self):
        print("eats")
class Dog(Animal):
    def bark(self):
        print("barks")
class Cat(Animal):
    def meow(self):
        print("meow")    
d=Dog("tommy")
d.eats()
d.bark()
c=Cat("cherry")
c.eats()
c.meow()

#  multipled  inheritance 
class Father:
    def skills(self):
        print("Gardening")

    def height(self):
        print("Tall")
class Mother:
    def cooking(self):
        print("Cooking")
    def skills(self):       
        print("Painting")
class Child(Father, Mother):
    pass
c = Child()
c.height()     #
c.cooking()    
c.skills()     



'''
Polymorphism:- is a greek word poly means many and morphism form when a action performed multiple operation in different ways is known as polymorphism
There are two types
1 overloaded
2 overriding

=> overloaded are three types 
a operrator overloading: same operator but different operation
ex; 10+20=30
   "100"+"200"="100200"
   3*3=9
   "ram"*3="ramramram
b method overloading- python cant support there are no dattypes in python
c constructor overloading- python cant support as there are no datatypes

=> overriding:- when parent class and child class having same method name but different logic is known as overriding 

'''

# class Parent:
#     def marry(self):
#         print("west indies girl")
# class Child(Parent):
#     def marry(self):
#         print("indian girls")
# c=Child()
# c.marry()
# p=Parent()
# p.marry()

# class Student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     class Address:
#         def __init__(self, city,state):
#             self.city=city
#             self.state=state
#         def show(self):
#             print("City is ",self.city)
#             print("State is ",self.state)        
# s=Student("rahul","java")
# a=Student.Address("noida","up")
# print("Name ",s.name)
# print("Course",s.course)
# a.show()

# class ShoppingCart:
#     def __init__(self):
#         self.cart=[]
#     class Product:
#         def __init__(self,name,price,quantity):
#             self.name=name
#             self.price=price
#             self.quantity=quantity
#         def total(self):
#             return self.price*self.quantity
#     def addproduct(self):
#         name=input("enterr product name")
#         price=int(input("enter product price"))
#         quantity=int(input("enter amount of quantity"))
#         p=self.Product(name,price,quantity,)
        
#         self.cart.append(p)
#         print("product added succesfully")
#     def show_cart(self):
#         for c in self.cart:
#            print(c.name,c.price,c.quantity,c.total())
# Shop=ShoppingCart()
# Shop.addproduct()
# Shop.show_cart()