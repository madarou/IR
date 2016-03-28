#coding=utf-8
from model.User_Intr import User_Intr
import random
'''
Created on 2016年3月9日

@author: makao

打印出用户所有标签和对应标签的话题参与次数，形如：
apr | 视频_14 音乐_22 幽默_28 生活_4 美剧_9
'''

if __name__ == '__main__':
    MAX_INTEREST_NUM=7#处理职业和地址外，兴趣标签最多可拥有的个数
    MAX_FREQUENT_NUM=36#某个interest标签的最多讨论次数
    MAX_LOCATION_FREQUENT_NUM=6#关于location的话题，一个用户最大的讨论次数
    MAX_JOB_FREQUENT_NUM=18#关于职业的话题，一个用户最大的讨论次数
    
    tag_interest=['兴趣']
    num_interest=0
    frequent_interest=['高频兴趣']
    tag_job=['工作']
    num_job=0
    tag_location=['地址']
    num_location=0
    user_intr=['用户-兴趣']
    
    for line in open('/Users/makao/Yun/Workspace/lab/data/tag-interest.txt'):
        tag_interest.append(line.split()[1])
        num_interest=num_interest+1
    for line in open('/Users/makao/Yun/Workspace/lab/data/frequent-interest.txt'):
        frequent_interest.append(line.split()[1])
    for line in open('/Users/makao/Yun/Workspace/lab/data/tag-job.txt'):
        tag_job.append(line.split()[1])
        num_job=num_job+1
    for line in open('/Users/makao/Yun/Workspace/lab/data/tag-location.txt'):
        tag_location.append(line.split()[1])
        num_location=num_location+1
        
    for line in open('/Users/makao/Yun/Workspace/lab/data/username.txt'):
        uname=line.split()[0]#不用[0]而直接用line回出现utf-8编码
        user = User_Intr(uname)
        interest_dict={}
        
        #生成兴趣
        interest_num=random.randint(1,MAX_INTEREST_NUM)
        for i in range(1,interest_num+1):
            chooser = random.randint(1,num_interest)
            target_interest=tag_interest[chooser]
            if target_interest in frequent_interest:
                interest_dict[target_interest]=random.randint(0,MAX_FREQUENT_NUM+random.randint(0,10))
            else:
                interest_dict[target_interest]=random.randint(0,MAX_FREQUENT_NUM)
        
        #生成地址
        location_chooser=random.randint(1,4)
        if location_chooser % 4 == 0:
            interest_dict[tag_location[random.randint(1,num_location)]]=random.randint(0,MAX_LOCATION_FREQUENT_NUM)
        elif location_chooser % 4 ==1:
            r1 = random.randint(1,num_location)
            r2 = random.randint(1,num_location)
            interest_dict[tag_location[r1]]=random.randint(0,MAX_LOCATION_FREQUENT_NUM)
            if r1 != r2:
                interest_dict[tag_location[r2]]=random.randint(0,MAX_LOCATION_FREQUENT_NUM)
        
        #生成职业
        job_chooser=random.randint(1,4)
        if job_chooser % 4 == 0:
            interest_dict[tag_job[random.randint(1,num_job)]]=random.randint(0,MAX_JOB_FREQUENT_NUM)
            
        user.setInterest(interest_dict)
        user_intr.append(user)   
        
    #直接print tag_interest打印出来的是utf-8编码，遍历打印就正常
    #for item in tag_job:
        #print item
        
    for item in user_intr:
        print item
    
    