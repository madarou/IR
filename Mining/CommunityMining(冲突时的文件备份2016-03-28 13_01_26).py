#coding=utf-8
from __future__ import division
from model.User_Intr import User_Intr
from model.User_Relation import User_Relation
'''
Created on 2016年3月26日

@author: makao
通过标签传播方式挖掘用户的兴趣社区
先不考虑使用rough core，因为所有标签都有初始化过了
'''

def user_propagate(x, source_list, target_list):
    '''
    用户x传播，去影响他的邻居
    source_list是当前用户兴趣度列表
    target_list是用户x传播后的，初始时为0
    '''
    x_user = source_list[x]
    x_neighbors_dict = x_user.interests
    for (key,value) in x_neighbors_dict.items():
        
        
if __name__ == '__main__':
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
            interests_dict[tag] = weight
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