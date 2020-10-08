class People:
    coutry='china'
    @classmethod
    def get_coutry(cls):
        return cls.coutry
    pass
    @classmethod
    def change_country(cls,data):
        cls.coutry=data
        pass
    @staticmethod
    def getDate():
        return People.coutry
print(People.get_coutry())
p=People()
print('实例对象访问%s'%p.get_coutry())
print('--------------修改之后-----------')
People.change_country('英国')
print(People.get_coutry())
print('--------------静态类-----------')
print(People.getDate())