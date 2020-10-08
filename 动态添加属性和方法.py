import types  #添加方法的库
#定义添加方法的
def dymicMethod(self):
    print('{}是体重是：{} 在{}大学读的书'.format(self.name,self.weight,Student.school))
    pass
@classmethod
def classTest(cls):
    print('只是一个类方法')
    pass
@staticmethod
def staticMethod():
    print('只是一个静态方法')
    pass
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)
    pass
print('-----------这是一个类方法----------')
Student.classMethod=classTest
Student.classMethod()
print('-----------这是一个静态方法----------')
Student.staticMethod=staticMethod
Student.staticMethod()

zyh=Student('张艳华',20)
zyh.weight=50
zyh.printInfo=types.MethodType(dymicMethod,zyh)
print(zyh)
print(zyh.weight)
print('-------------列外一个对象----------')
zm=Student('张明',20)
zm.weight=80
print(zm)
zm.printInfo=types.MethodType(dymicMethod,zm)
print('-------------类对象添加属性----------')
Student.school='北京邮电大学'
print(zm.school)
#动态的添加方法
print('-------------动态添加实例方法----------')
zyh.printInfo()
zm.printInfo()
zyh.classMethod()