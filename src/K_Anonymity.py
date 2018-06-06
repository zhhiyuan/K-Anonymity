from time import sleep

from model import *
import os
data=[] #数据元组
attributes = ('job', 'sex', 'age', 'disease')  #数据的所有属性值
QID = (0,1,2) #要进行匿名的属性值
Anonymity_data=[]
Trees = GetTrees()   #保存属性的树
Th = 0.4   #阈值：单个属性的信息损失量


def Init():
    '''
    初始化，生成树,设置阈值，初始化要匿名的属性值
    :return: 所有数据元祖，阈值，所有属性的树
    '''

    #第一步：读取数据，生成元组
    path = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹
    data_path = path + '\\data\\data.txt'
    data_file = open(data_path, 'r')
    lines = data_file.readlines()
    for line in lines:
        i = line[:-1].split(',')
        data.append(i)



def Anonymity():
    Init()
    PayOffs=1
    Loss = 0
    length=len(data)
    for i in range(length):
        for num in QID:
            Loss = GetLoss(Trees[num],data[i][num])
            PayOff= GetPayOff(Trees[num],data[i][num])
            while Loss<Th:
                tmp_attribute=climb(Trees[num],data[i][num])
                PayOff = GetPayOff(Trees[num],tmp_attribute)    #根据属性匿名程度不断更新PayOff
                data[i][num]=tmp_attribute  #更新匿名属性
                Loss=GetLoss(Trees[num],data[i][num])   #根据匿名程度更新属性
            PayOffs=PayOff*PayOffs  #更新PayOff
            data[i].append(PayOffs)
            PayOffs=1
    tmp_data=data[:]
    while tmp_data: #执行到原始数据库中没有数据为止
        EQ=tmp_data[0]
        EQ.append(1)    #计数
        tmp_data.remove(tmp_data[0])
        Anonymity_data.append(EQ)
        for i in range(len(tmp_data)):
            each=tmp_data[i]
            if Equal(EQ[:-1], each, QID):
                Anonymity_data.append(each)
                EQ[-1] = EQ[-1] + 1  # 更新K值
        tmp_data=Remove(tmp_data,EQ[:-1],QID)

    return Anonymity_data

if __name__ == '__main__':
    '''
      list=[1,2,3,4,4,2]
      list.remove(4)
      print(list)'''

    Anonymity_data=Anonymity()
    Save2File(Anonymity_data)





