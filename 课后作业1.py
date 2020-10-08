# 1、Python中new方法作用是什么？
# 2、什么是单例模式？单例模式适用于什么场景？
# 3、私有化方法与私有化属性在子类中能否继承？
# 4、在Python中什么是异常？
# 5、Python中是如何处理异常的。
# 6、Python中异常处理语句的一般格式，可以使用伪代码的形式描述。
# 7、__slots__属性的作用
# 8、私有化属性的作用？
# 9、在类外面是否能修改私有属性。
# # 10、如果一个类中，只有指定的属性或者方法能被外部修改。那么该如何限制外部修改。
# 1、编写一段代码以完成下面的要求
# 定义一个Person类,类中要有初始化方法,方法中要有人的姓名,年龄两个私有属性.
# 提供获取用户信息的函数.
# 提供获取私有属性的方法.
# 提供可以设置私有属性的方法.
# 设置年龄的范围在(0-120)的方法，如果不在这个范围，不能设置成功.
class Person:
    def __init__(self,n,a):
        '''
        :param n:
        :param a:
        '''
        self.__name=n
        self.__age=a
        pass
    def __str__(self):
        return '{}的年龄是:{}'.format(self.__name,self.__age)
    def getAgeinfo(self):
        return self.__age
    def setAge(self,age):
        if 0<age<120:
            self.__age=age
            pass
        else:
            print('您设置的年龄不对')
    def getNameinfo(self):
        return self.__name
    def setName(self,name):
        self.__name=name
a=Person('小王',121)
a.setAge(121)
print(a)
# 2、请写一个单例模式
# 3、创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。
# 利用property 属性给调用者提供属性方式的调用获取和设置私有属性方法的方式。
class Student:
    def __init__(self,):
        self.__name='小张'
        self.__score=90
        pass
    @property
    def name(self):
        self.__name
        pass
    @name.setter
    def name(self,name):
        self.__name=name
        pass
    @property
    def score(self):
        self.__score
        pass
    @score.setter
    def score(self,score):
        self.__score=score
        pass
    def __str__(self):
        return self.__name
    def __call__(self, *args, **kwargs):
        print('{}的成绩是:{}'.format(self.__name,self.__score))
        pass
    pass
xw=Student()
xw()
print(xw)
xz=Student()
xz.name='小王'
xz.score=98
xz()
print(xz)
# 4、创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法
# ,给类绑定一个类属性colour,给类绑定一个类方法打印字符串'ok'。
import types
def cat(self):
    print('跑的飞快')
    pass
@classmethod
def color(cls):
    print('ok')
class Animal:
    pass
Animal.color='黑色'
Animal.info=color
xm=Animal()
xm.cat=types.MethodType(cat,xm)
xm.cat()
print(xm.color)
Animal.info()
