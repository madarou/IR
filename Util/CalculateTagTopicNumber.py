#coding=utf-8
from __future__ import division
from model.User_Intr import User_Intr
'''
Created on 2016年3月21日

@author: makao
计算各类标签话题总的话题数

tag_topic_num_total.txt中存了各个兴趣标签下当前话题的总数
(tag_number topic_total_number)
前面是兴趣标签
后面是其他标签

not_interest_tag_number_total.txt打印非兴趣标签名，编号和其次数的对应关系
非兴趣标签 编号 话题次数
'''

def isnumeric(s):
    '''returns True if string s is numeric'''
    return all(c in "0123456789.+-" for c in s)

if __name__ == '__main__':
    DELTA_T = 7#设置初步的时间跨度是7天
    
    user_interest_list=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_interest.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests_list = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests_list:
                tag_number = item.split('_')[0].strip()
                topic_number = item.split('_')[1].strip()
                interests_dict[tag_number] = topic_number
        user.setInterest(interests_dict)
        user_interest_list.append(user)
    #统计各个标签当前时间t2的话题数N2，即各个标签对应的话题总数
    #num_intr_user.txt里面存的是兴趣类的标签，先统计兴趣类的标签
    interest_tag_topic_total_list = []
    interest_tag_number = 0#统计interest标签数
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_intr_user.txt'):
        interest_tag_topic_total=0
        tag_number = line.split('|')[0].strip()
        user_numbers_list = line.split('|')[1].strip().split()
        for item in user_numbers_list:
            user = user_interest_list[int(item)]
            tag_topic_number = int(user.interests[tag_number])
            interest_tag_topic_total = interest_tag_topic_total + tag_topic_number
        interest_tag_topic_total_list.append(interest_tag_topic_total)
        interest_tag_number = interest_tag_number + 1
    i=0
    for item in interest_tag_topic_total_list:
        print (i,item)
        i = i + 1
    
    not_interest_tag_dict = {}#非兴趣标签{标签名:总次数#标签编号}标签编号是接兴趣标签编号的
    not_interest_tag_number = interest_tag_number
    for user in user_interest_list:
        interest_dict = user.interests
        for (key,value) in interest_dict.items():
            if not isnumeric(key):
                outer_value = int(value)
                #先检查是否已在not_interest_tag_dict中
                if key in not_interest_tag_dict.keys():
                    tag_number = not_interest_tag_dict[key].split('#')[1].strip()
                    topic_number = not_interest_tag_dict[key].split('#')[0].strip()
                    not_interest_tag_dict[key]=str(int(topic_number)+outer_value)+'#'+tag_number
                else:
                    not_interest_tag_dict[key]=str(outer_value)+'#'+str(not_interest_tag_number)
                    not_interest_tag_number = not_interest_tag_number + 1
    
    tosorted_not_interest_dict={}#按标签编号由小到大排序{标签编号:话题次数}
    for (key,value) in not_interest_tag_dict.items():
        #print key +' '+ str(value)
        tosorted_not_interest_dict[value.split('#')[1].strip()]=value.split('#')[0].strip()
    result = sorted(tosorted_not_interest_dict.items(), key=lambda d:d[0])#按key对tosorted_not_interest_dict字典排序
    for item in result:
        print (int(item[0]),int(item[1]))
    #打印非兴趣标签名，编号和其次数的对应关系
    for (key,value) in not_interest_tag_dict.items():
        print value.split('#')[1].strip()+ ' ' + key+' '+value.split('#')[0].strip()
    #统计各个标签在截至时间为t1时的各自的话题数N1
    #统计各个标签在截至时间为t2时的各自的话题数N2
    #计算Δ2=N2-N1/t2-t1
    #计算Δ1=N1-N0/t1-t0
    #计算Ini=Δ2/Δ1