#coding=utf-8
user_similarity = []
for line in open('/Users/makao/Yun/Workspace/lab/data/user_similarity.txt'):
        user_i_list = line.strip().lstrip('[').rstrip(']').split(', ')
        user_similarity.append(user_i_list)
for item in user_similarity:
    print item