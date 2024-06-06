import os
import json
import re

def clean_code(code):
    # Replace \n and \t with a single space
    code = re.sub(r'\s+', ' ', code)
    # Ensure space around certain characters
    code = re.sub(r'([{}()\[\]])', r' \1 ', code)
    # Replace multiple spaces with a single space
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def extract_code(folder_path):
    buggy_file_path = os.path.join(folder_path, 'buggy.java')
    fixed_file_path = os.path.join(folder_path, 'fixed.java')

    with open(buggy_file_path, 'r', encoding='utf-8') as file:
        buggy_code = file.read()

    with open(fixed_file_path, 'r', encoding='utf-8') as file:
        fixed_code = file.read()

    buggy_code = clean_code(buggy_code)
    fixed_code = clean_code(fixed_code)

    return buggy_code, fixed_code

def main(root_dir, output_file):
    # Initialize a list to store the data
    data_list = []

    # Define label mapping based on folder names
    label_map = {'CORRECT': 0, 'INCORRECT': 1}

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'buggy.java' in filenames and 'fixed.java' in filenames:
            buggy_code, fixed_code = extract_code(dirpath)
            if 'INCORRECT' in dirpath:
                label = 1
            else:
                label = 0
            if '_DA_' not in dirpath:
                data_list.append({
                    'buggy_code': buggy_code,
                    'fixed_code': fixed_code,
                    'label': label,
                    'path': dirpath
                })

    # Write to jsonl file
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in data_list:
            file.write(json.dumps(entry) + '\n')

# Example usage
if __name__ == '__main__':
    main('methods', 'data_clean.jsonl')
