# 决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# 属性：
# name 玩家的名字
# blood 玩家血量
#
# 方法：
# tong() 捅对方一刀,对方掉血10滴
# kanren() 砍对方一刀，对方掉血15滴
# chiyao() 吃一颗药，补血10滴
# __str__ 打印玩家状态。
# #
class Role:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def tong(self,enemy):
        '''
        捅了一刀
        :param enemy:对人
        :return:
        '''
        enemy.hp-=10
        info='%s捅了%s一刀'%(self.name,enemy.name)
        print(info)
    def kanren(self,enemy):
        '''
        砍了一刀
        :param enemy:对人
        :return:
        '''
        enemy.hp-=15
        info='%s砍了%s一刀'%(self.name,enemy.name)
        print(info)
    def chiyao(self):
        '''
        吃了一颗药丸
        :return:
        '''
        self.hp+=10
        info='%s吃了一颗药丸，补了10点血'%(self.name)
        print(info)
    def __str__(self):
        return '%s还剩下%d血量'%(self.name,self.hp)
xmcx=Role('西门吹雪',100)
ygc=Role('叶孤城',100)
import time
while True:
    if xmcx.hp<=0 or ygc.hp<=0:
        break
    xmcx.tong(ygc)
    print(xmcx)
    print(ygc)
    xmcx.kanren(ygc)
    print(xmcx)
    print(ygc)
    xmcx.chiyao()
    print(xmcx)
    print(ygc)
    time.sleep(1)
