#!/usr/bin/python3

# ©copyright 1999-2020 Hobee. All rights reserved.
# www.hobeedzc.com
# mailto:LZQpublic@163.com
# Never Settle

import sys
import random
import numpy as np
import networkx as nx
import GitHubItems as ghi



def try_develop():
    # 10%的人尝试开发
    l = random.sample(G.nodes(),int(G.number_of_nodes()*0.1))
    for c in l:
        c.Develop_item()

def try_watch():
    # 每天有50%的人会尝试浏览2个其他项目。
    item_rank = sorted(ghi.GitHubItem.All_item,key = lambda x:x.fork,reverse=True)
    l = random.sample(G.nodes(),int(G.number_of_nodes()*0.5))
    for c in l:
        for _ in range(2):
            rate = abs(random.gauss(0,1/3))
            rate = 1 if rate > 1 else rate
            try:
                item = item_rank[int(rate*len(item_rank))]
            except IndexError:
                item = item_rank[-1]
            if item.author == c:
                return
            flag = c.Watch_item(item)
            if flag:
                if (c,item.author) in G.edges():
                    continue
                else:
                    G.add_edge(c,item.author)

def add():
    # 每天增加30个用户
    for _ in range(30):
        g = ghi.GitHubUser()
        G.add_node(g)

def day():
    try_develop()
    try_watch()
    add()

if __name__=='__main__':
    # 模型基本假设如下：
    # 无权有向图
    # 原网络中有2626个节点，为保证数据相似性，本模型假设初始有1000用户，每天增加30用户，运行50天.
    # 每天有10%的人会尝试开发项目
    # 每天有50%的人会尝试浏览2个其他项目，如果这个项目属于自己，那么今天将不再浏览。
    # 新增加的用户会自带一个初始项目，但第一天不会做任何事情，之后会进入正轨。
    # 仅fork、star会被记录为一条边
    sys.stdout = open(r'data.csv','w')
    # 初始化有向图
    G = nx.DiGraph()
    # 建立初始用户1000名
    for _ in range(1000):
        g = ghi.GitHubUser()
        G.add_node(g)
    # 运行50天
    for _ in range(50):
        day()
    # 输出到文件，使用gephi进行数据分析
    for c in G.edges():
        print(c[0].id,c[1].id,sep = ',')
    sys.stdout.close()
