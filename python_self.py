class Person:
    '''
    定义一个类
    '''
    def eat(self,name,food):
        # print('self id= %d'%id(self))
        print('%s喜欢吃%s'%(name,food))
        pass
    pass
xw=Person()
print('self id= %d'%id(xw))
xw.eat('小王','橙子')
