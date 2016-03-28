#coding=utf-8
from __future__ import division
from model.User_Relation import User_Relation
import itertools 
'''
Created on 2016年3月17日

@author: makao
计算一个点的集聚系数ci
ci=2ei/[ki(ki-1)]
ei 表示节点 i 与其任意两个邻居节点之间所 形成的三角形的个数 
ki是i的度

'''
def perm(l):  
    if(len(l)<=1):  
        return [l]  
    r=[]  
    for i in range(len(l)):  
        s=l[:i]+l[i+1:]#取第0至i-1项和i以后的所有项
        p=perm(s)#这里只是一个比较特别赋值语句而已,里面放的是s，长度为len(l)-1
        for x in p:  
            r.append(l[i:i+1]+x)#将第i项与p中的值进行组合
    return r

def calculateEi(user_relation,user_relation_list):
    """
    计算节点 user_relation 与其任意两个邻居节点之间所 形成的三角形的个数 
    """
    ki = len(user_relation.follower)
    if ki < 2:
        return 0
    triangle = 0
    for item in list(itertools.combinations(user_relation.follower,2)):
        if (item[1] in user_relation_list[int(item[0])].follower) or (item[0] in user_relation_list[int(item[1])].follower):
            triangle = triangle + 1
    return triangle

def calculateCi(user_relation,user_relation_list):
    """
    计算user_relation的集聚系数
    """
    ki = len(user_relation.follower)
    if ki < 2:
        return 0
    triangle = 0
    for item in list(itertools.combinations(user_relation.follower,2)):
        if (item[1] in user_relation_list[int(item[0])].follower) or (item[0] in user_relation_list[int(item[1])].follower):
            triangle = triangle + 1
    return 2*triangle/(ki*(ki-1))

if __name__ == '__main__':
    #for item in perm([1,2,3,4]):
    #    print item
    user_relation_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        uname = line.split('|')[0].strip()
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        user_relation_list.append(user)
        
    for item in user_relation_list:
        print calculateCi(item,user_relation_list)