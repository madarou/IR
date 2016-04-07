#coding=utf-8
from model.User_Relation import User_Relation
from model.User_Intr import User_Intr
'''
Created on 2016年4月2日

@author: makao
输出用户关注关系图，是netdraw的文件形式
*Node data 
"ID" interest01
...
*Node properties
ID
...
*Tie data
FROM TO similarity
'''

if __name__ == '__main__':
    user_relation_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/user_relation.txt'):
        if line.strip() == '用户-关系':
            continue
        uname = line.split('|')[0].strip()
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        user_relation_list.append(user)
    #读取Sxy，用户相似度矩阵，注意值是string型，用的时候要float化
    user_similarity = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/user_similarity.txt'):
        user_i_list = line.strip().lstrip('[').rstrip(']').split(', ')
        user_similarity.append(user_i_list)
    
    #读用户最后所属的用户社区,final_user_intr.txt
    user_final_intr_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/final_user_intr.txt'):
        uname = line.split('|')[0].strip()
        user = User_Intr(uname)
        interests = line.split('|')[1].strip().split()
        interests_dict = {}
        for item in interests:
            tag = item.split('_')[0]
            weight = item.split('_')[1]
            interests_dict[tag] = weight
        user.setInterest(interests_dict)
        user_final_intr_list.append(user)
    
    f = open('/Users/makao/Yun/Workspace/lab/data/visual/user_relation.txt','w')
    print >> f, '*Node data'
    print >> f, 'ID'
    for item in user_relation_list:
        print >>  f, item.name
        
    print >> f, '*Node properties'
    print >> f, 'ID'
    for item in user_relation_list:
        print >> f, item.name
        
    print >> f, '*Tie data'
    print >> f, 'FROM TO similarity'
    for item in user_relation_list:
        follower_list = item.follower
        for flwr in follower_list:
            print >> f, "%s %s %s" % (item.name, flwr, 'no')
    f.close()
    
    '''
    -------以下为写入num类型，不写用户名字，写用户编号---------
    '''
    
    num_user_relation_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        if line.strip() == '用户-关系':
            continue
        uname = line.split('|')[0].strip()
        user = User_Relation(uname)
        follower = []
        if len(line.split('|')) > 1:
            follower = line.split('|')[1].split()
        user.setFollower(follower)
        num_user_relation_list.append(user)
    #读取Sxy，用户相似度矩阵，注意值是string型，用的时候要float化
    user_similarity = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/user_similarity.txt'):
        user_i_list = line.strip().lstrip('[').rstrip(']').split(', ')
        user_similarity.append(user_i_list)
    
    ff = open('/Users/makao/Yun/Workspace/lab/data/visual/num_user_relation.txt','w')
    print >> ff, '*Node data'
    print >> ff, 'ID interest01 interest02 interest03'
    for item in num_user_relation_list:
        final_user_intr = user_final_intr_list[int(item.name)]
        final_user_intr_interests_dict = final_user_intr.interests
        intr01 = 'none'
        intr02 = 'none'
        intr03 = 'none'
        if len(final_user_intr_interests_dict.keys()) > 0:
            intr01 = final_user_intr_interests_dict.keys()[0]
        if len(final_user_intr_interests_dict.keys()) > 1:
            intr02 = final_user_intr_interests_dict.keys()[1]
        if len(final_user_intr_interests_dict.keys()) > 2:
            intr03 = final_user_intr_interests_dict.keys()[2]
        print >> ff, "%s %s %s %s" % (item.name, intr01, intr02, intr03)
    
        
    print >> ff, '*Node properties'
    print >> ff, 'ID'
    for item in num_user_relation_list:
        print >>  ff, item.name
        
    print >> ff, '*Tie data'
    print >> ff, 'FROM TO similarity'
    for item in num_user_relation_list:
        follower_list = item.follower
        for flwr in follower_list:
            print >> ff, "%s %s %s" % (item.name, flwr, (user_similarity[int(item.name)][int(flwr)]!='0' and user_similarity[int(item.name)][int(flwr)]) or 'no')
    ff.close()