import os
import re
import numpy as np
import pandas as pd
import json
from sklearn.model_selection import StratifiedKFold


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
    file = open(patch_path, 'r', encoding='utf-8')
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

def run_divide_pk(path, output_path):
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
            if 'incorrect' in root.lower():
                labels.append(0)
            else:
                labels.append(1)
    data = buggy_arr, fixed_arr, labels
    with open(output_path, 'wb') as f:
        pd.to_pickle(data, f, protocol=4)

def run_divide_txt(path, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        with open('source.txt', 'r', encoding='utf-8') as file:
            paths = [line.strip() for line in file if line.strip()]
            for path in paths:
                file = path.split('/')[-1]
                root = '/'.join(path.split('/')[:-1])
                if file.endswith('.DS_Store'):
                    continue
                if file.endswith('.patch') and 'DA' not in root:
                    file_path = os.path.join(root, file)
                    print(file_path)
                    buggy_code = divide_buggy_fixed(file_path, 'buggy')
                    fixed_code = divide_buggy_fixed(file_path, 'fixed')
                    
                    # 判断当前文件是否在含有'correct'的目录下
                    label = 0 if 'incorrect' in root.lower() else 1
                    # print(label)

                    # APPT
                    # tool_name = root.split('\\')[-2]
                    # patch_name = file.split('-')[0]
                    # project_name = file.split('-')[1] + '_' + file.split('-')[2]

                    # COMPASS
                    # patch_name = root.split('\\')[-1].split('_')[-1]
                    # project_name = root.split('\\')[-2].split('_')[1] + '_' + root.split('\\')[-2].split('_')[2]
                    # tool_name = root.split('\\')[-2].split('_')[0]

                    # Original
                    # print(root)
                    tool_name = root.split('/')[-3]
                    patch_name = file.split('.')[0]
                    project_name = root.split('/')[-2] + '_' + root.split('/')[-1]
                    
                    # 创建一个字典，存储当前文件的buggy和fixed代码以及标签
                    data_dict = {
                        'buggy_code': buggy_code,
                        'fixed_code': fixed_code,
                        'label': label,
                        'tool_name' : tool_name,
                        'patch_name': patch_name,
                        'project_name': project_name
                    }
                    
                    # 将字典转换为JSON格式的字符串，并写入文件，每个对象一行
                    json_line = json.dumps(data_dict)
                    f.write(json_line + '\n')

def run_divide(path, output_path):
    unique_fields = extract_unique_fields('train_fold_5.jsonl')
    print(unique_fields)
    with open(output_path, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.DS_Store'):
                    continue
                if file.endswith('.patch'):
                    file_path = os.path.join(root, file)
                    print(file_path)
                    buggy_code = divide_buggy_fixed(file_path, 'buggy')
                    fixed_code = divide_buggy_fixed(file_path, 'fixed')
                    
                    # 判断当前文件是否在含有'correct'的目录下
                    label = 0 if 'incorrect' in root.lower() else 1
                    # print(label)

                    # APPT
                    # tool_name = root.split('\\')[-2]
                    # patch_name = file.split('-')[0]
                    # project_name = file.split('-')[1] + '_' + file.split('-')[2]

                    # COMPASS
                    if 'DA' not in root:
                        patch_name = root.split('\\')[-1].split('_')[-1]
                        project_name = root.split('\\')[-2].split('_')[1] + '_' + root.split('\\')[-2].split('_')[2]
                        tool_name = root.split('\\')[-2].split('_')[0]
                    else:
                        patch_name = root.split('\\')[-1].split('_')[-3]
                        project_name = root.split('\\')[-2].split('_')[1] + '_' + root.split('\\')[-2].split('_')[2]
                        tool_name = root.split('\\')[-2].split('_')[0]

                    # Original
                    # print(root)
                    # tool_name = root.split('\\')[-3]
                    # patch_name = file.split('.')[0]
                    # project_name = root.split('\\')[-2] + '_' + root.split('\\')[-1]
                    if (tool_name, patch_name, project_name) not in unique_fields:
                        # print(tool_name, patch_name, project_name)
                        continue
                    
                    # 创建一个字典，存储当前文件的buggy和fixed代码以及标签
                    data_dict = {
                        'buggy_code': buggy_code,
                        'fixed_code': fixed_code,
                        'label': label,
                        'tool_name' : tool_name,
                        'patch_name': patch_name,
                        'project_name': project_name
                    }
                    
                    # 将字典转换为JSON格式的字符串，并写入文件，每个对象一行
                    json_line = json.dumps(data_dict)
                    f.write(json_line + '\n')

def load_jsonl(file_path):
    """Load data from a jsonl file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def extract_unique_fields(file_path):
    """Extract unique tool_name, patch_name, and project_name from a jsonl file."""
    data = load_jsonl(file_path)
    
    unique_fields = set()
    
    for item in data:
        tool_name = item.get('tool_name')
        patch_name = item.get('patch_name')
        project_name = item.get('project_name')
        
        if tool_name and patch_name and project_name:
            unique_fields.add((tool_name, patch_name, project_name))
    
    return unique_fields

def divide_dataset_pk(data_path, output_path):
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

def load_data_from_jsonl(data_path):
    buggy_arr, fixed_arr, labels = [], [], []
    with open(data_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            buggy_arr.append(data['buggy_code'])
            fixed_arr.append(data['fixed_code'])
            labels.append(data['label'])
    return buggy_arr, fixed_arr, labels

def save_data_to_jsonl(data, output_path):
    with open(output_path, 'w') as file:
        for entry in zip(*data):
            json_obj = {'buggy_code': entry[0], 'fixed_code': entry[1], 'label': entry[2]}
            file.write(json.dumps(json_obj) + '\n')

def divide_dataset(data_path, output_path):
    # 加载数据
    buggy_arr, fixed_arr, label_arr = load_data_from_jsonl(data_path)
    texts_1, texts_2, labels = np.array(buggy_arr), np.array(fixed_arr), np.array(label_arr)

    # 划分训练与测试数据集
    skf = StratifiedKFold(n_splits=10, shuffle=True)
    index = [[train, test] for train, test in skf.split(texts_1, labels)]
    for i, (train_index, test_index) in enumerate(index):
        train_texts_1, train_texts_2, train_labels = texts_1[train_index], texts_2[train_index], labels[train_index]
        test_texts_1, test_texts_2, test_labels = texts_1[test_index], texts_2[test_index], labels[test_index]
        
        # 保存第 i 份训练数据
        data_train_path = os.path.join(output_path, f'data_code_train_{i}.jsonl')
        data_train = (train_texts_1, train_texts_2, train_labels)
        save_data_to_jsonl(data_train, data_train_path)
        
        # 保存第 i 份测试数据
        data_test_path = os.path.join(output_path, f'data_code_test_{i}.jsonl')
        data_test = (test_texts_1, test_texts_2, test_labels)
        save_data_to_jsonl(data_test, data_test_path)

def find_first_difference(str1, str2):
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] != str2[i]:
            return i, str1[i], str2[i]
    if len(str1) != len(str2):
        return length, 'End of shorter string', 'End of shorter string'
    return None  # Strings are equal

if __name__ == "__main__":
    # output_path = 'APPT.json'
    # data_path = 'patches//Small'
    # print('Running...')
    # run_divide(data_path, output_path)
    # print('Done!')

    output_path = 'train_DA_5.jsonl'
    data_path = 'C:\\Users\\yeren\\Desktop\\Cache-master\\methods'
    print('Running...')
    run_divide(data_path, output_path)
    print('Done!')

    # output_path = 'original_dedup.jsonl'
    # data_path = 'Total_final'
    # print('Running...')
    # run_divide(data_path, output_path)
    # print('Done!')

    # data_path = 'dataset/APPT_ORI_COMPASS.jsonl'
    # output_path = 'dataset/'
    # divide_dataset(data_path, output_path)

    # code = divide_buggy_fixed('/Users/robot17/PycharmProjects/EvaPatch/get_tran/patches/Small/correct/ACS/Chart/patch2-Chart-14-ACS.patch', 'buggy')
    # print(code)
