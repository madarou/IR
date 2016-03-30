#coding=utf-8
from __future__ import division
from model.User_Intr import User_Intr
from model.User_Relation import User_Relation
import string
'''
Created on 2016年3月26日

@author: makao
通过标签传播方式挖掘用户的兴趣社区
先不考虑使用rough core，因为所有标签都有初始化过了
'''
def isnumeric(s):
    '''returns True if string s is numeric'''
    return all(c in "0123456789.+-" for c in s)

def user_propagate(x, source_list, target_list, user_relation_list):
    '''
    用户x传播，去影响他的邻居，int型
    source_list是当前用户兴趣度列表
    target_list是用户x传播后的，初始时为0
    
    同步更新的方式
    '''
    x_user_intr = source_list[x]
    x_interest_dict = x_user_intr.interests
    x_user_relation = user_relation_list[x]
    x_neighbors_list = x_user_relation.follower
    for (key, value) in x_interest_dict.items():
        #如果是非兴趣标签，就不传播
        if not isnumeric(key):
            continue
        #neighbor_counter = 0
        for item in x_neighbors_list:
            #item是x的邻居的用户编号，字符型
            neighbor_user_intr = source_list[int(item)]
            neighbor_interest_dict = neighbor_user_intr.interests
            #如果neighbor_user_intr有标签key
            if key in neighbor_interest_dict.keys():
                #通过之前设计的公式计算当前标签key，用户x和当前邻居neighbor之间的传播衰减系数w(weaken)
                w = computeWeaken(key, x, int(item)) 
                target_list[int(item)].interests[key]=neighbor_interest_dict[key] + value*w
            else:
                w = computeWeaken(key, x, int(item))
                target_list[int(item)].interests[key]=value*w
            #neighbor_counter = neighbor_counter + 1

def normalizeIntr(before_list, after_list, user_interest_list, I):
    '''
    每轮传播结束后，整理各个用户的兴趣度，包括
    1.选出兴趣度最高的I个兴趣和兴趣度
    2.重新计算用户兴趣度
    '''
    for i in range(0,len(before_list)):
        #对user的interest_dict按value值从大到小进行排序
        user = before_list[i]
        interest_dict = user.interests
        #interest_dict.sort(lambda y, x: cmp(x[1],y[1]))
        sorted(interest_dict.items(), key = lambda d:d[1])
        counter = 0 #记录取最大的前I个兴趣
        
        user_after = User_Intr(user_interest_list[i].name)
        new_interest_dict = {}
        #选出最大的I个兴趣
        intr_sum = 0#前I个兴趣的度的总和，后面归一化用
        for (key, value) in interest_dict.items():
            if counter == I:
                break
            new_interest_dict[key] = value
            intr_sum = intr_sum + string.atof(value)
            counter = counter + 1
        #归一化
        for (key, value) in new_interest_dict.items():
            new_interest_dict[key] = string.atof(value)/intr_sum

        user_after.setInterest(new_interest_dict)
        after_list.append(user_after)
        
def computeWeaken(tag, user_i, user_j):
    return 1

def tag_distribution(user_interest_list):
    '''
    统计user_interest_list中各个兴趣总共出现的次数，即各个tag出现的user个数
    '''
    result = set()
    result_dict = {}
    for item in user_interest_list:
        interests_dict = item.interests
        for key in interests_dict.keys():
            if key in result_dict.keys():
                result_dict[key] = result_dict[key] + 1
            else:
                result_dict[key] = 1
    for (key, value) in result_dict.items():
        result.add((key, value))
    
    return result

if __name__ == '__main__':
    MAX_TAG_NUM = 8#传播时，每个用户保留的最大标签数
    user_interest_list=[]
    line_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = string.atof(weight)
        user.setInterest(interests_dict)
        user_interest_list.append(user)
        line_counter = line_counter + 1
    
    user_relation_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        uname = line.split('|')[0].strip()
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        user_relation_list.append(user)
    #读取rough core
#     cores_list = []
#     for line in open('/Users/makao/Yun/Workspace/lab/data/rough_core.txt'):
#         cores_list.append(line.strip().strip('[]').split(', '))
    #初始化
    target_list = []
    for i in range(0, line_counter):
        user = User_Intr('None')
        target_list.append(user)
    
    after_list = []
        
    for i in range(0, line_counter):
        user_propagate(i, user_interest_list, target_list, user_relation_list)
        
    normalizeIntr(target_list, after_list, user_interest_list, MAX_TAG_NUM)
    old_tag_distribution = tag_distribution(after_list)
    new_tag_distribution = set()
    
    #如果没有稳定，需要再次传播，after_list就成了下一轮的初始传播list
    run = 0
    while len(old_tag_distribution.symmetric_difference(new_tag_distribution))>0:
        print str(run) + ' run'
        for item in target_list:
            item.setInterest({})
        old_tag_distribution = tag_distribution(after_list)
        for i in range(0, line_counter):
            user_propagate(i, after_list, target_list, user_relation_list)
        del after_list[:]
        normalizeIntr(target_list, after_list, user_interest_list, MAX_TAG_NUM)
        new_tag_distribution = tag_distribution(after_list)
        run = run + 1
    
    for item in after_list:
        print item