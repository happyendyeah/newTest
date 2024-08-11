### Setup

不加入对比学习预训练，以及微调数据集的增强。

相当于单独只对2274条数据做五倍交叉验证的微调测试，分别测试了两个模型（Bert，CodeBERT）以及两种bs（32，64）下的表现.

#### CodeBERT bs=64
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

#### CodeBERT bs=32
```
Best Epoch Results:
Round 1 - Best Epoch 11 : {'accuracy': 0.8857, 'precision': 0.8578, 'recall': 0.9128, 'f1': 0.8844, 'auc': 0.9294}
Round 2 - Best Epoch 25 : {'accuracy': 0.8769, 'precision': 0.8767, 'recall': 0.8767, 'f1': 0.8767, 'auc': 0.9248}
Round 3 - Best Epoch 20 : {'accuracy': 0.8791, 'precision': 0.9202, 'recall': 0.8376, 'f1': 0.877, 'auc': 0.9474}
Round 4 - Best Epoch 35 : {'accuracy': 0.8747, 'precision': 0.8619, 'recall': 0.866, 'f1': 0.864, 'auc': 0.9193}
Round 5 - Best Epoch 35 : {'accuracy': 0.8678, 'precision': 0.8428, 'recall': 0.8894, 'f1': 0.8655, 'auc': 0.9097}

Early Stop Epoch Results:
Round 1 - Early Epoch 5 : {'accuracy': 0.8791, 'precision': 0.8528, 'recall': 0.9037, 'f1': 0.8775, 'auc': 0.9414}
Round 2 - Early Epoch 4 : {'accuracy': 0.8396, 'precision': 0.8377, 'recall': 0.8414, 'f1': 0.8396, 'auc': 0.9063}
Round 3 - Early Epoch 8 : {'accuracy': 0.8725, 'precision': 0.9037, 'recall': 0.8419, 'f1': 0.8717, 'auc': 0.9404}
Round 4 - Early Epoch 5 : {'accuracy': 0.8637, 'precision': 0.8517, 'recall': 0.8517, 'f1': 0.8517, 'auc': 0.9296}
Round 5 - Early Epoch 7 : {'accuracy': 0.8546, 'precision': 0.8268, 'recall': 0.8802, 'f1': 0.8527, 'auc': 0.9086}

Average Best Metrics: {'accuracy': 0.8768, 'precision': 0.8719, 'recall': 0.8765, 'f1': 0.8735, 'auc': 0.9261}
Average Early Metrics: {'accuracy': 0.8619, 'precision': 0.8545, 'recall': 0.8638, 'f1': 0.8586, 'auc': 0.9253}
```

#### BERT bs=64
```
Best Epoch Results:
Round 1 - Best Epoch 38 : {'accuracy': 0.8637, 'precision': 0.8451, 'recall': 0.8761, 'f1': 0.8604, 'auc': 0.9044}
Round 2 - Best Epoch 29 : {'accuracy': 0.8571, 'precision': 0.8266, 'recall': 0.9031, 'f1': 0.8632, 'auc': 0.9204}
Round 3 - Best Epoch 11 : {'accuracy': 0.8615, 'precision': 0.8577, 'recall': 0.8761, 'f1': 0.8668, 'auc': 0.9221}
Round 4 - Best Epoch 17 : {'accuracy': 0.8681, 'precision': 0.8634, 'recall': 0.8469, 'f1': 0.8551, 'auc': 0.9224}
Round 5 - Best Epoch 21 : {'accuracy': 0.8436, 'precision': 0.812, 'recall': 0.8756, 'f1': 0.8426, 'auc': 0.8836}

Early Stop Epoch Results:
Round 1 - Early Epoch 8 : {'accuracy': 0.8505, 'precision': 0.8289, 'recall': 0.867, 'f1': 0.8475, 'auc': 0.9193}
Round 2 - Early Epoch 5 : {'accuracy': 0.844, 'precision': 0.8421, 'recall': 0.8458, 'f1': 0.844, 'auc': 0.9049}
Round 3 - Early Epoch 6 : {'accuracy': 0.8484, 'precision': 0.8235, 'recall': 0.8974, 'f1': 0.8589, 'auc': 0.9229}
Round 4 - Early Epoch 6 : {'accuracy': 0.8527, 'precision': 0.8008, 'recall': 0.9043, 'f1': 0.8494, 'auc': 0.9208}
Round 5 - Early Epoch 7 : {'accuracy': 0.8238, 'precision': 0.7686, 'recall': 0.9032, 'f1': 0.8305, 'auc': 0.8861}

Average Best Metrics: {'accuracy': 0.8588, 'precision': 0.841, 'recall': 0.8756, 'f1': 0.8576, 'auc': 0.9106}
Average Early Metrics: {'accuracy': 0.8439, 'precision': 0.8128, 'recall': 0.8835, 'f1': 0.8461, 'auc': 0.9108}
```

#### BERT bs=32
```
Best Epoch Results:
Round 1 - Best Epoch 28 : {'accuracy': 0.8593, 'precision': 0.8632, 'recall': 0.8395, 'f1': 0.8512, 'auc': 0.9199}
Round 2 - Best Epoch 47 : {'accuracy': 0.8593, 'precision': 0.8354, 'recall': 0.8943, 'f1': 0.8638, 'auc': 0.899}
Round 3 - Best Epoch 30 : {'accuracy': 0.8659, 'precision': 0.8712, 'recall': 0.8675, 'f1': 0.8694, 'auc': 0.9083}
Round 4 - Best Epoch 16 : {'accuracy': 0.8637, 'precision': 0.8451, 'recall': 0.8612, 'f1': 0.8531, 'auc': 0.9205}
Round 5 - Best Epoch 15 : {'accuracy': 0.8392, 'precision': 0.813, 'recall': 0.8618, 'f1': 0.8367, 'auc': 0.8914}

Early Stop Epoch Results:
Round 1 - Early Epoch 8 : {'accuracy': 0.844, 'precision': 0.8, 'recall': 0.8991, 'f1': 0.8467, 'auc': 0.9081}
Round 2 - Early Epoch 6 : {'accuracy': 0.8396, 'precision': 0.7962, 'recall': 0.9119, 'f1': 0.8501, 'auc': 0.9121}
Round 3 - Early Epoch 11 : {'accuracy': 0.8527, 'precision': 0.8523, 'recall': 0.8632, 'f1': 0.8577, 'auc': 0.9359}
Round 4 - Early Epoch 6 : {'accuracy': 0.8418, 'precision': 0.7665, 'recall': 0.9426, 'f1': 0.8455, 'auc': 0.9143}
Round 5 - Early Epoch 4 : {'accuracy': 0.804, 'precision': 0.8333, 'recall': 0.7373, 'f1': 0.7824, 'auc': 0.8894}

Average Best Metrics: {'accuracy': 0.8575, 'precision': 0.8456, 'recall': 0.8649, 'f1': 0.8548, 'auc': 0.9078}
Average Early Metrics: {'accuracy': 0.8364, 'precision': 0.8097, 'recall': 0.8708, 'f1': 0.8365, 'auc': 0.912}
```

