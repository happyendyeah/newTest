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

### 外加CodeBERT在两个数据集上的表现，均为同一代码运行

#### diff
```
Best Epoch Results:
Round 1 - Best Epoch 23 : {'accuracy': 0.9033, 'precision': 0.875, 'recall': 0.9312, 'f1': 0.9022, 'auc': 0.9368}
Round 2 - Best Epoch 20 : {'accuracy': 0.8923, 'precision': 0.8973, 'recall': 0.8855, 'f1': 0.8914, 'auc': 0.919}
Round 3 - Best Epoch 23 : {'accuracy': 0.8857, 'precision': 0.9027, 'recall': 0.8718, 'f1': 0.887, 'auc': 0.9372}
Round 4 - Best Epoch 36 : {'accuracy': 0.8703, 'precision': 0.8947, 'recall': 0.8134, 'f1': 0.8521, 'auc': 0.9299}
Round 5 - Best Epoch 6 : {'accuracy': 0.859, 'precision': 0.8341, 'recall': 0.8802, 'f1': 0.8565, 'auc': 0.9183}

Early Stop Epoch Results:
Round 1 - Early Epoch 9 : {'accuracy': 0.8945, 'precision': 0.8728, 'recall': 0.9128, 'f1': 0.8924, 'auc': 0.9422}
Round 2 - Early Epoch 10 : {'accuracy': 0.8813, 'precision': 0.8712, 'recall': 0.8943, 'f1': 0.8826, 'auc': 0.9241}
Round 3 - Early Epoch 10 : {'accuracy': 0.8857, 'precision': 0.8824, 'recall': 0.8974, 'f1': 0.8898, 'auc': 0.9351}
Round 4 - Early Epoch 8 : {'accuracy': 0.8659, 'precision': 0.8854, 'recall': 0.8134, 'f1': 0.8479, 'auc': 0.9295}
Round 5 - Early Epoch 6 : {'accuracy': 0.859, 'precision': 0.8341, 'recall': 0.8802, 'f1': 0.8565, 'auc': 0.9183}

Average Best Metrics: {'accuracy': 0.8821, 'precision': 0.8808, 'recall': 0.8764, 'f1': 0.8778, 'auc': 0.9282}
Average Early Metrics: {'accuracy': 0.8773, 'precision': 0.8692, 'recall': 0.8796, 'f1': 0.8738, 'auc': 0.9298}
```

#### full
```
Best Epoch Results:
Round 1 - Best Epoch 22 : {'accuracy': 0.8355, 'precision': 0.834, 'recall': 0.8448, 'f1': 0.8394, 'auc': 0.8793}
Round 2 - Best Epoch 18 : {'accuracy': 0.8355, 'precision': 0.8112, 'recall': 0.8783, 'f1': 0.8434, 'auc': 0.8762}
Round 3 - Best Epoch 26 : {'accuracy': 0.8154, 'precision': 0.7953, 'recall': 0.8104, 'f1': 0.8028, 'auc': 0.8692}
Round 4 - Best Epoch 24 : {'accuracy': 0.844, 'precision': 0.8296, 'recall': 0.8486, 'f1': 0.839, 'auc': 0.8964}
Round 5 - Best Epoch 22 : {'accuracy': 0.8725, 'precision': 0.8533, 'recall': 0.8848, 'f1': 0.8688, 'auc': 0.9203}

Early Stop Epoch Results:
Round 1 - Early Epoch 5 : {'accuracy': 0.8158, 'precision': 0.8058, 'recall': 0.8405, 'f1': 0.8228, 'auc': 0.894}
Round 2 - Early Epoch 7 : {'accuracy': 0.8289, 'precision': 0.8167, 'recall': 0.8522, 'f1': 0.834, 'auc': 0.8924}
Round 3 - Early Epoch 8 : {'accuracy': 0.7978, 'precision': 0.7742, 'recall': 0.7962, 'f1': 0.785, 'auc': 0.8772}
Round 4 - Early Epoch 5 : {'accuracy': 0.8154, 'precision': 0.7839, 'recall': 0.8486, 'f1': 0.815, 'auc': 0.8902}
Round 5 - Early Epoch 4 : {'accuracy': 0.8527, 'precision': 0.8713, 'recall': 0.8111, 'f1': 0.8401, 'auc': 0.9226}

Average Best Metrics: {'accuracy': 0.8406, 'precision': 0.8247, 'recall': 0.8534, 'f1': 0.8387, 'auc': 0.8883}
Average Early Metrics: {'accuracy': 0.8221, 'precision': 0.8104, 'recall': 0.8297, 'f1': 0.8194, 'auc': 0.8953}
```
