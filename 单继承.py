class Animal:
    def eat(self):
        print('吃饭了')
        pass
    def drink(self):
        print('喝饮料了')
        pass
    pass
class Dog(Animal):#继承了父类
    def wwj(self):
        print('小狗旺旺叫')
    pass
class Cat(Animal):
    def mmj(self):
        print('喵喵叫')
    pass
d1=Dog()
d1.eat()
print('*'*40)
c1=Cat()
c1.drink()
c1.mmj()

