import time
import xlrd

def reader(txt_path, excel_path1, excel_path2):
    with open(txt_path, 'r', encoding='utf8')as f:
        txt_lines = f.readlines()  #
    # print(txt_lines)
    # print(type(txt_lines))
    txt_lines = txt_lines[0].replace(' ', '').replace('﻿', '')
    # print(txt_lines)
    print(len(txt_lines))

    x1 = xlrd.open_workbook(excel_path1)  # 打开第一个表格(词表)
    sheet1 = x1.sheets()[0]
    words = []
    words = sheet1.col_values(1)
    # print(len(words))

    x1 = xlrd.open_workbook(excel_path2)
    sheet1 = x1.sheets()[0]
    stop_words = []
    stop_words = sheet1.col_values(1)
    # print(len(stop_words))

    return txt_lines, words, stop_words

def seprate(txt_lines, words, stop_words):
    # print(txt_lines)
    max_length = 6
    txt_length = len(txt_lines)
    lit_lines = []
    save_lines = []
    i = 0
    while i <= txt_length - max_length:
        # print(i)
        a = i + max_length
        word = txt_lines[i:a]
        # print(word)

        if txt_length - i < max_length and txt_length > 1:
            max_length = txt_length - i
            # print('11111111111')

        if txt_length - i == 1:
            # print('222222222222222')
            word = txt_lines[-1]
            lit_lines.append(word)

        if word in words:
            # print(word)
            lit_lines.append(word)
            i += max_length
        if word not in words:
            # print(word)
            for l in range(max_length-1, 0, -1):  ##########
                # print(l)
                # print(word[i:i + l])
                if l == 1:
                    # print(word[i:i + l])
                    lit_lines.append(word[0:l + l])
                    i += l+1
                    break

                if word[0:l] in words:
                    # print(word[i:i + l])
                    lit_lines.append(word[0:l + l])
                    i += l + 1
                    break
                    # continue
        print(lit_lines)
        # print(i)
        save_lines.append(lit_lines)
        lit_lines = []
    return save_lines

def save(save_lines):
    all_words = []
    for line in save_lines:
        for i in line:
            all_words.append(i)

    with open(r'C:\Users\DELL-80\Desktop\hhhh.txt', 'w', encoding="utf8")as f:
        for i in all_words:
            f.write(str(i) + '/')

def main():
    print('开始执行最大正向匹配算法')
    begin = time.clock()
    txt_path = r'D:\Pythontask\第五次任务20170313\20170313最大逆向匹配分词算法\分词文本\2012.11.15北京：习总书记会见出席党的十八大代表、特邀代表和列席人员时的重要讲话.txt'
    excel_path1 = r'D:\Pythontask\第五次任务20170313\20170313最大逆向匹配分词算法\词表\words.xlsx'
    excel_path2 = r'D:\Pythontask\第五次任务20170313\20170313最大逆向匹配分词算法\词表\stopwords.xlsx'
    txt_lines, words, stop_words = reader(txt_path, excel_path1, excel_path2)
    save_lines = seprate(txt_lines, words, stop_words)
    # print(save_lines)
    save(save_lines)
    end = time.clock()
    print('用时为：' + str(end - begin) + 's')

if __name__ == '__main__':
    main()