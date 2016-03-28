#coding=utf-8
from model.User_Relation import User_Relation
'''
Created on 2016年3月25日

@author: makao
标签传播前，找初始传播的core
'''

if __name__ == '__main__':
    user_degree_list=[]#存各个用户被关注的度，即出度
    user_relation_list=[]
    total_user_num = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        user_number = line.split('|')[0].strip()
        follower_list = line.split('|')[1].strip().split()
        user = User_Relation(user_number)
        user.setFollower(follower_list)
        user_relation_list.append(user)
        user_degree_list.append((int(user_number),len(follower_list)))
        total_user_num = total_user_num + 1
    
    has_accessed_list = [0]*total_user_num#标记第i号点已经在core中了值为1，否则为0
    #按出度大小排序
    user_degree_list.sort(lambda y,x:cmp(x[1],y[1]))
    for item in user_degree_list:
        user_number = item[0]
        user_degree = item[1]
        