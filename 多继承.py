class shenxian:
    def fly(self):
        print('神仙都会飞')
    pass
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')
    pass
class Sunwukong(shenxian,Monkey):#即是神仙也是猴子
    pass
swk=Sunwukong()
swk.chitao()
swk.fly()
#问题 当多个父类当中存在相同的方法的时候 应该去调用哪一个呢？
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass
class A(B,C):
    pass
a=A()
a.eat()
print(A.__mro__)#可以显示类的继承依次关系
#在执行eat的方法时 查找的方法是先去A中查下，如果A没有去父类B中查找，如果B中没有，那么则去C类中查找
#如果C类中没有，则去D类中查找。如果还没找到 就报错