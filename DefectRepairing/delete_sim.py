import json

# 设置文件路径
file_a_path = 'deduplicated_data.jsonl'
file_b_path = 'deduplicated_patch_sim.jsonl'
output_file_path = 'result.jsonl'

def remove_entries_from_a():
    # 读取b中的所有数据并添加到集合中
    total_b = 0
    entries_in_b = set()
    with open(file_b_path, 'r', encoding='utf-8') as file_b:
        for line in file_b:
            total_b += 1
            data = json.loads(line)
            entry_tuple = (data['buggy_code'], data['fixed_code'], data['label'])
            entries_in_b.add(entry_tuple)
    
    # 遍历a中的数据，排除在b中存在的数据
    total_a = 0
    both = 0
    unique_entries = []
    with open(file_a_path, 'r', encoding='utf-8') as file_a:
        for line in file_a:
            total_a += 1
            data = json.loads(line)
            entry_tuple = (data['buggy_code'], data['fixed_code'], data['label'])
            if entry_tuple not in entries_in_b:
                unique_entries.append(data)
            else:
                both += 1
    
    # 将剩余的唯一数据写入新文件
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for entry in unique_entries:
            json.dump(entry, outfile)
            outfile.write('\n')  # 确保每个数据对象后都有换行符，以符合jsonl的格式
    
    # 打印信息
    print(f"Total entries in file PatchSim: {total_b}")
    # print(f"After duplicates removed in file PatchSim: {len(entries_in_b)}")

    print(f"Total entries in file new2000T: {total_a}")

    print(f"Repeat in both files: {both}")
    print(f"Total entries in both files after deduplicating: {len(unique_entries) + len(entries_in_b)}")

    print(f"entries in file new2000T after remove PatchSim: {len(unique_entries)}")

# 调用函数执行任务
remove_entries_from_a()
