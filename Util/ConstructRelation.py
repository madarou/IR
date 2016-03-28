#coding=utf-8
import random
from model.User_Relation import User_Relation
'''
Created on 2016年3月10日

@author: makao
生成用户关注关系
'''

if __name__ == '__main__':
    MAX_FOLLOW_NUM=7#一个用户最多关注人数
    
    user_relation_list=['用户-关系']
    userlist=['用户列表']
    user_num=0
    for line in open('/Users/makao/Yun/Workspace/lab/data/username.txt'):
        userlist.append(line.split()[0].strip())
        user_num=user_num+1
    for line in open('/Users/makao/Yun/Workspace/lab/data/username.txt'):
        uname = line.split()[0].strip()
        user = User_Relation(uname)
        follower_num=random.randint(0,MAX_FOLLOW_NUM)
        follower=[]
        #choosed_users=[]
        for i in range(0,follower_num):
            choosen_user = userlist[random.randint(1,user_num)]
            if choosen_user in follower or choosen_user == uname:
                continue
            follower.append(choosen_user)
            #choosed_users.append(choosen_user)
        user.setFollower(follower)
        user_relation_list.append(user)
    
    for item in user_relation_list:
        print item