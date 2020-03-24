#!/usr/bin/python3

# ©copyright 1999-2020 Hobee. All rights reserved.
# www.hobeedzc.com
# mailto:LZQpublic@163.com
# Never Settle

import random
import math
import numpy as np

def convolution(x):
    # 将0-inf的数据映射到0-1
    return 1-math.e**(-x)

def fluctuation(x):
    # 为使数据更加真实，考虑小范围正态波动。
    return np.random.normal(x,0.1,1)[0]

def decision(x):
    # 根据一个0-1的变量值+随机数的方式做出决策。
    if x + random.random() >= 1:
        return 1
    else:
        return 0

class GitHubItem():
    All_item = []
    def __init__(self,author):
        GitHubItem.All_item.append(self)
        self.author = author
        self.fork = 0
        self.star = 0
        self.watch = 0
        self.quality = 0 # 取值范围[0,1],假设完全取决于开发者能力与以前开发项目数量，在小范围内以正太分布形式波动。

class GitHubUser():
    id = 0
    def __init__(self):
        self.id = GitHubUser.id
        GitHubUser.id += 1
        self.ability = random.random()
        self.demo_item = GitHubItem(self)
        self.itemlist = [self.demo_item]
        self.all_fork = 0
        self.all_star = 0
        self.all_watch = 0

    def Develop_item(self):
        # 对开发的基本假设如下：
        # 能力和开发次数决定下一次开发质量、开发周期
        # 简化问题，假设开发周期全部为一天
        # fork、star、watch决定开发动力
        # 开发能力会有进步，不开发能力会退步

        self.all_fork = sum([x.fork for x in self.itemlist])
        self.all_star = sum([x.star for x in self.itemlist])
        self.all_watch = sum([x.watch for x in self.itemlist])

        q_weight = self.ability*0.7 + convolution(len(self.itemlist))*0.3 # 开发质量权重,将作品个数映射到0-1.
        p_weight = convolution(self.all_fork)*0.5 + convolution(self.all_star)*0.3 + convolution(self.all_watch)*0.2 # 开发动力权重

        if decision(p_weight): # 进行开发
            new_item = GitHubItem(self)
            new_item.quality = fluctuation(q_weight)
            # 对开发者的影响
            self.ability += abs(fluctuation(0.01))
            self.itemlist.append(new_item)
        else: # 不进行开发
            self.ability -= abs(fluctuation(0.01))
        
    def Watch_item(self,item):
        # 对浏览的基本假设如下：
        # 随机浏览项目，fork多的项目有更高概率被看到。(这部分并不属于这个方法要实现的功能)
        # 项目每被浏览一次就会获得一次watch，根据项目质量获得fork、star。(根据GitHub上的经验来看，获得fork之后一般都会随手给一个star)
        # 项目获得fork之后并不会加入到浏览者账户，只会提高被浏览的概率。
        # 浏览者阅读优秀内容会使自己的ability提升。
        item.watch += 1
        if decision(item.quality):
            item.star += 1
            self.ability += abs(fluctuation(0.01))
            if decision(item.quality):
                item.fork += 1
                self.ability += abs(fluctuation(0.01))
                return 1
            return 1
        return 0

if __name__=='__main__':
    pass