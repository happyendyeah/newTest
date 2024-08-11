使用codebert的tokenizer进行分割之后对长度进行统计：
```
Proportions for Bug Tokens:
  Less than 512: 48.66%
  Less than 1024: 72.68%
  Less than 2048: 88.89%
Proportions for Fix Tokens:
  Less than 512: 46.60%
  Less than 1024: 71.37%
  Less than 2048: 88.19%
```
可以看出小于512的数据只有不到50%，所以可能存在较差的结果。

### codebert train
#### epoch=50, lr=1e-5, bs=16
```
Average of Best Results Across Folds:
{
    "Accuracy": 83.13,
    "Precision": 82.22,
    "Recall": 83.57,
    "F1": 82.85,
    "AUC": 86.89
}
Best Epoch:39 | Accuracy:83.33%, Precision:81.74%, Recall:84.68%, F1:83.19%, AUC:86.92%
Best Epoch:44 | Accuracy:84.65%, Precision:86.19%, Recall:81.53%, F1:83.8%, AUC:88.27%
Best Epoch:11 | Accuracy:80.66%, Precision:79.3%, Recall:81.45%, F1:80.36%, AUC:83.93%
Best Epoch:20 | Accuracy:85.71%, Precision:85.45%, Recall:85.07%, F1:85.26%, AUC:90.3%
Best Epoch:36 | Accuracy:81.32%, Precision:78.42%, Recall:85.14%, F1:81.64%, AUC:85.02%
```

### transformer_train
#### epoch=50, lr=5e-4
```
Average of Best Results Across Folds:
{
    "Accuracy": 82.21,
    "Precision": 79.19,
    "Recall": 86.19,
    "F1": 82.5,
    "AUC": 88.13
}
Best Epoch:15 | Accuracy:82.46%, Precision:80.87%, Recall:83.78%, F1:82.3%, AUC:89.72%
Best Epoch:22 | Accuracy:81.58%, Precision:76.54%, Recall:89.64%, F1:82.57%, AUC:88.93%
Best Epoch:27 | Accuracy:85.71%, Precision:81.97%, Recall:90.5%, F1:86.02%, AUC:90.45%
Best Epoch:46 | Accuracy:80.0%, Precision:76.64%, Recall:84.62%, F1:80.43%, AUC:85.64%
Best Epoch:35 | Accuracy:81.32%, Precision:79.91%, Recall:82.43%, F1:81.15%, AUC:85.9%
```
#### epoch=50, lr=5e-5
```
Average of Best Results Across Folds:
{
    "Accuracy": 80.37,
    "Precision": 78.36,
    "Recall": 82.58,
    "F1": 80.36,
    "AUC": 86.29
}
Best Epoch:42 | Accuracy:82.24%, Precision:79.25%, Recall:86.04%, F1:82.51%, AUC:88.43%
Best Epoch:28 | Accuracy:80.04%, Precision:81.04%, Recall:77.03%, F1:78.98%, AUC:85.39%
Best Epoch:50 | Accuracy:85.93%, Precision:83.4%, Recall:88.69%, F1:85.96%, AUC:90.34%
Best Epoch:47 | Accuracy:75.82%, Precision:73.82%, Recall:77.83%, F1:75.77%, AUC:82.28%
Best Epoch:44 | Accuracy:77.8%, Precision:74.3%, Recall:83.33%, F1:78.56%, AUC:84.99%
```
#### epoch=100, lr=5e-5
```
Average of Best Results Across Folds:
{
    "Accuracy": 80.28,
    "Precision": 76.68,
    "Recall": 86.01,
    "F1": 80.99,
    "AUC": 86.51
}
Best Epoch:86 | Accuracy:80.26%, Precision:76.61%, Recall:85.59%, F1:80.85%, AUC:87.89%
Best Epoch:58 | Accuracy:79.82%, Precision:75.39%, Recall:86.94%, F1:80.75%, AUC:86.04%
Best Epoch:72 | Accuracy:84.84%, Precision:84.55%, Recall:84.16%, F1:84.35%, AUC:90.56%
Best Epoch:95 | Accuracy:78.02%, Precision:73.54%, Recall:85.52%, F1:79.08%, AUC:83.74%
Best Epoch:91 | Accuracy:78.46%, Precision:73.31%, Recall:87.84%, F1:79.92%, AUC:84.32%
```
