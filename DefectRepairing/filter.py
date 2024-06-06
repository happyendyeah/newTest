import os

# 指定你的文件夹路径
folder_path = 'filter_patches'

# 给定的列表
keep_files = [
    1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 36, 37, 38, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 58, 59, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75,
    76, 77, 78, 79, 80, 81, 82, 83, 84, 88, 89, 90, 91, 92, 93, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161,
    162, 163, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 180, 181, 182, 183, 184, 185, 186, 187,
    188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 'HDRepair1',
    'HDRepair3', 'HDRepair4', 'HDRepair5', 'HDRepair6', 'HDRepair7', 'HDRepair8', 'HDRepair9', 'HDRepair10'
]

print(len(keep_files))

# 将数字转换为字符串，并添加前缀'Patch'或'PatchHDRepair'
keep_filenames = [f'Patch{i}' for i in keep_files if isinstance(i, int)] + [f'Patch{i}' for i in keep_files if isinstance(i, str)]

# 获取文件夹中的所有文件名
all_files = os.listdir(folder_path)

delete_number = 0
keep_number = 0
# 删除不在列表中的文件
for file in all_files:
    if file not in keep_filenames:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        delete_number += 1
        print(f"Deleted: {file}")
    else:
        print(f"Kept: {file}")
        keep_number += 1

print(f"Deleted {delete_number} files.")
print(f"Kept {keep_number} files.")
