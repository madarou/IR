#coding=utf-8
from __future__ import division
from model.Intr_User import Intr_User
import itertools 
'''
Created on 2016年3月22日

@author: makao
使用关联规则，计算任意两个标签的之间的相互传播影响的置信度
比如在传播标签i时，用户已经有标签j了，那用户接受标签i的概率有多大
只计算兴趣标签的，地点和工作的标签不计算，因为这之间没有关联性

得到二维矩阵fitness，fitness[i][j]表示在用户拥有标签i的情况下，接受标签j的概率
'''

if __name__ == '__main__':
    interest_user_list=[]
    interest_one_frequent=[]#兴趣标签的频繁1项集，即各个标签分别被多少标签所拥有
    tag_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_intr_user.txt'):
        if line.strip() == '兴趣-用户':
            continue
        tag_number = line.split('|')[0].strip()
        user_number_list = line.split('|')[1].split()
        interest_one_frequent.append(len(user_number_list))
        intr_user = Intr_User(tag_number)
        intr_user.setOwner(user_number_list)
        interest_user_list.append(intr_user)
        tag_counter = tag_counter + 1
    
    fitness = []
    for i in range(0, tag_counter):
        tmp = []
        for j in range(0, tag_counter):
            if i == j:
                tmp.append(1)
            else:
                tmp.append(0)
        fitness.append(tmp)
     
    #挖掘频繁二项集
    #interest_two_frequent=[]
    for item in list(itertools.combinations(range(0,tag_counter),2)):
        interest_user_i = interest_user_list[item[0]]
        interest_user_j = interest_user_list[item[1]]
        owners_i = set(interest_user_i.owner)
        owners_j = set(interest_user_j.owner)
        intersaction_number = len(owners_i & owners_j)
        if intersaction_number > 0:
            fitness[item[0]][item[1]]=intersaction_number/interest_one_frequent[item[0]]
            fitness[item[1]][item[0]]=intersaction_number/interest_one_frequent[item[1]]
    
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag_fitness.txt','w')
    for item in fitness:
        print >> f, '%s' % item  
    f.close()
    
    