#coding=utf-8
'''
Created on 2016年6月27日

@author: makao
生成用于对比的final_user_intr_1.txt
0-0.6的比例的标签被修改为其一个group下的其他标签，
并且将0.8-1比例的标签的兴趣度减小为原来的0.6-1
'''
from __future__ import division
from model.User_Intr import User_Intr
import string
import random

if __name__ == '__main__':
    tag_group_dict = {}
    group_tag_dict = {}
    line_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/intrcom-compare/tag-group2.txt'):
        tag_list = []
        tags = line.split()
        for t in tags:
            tag_group_dict[t.strip()]=line_counter
            tag_list.append(t)
        group_tag_dict[line_counter]=tag_list
        line_counter = line_counter + 1
    
    user_interest_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/intrcom-compare/final_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = string.atof(weight)
        
        new_interests_dict = {}#修改后的用户兴趣度
        change_tag_n = int(round(random.randint(0,6)/10*len(interests_dict)))#0-0.6的比例的标签被修改为其一个group下的其他标签中按比例算出来的当前应该取几个标签来被修改
        print 'change_tag_n', change_tag_n, len(interests_dict)
        access_mark={}#记录之前随机访问已经访问过的tag，保证访问过了就不访问
        i = 0
        while i < change_tag_n:
            tag_index = random.randint(0,len(interests_dict)-1)
            j = 0
            for (key, value) in interests_dict.items():
                if tag_index == j:
                    if key in access_mark.keys():
                        i = i - 1
                        break
                    else:
                        access_mark[key]=value
                        break
                else:
                    j = j + 1
                    #new_interests_dict[key]=value
            i = i + 1           
        for (key,value) in interests_dict.items():
            if not key in access_mark.keys():
                new_interests_dict[key]=value
        #现在access_mark中记录的就是要修改的tag的key:value
        for (key, value) in access_mark.items():
            #将标签改为同一group下的其他标签
            group_list = group_tag_dict[tag_group_dict[key]]
            #在group_list中随机选一个标签来替代它
            while True:
                random_index = random.randint(0,len(group_list)-1)
                target_tag = group_list[random_index]
                if target_tag in new_interests_dict.keys():
                    continue
                else:
                    new_interests_dict[target_tag]=value
                    #print '标签%s被修改为%s,兴趣度%s' % (key, target_tag, value)
                    break

        change_tag_n = int(round(random.randint(8,10)/10*len(new_interests_dict)))
        changed=[]
        i = 0
        while i < change_tag_n:
            change_index = random.randint(0,len(new_interests_dict)-1)
            while change_index in changed:
                change_index = random.randint(0,len(new_interests_dict)-1)
            changed.append(change_index)
            j = 0
            for (k,v) in new_interests_dict.items():
                if j != change_index:
                    j = j + 1
                else:
                    new_interests_dict[k]=v*(random.randint(6,10)/10.0)
                    break
            i = i + 1
        #print change_tag_n,len(new_interests_dict)   
#         for (key,value) in new_interests_dict.items():
#             print key, value 
        user.setInterest(new_interests_dict)
        user_interest_list.append(user)
    
    ff = open('/Users/makao/Yun/Workspace/lab/data/java_relation/intrcom-compare/final_user_intr_1.txt','w')
    for item in user_interest_list:
        print >> ff, '%s' % item