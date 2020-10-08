class Student():
    __slots__ = ('name','age','score')
    pass
    def __str__(self):
        return '{}.....{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='小王'
xw.age=20
xw.score=90
# print(xw.__dict__)#所有可引用的属性在这里存储 不足的地方 是占用内存大
#可以看到 在定义了slots变量之后 student 类实例已经不能随意创建  不在__slots__定义属性了
print(xw)

class SubStudent(Student):
    __slots__ = ('gender','pro')
    pass

xq=SubStudent()
xq.gender='男'
xq.pro='IT'
print(xq.gender,xq.pro)