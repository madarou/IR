#coding=utf-8
import random
from model.User_Relation import User_Relation
'''
Created on 2016年4月9日

@author: makao
根据user_nodes_csv和user_edges.csv中的边情况构造
0 | 490 730 337 567 40 35 
和
Forget | 刘树岱 名字长才impressed 丹宝拉 北京小丫丫 -Modana- -LittleSthToBuy 
分别输出到num_user_relation.txt
和user_relation.txt中
'''
if __name__ == '__main__':
    user_relation_dict = {}#{用户编号：User_Relation对象}
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_edges.csv'):
        if line == 'Source,Target,Type,Id,Label,Weight':
            continue
        comma_list = line.strip().split(',')
        from_node = comma_list[0]
        to_node = comma_list[1]
        if to_node in user_relation_dict.keys():
            user_relation = user_relation_dict[to_node]
            user_relation.follower.append(from_node)
        else:
            user_relation = User_Relation(to_node)
            user_relation.setFollower([from_node])
            user_relation_dict[to_node]=user_relation
            
    #获取总的点数
    user_number = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_nodes.csv'):
        if line.strip()=='Id,Label':
            continue
        user_number = user_number + 1
    
    print user_number
    #写到num_user_relation.txt中
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_user_relation.txt','w')
    for i in range(0, user_number):
        if str(i) in user_relation_dict.keys():
            user_relation = user_relation_dict[str(i)]
            print >> f, '%s' % user_relation
        else:
            print >> f, '%s |' % str(i)
    f.close()    