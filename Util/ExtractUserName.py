#coding=utf-8
'''
Created on 2016年3月9日

@author: makao
提取用户名字，存到username.txt中
'''

if __name__ == '__main__':
    for line in open('/Users/makao/Yun/Workspace/lab/data/user-interest.txt'):
        print line.split('|')[0].strip()