#coding=utf-8
from model.User_Relation import User_Relation
'''
Created on 2016年3月17日

@author: makao
给用户名编号，这样更方便在列表中更快地取到用户而不用遍历
'''

if __name__ == '__main__':
    name_num_dict = {}
    counter = 0
    
    user_relation_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/user_relation.txt'):
        uname = line.split('|')[0].strip()
        if uname == '用户-关系':
            continue
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        user_relation_list.append(user)
        
        name_num_dict[uname] = counter
        counter = counter + 1
    
    num_user_relation_list = []
    for item in user_relation_list:
        uname = item.name
        unumber = name_num_dict[uname]
        user = User_Relation(unumber)
        num_follower = []
        for flwr in item.follower:
            num_follower.append(name_num_dict[flwr.strip()])
        user.setFollower(num_follower)
        num_user_relation_list.append(user)
    
    for item in num_user_relation_list:
        print item