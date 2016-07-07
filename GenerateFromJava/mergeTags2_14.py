#coding=utf-8
'''
Created on 2016年6月26日

@author: makao
将第13步中输出的final_user_intr.txt根据tag_group.txt中的标签分组重新整合，
统一组中的标签归为一个新的组，兴趣度为该组下面标签的兴趣度之和
'''
from model.User_Intr import User_Intr
import string

if __name__ == '__main__':
    user_interest_list=[]
    #标签字典，key为子标签，value为该标签在tag_group.txt中被划分到的组，即该文件中的第几行就标为第几组
    tag_group_dict = {}
    line_counter = 0
    ff = open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag_interest_merge2.txt','w')
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag-group2.txt'):
        tags = line.split()
        for t in tags:
            tag_group_dict[t.strip()]=line_counter
        print >> ff, '%d %s' % (line_counter, tags[0])
        line_counter = line_counter + 1

    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/final_user_intr_merged_2.txt','w')
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/final_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = string.atof(weight)
        new_interests_dict = {}#一个新的用户兴趣key：value字典，将同一个group下的标签合并，并将兴趣度相加到一起
        i = -1
        has_added_key2=[]#记录在前面的遍历中，已经因为tag_group_dict[key]==tag_group_dict[key2]而被访问过的key2，不再访问
        for key in sorted(interests_dict):
            i = i + 1
            j = 0
            for key2 in sorted(interests_dict):
                if j < i:
                    j = j + 1
                    continue
                if key2 in has_added_key2:
                    continue
                if key == key2:
                    new_interests_dict[tag_group_dict[key]]=interests_dict[key]
                    #print key, tag_group_dict[key],new_interests_dict[tag_group_dict[key]],"11"
                elif key != key2 and tag_group_dict[key]==tag_group_dict[key2]:
                    new_interests_dict[tag_group_dict[key]]=new_interests_dict[tag_group_dict[key]]+interests_dict[key2]
                    has_added_key2.append(key2)
                    #print key, tag_group_dict[key],new_interests_dict[tag_group_dict[key]],"22"
                else:
                    new_interests_dict[tag_group_dict[key]]=interests_dict[key]
                    #print key, tag_group_dict[key],new_interests_dict[tag_group_dict[key]],"33"
                    
        user.setInterest(new_interests_dict)
        user_interest_list.append(user)
    for item in user_interest_list:
        print >> f, '%s' % item    
    
    