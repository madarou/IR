#coding=utf-8
from model.User_Intr import User_Intr
'''
Created on 2016年3月19日

@author: makao
给user-interest.txt中的用户姓名编号
'''

if __name__ == '__main__':
    name_num_dict = {}
    counter = 0
    
    user_interest_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/user-interest.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(counter)
        interests = line.split('|')[1].strip().split()
        
        interest_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interest_dict[tag] = weight
        user.setInterest(interest_dict)
        user_interest_list.append(user)
        
        counter = counter + 1
    
    for item in user_interest_list:
        print item
