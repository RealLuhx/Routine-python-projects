import sqlite3
import time
import random

def get_section_title():
    conn = sqlite3.connect(r"D:\Pythontask\SRT汇报20171007\中期汇报20171007\JasistData.sqlite")
    c = conn.cursor()
    cursor = c.execute("SELECT id, section_title, sentence_id, sentence  from jasistdata")

    get_title = []
    for row in cursor:
        get_title.append(row[1])

    return get_title

def get_sentence(get_title):
    conn = sqlite3.connect(r"D:\Pythontask\SRT汇报20171007\中期汇报20171007\JasistData.sqlite")
    c = conn.cursor()
    cursor = c.execute("SELECT id, section_title, sentence_id, sentence  from jasistdata")

    getsentence = []
    for row in cursor:
        getsentence.append(row[3])

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title_引言.txt','r',encoding='utf8')as f:
        a_ = f.readlines()#去重之后的引言

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title_相关研究.txt','r',encoding='utf8')as f:
        b_ = f.readlines()#去重之后的相关研究

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title_方法.txt','r',encoding='utf8')as f:
        c_ = f.readlines()#去重之后的方法

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title_实验.txt','r',encoding='utf8')as f:
        d_ = f.readlines()#去重之后的实验

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title_结论.txt','r',encoding='utf8')as f:
        e_ = f.readlines()#去重之后的结论

    a = []
    b = []
    c = []
    d = []
    e = []
    for i in a_:
        i = i.replace('\n','')
        a.append(i)
    for i in b_:
        i = i.replace('\n','')
        b.append(i)
    for i in c_:
        i = i.replace('\n','')
        c.append(i)
    for i in d_:
        i = i.replace('\n','')
        d.append(i)
    for i in e_:
        i = i.replace('\n','')
        e.append(i)
    # print(len(a))
    # print('the length of getsentence is %d' % len(getsentence))
    return a,b,c,d,e,getsentence

def union_data(a,b,c,d,e,get_title,getsentence):
    hh = []
    all_data = []

    for i in range(1, len(getsentence)):
        hh.append(get_title[i])
        hh.append(getsentence[i])
        all_data.append(hh)
        hh = []

    del all_data[24580]
    del all_data[24591]
    del all_data[190113]

    out_data = []
    for i in range(1,len(all_data)-1):
        gg = []
        if all_data[i][0] in a and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            # print('2222222222')
            gg.append(all_data[i][1])
            gg.append('AB')
            out_data.append(gg)
        if all_data[i][0] in a and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('AM')
            out_data.append(gg)
        if all_data[i][0] in a and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('AE')
            out_data.append(gg)
        if all_data[i][0] in a and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('AS')
            out_data.append(gg)
    #相关研究
        if all_data[i][0] in b and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            # print('2222222222')
            gg.append(all_data[i][1])
            gg.append('BB')
            out_data.append(gg)
        if all_data[i][0] in b and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('BM')
            out_data.append(gg)
        if all_data[i][0] in b and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('BE')
            out_data.append(gg)
        if all_data[i][0] in b and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('BS')
            out_data.append(gg)
    #方法
        if all_data[i][0] in c and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            # print('2222222222')
            gg.append(all_data[i][1])
            gg.append('CB')
            out_data.append(gg)
        if all_data[i][0] in c and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('CM')
            out_data.append(gg)
        if all_data[i][0] in c and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('CE')
            out_data.append(gg)
        if all_data[i][0] in c and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('CS')
            out_data.append(gg)
    #实验
        if all_data[i][0] in d and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            # print('2222222222')
            gg.append(all_data[i][1])
            gg.append('DB')
            out_data.append(gg)
        if all_data[i][0] in d and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('DM')
            out_data.append(gg)
        if all_data[i][0] in d and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('DE')
            out_data.append(gg)
        if all_data[i][0] in d and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('DS')
            out_data.append(gg)
    #结论
        if all_data[i][0] in e and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            # print('2222222222')
            gg.append(all_data[i][1])
            gg.append('EB')
            out_data.append(gg)
        if all_data[i][0] in e and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] == all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('EM')
            out_data.append(gg)
        if all_data[i][0] in e and all_data[i-1][0] == all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('EE')
            out_data.append(gg)
        if all_data[i][0] in e and all_data[i-1][0] != all_data[i][0] and all_data[i+1][0] != all_data[i][0]:
            gg.append(all_data[i][1])
            gg.append('ES')
            out_data.append(gg)
    # print((len(out_data)))
    # print('the length of out_data is %d' % len(out_data))

    return out_data

def add_feat(out_list, al, bl, cl, dl, el):
    with open(r'D:\learnPython\SRT\SRT中期汇报\前1000个全关键词\前1000个全关键词_引言.txt','r',encoding='utf8')as f:
        aa = f.readlines()
    with open(r'D:\learnPython\SRT\SRT中期汇报\前1000个全关键词\前1000个全关键词_相关研究.txt','r',encoding='utf8')as f:
        bb = f.readlines()
    with open(r'D:\learnPython\SRT\SRT中期汇报\前1000个全关键词\前1000个全关键词_方法.txt','r',encoding='utf8')as f:
        cc = f.readlines()
    with open(r'D:\learnPython\SRT\SRT中期汇报\前1000个全关键词\前1000个全关键词_实验.txt','r',encoding='utf8')as f:
        dd = f.readlines()
    with open(r'D:\learnPython\SRT\SRT中期汇报\前1000个全关键词\前1000个全关键词_结论.txt','r',encoding='utf8')as f:
        ee = f.readlines()

    aa_ = get_word_only(aa)
    bb_ = get_word_only(bb)
    cc_ = get_word_only(cc)
    dd_ = get_word_only(dd)
    ee_ = get_word_only(ee)


    final_list=[]
    for item in out_list:
        # if '  ' not in item[0]:
        line = item[0].strip().replace('【','').replace('】','')
        left_word=line.split(' ')[0]
        if left_word in al:
            al_left = 'Y'
        else:
            al_left = 'N'
        if left_word in bl:
            bl_left = 'Y'
        else:
            bl_left = 'N'
        if left_word in cl:
            cl_left = 'Y'
        else:
            cl_left = 'N'
        if left_word in dl:
            dl_left = 'Y'
        else:
            dl_left = 'N'
        if left_word in el:
            el_left = 'Y'
        else:
            el_left = 'N'

        key_word = line.split(' ')
        # plus_n = str(item[i]) + '\n'
        # for i in range(len(key_word)):
        #     if key_word[i] in aa_:
        #         ak = 'Y'
        #         break
        #     if i == len(key_word)-1 and key_word[i] not in aa_:
        #         ak = 'N'
        #
        # for i in range(len(key_word)):
        #     if key_word[i] in bb_:
        #         bk = 'Y'
        #         break
        #     if i == len(key_word)-1 and key_word[i] not in bb_:
        #         bk = 'N'
        #
        # for i in range(len(key_word)):
        #     if key_word[i] in cc_:
        #         ck = 'Y'
        #         break
        #     if i == len(key_word)-1 and key_word[i] not in cc_:
        #         ck = 'N'
        #
        # for i in range(len(key_word)):
        #     if key_word[i] in dd_:
        #         dk = 'Y'
        #         break
        #     if i == len(key_word)-1 and key_word[i] not in dd_:
        #         dk = 'N'

        # for i in range(len(key_word)):
        #     if key_word[i] in ee_:
        #         ek = 'Y'
        #         break
        #     if i == len(key_word)-1 and key_word[i] not in ee_:
        #         ek = 'N'

        if line.strip() != '' and line.strip() != ' ':
            # left = line.split(' ')[0]
            # right = line.split(' ')[-1]
            length = len(line)
            line = line.replace(' ','_').replace('  ','_').replace('   ','_').replace('    ','_').replace('     ','_').replace('      ','_')
            # out_line = str(line) + '\t' + str(left) + '\t' + str(length) + '\t' + str(item[1])
            out_line = str(line) + '\t' +str(al_left) + '\t' + str(bl_left) + '\t' + str(cl_left) + '\t' + str(dl_left) + '\t' + str(el_left) + '\t' + str(length) + '\t' + str(item[1])
            # out_line = str(line) + '\t' + str(item[1])

            final_list.append(out_line)
        #print(len(final_list))
    # print('the length of final_list is %d' % len(final_list))

    return final_list

def get_word_only(data):
    out_list=[]
    for item in data:
        out_list.append(item.split('\t')[0])
    return out_list

def get_leftword():
    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title左关键词\引言左关键词.txt','r',encoding='utf8')as f:
        a_ = f.readlines()#去重之后的引言

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title左关键词\相关研究左关键词.txt','r',encoding='utf8')as f:
        b_ = f.readlines()#去重之后的相关研究

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title左关键词\方法左关键词.txt','r',encoding='utf8')as f:
        c_ = f.readlines()#去重之后的方法

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title左关键词\实验左关键词.txt','r',encoding='utf8')as f:
        d_ = f.readlines()#去重之后的实验

    with open(r'D:\learnPython\SRT\SRT中期汇报\section_title左关键词\结论左关键词.txt','r',encoding='utf8')as f:
        e_ = f.readlines()#去重之后的结论

    al = get_word_only(a_)
    bl = get_word_only(b_)
    cl = get_word_only(c_)
    dl = get_word_only(d_)
    el = get_word_only(e_)
    return al,bl,cl,dl,el

def save(name_list, name):
    with open(r'D:\learnPython\SRT\十折交叉\%s.txt'%name, 'w', encoding='utf8')as f:
        for each in name_list:
            for i in each:
                f.write(str(i)+'\n')
            f.write('\n')

def main():
    print('开始工作，请耐心等待.................')
    begin = time.clock()
    get_title = get_section_title()#从数据库获取settion_title数据
    a, b, c, d, e, getsentence = get_sentence(get_title)
    out_data = union_data(a,b,c,d,e,get_title,getsentence)
    al, bl, cl, dl, el = get_leftword()
    final_list = add_feat(out_data, al, bl, cl, dl, el)

    each_list = []
    ff = []
    for i in range(len(final_list)-1):
        each_1 = final_list[i].split('\t')
        each_2 = final_list[i+1].split('\t')
        ff.append(final_list[i])
        if each_2[-1][-2] == each_1[-1][-2] and each_2[-1][-1] != 'B':
            # ff.append(final_list[i+1])
            continue
        if each_2[-1][-2] == each_1[-1][-2] and each_2[-1][-1] == 'B':
            if len(ff) != 0:
                each_list.append(ff)
                ff = []

        if each_2[-1][-2] != each_1[-1][-2]:
            if len(ff) != 0:
                each_list.append(ff)
                ff = []

    last_list = []

    for each in each_list:
        aa = []
        aa.append(each[0])
        for i in range(1,len(each)-1):
            if each[i] == each[i-1]:
                continue
            if each[i] != each[i-1]:
                aa.append(each[i])
        aa.append(each[-1])
        last_list.append(aa)

    for i in range(1,11):

        random.shuffle(last_list)

        a = int(0.9 * len(last_list))

        train_list = last_list[0:a]
        test_list = last_list[a:]
        train = 'train_' + str(i)
        test = 'test_' + str(i)

        save(train_list, train)
        save(test_list, test)

    end = time.clock()
    print('工作结束，用时为：'+str(end-begin))

if __name__ == '__main__':
    main()

