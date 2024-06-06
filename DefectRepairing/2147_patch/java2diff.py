import json
import os
import subprocess

def process_functions(input_file, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取jsonl文件
    with open(input_file, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            data = json.loads(line)
            function1 = data["function1"]
            function2 = data["function2"]

            # 为每对function创建新的目录
            current_dir = os.path.join(output_dir, f"example_{index}")
            os.makedirs(current_dir, exist_ok=True)

            # 写入buggy.java和fixed.java
            buggy_path = os.path.join(current_dir, "buggy.java")
            fixed_path = os.path.join(current_dir, "fixed.java")
            with open(buggy_path, 'w', encoding='utf-8') as f:
                f.write(function1)
            with open(fixed_path, 'w', encoding='utf-8') as f:
                f.write(function2)

            # 运行diff命令并保存到patch.diff
            patch_path = os.path.join(current_dir, "patch.diff")
            with open(patch_path, 'w', encoding='utf-8') as f:
                subprocess.run(['diff', '-u', buggy_path, fixed_path], stdout=f)

# 调用函数
process_functions('train.jsonl', 'output')
