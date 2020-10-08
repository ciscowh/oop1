class Person():
    '''
    定义一个类
    '''
    def __init__(self,name,food,pro):
        self.name=name
        self.food=food
        self.pro=pro
        print('---------执行init-----')
    def __str__(self):
        return '%s喜欢吃%s修的的专业%s'%(self.name,self.food,self.pro)
        pass
    def eat(self,name,food):
        # print('self id= %d'%id(self))
        # print('%s喜欢吃%s'%(name,food))
        pass
    def __new__(cls, *args, **kwargs):
        print('--------执行new——————————')
        return  object.__new__(cls)
    pass
xw=Person('小王','橙子','心理学')
print(xw)
print('self id= %d'%id(xw))
# xw.eat('小王','橙子')
