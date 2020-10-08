class Animal:
    def __init__(self):
        self.__age=18
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age<0:
            print('请输入不能小于0')
        else:
            self.__age
        pass
    pass
xm=Animal()
xm.age=1
print(xm.age)
