import json
import random

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

def split_data(data, n_splits=5):
    """Split data into n_splits random parts."""
    random.shuffle(data)
    return [data[i::n_splits] for i in range(n_splits)]

def create_cross_validation_sets(data_splits):
    """Create cross validation sets from data splits."""
    cv_sets = []
    n_splits = len(data_splits)
    for i in range(n_splits):
        test_set = data_splits[i]
        train_set = [item for s in range(n_splits) if s != i for item in data_splits[s]]
        cv_sets.append((train_set, test_set))
    return cv_sets

if __name__ == "__main__":
    input_file = 'APPT_ORI_COMPASS.jsonl'  # 替换为你的输入jsonl文件路径
    
    data = load_jsonl(input_file)
    data_splits = split_data(data, n_splits=5)
    cv_sets = create_cross_validation_sets(data_splits)
    
    for i, (train_set, test_set) in enumerate(cv_sets):
        train_file = f'train_fold_{i+1}.jsonl'
        test_file = f'test_fold_{i+1}.jsonl'
        save_jsonl(train_set, train_file)
        save_jsonl(test_set, test_file)
        print(f"Training set {i+1} has been saved to {train_file}")
        print(f"Testing set {i+1} has been saved to {test_file}")
