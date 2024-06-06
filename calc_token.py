import json
import matplotlib.pyplot as plt
from transformers import BertTokenizer

def load_data(jsonl_file):
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data = [json.loads(line) for line in lines]
    return data

def tokenize_data(data, tokenizer):
    lengths_buggy = []
    lengths_fixed = []

    for item in data:
        tokens_buggy = tokenizer.tokenize(item['buggy_code'])
        tokens_fixed = tokenizer.tokenize(item['fixed_code'])
        lengths_buggy.append(len(tokens_buggy))
        lengths_fixed.append(len(tokens_fixed))
    
    return lengths_buggy, lengths_fixed

def calculate_proportions(lengths, thresholds):
    proportions = {}
    for threshold in thresholds:
        count = sum(1 for length in lengths if length < threshold)
        proportions[threshold] = count / len(lengths)
    return proportions

def plot_histogram(lengths_buggy, lengths_fixed):
    plt.figure(figsize=(12, 6))
    plt.hist(lengths_buggy, bins=50, color='blue', alpha=0.7, label='Buggy Code')
    plt.hist(lengths_fixed, bins=50, color='green', alpha=0.7, label='Fixed Code')
    plt.title('Token Length Distribution: Buggy Code vs Fixed Code')
    plt.xlabel('Token Length')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

def main(jsonl_file):
    # Load data from JSONL file
    data = load_data(jsonl_file)
    
    # Load BERT tokenizer
    tokenizer = BertTokenizer.from_pretrained(r'C:\Users\yeren\Desktop\model\bert')
    
    # Tokenize the data
    lengths_buggy, lengths_fixed = tokenize_data(data, tokenizer)
    
    # Calculate proportions for various thresholds
    thresholds = [256, 512, 1024, 2048]
    proportions_buggy = calculate_proportions(lengths_buggy, thresholds)
    proportions_fixed = calculate_proportions(lengths_fixed, thresholds)
    
    print("Proportions for buggy_code:")
    for threshold, proportion in proportions_buggy.items():
        print(f"Tokens < {threshold}: {proportion:.2%}")
        
    print("\nProportions for fixed_code:")
    for threshold, proportion in proportions_fixed.items():
        print(f"Tokens < {threshold}: {proportion:.2%}")

    # Plot histogram
    plot_histogram(lengths_buggy, lengths_fixed)

if __name__ == '__main__':
    main('data_clean.jsonl')
