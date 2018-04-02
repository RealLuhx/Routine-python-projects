import xlrd
import time
import random
import os
from gensim.models import word2vec
import codecs
import pynlpir

def fun(file_path):
    fileArray = []
    for root, dirs, files in os.walk(file_path):
        for fn in files:
            eachpath = str(root + '/' + fn)
            fileArray.append(eachpath)
    return fileArray  # 返回的是列表

def get_data(path):
    x1 = xlrd.open_workbook(path)
    sheet = x1.sheets()[0]
    b_text = sheet.col_values(1)
    e_text = sheet.col_values(4)
    gg = []
    each_file = []
    each_data = []
    for i in range(len(e_text)):
        if e_text[i] == 'b':
            gg.append(b_text[i])
        if e_text[i] == 'm' or e_text[i] == 's' or e_text[i] == 's1' or e_text[i] == 's2' or e_text[i] == 's3' or e_text[i] == 's4' or e_text[i] == 's5':
            gg.append(b_text[i])
        if e_text[i] == 'e':
            gg.append(b_text[i])
            each_file.append(gg)
            gg = []

    return each_file

def add_tag(all_data):
    str_save = ''
    for each in all_data:
        for i in each:
            str_save += str(i)

    str_save = str_save.replace('〜', '~')
    str_save = str_save.replace('•', '')
    str_save = str_save.replace('»', '')
    str_save = str_save.replace('«', '')
    str_save = str_save.replace('£', '')
    str_save = str_save.replace('¥', '')
    str_save = str_save.replace('〇', '')
    str_save = str_save.replace('◦', '')
    str_save = str_save.replace('„', '')
    str_save = str_save.replace('^^', '')
    str_save = str_save.replace('©', '')
    str_save = str_save.replace('�', '')
    str_save = str_save.replace('€', '')
    str_save = str_save.replace('®', '')
    str_save = str_save.replace('㊉', '')
    str_save = str_save.replace('™', '')
    str_save = str_save.replace('►', '')
    str_save = str_save.replace('♦', '')
    str_save = str_save.replace('⑪', '')
    str_save = str_save.replace('⑫', '')
    str_save = str_save.replace('⑭', '')

    line = str_save.replace('  ', '')
    # line = line.replace('  ', '')
    # line = line.replace('【OAIS(OpenArchivalInformationSys-为长期保存数字信息','【OAIS】(OpenArchivalInformationSys-为长期保存数字信息')
    line = line.replace('。', '。￥')
    line = line.replace('\n', '')

    data_ = line.split('￥')


    with open(r'D:\Pythontask\第十次任务20170509\情报学报标注错误修正.txt','r',encoding='utf8')as f:
        new_word = f.readlines()
    # print(new_word[-2])
    # print(new_word[-1])
    # print('--------------------------------------')
    old_word = []
    for i in range(len(data_)):
        if list(data_[i]).count('【') != list(data_[i]).count('】'):
            old_word.append(data_[i])

    # for i in old_word:
    #     print(i)

    data = []
    for i in range(len(data_)):
        tag1 = 0
        for j in range(len(old_word)):
            if data_[i] == old_word[j]:
                data.append(new_word[j])
                tag1 = 1
            if tag1 == 0 and j == len(old_word)-1:
                data.append(data_[i])

    tag_data = []
    left_flg = 0

# 分词，加词性（需要修改路径、输出和构建词向量的部分）

    for gg in data:
        list_ = []
        list_1 = []
        pynlpir.open()
        try:
            list_1 = pynlpir.segment(gg, pos_names=None)  # p是一个二维列表
            for i in list_1:
                list_.append(i[0])
                list_.append(i[1])
            hh = []
            if '【' not in list_ and '】' not in list_:
                # print('11111111111111')
                for i in range(0, len(list_), 2):
                    hh.append(list_[i])
                    hh.append(list_[i+1])
                    hh.append('O')
                # all_data.append(hh)
                tag_data.append(hh)
                hh = []
            if '【' in list_:
                hh = []
                # print('222222222222222222')
                if list_[0] != '【':
                    hh.append(list_[0])
                    hh.append(list_[1])
                    hh.append('O')
                if list_[0] == '【':
                    left_flg = 1
                for i in range(2, len(list_) - 2, 2):

                    if list_[i] == '【':
                        left_flg = 1

                    if list_[i] == '】':
                        left_flg = 0

                    if list_[i - 2] != '【' and list_[i] != '【' and list_[i] != '】' and list_[i + 2] != '】' and left_flg == 0:
                        hh.append(list_[i])
                        hh.append(list_[i + 1])
                        hh.append('O')

                    if list_[i - 2] == '【' and list_[i + 2] != '】':  ##########
                        hh.append(list_[i])
                        hh.append(list_[i + 1])
                        hh.append('B-nt')
                    if list_[i - 2] != '【' and left_flg == 1 and list_[i + 2] != '】' and list_[i] != '【' and list_[i] != '】':
                        hh.append(list_[i])
                        hh.append(list_[i + 1])
                        hh.append('I-nt')
                    if list_[i - 2] != '【' and list_[i + 2] == '】':
                        hh.append(list_[i])
                        hh.append(list_[i + 1])
                        hh.append('E-nt')
                    if list_[i - 2] == '【' and list_[i + 2] == '】':
                        hh.append(list_[i])
                        hh.append(list_[i + 1])
                        hh.append('S-nt')
                if list_[-2] != '】':
                    hh.append(list_[-2])
                    hh.append(list_[-1])
                    hh.append('O')
                tag_data.append(hh)
                hh = []
            pynlpir.close()
        except:
            pass
    print(len(tag_data))
    return tag_data, data


# 把英文实体变成单词，中文实体还是单个字
'''
    con = ''
    for ff in data:
        list_ = []
        each = list(ff)
        if len(each) != 0:
            # print(each)
            for i in range(0, len(each) - 1):
                if each[i].encode('UTF-8').isalpha() == True and each[i + 1].encode('UTF-8').isalpha() != False:
                    # print(each[i])
                    con += each[i]
                if each[i].encode('UTF-8').isalpha() == True and each[i + 1].encode('UTF-8').isalpha() == False:
                    # print(each[i])
                    con += each[i]
                    # print(con)
                    list_.append(con)
                    con = ''
                if each[i].encode('UTF-8').isalpha() == False:
                    list_.append(each[i])
            list_.append(each[-1])
            # print(data)
            hh = []
            if '【' not in list_ and '】' not in list_:
                for i in list_:
                    hh.append(i)
                    hh.append('O')
                all_data.append(hh)
                hh = []
            if '【' in list_:
                if list_[0] != '【':
                    hh.append(list_[0])
                    hh.append('O')
                if list_[0] == '【':
                    left_flg = 1
                for i in range(1, len(list_) - 1):

                    if list_[i] == '【':
                        left_flg = 1

                    if list_[i] == '】':
                        left_flg = 0

                    if list_[i - 1] != '【' and list_[i] != '【' and list_[i] != '】' and list_[
                                i + 1] != '】' and left_flg == 0:
                        hh.append(list_[i])
                        hh.append('O')

                    if list_[i - 1] == '【' and list_[i + 1] != '】':  ##########
                        hh.append(list_[i])
                        hh.append('B-nt')
                    if list_[i - 1] != '【' and left_flg == 1 and list_[i + 1] != '】' and list_[i] != '【' and list_[
                        i] != '】':
                        hh.append(list_[i])
                        hh.append('I-nt')
                    if list_[i - 1] != '【' and list_[i + 1] == '】':
                        hh.append(list_[i])
                        hh.append('E-nt')
                    if list_[i - 1] == '【' and list_[i + 1] == '】':
                        hh.append(list_[i])
                        hh.append('S-nt')
                if list_[-1] != '】':
                    hh.append(list_[-1])
                    hh.append('O')
                tag_data.append(hh)
    return tag_data, data
'''

    # 分词，没有词性
'''
    list_ = []
    for gg in data:
        pynlpir.open()
        try:
            list_ = pynlpir.segment(gg, pos_names=None, pos_tagging=False)  # p是一个二维列表
            # print(list_)
            hh = []

            if '【' not in list_ and '】' not in list_:
                # print('11111111111111')
                for i in list_:
                    hh.append(i)
                    hh.append('O')
                all_data.append(hh)
                hh = []
            if '【' in list_:
                if list_[0] != '【':
                    hh.append(list_[0])
                    hh.append('O')
                if list_[0] == '【':
                    left_flg = 1
                for i in range(1, len(list_) - 1):

                    if list_[i] == '【':
                        left_flg = 1

                    if list_[i] == '】':
                        left_flg = 0

                    if list_[i - 1] != '【' and list_[i] != '【' and list_[i] != '】' and list_[i + 1] != '】' and left_flg == 0:
                        hh.append(list_[i])
                        hh.append('O')

                    if list_[i - 1] == '【' and list_[i + 1] != '】':  ##########
                        hh.append(list_[i])
                        hh.append('B-nt')
                    if list_[i - 1] != '【' and left_flg == 1 and list_[i + 1] != '】' and list_[i] != '【' and list_[i] != '】':
                        hh.append(list_[i])
                        hh.append('I-nt')
                    if list_[i - 1] != '【' and list_[i + 1] == '】':
                        hh.append(list_[i])
                        hh.append('E-nt')
                    if list_[i - 1] == '【' and list_[i + 1] == '】':
                        hh.append(list_[i])
                        hh.append('S-nt')
                if list_[-1] != '】':
                    hh.append(list_[-1])
                    hh.append('O')
                tag_data.append(hh)
        except:
            pass
    pynlpir.close()
    return tag_data, data
'''


def save(save_list, name):
#加词性
    with open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\正文_词+词性+标签\qbxb_%s.txt' % name, 'w', encoding='utf8')as f:
        for each in save_list:
            for i in range(0, len(each), 3):
                if each[i] != ' ':
                    f.write(str(each[i]) + '\t' + str(each[i + 1]) + '\t'+ str(each[i+2]) + '\n')#将分隔符从空格改成tab
            f.write('\n')

#不加词性
'''
    with open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\正文_词+词性+标签\qbxb_%s.txt'%name,'w',encoding='utf8')as f:
        for each in save_list:
            for i in range(0,len(each),2):
                f.write(str(each[i])+' '+str(each[i+1])+'\n')
            f.write('\n')
'''
def main():

    print('开始...........')
    begin = time.clock()
    file_path = r'D:\Pythontask\第十次任务20170509\情报学报语料'
    # file_path = r'D:\Pythontask\第十次任务20170509\新建文件夹'
    fileArray = fun(file_path)
    all_data = []
    for path in fileArray:
        each_data = get_data(path)
        for i in each_data:
            all_data.append(i)
    tag_data, data = add_tag(all_data)

    random.shuffle(tag_data)

    a = int(0.7*len(tag_data))
    train = tag_data[:a]
    vec = tag_data[a+1:]

    save(train, 'train')
    save(vec, 'vec')
    save(tag_data, 'all')

    test_data = ''
    for j in range(len(vec)):
        each = vec[j]
        for i in range(0, len(each), 3):
            test_data += each[i]

    save_list = []

    # for each in data:
    #     each = each.replace('【', '').replace('】', '')
    #     lit = list(each)
    #     for i in lit:
    #         set_.append(i)
    #     save_list.append(lit)

    for each in tag_data:
        set_ = []
        for i in range(0, len(each), 3):
            set_.append(each[i])
        save_list.append(set_)

    test_data = test_data.replace(' ', '').replace('\\n\'', '').replace(',\'', '').replace('【','').replace('】','')
    with open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\正文_词+词性+标签\qbxbtest.txt', 'w', encoding='utf8')as f:
        f.write(test_data)

    model = word2vec.Word2Vec(save_list, alpha=0.001, min_count=5, size=100)
    fw = codecs.open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\正文_词+词性+标签\qbxb_wordvec.txt', "w", "utf-8")
    fw.write(str(len(model.wv.vocab.keys())) + " " + "100")
    fw.write("\n")
    for k in model.wv.vocab.keys():
        fw.write(k + " " + ' '.join([str(wxs) for wxs in model[k].tolist()]))
        fw.write("\n")

    end = time.clock()
    print('任务结束，用时为：'+str(end-begin)+'s')


if __name__ == '__main__':
    main()


















