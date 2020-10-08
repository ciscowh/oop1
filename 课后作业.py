# 1、python中如何通过类创建对象，请用代码举例说明。
class Person:
    def run(self):
        print("小王跑的真快")
        pass
    pass
xw=Person()
xw.run()
# 2、如何在类中定义一个方法，请用代码举例说明。
# 3、定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
class Fruits:
    def __init__(self,colour,name):
        self.colour=colour
        self.name=name
        pass
    def __str__(self):
        return '%s的颜色是%s'%(self.name,self.colour)
    pass
sg=Fruits('红色','苹果')
print(sg)
xg=Fruits('绿色','西瓜')
print(xg)
jz=Fruits('黄色','桔子')
print(jz)

# 4、请编写代码，验证self就是实例本身。
# 5、定义一个Animal类
# (1)、使用__init__初始化方法为对象添加初始属性。如颜色，名字，年龄。
# (2)、定义动物方法，如run，eat等方法。如调用eat方法时打印xx在吃东西就可以。
# (3)、定义一个__str__方法，输出对象的所有属性。
class Animal:
    def __init__(self,colour,name,age):
        self.colour=colour
        self.name=name
        self.age=age
        pass
    def run(self):
        print('%s在跑'%self.name)
        pass
    def eat(self):
        print('%s在吃东西'%self.name)
        pass
    def __str__(self):
        return '%s是%s，今年%d'%(self.name,self.colour,self.age)
    pass
lg=Animal('黑色','老虎',5)
lg.eat()
lg.run()
print(lg)

# 6、请将课件上 决战紫荆之巅 重写一遍，并理解每一个方法的使用。
class Role:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        pass
    def tong(self,ememy):
        ememy.hp-=10
        print('{}捅了{}一刀'.format(self.name,ememy.name))
    pass
    def kanren(self,ememy):
        ememy.hp-=15
        print('{}砍了{}一刀'.format(self.name,ememy.name))
    pass
    def chiyao(self):
        self.hp+=10
        print('{}吃了一颗药，增加了10滴血'.format(self.name))
    pass
    def __str__(self):
        return '{}还剩下{}滴血'.format(self.name,self.hp)
    pass
xfcx=Role('西风崔雪',100)
ygc=Role('叶孤城',100)
import time
while True:
    if xfcx.hp<=0 or ygc.hp<=0:
        break
        pass
    xfcx.tong(ygc)
    print(ygc)
    xfcx.kanren(ygc)
    print(ygc)
    xfcx.chiyao()
    print(xfcx)
    time.sleep(1)