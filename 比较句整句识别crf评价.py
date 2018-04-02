# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:08:37 2017

@author: AloneNotLongly
"""
import time


def PRF(name):
    path2 = r'D:\learnPython\第十五次任务\完整语句比较20171029\output_lhx_20171029.txt'
    with open(path2, 'r', encoding='utf8')as f:
        linep = f.readlines()
    # print(linep)
    num = 0
    countname1 = 0
    countname2 = 0

    for i in linep:
        i = str(i).split('\t')
        if len(i) == 3:
            i[2] = i[2].replace('\n', '')
            if i[1] == name:
                countname1 += 1
            if i[2] == name:
                countname2 += 1
            if i[1] == name and i[2] == name:
                num += 1
                # print(countname1)
    P = (num / countname2)  # 正确率
    R = (num / countname1)  # 召回率
    F = (2 * P * R) / (P + R)
    with open(r'D:\learnPython\第十五次任务\完整语句比较20171029\%s的PRF值.txt' % name, 'w', encoding='utf8')as f:
        f.write('正确率（P）' + '\t' + '%.2f%%' % (P * 100) + '\n')
        f.write('召回率（R）' + '\t' + '%.2f%%' % (R * 100) + '\n')  # print("分类正确率是：%.2f%%"  %(rate*100))
        f.write('F值（F）' + '\t' + '%.2f%%' % (F * 100))


def main():
    print('开始............')
    begin = time.clock()
    all_ = ['BE']
    for name in all_:
        PRF(name)
    # PRF('BE')
    end = time.clock()
    print('结束')
    print('用时为：' + str(end - begin))


if __name__ == '__main__':
    main()







