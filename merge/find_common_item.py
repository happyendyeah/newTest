import json

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def save_jsonl(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def find_common_entries(appt_data, compass_data):
    common_entries = []
    
    # Create sets for fast lookup
    appt_set1 = {(entry['buggy_code'], entry['fixed_code'], entry['label']) for entry in appt_data}
    appt_set2 = { (entry['tool_name'], entry['project_name']) for entry in appt_data}
    #  entry['patch_name'],
    match1_count = 0
    match2_count = 0
    
    for entry in compass_data:
        if (entry['buggy_code'], entry['fixed_code'], entry['label']) in appt_set1:
            if ( entry['tool_name'],entry['project_name']) in appt_set2:
                match2_count += 1
            common_entries.append(entry)
            match1_count += 1
        elif ( entry['tool_name'], entry['project_name']) in appt_set2:
            common_entries.append(entry)
            match2_count += 1
    
    return common_entries, match1_count, match2_count

def main():
    appt_file = '638_original.jsonl'
    compass_file = 'COMPASS.jsonl'
    output_file = '638_original_COMPASS.jsonl'

    appt_data = load_jsonl(appt_file)
    compass_data = load_jsonl(compass_file)
    
    common_entries, match1_count, match2_count = find_common_entries(appt_data, compass_data)
    
    save_jsonl(output_file, common_entries)
    
    print(f"Saved {len(common_entries)} common entries to {output_file}")
    print(f"Number of entries matched by 'buggy_code', 'fixed_code', 'label': {match1_count}")
    print(f"Number of entries matched by 'tool_name', 'patch_name', 'project_name': {match2_count}")

if __name__ == '__main__':
    main()
