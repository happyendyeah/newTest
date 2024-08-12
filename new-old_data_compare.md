### 对照实验

- 使用旧数据与新数据进行对比试验
- 旧数据为ly dataset中New2000T数据集，包含2268条数据，应该与2274条数据同源。
- 新数据为hhc提供的2274条数据处理而来。

本次实验主要探究当前实验与之前实验结果差异的原因。
差异主要包括：

1. 之前实验在没有DACL时Accu为83，而当前实验为87
2. 之前实验在有DACL之后Accu为88，而当前实验为87
3. 当前实验在有无DACL上表现差异不大

设计实验主要包括
1. new_data: DACL, DA, CL, ori(之前已有结果)
2. old_data: DACL, DA, CL, ori
> new_data在跑DA时，数据为包含规则0的所有扩增结果

#### new_data-DACL
```
Best Epoch Results:
Round 1 - Best Epoch 32 : {'accuracy': 0.8945, 'precision': 0.8864, 'recall': 0.8945, 'f1': 0.8904, 'auc': 0.9157}
Round 2 - Best Epoch 27 : {'accuracy': 0.8681, 'precision': 0.8381, 'recall': 0.9119, 'f1': 0.8734, 'auc': 0.9017}
Round 3 - Best Epoch 49 : {'accuracy': 0.8945, 'precision': 0.8974, 'recall': 0.8974, 'f1': 0.8974, 'auc': 0.9245}
Round 4 - Best Epoch 32 : {'accuracy': 0.8769, 'precision': 0.8525, 'recall': 0.8852, 'f1': 0.8685, 'auc': 0.9335}
Round 5 - Best Epoch 47 : {'accuracy': 0.8744, 'precision': 0.8448, 'recall': 0.9032, 'f1': 0.8731, 'auc': 0.9166}

Early Stop Epoch Results:
Round 1 - Early Epoch 17 : {'accuracy': 0.8901, 'precision': 0.8889, 'recall': 0.8807, 'f1': 0.8848, 'auc': 0.918}
Round 2 - Early Epoch 12 : {'accuracy': 0.8505, 'precision': 0.8472, 'recall': 0.8546, 'f1': 0.8509, 'auc': 0.9107}
Round 3 - Early Epoch 14 : {'accuracy': 0.8747, 'precision': 0.8831, 'recall': 0.8718, 'f1': 0.8774, 'auc': 0.9405}
Round 4 - Early Epoch 20 : {'accuracy': 0.8637, 'precision': 0.8387, 'recall': 0.8708, 'f1': 0.8545, 'auc': 0.9324}
Round 5 - Early Epoch 18 : {'accuracy': 0.8568, 'precision': 0.8363, 'recall': 0.871, 'f1': 0.8533, 'auc': 0.9143}

Average Best Metrics: {'accuracy': 0.8817, 'precision': 0.8638, 'recall': 0.8984, 'f1': 0.8806, 'auc': 0.9184}
Average Early Metrics: {'accuracy': 0.8672, 'precision': 0.8588, 'recall': 0.8698, 'f1': 0.8642, 'auc': 0.9232}
```

#### new_data-DA
```

```

#### new_data-CL
```
Best Epoch Results:
Round 1 - Best Epoch 20 : {'accuracy': 0.8747, 'precision': 0.8815, 'recall': 0.8532, 'f1': 0.8671, 'auc': 0.9258}
Round 2 - Best Epoch 26 : {'accuracy': 0.8549, 'precision': 0.8515, 'recall': 0.859, 'f1': 0.8553, 'auc': 0.9182}
Round 3 - Best Epoch 41 : {'accuracy': 0.8769, 'precision': 0.8803, 'recall': 0.8803, 'f1': 0.8803, 'auc': 0.9333}
Round 4 - Best Epoch 24 : {'accuracy': 0.8659, 'precision': 0.8524, 'recall': 0.8565, 'f1': 0.8544, 'auc': 0.9251}
Round 5 - Best Epoch 37 : {'accuracy': 0.8524, 'precision': 0.8348, 'recall': 0.8618, 'f1': 0.8481, 'auc': 0.9091}

Early Stop Epoch Results:
Round 1 - Early Epoch 15 : {'accuracy': 0.8571, 'precision': 0.84, 'recall': 0.867, 'f1': 0.8533, 'auc': 0.9168}
Round 2 - Early Epoch 18 : {'accuracy': 0.8484, 'precision': 0.8465, 'recall': 0.8502, 'f1': 0.8484, 'auc': 0.9052}
Round 3 - Early Epoch 17 : {'accuracy': 0.8659, 'precision': 0.8914, 'recall': 0.8419, 'f1': 0.8659, 'auc': 0.9326}
Round 4 - Early Epoch 17 : {'accuracy': 0.8462, 'precision': 0.8325, 'recall': 0.8325, 'f1': 0.8325, 'auc': 0.912}
Round 5 - Early Epoch 19 : {'accuracy': 0.8436, 'precision': 0.8349, 'recall': 0.8387, 'f1': 0.8368, 'auc': 0.8962}

Average Best Metrics: {'accuracy': 0.865, 'precision': 0.8601, 'recall': 0.8622, 'f1': 0.861, 'auc': 0.9223}
Average Early Metrics: {'accuracy': 0.8522, 'precision': 0.8491, 'recall': 0.8461, 'f1': 0.8474, 'auc': 0.9126}
```

#### new_data-ori(codebert_ori_bs64)
```
Best Epoch Results:
Round 0 - Best Epoch 9 : {'accuracy': 0.8945, 'precision': 0.8728, 'recall': 0.9128, 'f1': 0.8924, 'auc': 0.9422}
Round 1 - Best Epoch 23 : {'accuracy': 0.9033, 'precision': 0.875, 'recall': 0.9312, 'f1': 0.9022, 'auc': 0.9368}
Round 2 - Best Epoch 20 : {'accuracy': 0.8923, 'precision': 0.8973, 'recall': 0.8855, 'f1': 0.8914, 'auc': 0.919}
Round 3 - Best Epoch 23 : {'accuracy': 0.8857, 'precision': 0.9027, 'recall': 0.8718, 'f1': 0.887, 'auc': 0.9372}
Round 4 - Best Epoch 36 : {'accuracy': 0.8703, 'precision': 0.8947, 'recall': 0.8134, 'f1': 0.8521, 'auc': 0.9299}
Round 5 - Best Epoch 47 : {'accuracy': 0.8568, 'precision': 0.8393, 'recall': 0.8664, 'f1': 0.8526, 'auc': 0.9149}

Early Stop Epoch Results:
Round 0 - Early Epoch 9 : {'accuracy': 0.8945, 'precision': 0.8728, 'recall': 0.9128, 'f1': 0.8924, 'auc': 0.9422}
Round 1 - Early Epoch 12 : {'accuracy': 0.9011, 'precision': 0.8879, 'recall': 0.9083, 'f1': 0.898, 'auc': 0.9283}
Round 2 - Early Epoch 10 : {'accuracy': 0.8813, 'precision': 0.8712, 'recall': 0.8943, 'f1': 0.8826, 'auc': 0.9241}
Round 3 - Early Epoch 10 : {'accuracy': 0.8857, 'precision': 0.8824, 'recall': 0.8974, 'f1': 0.8898, 'auc': 0.9351}
Round 4 - Early Epoch 15 : {'accuracy': 0.8703, 'precision': 0.875, 'recall': 0.8373, 'f1': 0.8557, 'auc': 0.939}
Round 5 - Early Epoch 13 : {'accuracy': 0.8458, 'precision': 0.8326, 'recall': 0.8479, 'f1': 0.8402, 'auc': 0.9112}

Average Best Metrics: {'accuracy': 0.8838, 'precision': 0.8803, 'recall': 0.8802, 'f1': 0.8796, 'auc': 0.93}
Average Early Metrics: {'accuracy': 0.8798, 'precision': 0.8703, 'recall': 0.883, 'f1': 0.8765, 'auc': 0.93}
```

#### old_data-DACL
```
Best Epoch Results:
Round 1 - Best Epoch 17 : {'accuracy': 0.8786, 'precision': 0.8571, 'recall': 0.9, 'f1': 0.878, 'auc': 0.9169}
Round 2 - Best Epoch 44 : {'accuracy': 0.8764, 'precision': 0.8796, 'recall': 0.8636, 'f1': 0.8716, 'auc': 0.9307}
Round 3 - Best Epoch 33 : {'accuracy': 0.8769, 'precision': 0.8541, 'recall': 0.9005, 'f1': 0.8767, 'auc': 0.9276}
Round 4 - Best Epoch 34 : {'accuracy': 0.8414, 'precision': 0.8426, 'recall': 0.8273, 'f1': 0.8349, 'auc': 0.908}
Round 5 - Best Epoch 23 : {'accuracy': 0.8874, 'precision': 0.875, 'recall': 0.895, 'f1': 0.8849, 'auc': 0.9379}

Early Stop Epoch Results:
Round 1 - Early Epoch 17 : {'accuracy': 0.8786, 'precision': 0.8571, 'recall': 0.9, 'f1': 0.878, 'auc': 0.9169}
Round 2 - Early Epoch 16 : {'accuracy': 0.8676, 'precision': 0.8509, 'recall': 0.8818, 'f1': 0.8661, 'auc': 0.9186}
Round 3 - Early Epoch 14 : {'accuracy': 0.8615, 'precision': 0.8465, 'recall': 0.8733, 'f1': 0.8597, 'auc': 0.9244}
Round 4 - Early Epoch 17 : {'accuracy': 0.8348, 'precision': 0.8404, 'recall': 0.8136, 'f1': 0.8268, 'auc': 0.9128}
Round 5 - Early Epoch 17 : {'accuracy': 0.8874, 'precision': 0.8621, 'recall': 0.9132, 'f1': 0.8869, 'auc': 0.9354}

Average Best Metrics: {'accuracy': 0.8721, 'precision': 0.8617, 'recall': 0.8773, 'f1': 0.8692, 'auc': 0.9242}
Average Early Metrics: {'accuracy': 0.866, 'precision': 0.8514, 'recall': 0.8764, 'f1': 0.8635, 'auc': 0.9216}
```

#### old_data-DA
```
Best Epoch Results:
Round 0 - Best Epoch 4 : {'accuracy': 0.8742, 'precision': 0.8382, 'recall': 0.9182, 'f1': 0.8764, 'auc': 0.9294}
Round 1 - Best Epoch 15 : {'accuracy': 0.8896, 'precision': 0.8795, 'recall': 0.8955, 'f1': 0.8874, 'auc': 0.9218}
Round 2 - Best Epoch 28 : {'accuracy': 0.8852, 'precision': 0.8925, 'recall': 0.8682, 'f1': 0.8802, 'auc': 0.932}
Round 3 - Best Epoch 14 : {'accuracy': 0.8967, 'precision': 0.8718, 'recall': 0.9231, 'f1': 0.8967, 'auc': 0.9451}
Round 4 - Best Epoch 5 : {'accuracy': 0.8962, 'precision': 0.8909, 'recall': 0.895, 'f1': 0.8929, 'auc': 0.9453}
Round 5 - Best Epoch 20 : {'accuracy': 0.8962, 'precision': 0.8839, 'recall': 0.9041, 'f1': 0.8939, 'auc': 0.9463}

Early Stop Epoch Results:
Round 0 - Early Epoch 4 : {'accuracy': 0.8742, 'precision': 0.8382, 'recall': 0.9182, 'f1': 0.8764, 'auc': 0.9294}
Round 1 - Early Epoch 12 : {'accuracy': 0.8742, 'precision': 0.8721, 'recall': 0.8682, 'f1': 0.8702, 'auc': 0.91}
Round 2 - Early Epoch 10 : {'accuracy': 0.8852, 'precision': 0.8962, 'recall': 0.8636, 'f1': 0.8796, 'auc': 0.928}
Round 3 - Early Epoch 11 : {'accuracy': 0.8835, 'precision': 0.8559, 'recall': 0.914, 'f1': 0.884, 'auc': 0.9405}
Round 4 - Early Epoch 13 : {'accuracy': 0.8634, 'precision': 0.8762, 'recall': 0.8364, 'f1': 0.8558, 'auc': 0.906}
Round 5 - Early Epoch 10 : {'accuracy': 0.8852, 'precision': 0.8884, 'recall': 0.8721, 'f1': 0.8802, 'auc': 0.9509}

Average Best Metrics: {'accuracy': 0.8897, 'precision': 0.8761, 'recall': 0.9007, 'f1': 0.8879, 'auc': 0.9367}
Average Early Metrics: {'accuracy': 0.8776, 'precision': 0.8712, 'recall': 0.8788, 'f1': 0.8744, 'auc': 0.9275}
```

#### old_data-CL
```
Best Epoch Results:
Round 1 - Best Epoch 48 : {'accuracy': 0.9007, 'precision': 0.8924, 'recall': 0.9045, 'f1': 0.8984, 'auc': 0.9399}
Round 2 - Best Epoch 20 : {'accuracy': 0.8698, 'precision': 0.8676, 'recall': 0.8636, 'f1': 0.8656, 'auc': 0.9303}
Round 3 - Best Epoch 39 : {'accuracy': 0.8747, 'precision': 0.8694, 'recall': 0.8733, 'f1': 0.8713, 'auc': 0.9255}
Round 4 - Best Epoch 45 : {'accuracy': 0.8414, 'precision': 0.8491, 'recall': 0.8182, 'f1': 0.8333, 'auc': 0.9112}
Round 5 - Best Epoch 31 : {'accuracy': 0.894, 'precision': 0.8869, 'recall': 0.895, 'f1': 0.8909, 'auc': 0.94}

Early Stop Epoch Results:
Round 1 - Early Epoch 15 : {'accuracy': 0.8587, 'precision': 0.8, 'recall': 0.9455, 'f1': 0.8667, 'auc': 0.9191}
Round 2 - Early Epoch 20 : {'accuracy': 0.8698, 'precision': 0.8676, 'recall': 0.8636, 'f1': 0.8656, 'auc': 0.9303}
Round 3 - Early Epoch 16 : {'accuracy': 0.8593, 'precision': 0.8428, 'recall': 0.8733, 'f1': 0.8578, 'auc': 0.9285}
Round 4 - Early Epoch 12 : {'accuracy': 0.804, 'precision': 0.7718, 'recall': 0.8455, 'f1': 0.8069, 'auc': 0.8777}
Round 5 - Early Epoch 23 : {'accuracy': 0.8896, 'precision': 0.8894, 'recall': 0.8813, 'f1': 0.8853, 'auc': 0.9411}

Average Best Metrics: {'accuracy': 0.8761, 'precision': 0.8731, 'recall': 0.8709, 'f1': 0.8719, 'auc': 0.9294}
Average Early Metrics: {'accuracy': 0.8563, 'precision': 0.8343, 'recall': 0.8818, 'f1': 0.8565, 'auc': 0.9193}
```

#### old_data-ori
```
Best Epoch Results:
Round 0 - Best Epoch 5 : {'accuracy': 0.8786, 'precision': 0.8541, 'recall': 0.9045, 'f1': 0.8786, 'auc': 0.9353}
Round 1 - Best Epoch 32 : {'accuracy': 0.8962, 'precision': 0.8879, 'recall': 0.9, 'f1': 0.8939, 'auc': 0.9311}
Round 2 - Best Epoch 8 : {'accuracy': 0.8813, 'precision': 0.8523, 'recall': 0.914, 'f1': 0.8821, 'auc': 0.9379}
Round 3 - Best Epoch 49 : {'accuracy': 0.8923, 'precision': 0.8909, 'recall': 0.8869, 'f1': 0.8889, 'auc': 0.9293}
Round 4 - Best Epoch 9 : {'accuracy': 0.8874, 'precision': 0.8684, 'recall': 0.9041, 'f1': 0.8859, 'auc': 0.9401}
Round 5 - Best Epoch 39 : {'accuracy': 0.8962, 'precision': 0.8981, 'recall': 0.8858, 'f1': 0.892, 'auc': 0.9525}

Early Stop Epoch Results:
Round 0 - Early Epoch 5 : {'accuracy': 0.8786, 'precision': 0.8541, 'recall': 0.9045, 'f1': 0.8786, 'auc': 0.9353}
Round 1 - Early Epoch 17 : {'accuracy': 0.8918, 'precision': 0.8701, 'recall': 0.9136, 'f1': 0.8914, 'auc': 0.9246}
Round 2 - Early Epoch 10 : {'accuracy': 0.8631, 'precision': 0.8911, 'recall': 0.8182, 'f1': 0.8531, 'auc': 0.9158}
Round 3 - Early Epoch 18 : {'accuracy': 0.8813, 'precision': 0.8778, 'recall': 0.8778, 'f1': 0.8778, 'auc': 0.9297}
Round 4 - Early Epoch 10 : {'accuracy': 0.8502, 'precision': 0.8619, 'recall': 0.8227, 'f1': 0.8419, 'auc': 0.9293}
Round 5 - Early Epoch 10 : {'accuracy': 0.894, 'precision': 0.88, 'recall': 0.9041, 'f1': 0.8919, 'auc': 0.9454}

Average Best Metrics: {'accuracy': 0.8887, 'precision': 0.8753, 'recall': 0.8992, 'f1': 0.8869, 'auc': 0.9377}
Average Early Metrics: {'accuracy': 0.8765, 'precision': 0.8725, 'recall': 0.8735, 'f1': 0.8725, 'auc': 0.93}
```



