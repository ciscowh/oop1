#为什么要重写，父类不能满足子类的需求，那么子类可以重写父类或者完善父类

class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        pass

    def bark(self):
        print('汪汪叫。。。。')
        pass
    pass
class kejiquan(Dog):
    def __init__(self,name,color):#属于重写父类的方法
        #针对这种诉求  我们就需要调用父类的函数了
        Dog.__init__(self,name,color) #手动调用父类方法，执行完毕就可以具备name color 这两个实例属性
        super().__init__(name,color)#supper是自动找到父类，进而调用方法
        #扩展属性
        self.height=90
        self.weight=20
        pass
    def __str__(self):
        return '{}的颜色是{}  身高是{} 体重是{}' .format(self.name,self.color,self.height,self.weight)
    def bark(self):#属于类的重写的方法
        super().bark()
        print('叫的和神一样')
        print(self.name)
    pass
kj=kejiquan('柯基犬','百色')
kj.bark()
print(kj)
