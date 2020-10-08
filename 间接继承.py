class Grandfather:
    def eat(self):
        print('吃的 方法')
        pass
    pass
class Father(Grandfather):
    def eat(self):#因为父类中存在这样的方法 在这里相当于方法覆盖了。
        print('爸爸经常吃海鲜')
    pass
class Son(Father):
    pass
pass
son=Son()
son.eat()
print(Son.__mro__)