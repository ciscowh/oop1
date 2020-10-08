class Animal:
     def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls, *args, **kwargs)
        return cls._instance

db1=Animal()
print(id(db1))
db2=Animal()
print(id(db2))
db3=Animal()
print(id(db3))

class SingleCase(object):
    __instance=None
    __isinit=True
    def __init__(self,name,age):
        self.name=name
        self.age=age
        SingleCase.__isinit =False
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance=super(SingleCase,cls).__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
        pass
    pass
obj1=SingleCase('xiaoming',18)
obj2=SingleCase('luban',118)
print(id(obj1))
print(id(obj2))
