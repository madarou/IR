#coding=utf-8
from model.User_Relation import User_Relation
'''
Created on 2016年3月25日

@author: makao
标签传播前，找初始传播的core

存入rough_core.txt
[用户编号1 用户编号2 ...]
[用户编号4 用户编号5 ...]
能组成一个core的就是一个列表
'''

def commonNeighbors(user_relation_list,user_i,user_j):
    '''
    找user_i和user_j的共同邻居
    返回的是string行的user编号组成的list
    '''
    useri = user_relation_list[user_i]
    userj = user_relation_list[user_j]
    i_neighbors = useri.follower
    j_neighbors = userj.follower
    return list(set(i_neighbors).intersection(set(j_neighbors)))
    
if __name__ == '__main__':
    user_degree_list=[]#存各个用户被关注的度，即出度
    user_relation_list=[]
    total_user_num = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/num_user_relation.txt'):
        user_number = line.split('|')[0].strip()
        follower_list = line.split('|')[1].strip().split()
        user = User_Relation(user_number)
        user.setFollower(follower_list)
        user_relation_list.append(user)
        user_degree_list.append((int(user_number),len(follower_list)))
        total_user_num = total_user_num + 1
    
    has_accessed_list = [0]*total_user_num#标记第i号点已经在core中了值为1，否则为0
    
    user_degree_sorted_list=user_degree_list[:]    
    #按出度大小排序
    user_degree_sorted_list.sort(lambda y,x:cmp(x[1],y[1]))
    
    cores_list = []#最后要找的core
    for item in user_degree_sorted_list:
        user_number = item[0]
        user_degree = item[1]
        current_core=[]#当前要寻找的core
        if user_degree >= 3 and has_accessed_list[user_number]==0:
            user_follower_list = user_relation_list[user_number].follower#用户肯定有follower
            #找到当前user的邻居中有最大degree的点
            max_follower_degree = -1
            max_follower_number = -1#表示没找到
            for item in user_follower_list:
                current_follower_degree = user_degree_list[int(item)][1]
                if max_follower_degree < current_follower_degree and has_accessed_list[int(item)]==0:
                    max_follower_degree = current_follower_degree
                    max_follower_number = int(item)
            if max_follower_number != -1:#如果给user找到这样的邻居
                current_core.append(user_number)
                current_core.append(max_follower_number)
                commonNeighbors_list = commonNeighbors(user_relation_list,user_number,max_follower_number)
                if len(commonNeighbors_list) > 0:
                    commonNeighbors_degree_list = []#(user编号，user度)
                    for commonNeighbor in commonNeighbors_list:
                        neighbor_degree = user_degree_list[int(commonNeighbor)][1]
                        commonNeighbors_degree_list.append((commonNeighbor,neighbor_degree))
                    #对commonNeighbors_degree_list排序,按度由小到大
                    commonNeighbors_degree_list.sort(lambda x,y:cmp(x[1],y[1]))
                    to_remove_from_commonNeighbors=set()#记录要从commonNeighbor中删掉的(user编号,user度)
                    while len(commonNeighbors_degree_list) > 0:
                        #for h in commonNeighbors_degree_list:#这里可能会出现遍历列表时删除列表元素的问题
                        h = commonNeighbors_degree_list[0]
                        current_core.append(int(h[0]))#add h to core
                        h_neighbors = user_relation_list[int(h[0])].follower
                        for n in commonNeighbors_degree_list:
                            if str(n[0]) not in h_neighbors:
                                #commonNeighbors_degree_list.remove(n)#delete vertices not in N(h) from commonNeighbors
                                to_remove_from_commonNeighbors.add(n)
                        #commonNeighbors_degree_list.remove(h)#delete h from commonNeighbors
                        to_remove_from_commonNeighbors.add(h)
                        #现在才开始删除commonNeighbors_degree_list中的元素
                        for i in to_remove_from_commonNeighbors:
                        	if i in commonNeighbors_degree_list:
                        		commonNeighbors_degree_list.remove(i)        
        if len(current_core)>=3:
            cores_list.append(current_core)
        has_accessed_list[user_number]=1
    for item in cores_list:
        print item