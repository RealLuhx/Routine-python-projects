import xlrd
import time
import random

def readxls(path):
    x1 = xlrd.open_workbook(path)
    sheet1 = x1.sheets()[0]
    f_values = sheet1.col_values(5)
    h_values = sheet1.col_values(7)
    j_values = sheet1.col_values(9)
    # a = 0
    # for i in j_values:
    #     if i == 1.0:
    #         a += 1
    # print(a)
    return f_values, h_values, j_values

def separate(f_values, h_values, j_values):
    save = []
    for i in range(len(f_values)):
        each = []
        each.append(f_values[i])
        each.append(h_values[i])
        each.append(j_values[i])
        save.append(each)
    # print(save[12])
    lit = []
    all_data = []
    lit.append(str(save[0][1]).replace(' ', '_'))
    lit.append(save[0][2])
    for i in range(1, len(save)):
        if save[i][0] == save[i-1][0]:
            lit.append(str(save[i][1]).replace(' ', '_'))
            lit.append(save[i][2])
        if save[i][0] != save[i-1][0]:
            # print(lit)
            all_data.append(lit)
            lit = []
            lit.append(str(save[i][1]).replace(' ', '_'))
            lit.append(save[i][2])
    print(len(all_data))
    return all_data

def add_tag(all_data):
    # for each in all_data:
    #     for i in each:
    #         if i == '1.0':
    #             print(each)
    tag_data = []
    for each in all_data:
        hh = []
        for i in range(0,len(each),2):
            if each[i+1] == 1.0:
                # print('fffffffffffffffffffffff')
                hh.append(each[i])
                hh.append('BE')
            else:
                hh.append(each[i])
                hh.append('S')
        tag_data.append(hh)
    return tag_data

def save(tag_data,name):
    gg = []
    with open(r'D:\learnPython\第十五次任务\完整语句比较20171029\整句识别%s.txt'%name,'w',encoding='utf8')as f:
        for each in tag_data:
            for i in range(0,len(each),2):
                f.write(str(each[i])+'\t'+str(each[i+1])+'\n')
                gg.append(str(each[i])+'\t'+str(each[i+1]))

            f.write('\n')


def main():
    print('正在工作，请耐心等候.............')
    begin = time.clock()
    path = r'D:\Pythontask\第十二次任务20170730\比较句\jasist.xlsx'
    f_values, h_values, j_values = readxls(path)
    all_data = separate(f_values, h_values, j_values)
    tag_data = add_tag(all_data)
    random.shuffle(tag_data)
    a = int(0.9*len(tag_data))
    train_data = tag_data[:a]
    test_data = tag_data[a+1:]
    train = 'train'
    test = 'test'
    save(train_data,train)
    save(test_data, test)
    print('结束')
    end = time.clock()
    print('用时为：'+str(end-begin))

if __name__ == '__main__':
    main()