import os
import re
import numpy as np
import pandas as pd
# from sklearn.model_selection import StratifiedKFold
import json


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
    with open(output_path, 'w') as f:
        for root, dirs, files in os.walk(path):
            files.sort()
            print(files)
            for file in files:
                if file.endswith('.DS_Store'):
                    continue
                file_path = os.path.join(root, file)
                buggy_code = divide_buggy_fixed(file_path, 'buggy')
                fixed_code = divide_buggy_fixed(file_path, 'fixed')
                if 'correct' in root:
                    label = 1
                else:
                    label = 0
                data = {
                    'buggy_code': buggy_code,
                    'fixed_code': fixed_code,
                    'label': label
                }
                json.dump(data, f)
                f.write('\n')

if __name__ == "__main__":
    output_path = './patch_sim.jsonl'
    data_path = './filter_patches'
    run_divide(data_path, output_path)

    # data_path = './temp_code_data_wang.pkl'
    # output_path = './'
    # divide_dataset(data_path, output_path)

    # code = divide_buggy_fixed('/Users/robot17/PycharmProjects/EvaPatch/get_tran/patches/Small/correct/ACS/Chart/patch2-Chart-14-ACS.patch', 'buggy')
    # print(code)