import json

# 指定你的jsonl文件路径
# file_path = 'patch_sim.jsonl'
file_path = 'data_total.jsonl'

# 指定原始jsonl文件路径
input_file_path = 'patch_sim.jsonl'
# 指定去重后的jsonl文件路径
output_file_path = 'deduplicated_patch_sim.jsonl'

file_mapping = ['Patch1', 'Patch10', 'Patch11', 'Patch12', 'Patch13', 'Patch14', 'Patch15', 'Patch150', 'Patch151', 'Patch152', 'Patch153', 'Patch154', 'Patch155', 'Patch157', 'Patch158', 'Patch159', 'Patch16', 'Patch160', 'Patch161', 'Patch162', 'Patch163', 'Patch165', 'Patch166', 'Patch167', 'Patch168', 'Patch169', 'Patch17', 'Patch170', 'Patch171', 'Patch172', 'Patch173', 'Patch174', 'Patch175', 'Patch176', 'Patch177', 'Patch18', 'Patch180', 'Patch181', 'Patch182', 'Patch183', 'Patch184', 'Patch185', 'Patch186', 'Patch187', 'Patch188', 'Patch189', 'Patch19', 'Patch191', 'Patch192', 'Patch193', 'Patch194', 'Patch195', 'Patch196', 'Patch197', 'Patch198', 'Patch199', 'Patch2', 'Patch20', 'Patch201', 'Patch202', 'Patch203', 'Patch204', 'Patch205', 'Patch206', 'Patch207', 'Patch208', 'Patch209', 'Patch21', 'Patch210', 'Patch22', 'Patch23', 'Patch24', 'Patch25', 'Patch26', 'Patch27', 'Patch28', 'Patch29', 'Patch30', 'Patch31', 'Patch32', 'Patch33', 'Patch34', 'Patch36', 'Patch37', 'Patch38', 'Patch4', 'Patch44', 'Patch45', 'Patch46', 'Patch47', 'Patch48', 'Patch49', 'Patch5', 'Patch51', 'Patch53', 'Patch54', 'Patch55', 'Patch58', 'Patch59', 'Patch6', 'Patch62', 'Patch63', 'Patch64', 'Patch65', 'Patch66', 'Patch67', 'Patch68', 'Patch69', 'Patch7', 'Patch72', 'Patch73', 'Patch74', 'Patch75', 'Patch76', 'Patch77', 'Patch78', 'Patch79', 'Patch8', 'Patch80', 'Patch81', 'Patch82', 'Patch83', 'Patch84', 'Patch88', 'Patch89', 'Patch9', 'Patch90', 'Patch91', 'Patch92', 'Patch93', 'PatchHDRepair1', 'PatchHDRepair10', 'PatchHDRepair3', 'PatchHDRepair4', 'PatchHDRepair5', 'PatchHDRepair6', 'PatchHDRepair7', 'PatchHDRepair8', 'PatchHDRepair9']

def check_duplicates(file_path):
    # 用来存储每条数据的集合
    seen_data = {}
    duplicates = []
    total_entries = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            # 将每行的json字符串转换成字典
            data = json.loads(line)
            # 构建一个元组，包含我们关心的字段
            data_tuple = (data['buggy_code'], data['fixed_code'], data['label'])
            # 检查这个元组是否已经在集合中
            if data_tuple in seen_data:
                if data_tuple not in duplicates:
                    duplicates.append(data_tuple)
                seen_data[data_tuple].append(line_num)
            else:
                seen_data[data_tuple] = [line_num]
            total_entries += 1

    # 打印结果
    print(f"Total entries: {total_entries}")
    print(f"Unique entries: {len(seen_data)}")
    if duplicates:
        print(f"Number of duplicates: {len(duplicates)}")
        for dup in duplicates:
            line_nums = seen_data[dup]
            # print(f"Duplicate entry: {dup}")
            # print(f"Line numbers: {line_nums} : {file_mapping[line_nums[0] - 1]} and {file_mapping[line_nums[1] - 1]}")
            print(f"Line numbers: {line_nums}")
    else:
        print("No duplicates found.")

def remove_duplicates_and_save(input_file_path, output_file_path):
    seen_data = set()
    unique_entries = []
    total_entries = 0

    # 读取原始数据并检测重复
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            data_tuple = (data['buggy_code'], data['fixed_code'], data['label'])
            if data_tuple not in seen_data:
                seen_data.add(data_tuple)
                unique_entries.append(data)
            total_entries += 1

    # 将不重复的数据写入新文件
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for entry in unique_entries:
            json.dump(entry, outfile)
            outfile.write('\n')  # 确保每个数据对象后都有换行符，以符合jsonl的格式

    # 打印统计结果
    print(f"Total entries read: {total_entries}")
    print(f"Unique entries saved: {len(unique_entries)}")

# 调用函数
# check_duplicates(file_path)
remove_duplicates_and_save(input_file_path, output_file_path)