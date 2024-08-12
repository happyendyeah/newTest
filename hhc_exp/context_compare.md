### 比较有无上下文对结果的影响

模型：transformers默认encoder

数据集：无上下文diff拆分数据集（简称diff），有上下文还原后函数级数据集（简称full），采用相同五倍交叉验证分割

参数：lr=5e-4，bs=32

#### diff
```
Average of Best Results Across Folds:
{
    "Accuracy": 82.34,
    "Precision": 80.15,
    "Recall": 84.56,
    "F1": 82.27,
    "AUC": 88.23
}
Best Epoch:37 | Accuracy:82.02%, Precision:80.0%, Recall:86.21%, F1:82.99%, AUC:88.68%
Best Epoch:23 | Accuracy:83.99%, Precision:80.78%, Recall:89.57%, F1:84.95%, AUC:89.03%
Best Epoch:12 | Accuracy:81.54%, Precision:80.09%, Recall:80.09%, F1:80.09%, AUC:87.82%
Best Epoch:40 | Accuracy:80.66%, Precision:79.28%, Recall:80.73%, F1:80.0%, AUC:86.91%
Best Epoch:40 | Accuracy:83.52%, Precision:80.6%, Recall:86.18%, F1:83.3%, AUC:88.68%
```

#### full
```
Average of Best Results Across Folds:
{
    "Accuracy": 81.91,
    "Precision": 77.92,
    "Recall": 87.65,
    "F1": 82.48,
    "AUC": 87.68
}
Best Epoch:22 | Accuracy:80.26%, Precision:75.91%, Recall:89.66%, F1:82.21%, AUC:86.16%
Best Epoch:20 | Accuracy:83.77%, Precision:80.0%, Recall:90.43%, F1:84.9%, AUC:89.21%
Best Epoch:45 | Accuracy:80.44%, Precision:76.07%, Recall:84.36%, F1:80.0%, AUC:86.4%
Best Epoch:22 | Accuracy:80.22%, Precision:76.02%, Recall:85.78%, F1:80.6%, AUC:85.64%
Best Epoch:38 | Accuracy:84.84%, Precision:81.62%, Recall:88.02%, F1:84.7%, AUC:91.01%
```
