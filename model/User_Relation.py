#coding=utf-8
'''
Created on 2016年3月10日

@author: makao
'''

class User_Relation(object):
    '''
    aapr | Marco Mike John Lily
    '''

    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
        self.follower=[]
        
    def setFollower(self,follower):
        self.follower=follower[:]
        
    def formatFollower(self):
        s = ''
        for item in self.follower:
            s += '%s ' % item
        return s
    
    def __str__(self):
        return '%s | %s' % (self.name,self.formatFollower())