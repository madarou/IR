#coding=utf-8
from model.User_Intr import User_Intr
from model.Intr_User import Intr_User
import string
'''
Created on 2016年3月30日

@author: makao
将CommunityMining中的结果重新整理成
兴趣 | 用户1_兴趣度 用户2_兴趣度 ...
的形式
并且按兴趣度的大小排序用户的顺序
'''

if __name__ == '__main__':
    
    interest_counter = 0
    interest_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/tag-interest.txt'):
        interest_list.append(line.strip().split()[1])
        interest_counter = interest_counter + 1
        
    user_interest_list=[]
    intr_username_list=[]#用来存用户名字，展示用
    intr_usernumber_list=[]#存用户编号
    for i in range(0,interest_counter):
        intr_username_list.append(Intr_User('None'))
        intr_usernumber_list.append(Intr_User('None'))
    
    line_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/final_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = string.atof(weight)

            intr_username = intr_username_list[int(tag)]
            intr_usernumber = intr_usernumber_list[int(tag)]
            if intr_username.name == 'None':
                intr_username.name = interest_list[int(tag)]+'#'+tag
            if intr_usernumber.name == 'None':
                intr_usernumber.name = interest_list[int(tag)]+'#'+tag
            intr_username.owner.append(uname.split('#')[0]+'#'+weight)
            intr_usernumber.owner.append(uname.split('#')[1]+'#'+weight)
            
        user.setInterest(interests_dict)
        user_interest_list.append(user)
        line_counter = line_counter + 1
    
    #将intr_username_list和intr_usernumber_list按照用户兴趣度排序
    for intr in intr_username_list:
        owners = intr.owner
        user_weight_dict = {}
        for item in owners:
            uname = item.strip().split('#')[0]
            weight = string.atof(item.strip().split('#')[1])
            user_weight_dict[uname] = weight
        user_weight_list = sorted(user_weight_dict.items(), key = lambda d:d[1], reverse=True)
        new_owner_list = []
        for item in user_weight_list:
            new_owner_list.append(item[0]+'_'+str(item[1]))
        intr.setOwner(new_owner_list)
    
    for intr in intr_usernumber_list:
        owners = intr.owner
        user_weight_dict = {}
        for item in owners:
            unumber = item.strip().split('#')[0]
            weight = string.atof(item.strip().split('#')[1])
            user_weight_dict[unumber] = weight
        user_weight_list = sorted(user_weight_dict.items(), key = lambda d:d[1], reverse=True)
        new_owner_list = []
        for item in user_weight_list:
            new_owner_list.append(item[0]+'_'+str(item[1]))
        intr.setOwner(new_owner_list)
        
    #这里打印出的是只有兴趣标签的，兴趣对应的用户列表，用户列表是按兴趣度从大到小排的
    for item in intr_username_list:
        print item
    for item in intr_usernumber_list:
        print item
    
    #将用户的