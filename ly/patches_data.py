import os
import re
import numpy as np
import pandas as pd
# from sklearn.model_selection import StratifiedKFold


# def divide_buggy_fixed(patch_path):
#     buggy_code = ""
#     fixed_code = ""
#     with open(patch_path) as f:
#         lines = f.read().splitlines()
#     i = 0
#     while i < len(lines):
#         if not lines[i].startswith("@@"):
#             i += 1
#         else:
#             break
#     while i < len(lines)-1:
#         i += 1
#         if lines[i].startswith('---') or lines[i].startswith('+++') or lines[i].startswith("@@"):
#             continue
#         elif lines[i].startswith('- '):
#             buggy_code += lines[i]
#         elif lines[i].startswith('+ '):
#             fixed_code += lines[i]
#         else:
#             buggy_code += lines[i]
#             fixed_code += lines[i]
#     return buggy_code, fixed_code

def divide_buggy_fixed(patch_path, type):
    lines = []
    file = open(patch_path, 'r')
    p = r"([^\w_])"
    flag = True
    # try:
    for line in file:
        line = line.strip()
        if '*/' in line:
            flag = True
            continue
        if flag == False:
            continue
        if line != '':
            if line.startswith('@@') or line.startswith('diff') or line.startswith('index'):
                continue
            if line.startswith('Index') or line.startswith('==='):
                continue
            elif '/*' in line:
                flag = False
                continue
            elif type == 'buggy':
                if line.startswith('---') or line.startswith('PATCH_DIFF_ORIG=---'):
                    continue
                    line = re.split(pattern=p, string=line.split(' ')[1].strip())
                    lines.append(' '.join(line))
                elif line.startswith('-'):
                    if line[1:].strip().startswith('//'):
                        continue
                    line = re.split(pattern=p, string=line[1:].strip())
                    line = [x.strip() for x in line]
                    while '' in line:
                        line.remove('')
                    line = ' '.join(line)
                    lines.append(line.strip())
                elif line.startswith('+'):
                    # do nothing
                    pass
                else:
                    line = re.split(pattern=p, string=line.strip())
                    line = [x.strip() for x in line]
                    while '' in line:
                        line.remove('')
                    line = ' '.join(line)
                    lines.append(line.strip())
            elif type == 'fixed':
                if line.startswith('+++'):
                    continue
                    line = re.split(pattern=p, string=line.split(' ')[1].strip())
                    lines.append(' '.join(line))
                elif line.startswith('+'):
                    if line[1:].strip().startswith('//'):
                        continue
                    line = re.split(pattern=p, string=line[1:].strip())
                    line = [x.strip() for x in line]
                    while '' in line:
                        line.remove('')
                    line = ' '.join(line)
                    lines.append(line.strip())
                elif line.startswith('-'):
                    # do nothing
                    pass
                else:
                    line = re.split(pattern=p, string=line.strip())
                    line = [x.strip() for x in line]
                    while '' in line:
                        line.remove('')
                    line = ' '.join(line)
                    lines.append(line.strip())
    return ' '.join(lines)

def run_divide(path, output_path):
    buggy_arr, fixed_arr, labels = list(), list(), list()

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.DS_Store'):
                continue
            file_path = os.path.join(root, file)
            buggy_code = divide_buggy_fixed(file_path, 'buggy')
            fixed_code = divide_buggy_fixed(file_path, 'fixed')
            buggy_arr.append(buggy_code)
            fixed_arr.append(fixed_code)
            if 'correct' in root:
                labels.append(1)
            else:
                labels.append(0)
    data = buggy_arr, fixed_arr, labels
    with open(output_path, 'wb') as f:
        pd.to_pickle(data, f, protocol=4)

def divide_dataset(data_path, output_path):
    '''划分训练数据与测试数据，采用n_splits倍交叉验证的方式进行划分'''
    # 加载数据
    with open(data_path, 'rb') as f:
        buggy_arr, fixed_arr, label_arr = pd.read_pickle(f)
    texts_1, texts_2, labels = np.array(buggy_arr), np.array(fixed_arr), np.array(label_arr)

    # 划分训练与测试数据集
    skf = StratifiedKFold(n_splits=10, shuffle=True)
    index = [[train, test] for train, test in skf.split(texts_1, labels)]
    for i in range(len(index)):
        train_index, test_index = index[i][0], index[i][1]
        train_texts_1, train_texts_2, train_labels = texts_1[train_index], texts_2[train_index], labels[train_index]
        test_texts_1, test_texts_2, test_labels = texts_1[test_index], texts_2[test_index], labels[test_index]
        # 保存第 i 份训练数据
        data_train_path = os.path.join(output_path, 'data_code_train_' + str(i) + '.pkl')
        data_train = np.array(train_texts_1), np.array(train_texts_2), np.array(train_labels)
        with open(data_train_path, 'wb') as f:
            pd.to_pickle(data_train, f, protocol=4)
        # 保存第 i 份测试数据
        data_test_path = os.path.join(output_path, 'data_code_test_' + str(i) + '.pkl')
        data_test = np.array(test_texts_1), np.array(test_texts_2), np.array(test_labels)
        with open(data_test_path, 'wb') as f:
            pd.to_pickle(data_test, f, protocol=4)

if __name__ == "__main__":
    output_path = './data_code_large.pkl'
    data_path = './patches/Large'
    run_divide(data_path, output_path)

    # data_path = './temp_code_data_wang.pkl'
    # output_path = './'
    # divide_dataset(data_path, output_path)

    # code = divide_buggy_fixed('/Users/robot17/PycharmProjects/EvaPatch/get_tran/patches/Small/correct/ACS/Chart/patch2-Chart-14-ACS.patch', 'buggy')
    # print(code)