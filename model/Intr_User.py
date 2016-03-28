#coding=utf-8
'''
Created on 2016年3月22日

@author: makao
'''

class Intr_User(object):
    '''
    兴趣 | [用户1，用户2，...]
    '''


    def __init__(self,name):
        '''
        Constructor
        '''
        self.name = name
        self.owner = [] 
        
    def setOwner(self,owner):
        self.owner=owner[:]
        
    def appendOwner(self,user):
        self.owner.append(user)
        
    def formatOwner(self):
        s = ''
        for item in self.owner:
            s += '%s ' % item
        return s
    
    def __str__(self):
        return '%s | %s' % (self.name,self.formatOwner())