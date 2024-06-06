import os
import subprocess

def generate_patches(root_dir):
    # 遍历根目录下的所有文件夹和子文件夹
    for subdir, dirs, files in os.walk(root_dir):
        # 检查是否同时存在buggy.java和fixed.java
        if 'buggy.java' in files and 'fixed.java' in files:
            # 构建完整的文件路径
            buggy_path = os.path.join(subdir, 'buggy.java')
            fixed_path = os.path.join(subdir, 'fixed.java')
            patch_path = os.path.join(subdir, 'changes.patch')
            
            # 执行diff命令
            with open(patch_path, 'w') as f:
                subprocess.run(['diff', '-u', buggy_path, fixed_path], stdout=f)

            print(f'Patch file created at: {patch_path}')

# 设定你的根目录路径
root_directory = 'methods'
generate_patches(root_directory)
