from model import *
import os
low=('neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
     'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis',
     'tonsillitis', 'periodontitis')
high=('malignant lymphoma', 'HIV', 'leprosy', 'glioma', 'tuberculosis')
data=[] #数据元组
attributes = ('age','sex','weight','marital-status','workclass','disease')  #数据的所有属性值
QID = (0,1,2,3,4,5) #要进行匿名的属性值
QID_Th=(0.1 ,0.1 ,0.1,0.1 ,0.01)#阈值：每个属性的信息损失量能承受的最大值
Anonymity_data=[]
Trees = GetTrees()   #保存属性的树


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
    for i in range(length):#对于每条数据
        for num in QID:#对于每个属性
            if num==QID[5]:#为第五个疾病敏感属性，则根据级别匿名
                tmp_attribute=data[i][num]
                if data[i][num] not in low:#如果是低级别属性则不匿名
                    tmp_attribute=climb(Trees[num],data[i][num])#中级属性匿名一次
                    if data[i][num] in high:
                        tmp_attribute=climb(Trees[num],data[i][num])#高级属性匿名两次
                data[i][num] = tmp_attribute  # 更新匿名属性
            else:#其余根据阈值匿名
                Loss = GetLoss(Trees[num], data[i][num])#计算损失率
                PayOff = GetPayOff(Trees[num], data[i][num])#计算收益
                while Loss < QID_Th[num]:#损失率小于阈值则继续匿名
                    tmp_attribute = climb(Trees[num], data[i][num])
                    PayOff = GetPayOff(Trees[num], tmp_attribute)  # 根据属性匿名程度不断更新PayOff
                    data[i][num] = tmp_attribute  # 更新匿名属性
                    Loss = GetLoss(Trees[num], data[i][num])  # 根据匿名程度更新属性
                PayOffs = PayOff * PayOffs  # 更新PayOff
                data[i].append(PayOffs)#加入到data中
                PayOffs = 1
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
    Anonymity_data=Anonymity()
    Save2File(Anonymity_data)
