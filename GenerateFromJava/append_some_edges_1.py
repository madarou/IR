#coding=utf-8
import random
'''
Created on 2016年4月9日

@author: makao
在user_edges.csv中增加边

先复制'user_edges副本.txt'再运行程序向里面追加
'''
if __name__ == '__main__':
    existed_edge_dict = {}#以边的结点{from#to:1}的形式记录哪些点之间有边存在了
    nodes_indegree = {}#{nodes_number:degree}记各个点的入度
    nodes_outdegree = {}#记各个点的出度
    nodes_in_node = {}#{目标结点：指向目标结点的点的list}
    edge_number = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_edges.csv'):
        if line == 'Source,Target,Type,Id,Label,Weight':
            continue
        comma_list = line.strip().split(',')
        from_node = comma_list[0]
        to_node = comma_list[1]
        existed_edge_dict[from_node+'#'+to_node]=1
        if to_node in nodes_in_node.keys():
            nodes_in_node[to_node].append(from_node)
        else:
            nodes_in_node[to_node]=[from_node]
            
        if to_node in nodes_indegree.keys():
            nodes_indegree[to_node]=nodes_indegree[to_node]+1
        else:
            nodes_indegree[to_node]=0
        if from_node in nodes_outdegree.keys():
            nodes_outdegree[from_node]=nodes_outdegree[from_node]+1
        else:
            nodes_outdegree[from_node]=0
            
        edge_number = edge_number + 1
    node_counter = 0
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_nodes.csv'):
        if line == 'Id,Label':
            continue
        node_counter = node_counter + 1
    
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_edges.csv','a')
    #遍历所有边
    for (key,value) in existed_edge_dict.items():
        #如果该边的源点只有一个出度
        from_node = key.split('#')[0]
        to_node = key.split('#')[1]
        if nodes_outdegree[from_node] == 1:
            #再找出另外一个指向to_node的，且也是出度为1的点
            for another_node in nodes_in_node[to_node]:#遍历的是list
                if from_node == another_node:
                    continue
                if nodes_outdegree[another_node] == 1 and ((from_node+'#'+another_node) not in existed_edge_dict.keys()):#保证两点之间还没边
                    #一半的几率让from_node指向another_node 2,6,Directed,14,,1.0
                    if random.randint(0,10)%3==0:
                        continue

                    print >> f, '%s,%s,Directed,%s,,1.0' % (from_node,another_node,str(edge_number+1000))
                    edge_number = edge_number + 1
            
            
    
        