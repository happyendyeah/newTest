import torch.nn.functional as F
import torch
from transformers import AutoModelForMaskedLM,AutoTokenizer
import pandas as pd
from tqdm import tqdm

model = AutoModelForMaskedLM.from_pretrained('bert-base-uncased')
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def predict_words(input_ids, diff_left, diff_right):
    predict = torch.ones(1, len(input_ids[0]))
    count = 0
    for i in range(diff_left, diff_right + 1):
        input_ids_masked = input_ids.clone()
        input_ids_masked[0][i] = 103
        output = model(input_ids_masked)
        prods = F.softmax(output.logits, -1)
        predict[0][i] = prods[0][i][input_ids[0][i]]
        count += 1
    if count == 0:
        count = 1
    predict = -torch.log(predict).sum(1)
    predict = torch.div(predict, count)
    return predict.item()

def predict_diff(text1, text2):
    input_ids_1 = tokenizer(text1, return_tensors="pt")["input_ids"]
    input_ids_2 = tokenizer(text2, return_tensors="pt")["input_ids"]
    len1 = len(input_ids_1[0])
    len2 = len(input_ids_2[0])
    diff_left = 0
    diff_right = 0
    for i in range(min(len1, len2)):
        if input_ids_1[0][i] != input_ids_2[0][i]:
            diff_left = i
            break
    for i in range(min(len1, len2)):
        if input_ids_1[0][len1 - i - 1] != input_ids_2[0][len2 - i - 1]:
            diff_right = len2 - i - 1
            break
    predict = predict_words(input_ids_2, diff_left, diff_right)
    return predict

def classify_threshold(file_path):
    with open(file_path, 'rb') as f:
        texts1, texts2, labels = pd.read_pickle(f)
    predicts_P = []
    predicts_N = []
    for i in tqdm(range(1, len(labels))):
        text1 = texts1[i]
        text2 = texts2[i]
        label = labels[i]
        predict = predict_diff(text1, text2)
        if label == 0:
            predicts_N.append(predict)
        else:
            predicts_P.append(predict)
    threshold = 0
    temp_best_accuracy = 0
    temp_best_f1 = 0
    temp_best_recall = 0
    temp_best_precision = 0
    temp_FP = 0
    temp_FN = 0
    temp_TP = 0
    temp_TN = 0
    temp_best_threshold = 0
    P = len(predicts_P)
    N = len(predicts_N)
    for i in range(1, 1000):
        TP = 0
        TN = 0
        threshold = i / 1000
        for i in predicts_P:
            if predicts_P[i] >= threshold:
                TP += 1
        for i in predicts_N:
            if predicts_N[i] < threshold:
                TN += 1
        FP = P - TP
        FN = N - TN

        accuracy = (TP + TN) / (P + N)
        correct_recall = TP / P
        if FN + TP == 0:
            continue
        precision = TP / (TP + FN)
        if precision + correct_recall == 0:
            continue
        F1 = 2 * precision * correct_recall / (precision + correct_recall)
        if accuracy > temp_best_accuracy:
            temp_best_accuracy = accuracy
            temp_best_f1 = F1
            temp_best_recall = correct_recall
            temp_best_precision = precision
            temp_P = P
            temp_N = N
            temp_TP = TP
            temp_TN = TN
            temp_best_threshold = threshold
    print('TP', temp_TP, 'TN', temp_TN, 'P', temp_P, 'N', temp_N)
    result = {'accuracy': temp_best_accuracy, 'recall': temp_best_recall, 'precision': temp_best_precision,
              'F1': temp_best_f1, 'threshold': temp_best_threshold, 'TP': temp_TP, 'TN': temp_TN, 'P': temp_P, 'N': temp_N}
    print(result)

def log(content):
    with open('./log.txt', 'w') as f:
        f.write(content)



if __name__ == '__main__':
    file_path = './data_code_test_1.pkl'
    classify_threshold(file_path)
