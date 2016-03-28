#coding=utf-8
from __future__ import division
from model.User_Relation import User_Relation
from model.User_Intr import User_Intr
import itertools 
'''
Created on 2016年3月18日

@author: makao
计算一个点的兴趣标签的集聚系数ti
ti=2hi/[ki(ki-1)]
hi 表示节点 i 与其任意两个邻居节点之间的标签所形成的三角形的个数,比如i的两个邻居都有tag x，则视为构成一个三角形,
不管有多少个相同的标签，都只算一个，为了降低算法的复杂度
ki是i的度

最后使用趋同化方法将ti和ci相加
'''

def getUserInteresttags(user_number,user_interest_list):
    '''
    已知一个User_Relation对象，从User_Intr对象列表中取出这个对象的所有兴趣标签,
    为了提高效率，user_intr也应该number化
    '''
    #uname = user_relation.name
    user = user_interest_list[int(user_number)]
    interests = user.interests
    tags = []
    for key in interests:
        tags.append(key)
    return set(tags)

def calculateTi(user_relation,user_relation_list,user_interest_list):
    """
    计算节点 user_relation 与其任意两个邻居节点之间相同标签形成的三角形的个数 后 算出集聚系数Ti
    """
    ki = len(user_relation.follower)
    if ki < 2:
        return 0
    triangle = 0
    tag_set_i = getUserInteresttags(user_relation.name,user_interest_list)#用户i的所有兴趣标签构成的集合
    #先选出与i有至少一个相同标签的人
    has_common_tag_users = []
    for item in user_relation.follower:
        tag_set_item = getUserInteresttags(item,user_interest_list)
        if tag_set_i & tag_set_item:
            has_common_tag_users.append(item)
            
    for item in list(itertools.combinations(has_common_tag_users,2)):
        if getUserInteresttags(item[0],user_interest_list) & getUserInteresttags(item[1],user_interest_list):
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
    
    user_interest_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = weight
        user.setInterest(interests_dict)
        user_interest_list.append(user)
        
    for item in user_relation_list:
        print calculateTi(item,user_relation_list,user_interest_list)