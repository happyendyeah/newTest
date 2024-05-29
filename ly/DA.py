import os
import subprocess

def enhance_files(root_dir, path_of_jre, path_of_dependent_jar=None):
    for root, dirs, files in os.walk(root_dir):
        # 检查当前目录下是否有Java文件
        java_files = [file for file in files if file.endswith('.java')]
        if len(java_files) == 2:  # 假设我们每个目录下应该有两个Java文件
            
            for file in java_files:
                java_file_path = os.path.join(root, file)
                for rule_id in range(18):
                    output_subdir = f"{root}_DA_{rule_id}"  # 创建特定的输出目录名
                    output_dir = os.path.join(root, output_subdir)
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)  # 创建输出目录
                    # 构造增强命令
                    command = [
                        'java', '-jar', 'C:\\Users\\yeren\\Desktop\\ly\\SPAT\\artifacts\\SPAT.jar',
                        str(rule_id), root, output_dir + '\\', 
                        path_of_jre
                    ]
                    if path_of_dependent_jar:
                        command.extend(['&', path_of_dependent_jar])
                    
                    # 执行命令
                    stdout, stderr = "", ""
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"stdout: {stdout}")
                    print(f"stderr: {stderr}")
                    print(f"Processed and stored in {output_dir}: {java_file_path}")

# 参数设置
root_dir = 'C:\\Users\\yeren\\Desktop\\ly\\methods'
# output_dir = 'C:\\Users\\yeren\\Desktop\\ly\\methods\\methods'
path_of_jre = 'C:\\Java\\jdk1.8.0_201\\jre\\lib\\rt.jar'
# path_of_dependent_jar = '/path/to/other/dependent.jar'  # 如有需要，填写此项

# 调用函数
# enhance_files(root_dir, output_dir, rule_id, path_of_jre)

print("start handle")
enhance_files(root_dir, path_of_jre)
print("end handle")