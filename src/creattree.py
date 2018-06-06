#coding:utf8
import os

'''
def creattree(root):
    in_filename = os.path.dirname(os.path.abspath('__file__'))
    node = treenode.Treenode(root)#创建树的根节点
    infile = open('F:\\boyi\\data\\cluster_Anv','r')
    lines = infile.readlines()#读取多行
    i=0
    j=0
    '''
'''
    for line in lines:
        c_node = treenode.Treenode(line[i])
        node.chiled.append(c_node)
    '''
'''
    leave = len(lines[0].split(';'))#得到层数
    while True:
        for line in lines:
            leaves = len(line.split(';'))
                c_node = treenode.Treenode(line[i])
                node.chiled.append(c_node)


def add(L,data):#L表示这个节点的父亲节点的孩子列表，node表示该节点
    node =  treenode.Treenode(data)
    L.apend(node)
def bianli(L,data):
    if(L.mes==data):
        return  data
    bianli(L.leftchild,data)
    bianli(L.rightchild)
    return None

'''
'''
def creat_tree(filename):
    in_file = open(filename)
    lines = in_file.readlines()
    for line in lines:

        pass

if __name__=='__main__':
'''