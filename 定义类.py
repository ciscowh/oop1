class Person:
    '''
    对应人的特征
    '''
    # name='小明'
    # age='18'
    '''
    对应人的的行为  实例方法
    '''
    def __init__(self,name,age,sex):
        self.name=name   #实例的属性
        self.age=age
        self.sex=sex
    def eat(self,food):
        print(self.name+'大口大口的吃'+food)
        pass
    def run(self): #实例方法
        print('跑的飞快飞快')
        pass
    pass
#创建一个对象【类的实例化】
#规则格式 对象名=类名()
# xm=Person()
# xm.run()  #调用函数
# print('{}的年龄是{}'.format(xm.name,xm.age))
# xw=Person()
# xw.eat() #实例方法
# xx=Person()
# xx.age=20
# print(xx.name)

lh=Person('李辉',19,'男生')
print(lh.name,lh.sex,lh.age)
lh.eat('榴莲')

xq=Person('小强',29,'男生')
print(xq.name,xq.sex,xq.age)
xq.eat('苹果')

xh=Person('小花',21,'女生')
print(xh.name,xh.sex,xh.age)
xh.eat('香蕉')

