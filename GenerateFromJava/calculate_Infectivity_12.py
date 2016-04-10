#coding=utf-8
from __future__ import division
import random
'''
Created on 2016年3月21日

@author: makao
计算各类标签在近期的感染度

tag_topic_num_total.txt中存了各个兴趣标签下当前话题的总数
(tag_number topic_total_number)
前面是兴趣标签
后面是其他标签
'''

def isnumeric(s):
    '''returns True if string s is numeric'''
    return all(c in "0123456789.+-" for c in s)

if __name__ == '__main__':
    DELTA_T = 7#设置初步的时间跨度是7天
    
    total_t2_list=[]#t2时的话题量
    #total_t1_list=[]#t1时的话题量
    #total_t0_list=[]#t0时的话题量
    #delta2_list = []
    #delta1_list = []
    infectivity = []
    
    tag_total_number = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag_topic_num_total.txt'):
        #tag_number = line.split(',')[0].lstrip('(').strip()
        topic_number = line.split(',')[1].strip().rstrip(')')
        total_t2_list.append(int(topic_number))
        tag_total_number = tag_total_number + 1
    #统计各个标签在截至时间为t1时的各自的话题数N1
    #统计各个标签在截至时间为t0时的各自的话题数N0
    for i in range(0, tag_total_number):
        max_value = total_t2_list[i]
        choosen_value_t1 = random.randint(1,max_value)
        #total_t1_list.append(choosen_value_t1)
        choosen_value_t0 = random.randint(1,choosen_value_t1)
        #total_t0_list.append(choosen_value_t0)
        
        #计算Δ2=N2-N1/t2-t1
        delta2 = (max_value-choosen_value_t1)/DELTA_T
        #delta2_list.append(delta2)
        #计算Δ1=N1-N0/t1-t0
        delta1 = (choosen_value_t1-choosen_value_t0)/DELTA_T
        #delta1_list.append(delta1)
        if delta1 != 0:
            infectivity.append(delta2/delta1)#计算Ini=Δ2/Δ1
        else:
            infectivity.append(delta2)
    
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/infectivity.txt','w')
    for item in infectivity:
        print >> f, '%s' % item
    f.close()