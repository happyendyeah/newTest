import json

def load_jsonl(file_path):
    """Load data from a jsonl file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def save_jsonl(data, file_path):
    """Save data to a jsonl file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

def merge_and_deduplicate(file1, file2, output_file):
    """Merge two jsonl files and remove duplicates."""
    data1 = load_jsonl(file1)
    data2 = load_jsonl(file2)

    # Combine the data
    combined_data = data1 + data2

    # Remove duplicates by converting the list to a set of JSON strings and back to a list of dictionaries
    unique_data = [json.loads(item) for item in set(json.dumps(d, ensure_ascii=False) for d in combined_data)]

    print(len(unique_data))

    # Save the deduplicated data to the output file
    save_jsonl(unique_data, output_file)

if __name__ == "__main__":
    file1 = 'APPT_COMPASS.jsonl'
    file2 = 'APPT_original_COMPASS.jsonl'
    output_file = 'merged_output.jsonl'
    
    merge_and_deduplicate(file1, file2, output_file)
    print(f"Merged and deduplicated data has been saved to {output_file}")
