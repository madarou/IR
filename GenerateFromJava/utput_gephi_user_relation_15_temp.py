#coding=utf-8
from model.User_Relation import User_Relation
from model.User_Intr import User_Intr
import string
'''
Created on 2016年4月2日

@author: makao
输出用户关注关系图，是gephi读取的文件形式，分点文件nodes.csv和边文件edges.csv
nodes.csv格式：
Id,Label,colourList
1,java.applet.AppletContext,"-100000,-10000,-1000,100000,1000000"
2,java.applet.Applet,"-100000,-10000,-1000,100000,1000000"
...
colourList的值表示点所属的社区的颜色在gephi中对应的值

edges.csv格式:
Source,Target,Type,Id,Label,Weight
1,2,Directed,0,,1.0
1,3,Directed,1,,1.0
...
把颜色步长压缩
'''

if __name__ == '__main__':
#     user_relation_list = []
#     for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_relation.txt'):
#         if line.strip() == '用户-关系':
#             continue
#         uname = line.split('|')[0].strip()
#         user = User_Relation(uname)
#         follower = []
#         if len(line.split('|')) > 1:
#             follower = line.split('|')[1].split()
#         user.setFollower(follower)
#         user_relation_list.append(user)
    #读取Sxy，用户相似度矩阵，注意值是string型，用的时候要float化
#     user_similarity = []
#     for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_similarity.txt'):
#         user_i_list = line.strip().lstrip('[').rstrip(']').split(', ')
#         user_similarity.append(user_i_list)
    
    #读用户最后所属的用户社区,final_user_intr.txt
    user_final_intr_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/final_user_intr.txt'):
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
    
    '''
    -------以下为写入num类型，不写用户名字，写用户编号---------
    '''
    
    num_user_relation_list = []
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/num_user_relation.txt'):
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
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_similarity.txt'):
        user_i_list = line.strip().lstrip('[').rstrip(']').split(', ')
        user_similarity.append(user_i_list)
    
    #将标签设置颜色对应编号
    tag_color_number_list = []
    color_base_value = -1000L
    color_step_value = 100L
    color_current_value = color_base_value
    ftagcolor = open('/Users/makao/Yun/Workspace/lab/data/java_relation/visual/tag-interest-color_temp.txt','w')
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/tag-interest.txt'):
    #for i in range(0, 234):
        tag_number = line.strip().split()[0]
        tag_name = line.strip().split()[1]
        tag_color_value = color_current_value + color_step_value
        color_current_value = tag_color_value
        tag_color_number_list.append(tag_color_value)
        print >> ftagcolor, '%s %s %d' % (tag_number,tag_name,tag_color_value)
    ftagcolor.close()
    #写点到文件
    ff = open('/Users/makao/Yun/Workspace/lab/data/java_relation/visual/num_nodes_gephi_temp.csv','w')
    print >> ff, 'Id,Label,colourList'

    for item in user_final_intr_list:
        user_id = item.name.split('#')[1]
        user_label = user_id#先用用户编号代替，不显示用户名
        user_interests_dict = item.interests
        user_interests_tags_list = user_interests_dict.keys()
        tag_color_str = ''
        for i in range(0,len(user_interests_tags_list)):
            if i == len(user_interests_tags_list)-1:
                tag_color_str = tag_color_str + str(tag_color_number_list[int(user_interests_tags_list[i])])
            else:
                tag_color_str = tag_color_str + str(tag_color_number_list[int(user_interests_tags_list[i])]) + ','
        print >> ff, '%d,%d,"%s"' % (string.atoi(user_id, 10)+1,string.atoi(user_id, 10)+1,tag_color_str)
    
    ff.close()
    
    #写边到文件
    fff = open('/Users/makao/Yun/Workspace/lab/data/java_relation/visual/num_edges_gephi_temp.csv','w')
    print >> fff, 'Source,Target,Type,Id,Label,Weight'
    
    edge_id_counter = 0
    for item in num_user_relation_list:
        target_id = item.name
        follower_list = item.follower 
        for flwr in follower_list:
            print >> fff, '%s,%s,Directed,%s,,%s' % (flwr,target_id,str(edge_id_counter),user_similarity[int(target_id)-1][int(flwr)-1])
            edge_id_counter = edge_id_counter + 1
    fff.close()