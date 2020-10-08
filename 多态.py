class Animal:
    '''
     父类【基类】
    '''
    def say_who(self):
        print('我是一个动物')
        pass
    pass
class Duck(Animal):
    '''
    子类【派生类】
    '''
    def say_who(self):
        '''
        在这里重写子类
        :return:
        '''
        print('我是一只漂亮的鸭子')
    pass
class Dog(Animal):
    '''
    子类【派生类】
    :return:
    '''
    def say_who(self):
        print('我是一个可爱的哈巴狗')
        pass
    pass
class Cat(Animal):
    '''
    子类【派生类】
    '''
    def say_who(self):
        print('我是一个可爱的小猫咪')
        pass
    pass
class Person:
    def say_who(self):
        print('我是人类')
        pass
    pass
class Student(Person):
    def say_who(self):
        print('我是一年级学生')
class Bird(Animal):
    def say_who(self):
        print('我是一只黄鹂鸟')
    pass
def commonInvoke(obj):
    '''
    统一调用的方法
    :param obj: 对象实例
    :return:
    '''
    obj.say_who()

# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()
# cat1=Cat()
# cat1.say_who()
objList=[Duck(),Dog(),Cat(),Bird(),Student()]
for item in objList:
    '''
    循环调用函数
    '''
    commonInvoke(item)
