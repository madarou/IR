#coding=utf-8
from __future__ import division
from model.User_Relation import User_Relation
from model.User_Intr import User_Intr
'''
Created on 2016年3月19日

@author: makao
计算用户的相似性，只计算相邻用户间的
'''

if __name__ == '__main__':
    LOCATION_WEIGHT = 1.1#如果两个人来自同一个地方的权重
    location_tags = set()
    
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
    
    similarity = []
    for i in range(0, line_counter):
        tmp = []
        for j in range(0, line_counter):
            tmp.append(0)
        similarity.append(tmp)
    #print similarity
    
    for item in user_relation_list:
        uname = item.name
        a_user_intr = user_interest_list[int(uname)]
        a_tags = a_user_intr.getInterestTags()
        for flwr in item.follower:
            b_user_intr = user_interest_list[int(flwr)]
            b_tags = b_user_intr.getInterestTags()
            intersactions = a_tags & b_tags
            if len(intersactions) > 0:
                if intersactions & location_tags:#如果两个人来自同一个地方
                    similarity[int(uname)][int(flwr)]=(len(intersactions)/len(b_tags))*LOCATION_WEIGHT
                else:
                    similarity[int(uname)][int(flwr)]=len(intersactions)/len(b_tags)
                    #print len(intersactions)/len(b_tags)
    for i in similarity:
        print i