import xlrd
import time
import random
import os
from gensim.models import word2vec
import codecs

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

    line = str_save.replace('。', '。 ')
    line = line.replace('\n', '')
    data = line.split(' ')
    tag_data = []
    left_flg = 0
    for each in data:
        # lit_list = list(lit)
        # temp = []
        # temp.append(lit_list[0])
        # temp.append('B-nt')
        # for i in range(1,len(lit_list)):
        #     temp.append(lit_list[i])
        #     temp.append('I-nt')
        # tag_data.append(temp)
        list_ = list(each)
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

                if list_[i - 1] != '【' and list_[i] != '【' and list_[i] != '】' and list_[i + 1] != '】' and left_flg == 0:
                    hh.append(list_[i])
                    hh.append('O')

                if list_[i - 1] == '【' :##########
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
    return tag_data, data


def save(save_list, name):
    # if name == 'train':
    with open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\情报学报正文\qbxb_%s.txt'%name,'w',encoding='utf8')as f:
        for each in save_list:
            for i in range(0,len(each),2):
                f.write(str(each[i])+' '+str(each[i+1])+'\n')
            f.write('\n')

def main():
    print('开始...........')
    begin = time.clock()
    file_path = r'D:\Pythontask\第十次任务20170509\情报学报语料'
    # file_path = r'D:\Pythontask\第十次任务20170509\新建文件夹'
    fileArray = fun(file_path)
    all_data = []
    for path in fileArray:
        each_file = get_data(path)
        for i in each_file:
            all_data.append(i)
    tag_data, data = add_tag(all_data)

    random.shuffle(tag_data)
    a = int(0.7*len(tag_data))
    train = tag_data[:a]
    vec = tag_data[a+1:]

    save(train, 'train')
    save(vec, 'vec')

    test_data = ''
    for j in range(len(vec)):
        each = vec[j]
        for i in range(0, len(each), 2):
            test_data += each[i]

    set_ = []
    save_list = []
    for each in data:
        each = each.replace('【','').replace('】','')
        lit = list(each)
        for i in lit:
            set_.append(i)
        save_list.append(lit)

    test_data = test_data.replace(' ', '').replace('\\n\'', '').replace(',\'', '').replace('【','').replace('】','')
    with open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\情报学报正文\qbxbtest.txt', 'w', encoding='utf8')as f:
        f.write(test_data)

    model = word2vec.Word2Vec(save_list, alpha=0.001, min_count=5, size=100)
    fw = codecs.open(r'D:\learnPython\深度学习\任务三_情报学报软件实体rnn+crf_20171027\情报学报正文\qbxb_wordvec.txt', "w", "utf-8")
    fw.write(str(len(model.wv.vocab.keys())) + " " + "100")
    fw.write("\n")
    for k in model.wv.vocab.keys():
        fw.write(k + " " + ' '.join([str(wxs) for wxs in model[k].tolist()]))
        fw.write("\n")

    end = time.clock()
    print('任务结束，用时为：'+str(end-begin)+'s')


if __name__ == '__main__':
    main()


















