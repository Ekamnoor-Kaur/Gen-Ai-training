from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod
    def show():
          pass
    @abstractmethod
    def msg():
         pass
class Test(Demo):
     def show(self):
          print("hello")
     def msg(self):
          print("hi")
t=Test()
t.show()
t.msg()

class Test1(ABC):
     def __init__(self):
          self.a=10
          self.b=20
     @abstractmethod
     def show():
          pass
class Test2(Test1):
     def show(self):
          print(self.a)
          print(self.b)
t2=Test2()
t2.show()

class Test3(ABC):
     @abstractmethod
     def m1():
          pass
class Test4(ABC):
     @abstractmethod
     def m2():
          pass
class Test5(Test3,Test4):
     def m1(self):
          print("m1")
     def m2(self):
          print("m2")
t3=Test5()
t3.m1()
t3.m2()

