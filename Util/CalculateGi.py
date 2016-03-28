#coding=utf-8
from __future__ import division
from model.User_Relation import User_Relation
from CalculateCi import *
'''
Created on 2016年3月17日

@author: makao
3月18日改：
该中表示方法暂时不用
'''

if __name__ == '__main__':
    user_relation_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        uname = line.split('|')[0].strip()
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        user_relation_list.append(user)
        
    max_cfi = 0
    min_cfi = 10000
    cfi_list=[]
    for item in user_relation_list:
        ki = len(item.follower)
        neighbors_ki = 0
        for flwr in item.follower:
            flwr_ki = len(user_relation_list[int(flwr)].follower)
            neighbors_ki = neighbors_ki + flwr_ki
        fi = ki + neighbors_ki
        ci = calculateCi(item,user_relation_list)
        current_cfi = 0
        if fi != 0:
            current_cfi = ci/fi
        cfi_list.append(current_cfi)
        if current_cfi > max_cfi:
            max_cfi = current_cfi
        if current_cfi < min_cfi:
            min_cfi = current_cfi
        cfi_list.append(current_cfi)
    
    max_min_diff = max_cfi-min_cfi
    print max_cfi
    print min_cfi
    for item in cfi_list:
        print (max_cfi-item)/max_min_diff