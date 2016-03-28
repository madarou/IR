#coding=utf-8
'''
Created on 2016年3月9日

@author: makao
'''
import copy

class User_Intr(object):
    '''
    aapr | 视频_14 音乐_22 幽默_28 生活_4 美剧_9
    '''

    def __init__(self,name):
        '''
        Constructor
        '''
        self.name=name
        self.interests={}
    
    def setInterest(self,intr_list):
        self.interests=copy.copy(intr_list)
    
    def getInterestTags(self):
        tags = []
        for key in self.interests:
            tags.append(key)
        return set(tags)
        
    def formatIntrests(self):
        s = ''
        for (key,value) in self.interests.items():
            s += '%s_%s ' % (key, value)
        return s
    
    def __str__(self):
        return '%s | %s' % (self.name,self.formatIntrests())
    
if __name__=="__main__":
    u1=User_Intr('makao')
    intr_list={'视频':14,'音乐':22,'幽默':28,'生活':4,'美剧':9}
    u1.setInterest(intr_list)
    print u1