#coding=utf-8
from __future__ import division
import string
'''
Created on 2016年3月22日

@author: makao
计算用户与各个标签的fitness
即用户所有标签中，与目标标签fitness最大的值，作为用户与该标签的fitness值

结果为user_fitness二维矩阵
user_fitness[i][j]表示用户i接受标签j的概率
'''

def isnumeric(s):
    '''returns True if string s is numeric'''
    return all(c in "0123456789.+-" for c in s)

def getMax(target_list):
    max_num = 0
    row_number = 0
    row_counter = 0
    for item in target_list:
        if max_num < string.atof(item):
            max_num = string.atof(item)
            row_number = row_counter
        row_counter = row_counter + 1
    return (max_num,row_number)

if __name__ == '__main__':
    #先从tag_fitness中读出fitness矩阵
    fitness=[]
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag_fitness.txt'):
        row = line.rstrip(']').lstrip('[').strip().split(',')
        new_row = []
        for item in row:
            new_row.append(item.strip(']').strip())
        fitness.append(new_row)
 
    user_fitness = []
    interest_num = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_intr_user.txt'):
        if line.strip() == '兴趣-用户':
            continue
        interest_num = interest_num+1
        
    user_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_user_intr.txt'):
        if line.strip() == '用户-兴趣':
            continue
        tmp=[]
        for i in range(0,interest_num):
            tmp.append(0)
        user_fitness.append(tmp)
        
        user_number = line.split('|')[0].strip()
        interests = line.split('|')[1].split()
        inter_counter = 0
        user_numeric_tag_fitness=[]
        keep_tag_number_list=[]
        for item in interests:
            tag = item.split('_')[0].strip()
            weight = item.split('_')[1].strip()
            #如果这个tag是数字，即兴趣标签而非其他类型标签
            if isnumeric(tag):
                #在fitness表中找出这一tag行所有列的概率值
                user_numeric_tag_fitness.append(fitness[int(tag)])
                keep_tag_number_list.append(int(tag))
            
        #遍历完interests后，得到几行数组user_numeric_tag_fitness，对比数组中相同列，选出最大的值作为user_fitness[user][列]的值
        #为了方便按列值取值来比较，先将user_numeric_tag_fitness转置
        user_numeric_tag_fitness_T = zip(*user_numeric_tag_fitness)
        for item in user_numeric_tag_fitness_T:
            max_tuple = getMax(item)
            max_num = max_tuple[0]
            max_row = max_tuple[1]
            user_fitness[user_counter][keep_tag_number_list[max_row]]=max_num
        user_counter = user_counter + 1
        
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_tag_fitness.txt','w')
    for item in user_fitness:
        print >> f, '%s' % item
    f.close()