import os

def fun(file_path):
    fileArray = []
    for root, dirs, files in os.walk(file_path):
        for fn in files:
            eachpath = str(root + '/' + fn)
            fileArray.append(eachpath)
    return fileArray  # 返回的是列表

def process(path, codes):
    lines = []
    each = []
    try:
        with open(path, 'r', encoding=codes)as f:
            lines = f.readlines()
    except:
        each = ['0', '1', '3', '4', '5', '6']
        return each

    if len(lines) < 60:
        for line in lines:
            if len(line) != 0:
                line = line.replace(' ', '').replace('\t', '')
                line = line.replace('h1', ' h1 ').replace('h2', ' h2 ').replace('h3', ' h3 ').replace('h4', ' h4 ')
                line = line.replace('g', ' g')
                each.append(line)
        return each
    else:
        each = ['0', '1', '3', '4', '5', '6']
        return each

def work(all_data, tag):
    select_tag = []
    if tag == 'h':
        for each in all_data:
            if 'h1' in each or 'h2' in each or 'h3' in each or 'h4' in each:
                each = each.replace(' ', '').replace('\t', '').replace('\n', '')
                each = each.replace('h1', ' h1 ').replace('h2', ' h2 ').replace('h3', ' h3 ').replace('h4', ' h4 ')
                select_tag.append(each.split(' ')[0])
        return select_tag

    if tag == 'g':
        for each in all_data:
            if 'g' in each:
                each = each.replace(' ', '').replace('\t', '').replace('\n', '')
                each = each.replace('g', ' h1')
                select_tag.append(each.split(' ')[0])
        return select_tag

def save(tag_data,tag):
    with open(r'D:\Pythontask\情报学报论文框架20171113\处理结果\%s标签所有数据.txt'%tag, 'w', encoding='utf8')as f:
        for each in tag_data:
            if len(each) != 0 and len(each) != 2:#去除空行和类似“图2”、“表1”这样的行
                f.write(each)
                f.write('\n')

def main():
    file_path = r'D:\Pythontask\情报学报论文框架20171113\所有论文txt'
    fileArray = fun(file_path)
    # print(len(fileArray))
    all_utf8 = []
    all_gbk = []
    codes_utf8 = 'utf8'
    codes_gbk = 'gbk'
    for path in fileArray:
        new1 = process(path, codes_utf8)
        if len(new1) != 6:
            all_utf8.append(new1)#197

        new2 = process(path, codes_gbk)
        if len(new2) != 6:
            all_gbk.append(new2)#1717

    all_data = []
    for each in all_utf8:
        for i in each:
            all_data.append(i)

    for each in all_gbk:
        for i in each:
            all_data.append(i)
    #print(len(all_data))    #25914
    h_data = work(all_data, 'h')
    g_data = work(all_data, 'g')

    save(h_data, 'h')
    save(g_data, 'g')

if __name__ == '__main__':
    main()