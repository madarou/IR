#coding=utf-8
from __future__ import division
import string
import math

'''
Created on 2016年3月19日

@author: makao
计算各个点基于目前关注关系的各自的影响力Ii
使用趋同化方法将ti和ci相加
'''

if __name__ == '__main__':
    user_counter = 0
    user_list = []
    Ci_list=[]
    ci_square_sum = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/ci.txt'):
        ci = string.atof(line.strip())
        ci_square_sum = ci*ci + ci_square_sum
        user_list.append([ci])
        user_counter = user_counter + 1
    Ti_list=[]
    ti_square_sum = 0
    line_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/ti.txt'):
        ti = string.atof(line.strip())
        ti_square_sum = ti*ti + ti_square_sum
        user_list[line_counter].append(ti)
        line_counter = line_counter + 1
        
    #for item in user_list:
    #    print '[%s %s]' % (item[0],item[1])
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/Ii.txt','w')
    ci_sqrt_sum = math.sqrt(ci_square_sum)
    ti_sqrt_sum = math.sqrt(ti_square_sum)
    for i in range(0,user_counter):
        ci = user_list[i][0]
        ti = user_list[i][1]
        Ii = ci/ci_sqrt_sum + ti/ti_sqrt_sum
        print >> f, '%s' % Ii
    f.close()