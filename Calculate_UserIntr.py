#coding=utf-8
from __future__ import division
from model.User_Intr import User_Intr
import string
'''
Created on 2016年3月10日

@author: makao
计算出用户的横向兴趣度，形如：
apr | 视频_0.182 音乐_0.286 幽默_0.364 生活_0.052 美剧_0.117
'''

if __name__ == '__main__':
    user_intr=['用户-兴趣']
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_interest_partici.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = line.split('|')[1].strip().split()
        
        total_frequent=0
        interest_dict={}
        for item in interests:
            weight = item.split('_')[1]
            total_frequent+=string.atof(weight)
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            if total_frequent != 0:
                interest_dict[tag]=string.atof(weight)/total_frequent
            else:
                interest_dict[tag]=0
        user.setInterest(interest_dict)
        user_intr.append(user)
        #tag_interest.append(line.split()[1])
        #num_interest=num_interest+1
        
    for item in user_intr:
        print item