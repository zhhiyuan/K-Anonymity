import random
Disease=['neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','neck injury', 'fever', 'cough', 'rhinitis', 'chicken pox', 'diarrhea', 'myopia', 'crus fracture',
         'headache', 'chilblain', 'acute pharyngitis', 'arthritis', 'drug allergy', 'osteoporosis', 'tonsillitis',
         'periodontitis','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','ankylosing spondylitis', 'primary immunodeficiency disease', 'burns', 'fibromyalgia',
         'epidemic b encephalitis', 'congenital ear deformity', 'diabetes','malignant lymphoma', 'HIV', 'leprosy', 'glioma', 'tuberculosis']
Sex=['male','female']
Married=['marital-status','alone', 'Married','alone','Divorced','Never-married','Separated','Widowed',
         'Married-civ-spouse','Married-AF-spouse','Married-spouse-absent']
Job=['workclass','gov','Private','Self-emp-not-inc','Self-emp-inc','Local-gov','Federal-gov']
#属性为Age,Sex,Weight,Married,Job,Disease

def CreatData(max):
    '''
    制造数据
    :param max: max为要制造的数据数量
    :return:
    '''
    n,b=0,1
    file=open('data.txt','w')
    while n<max:
        yield b
        line=[]
        line.append(random.randint(18,65))#年龄
        line.append(Sex[random.randint(0,1)])#性别
        line.append(int(random.randint(90,300)/5)*5)#体重
        line.append(Married[random.randint(0,len(Married)-1)])#结婚情况
        line.append(Job[random.randint(0,len(Job)-1)])#职业
        line.append(Disease[random.randint(0,len(Disease)-1)])#疾病
        str = ''
        for each in line:
            each = '{},'.format(each)
            str = str + each
        str = str[:-1]
        file.write(str+'\n')
        n=n+1
    file.close()
    return 'done'

if __name__ == '__main__':
    g=CreatData(10000)
    while True:
        try:
            x=next(g)
        except StopAsyncIteration as e:
            print(e.value)
            break