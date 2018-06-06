import tree as a
import os

#保存到文件的函数
def Save2File(data):
    '''
    把数据集保存到文件
    :param data:
    :return:
    '''
    path = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹
    data_path = path + '\\data\\Anonymity.txt'
    data_file = open(data_path, 'w')
    str=''
    for each in data:
        str=str + '{}\n'.format(each)
    data_file.write(str)
    data_file.close()


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#生成树的函数
def GetTrees():
    '''
    获取根据属性生成所有树
    :return: 返回所有属性的树，顺序在'attribute.txt'里面
    '''
    attribute = []
    path = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
    path1 = path + "\data//attribute"
    infile = open(path1, 'r')
    attribute_file = infile.readline()[:-1]  # 读取一行
    attribute = (attribute_file.split(','))
    trees = []
    for i in range(len(attribute)):
        path2 = path + "\data//attribute_" + attribute[i]
        tree = a.Tree1()
        tree1 = tree.createTree(path2)
        trees.append(tree1)
    return trees


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#获取PayOff的函数
def GetPayOff(tree,attribute):
    '''
    获取非数字型的PayOff
    :param tree: 属性的树
    :param attribute: 属性值
    :return: PayOff
    '''
    node = tree.get_node(attribute)
    level_all = tree.depth() + 1   #树的总层数
    level_site = tree.depth() + 1 - tree.depth(node)   #当前节点所在层数
    return float(level_site/level_all)   #返回当前节点的payoff

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#判断两个列表是否相等
def Equal(a,b,QID):
    '''
    判断两个列表对应的属性是否相等
    :param a: 列表a
    :param b: 列表b
    :param QID: 属性位置
    :return: 对应属性相同，返回True,不相同返回False
    '''
    for i in QID:
        if a[i]!=b[i]:
            return False
    if a[-1] ==b[-1] and a[-2]==b[-2]:
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
'''
下面一个函数属性网上匿名的函数
'''
def climb(tree,attribute):
    '''
    属性进一步根据树匿名
    :param tree: 属性的树
    :param attribute: 属性值
    :return: 进一步匿名后的结果
    '''
    node = tree.get_node(attribute)
    return (tree.parent(attribute).tag)   #返回父节点



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
'''
以下四个函数是获取损失率的函数
'''
def GetLoss(tree,attribute):
    '''
    根据是否是数值型的树，返回损失值
    :param tree: 属性的树
    :param attribute: 属性值
    :return: 损失率
    '''
    if(IntTree(tree)==True):
        return GetNumLoss(tree,attribute)

    else:
        return GetCharLoss(tree,attribute)


def IntTree(tree):
    '''
    判断是否是数值型的树，是返回True，不是返回false
    :param tree: 属性的树
    :return: true或者false
    '''
    node = tree.nodes.keys()
    keys=[]
    for each in node:
        keys.append(each)
    if '-' in keys[0]:
        return True
    else:
        return False


def GetCharLoss(tree,str):
    '''
    获取属性地损失
    :param tree: 属性树
    :param str: 属性值
    :return: 损失
    '''
    Child_len = len(tree.children(str))  # 子节点的个数
    Child_all = Child_len
    if Child_len == 0:  # 还未泛化的最底层节点
        return 0

    node = tree.get_node(str)
    level_site = tree.depth(node)  # 获取当前节点的深度
    if (level_site == 0):  # 根节点的深度为0
        return 1

    parent = tree.parent(str).tag  # 返回父节点
    childrens = tree.children(parent)  # 获取父节点
    for i in range(len(childrens)):  # 获取下一层的所有子节点
        if childrens[i].tag != str:
            parent1 = childrens[i].tag
            Child_all = Child_all + len(tree.children(parent1))  # 依次累加
    return (Child_len / Child_all)   #返回非数值型的loss



def GetNumLoss(tree,age):
    '''
    获取数值型的PayOff
    :param tree: 属性地树
    :param age: 属性值
    :return: PayOff
    '''
    Numrange = []
    depth = tree.depth()   #树的深度
    node = tree.get_node(age)    #当前节点所在层数
    level_site = tree.depth(node)  # 获取当前节点的深度
    if (level_site == 0):  # 根节点的深度为0
        return 1

    if (level_site == depth):   #未泛化的最底层节点
        return 0

    child = age.split('-')
    Range = int(child[1]) - int(child[0])   #当前节点的范围
    parent = tree.parent(age).tag    #获取父节点
    Numrange = parent.split('-')
    Range1 = int(Numrange[1]) - int(Numrange[0])     #父节点的范围
    return(Range/Range1)    #返回数值型的loss

def Remove(data,EQ,QID ):
    remove_set=[]
    for i in range(len(data)):
        each = data[i]
        if Equal(EQ,each,QID):
            remove_set.append(i)
    remove_set.sort(reverse=True)
    for j in remove_set:
        data.remove(data[j])
    return data
