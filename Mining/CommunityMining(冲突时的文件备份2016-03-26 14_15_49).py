#coding=utf-8
'''
Created on 2016年3月26日

@author: makao
通过标签传播方式挖掘用户的兴趣社区
'''

if __name__ == '__main__':
    #读取rough core
    cores_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/rough_core.txt'):
        cores_list.append(line.strip().strip('[]').split(', '))
    #计算rough core内点的兴趣标签和度
    
    for item in cores_list:
        print item[0]