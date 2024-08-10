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

```
