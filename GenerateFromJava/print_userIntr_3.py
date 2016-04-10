#coding=utf-8
from __future__ import division
from model.User_Intr import User_Intr
from model.Intr_User import Intr_User
import random
'''
Created on 2016年3月9日

@author: makao

打印出用户所有标签和对应标签的话题参与次数，形如：
apr | 视频_14 音乐_22 幽默_28 生活_4 美剧_9

3月22号改:
在生成如上格式的同时，
1. 将兴趣标签number化，地点和工作标签照旧
2. 同时统计各个标签对应的被拥有的用户数
3. 标签参与次数/间隔天数存入num_user_interest_partici.txt中
4. 标签参与次数存入num_user_intrerest.txt中(统计Infectivity要用)
'''

if __name__ == '__main__':
    MAX_INTEREST_NUM=7#除职业和地址外，兴趣标签最多可拥有的个数
    MAX_FREQUENT_NUM=36#某个interest标签的最多讨论次数
    MAX_LOCATION_FREQUENT_NUM=6#关于location的话题，一个用户最大的讨论次数
    MAX_JOB_FREQUENT_NUM=18#关于职业的话题，一个用户最大的讨论次数
    MAX_INTERVAL_DAY=5#最大讨论间隔天数
    
    tag_interest=['兴趣']
    num_interest=1
    frequent_interest=['高频兴趣']
    tag_job=['工作']
    num_job=1
    tag_location=['地址']
    num_location=1
    user_intr=['用户-兴趣']#存的是有除以时间MAX_INTERVAL_DAY的
    user_interest=['用户-兴趣']#存的是没有除以MAX_INTERVAL_DAY的，单纯记录话题次数
    
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag-interest.txt'):
        tag_interest.append(line.split()[0])
        num_interest=num_interest+1
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/frequent-interest.txt'):
        frequent_interest.append(line.split()[0])
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag-job.txt'):
        tag_job.append(line.split()[1])
        num_job=num_job+1
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag-location.txt'):
        tag_location.append(line.split()[1])
        num_location=num_location+1
    
    interest_user_list = ['兴趣-用户']
    for item in range(0,num_interest-1):
        intr_user=Intr_User(str(item))
        interest_user_list.append(intr_user)
    num_user=0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/extracted_names.txt'):
        uname=line.split()[0]#不用[0]而直接用line回出现utf-8编码
        user = User_Intr(uname+'#'+str(num_user))
        interest_dict={}
        
        user2 = User_Intr(uname+'#'+str(num_user))
        user2_interest_dict={}
        #生成兴趣
        interest_num=random.randint(1,MAX_INTEREST_NUM)
        for i in range(1,interest_num+1):
            chooser = random.randint(1,num_interest-1)
            target_interest=tag_interest[chooser]
            if target_interest in frequent_interest:
                topic_number = random.randint(0,MAX_FREQUENT_NUM+random.randint(0,10))
                interest_dict[target_interest]=topic_number/random.randint(1,MAX_INTERVAL_DAY)
                user2_interest_dict[target_interest]=topic_number
                interest_user_list[chooser].appendOwner(num_user)
            else:
                topic_number=random.randint(0,MAX_FREQUENT_NUM)
                interest_dict[target_interest]=topic_number/random.randint(1,MAX_INTERVAL_DAY)
                user2_interest_dict[target_interest]=topic_number
                interest_user_list[chooser].appendOwner(num_user)
        
        #生成地址
        location_chooser=random.randint(1,4)
        if location_chooser % 4 == 0:
            topic_number = random.randint(0,MAX_LOCATION_FREQUENT_NUM)
            target_interest = random.randint(1,num_location-1)
            interest_dict[tag_location[target_interest]]=topic_number
            user2_interest_dict[tag_location[target_interest]]=topic_number
        elif location_chooser % 4 ==1:
            r1 = random.randint(1,num_location-1)
            r2 = random.randint(1,num_location-1)
            topic_number = random.randint(0,MAX_LOCATION_FREQUENT_NUM)
            interest_dict[tag_location[r1]]=topic_number/random.randint(1,MAX_INTERVAL_DAY)
            user2_interest_dict[tag_location[r1]]=topic_number
            if r1 != r2:
                topic_number_2 = random.randint(0,MAX_LOCATION_FREQUENT_NUM)
                interest_dict[tag_location[r2]]=topic_number_2/random.randint(1,MAX_INTERVAL_DAY)
                user2_interest_dict[tag_location[r2]]=topic_number_2
        
        #生成职业
        job_chooser=random.randint(1,4)
        if job_chooser % 4 == 0:
            topic_number = random.randint(0,MAX_JOB_FREQUENT_NUM)
            target_interest = random.randint(1,num_job-1)
            interest_dict[tag_job[target_interest]]=topic_number/random.randint(1,MAX_INTERVAL_DAY)
            user2_interest_dict[tag_job[target_interest]]=topic_number
            
        user.setInterest(interest_dict)
        user_intr.append(user)   
        
        user2.setInterest(user2_interest_dict)
        user_interest.append(user2)
        num_user = num_user + 1
    #直接print tag_interest打印出来的是utf-8编码，遍历打印就正常
    #for item in tag_job:
        #print item
    
    fuser_interest = open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_user_interest.txt','w')
    fuser_intr = open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_user_interest_partici.txt','w')
    fnum_intr_user = open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_intr_user.txt','w')
    for item in user_interest:
        print >> fuser_interest,'%s' % item
    for item in user_intr:
        print >> fuser_intr, '%s' % item
    for item in interest_user_list:
        print >> fnum_intr_user, '%s' % item
        
    fuser_interest.close()
    fuser_intr.close()
    fnum_intr_user.close()
    