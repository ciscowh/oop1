class ToolongMyexecpt(Exception):
    def __init__(self,leng):
        self.len=leng
        pass
    def __str__(self):
        return '您输入的姓名长度是'+str(self.len)+'超过长度了'
    pass
def name_test():
    name=input('请输入您的姓名.....')
    try:
        if len(name)>4:
            raise ToolongMyexecpt(len(name))
            pass
        else:
            print(name)
            pass
    except ToolongMyexecpt as msg:
            print(msg)
    finally:
            print('程序执行完毕')
            pass
    pass
name_test()