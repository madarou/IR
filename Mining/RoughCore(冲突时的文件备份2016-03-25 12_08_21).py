#coding=utf-8
from model.User_Relation import User_Relation
'''
Created on 2016年3月25日

@author: makao
标签传播前，找初始传播的core
'''

if __name__ == '__main__':
    user_degree_list=[]#存各个用户被关注的度，即出度
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        user_number = line.split('|')[0].strip()
        follower_list = line.split('|')[1].strip()
        user = User_Relation(user_number)
        user.setFollower(follower_list)
        
        