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
