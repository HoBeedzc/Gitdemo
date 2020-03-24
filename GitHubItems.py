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
