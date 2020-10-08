class Person:
    def __init__(self,name,age,sex):
        self.name=name   #实例的属性
        self.age=age
        self.sex=sex
    def eat(self,food):
        print(self.name+'大口大口的吃'+food)
        pass
    pass

lh=Person('李辉',19,'男生')
print(lh.name,lh.sex,lh.age)
lh.eat('榴莲')

xq=Person('小强',29,'男生')
print(xq.name,xq.sex,xq.age)
xq.eat('苹果')

xh=Person('小花',21,'女生')
print(xh.name,xh.sex,xh.age)
xh.eat('香蕉')

