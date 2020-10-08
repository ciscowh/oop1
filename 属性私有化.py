class Person:
    def __init__(self):
        self._name='李四'
        self.age=30
        pass
    def __str__(self):
        '''
        私有化的属性在内部可以使用self._name
        :return:
        '''
        return '{}的年龄是{}'.format(self._name,self.age)
    pass
class Student(Person):
    pass

stu=Student()

xl=Person()
print(xl)