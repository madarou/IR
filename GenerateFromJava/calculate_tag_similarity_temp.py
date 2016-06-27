#coding=utf-8
'''
Created on 2016年5月9日

@author: makao

通过tag之间公共用户数量占两者数量和的比例来作为两个标签的相似度
'''
from __future__ import division
from model.Intr_User import Intr_User
import itertools

if __name__ == '__main__':
    interest_user_list=[]
    interest_one_frequent=[]#兴趣标签的频繁1项集，即各个标签分别被多少用户所拥有
    tag_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_intr_user.txt'):
        if line.strip() == '兴趣-用户':
            continue
        tag_number = line.split('|')[0].strip()
        user_number_list = line.split('|')[1].split()
        interest_one_frequent.append(len(user_number_list))
        intr_user = Intr_User(tag_number)
        intr_user.setOwner(user_number_list)
        interest_user_list.append(intr_user)
        tag_counter = tag_counter + 1
    
    fitness = []
    for i in range(0, tag_counter):
        tmp = []
        for j in range(0, tag_counter):
            if i == j:
                tmp.append(1)
            else:
                tmp.append(0)
        fitness.append(tmp)
     
    #挖掘频繁二项集
    #interest_two_frequent=[]
    total_similarity=[]
    for item in list(itertools.combinations(range(0,tag_counter),2)):
        interest_user_i = interest_user_list[item[0]]
        interest_user_j = interest_user_list[item[1]]
        owners_i = set(interest_user_i.owner)
        owners_j = set(interest_user_j.owner)
        intersaction_number = len(owners_i & owners_j)
        total_number = len(owners_i)+len(owners_j)
        if intersaction_number > 0:
            fitness[item[0]][item[1]]=intersaction_number/total_number
            fitness[item[1]][item[0]]=intersaction_number/total_number
            total_similarity.append(intersaction_number/total_number)
        else:
            total_similarity.append(0)
    
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag_similarity_temp.txt','w')
    for item in fitness:
        #print >> f, '%s' % item  
        item.sort()
        print >> f, '%s' % item  
    f.close()
    
    total_similarity.sort()
    for item in total_similarity:
        print item
    print len(total_similarity)