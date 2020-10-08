class Animal:
    def __init__(self,name):
        self.name=name
        print('这是构造初始化方法')
    pass
    def __del__(self):
        #主要的应用是操作 对象的释放 一旦释放 对象便不能在使用
        print('当某个作用域下面没有被使用『引用』的情况下 解释器会自动调用此函数')
        print('这个是析构方法')
        print('%s 这个对象 被彻底清理了 内存空间也释放了 ' %self.name)
        pass

cat=Animal('小花猫')
del cat #手动去清理删除对象 会指定__del__函数
print(cat.name)
input('程序等待中')
# print('*'*40)
# dog=Animal('科技小狗')