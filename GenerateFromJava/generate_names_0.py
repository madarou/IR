#coding=utf-8
'''
Created on 2016年4月9日

@author: makao
从origin_name.txt中提取用户名到extracted_names.txt中
并且按gephi的形式写到user_node.csv中
'''

if __name__ == '__main__':
    name_number = 1538
    names_set = set()
    for line in open('/Users/makao/Yun/Workspace/lab/data/java_relation/origin_name.txt'):
        name = line.strip().split()[0]
        names_set.add(name)
    
    f = open('/Users/makao/Yun/Workspace/lab/data/java_relation/extracted_names.txt','w')
    ff = open('/Users/makao/Yun/Workspace/lab/data/java_relation/user_node.csv','w')
    print >> ff, 'Id,Label'
    counter = 0
    for item in names_set:
        if counter == name_number:
            break
        print >> f, item
        counter = counter + 1
        print >> ff, '%s,%s' % (counter,item)
    f.close()
    ff.close()
    
    
    