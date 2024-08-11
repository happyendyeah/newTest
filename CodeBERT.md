### Setup
分析CodeBERT预训练之后10个epoch（ckpt0~9）模型分别进行微调后的结果，同时计算了考虑所有Epoch最优结果（简称All）以及加入early stop=2（简称ES）之后的最优结果。 微调的数据不包含DA规则一。

All：所有epoch中的最优结果
ES：early stop=2之后的最优结果

parameters: lr=5e-5, bs=32.

### 结论
1. 几乎所有的ckpt上ES的accuracy都比All的低两个点左右
2. All在ckpt0上取得最优结果，accu达到0.8733
3. ES在ckpt2上取得最优结果，accu为0.8562

### ckpt0
```
Best Epoch Results:
Round 1 - Best Epoch 32 : {'accuracy': 0.8989, 'precision': 0.8945, 'recall': 0.8945, 'f1': 0.8945, 'auc': 0.9369}
Round 2 - Best Epoch 33 : {'accuracy': 0.8769, 'precision': 0.8608, 'recall': 0.8987, 'f1': 0.8793, 'auc': 0.925}
Round 3 - Best Epoch 15 : {'accuracy': 0.8681, 'precision': 0.8816, 'recall': 0.859, 'f1': 0.8701, 'auc': 0.928}
Round 4 - Best Epoch 25 : {'accuracy': 0.8703, 'precision': 0.8788, 'recall': 0.8325, 'f1': 0.855, 'auc': 0.9296}
Round 5 - Best Epoch 31 : {'accuracy': 0.8524, 'precision': 0.8378, 'recall': 0.8571, 'f1': 0.8474, 'auc': 0.9036}

Early Stop Epoch Results:
Round 1 - Early Epoch 13 : {'accuracy': 0.8703, 'precision': 0.8472, 'recall': 0.8899, 'f1': 0.868, 'auc': 0.9307}
Round 2 - Early Epoch 12 : {'accuracy': 0.8549, 'precision': 0.8643, 'recall': 0.8414, 'f1': 0.8527, 'auc': 0.9175}
Round 3 - Early Epoch 12 : {'accuracy': 0.8527, 'precision': 0.8353, 'recall': 0.8889, 'f1': 0.8613, 'auc': 0.9252}
Round 4 - Early Epoch 17 : {'accuracy': 0.8615, 'precision': 0.8349, 'recall': 0.8708, 'f1': 0.8525, 'auc': 0.9234}
Round 5 - Early Epoch 14 : {'accuracy': 0.8348, 'precision': 0.8008, 'recall': 0.871, 'f1': 0.8344, 'auc': 0.8791}

Average Best Metrics: {'accuracy': 0.8733, 'precision': 0.8707, 'recall': 0.8684, 'f1': 0.8693, 'auc': 0.9246}
Average Early Metrics: {'accuracy': 0.8548, 'precision': 0.8365, 'recall': 0.8724, 'f1': 0.8538, 'auc': 0.9152}
```

### ckpt1
```
Best Epoch Results:
Round 1 - Best Epoch 36 : {'accuracy': 0.8901, 'precision': 0.8818, 'recall': 0.8899, 'f1': 0.8858, 'auc': 0.9231}
Round 2 - Best Epoch 33 : {'accuracy': 0.8747, 'precision': 0.8542, 'recall': 0.9031, 'f1': 0.8779, 'auc': 0.9118}
Round 3 - Best Epoch 32 : {'accuracy': 0.8857, 'precision': 0.9062, 'recall': 0.8675, 'f1': 0.8865, 'auc': 0.9396}
Round 4 - Best Epoch 19 : {'accuracy': 0.8571, 'precision': 0.8429, 'recall': 0.8469, 'f1': 0.8449, 'auc': 0.9179}
Round 5 - Best Epoch 16 : {'accuracy': 0.8458, 'precision': 0.8128, 'recall': 0.8802, 'f1': 0.8451, 'auc': 0.8991}

Early Stop Epoch Results:
Round 1 - Early Epoch 14 : {'accuracy': 0.8659, 'precision': 0.8618, 'recall': 0.8578, 'f1': 0.8598, 'auc': 0.9091}
Round 2 - Early Epoch 13 : {'accuracy': 0.8418, 'precision': 0.8298, 'recall': 0.859, 'f1': 0.8442, 'auc': 0.8985}
Round 3 - Early Epoch 14 : {'accuracy': 0.8725, 'precision': 0.8577, 'recall': 0.9017, 'f1': 0.8792, 'auc': 0.9285}
Round 4 - Early Epoch 14 : {'accuracy': 0.8527, 'precision': 0.8198, 'recall': 0.8708, 'f1': 0.8445, 'auc': 0.9167}
Round 5 - Early Epoch 13 : {'accuracy': 0.8304, 'precision': 0.8097, 'recall': 0.8433, 'f1': 0.8262, 'auc': 0.8931}

Average Best Metrics: {'accuracy': 0.8707, 'precision': 0.8596, 'recall': 0.8775, 'f1': 0.868, 'auc': 0.9183}
Average Early Metrics: {'accuracy': 0.8527, 'precision': 0.8358, 'recall': 0.8665, 'f1': 0.8508, 'auc': 0.9092}
```

### ckpt2
```
Best Epoch Results:
Round 1 - Best Epoch 19 : {'accuracy': 0.8901, 'precision': 0.8684, 'recall': 0.9083, 'f1': 0.8879, 'auc': 0.9201}
Round 2 - Best Epoch 33 : {'accuracy': 0.8725, 'precision': 0.8722, 'recall': 0.8722, 'f1': 0.8722, 'auc': 0.8955}
Round 3 - Best Epoch 26 : {'accuracy': 0.8725, 'precision': 0.8577, 'recall': 0.9017, 'f1': 0.8792, 'auc': 0.9176}
Round 4 - Best Epoch 31 : {'accuracy': 0.8593, 'precision': 0.8571, 'recall': 0.8325, 'f1': 0.8447, 'auc': 0.9174}
Round 5 - Best Epoch 18 : {'accuracy': 0.8458, 'precision': 0.8296, 'recall': 0.8525, 'f1': 0.8409, 'auc': 0.916}

Early Stop Epoch Results:
Round 1 - Early Epoch 19 : {'accuracy': 0.8901, 'precision': 0.8684, 'recall': 0.9083, 'f1': 0.8879, 'auc': 0.9201}
Round 2 - Early Epoch 15 : {'accuracy': 0.8527, 'precision': 0.8704, 'recall': 0.8282, 'f1': 0.8488, 'auc': 0.9076}
Round 3 - Early Epoch 13 : {'accuracy': 0.8505, 'precision': 0.8673, 'recall': 0.8376, 'f1': 0.8522, 'auc': 0.9219}
Round 4 - Early Epoch 13 : {'accuracy': 0.8484, 'precision': 0.8302, 'recall': 0.8421, 'f1': 0.8361, 'auc': 0.9169}
Round 5 - Early Epoch 15 : {'accuracy': 0.8392, 'precision': 0.8103, 'recall': 0.8664, 'f1': 0.8374, 'auc': 0.9}

Average Best Metrics: {'accuracy': 0.868, 'precision': 0.857, 'recall': 0.8734, 'f1': 0.865, 'auc': 0.9133}
Average Early Metrics: {'accuracy': 0.8562, 'precision': 0.8493, 'recall': 0.8565, 'f1': 0.8525, 'auc': 0.9133}
```

### ckpt3
```
Best Epoch Results:
Round 1 - Best Epoch 28 : {'accuracy': 0.8725, 'precision': 0.854, 'recall': 0.8853, 'f1': 0.8694, 'auc': 0.9126}
Round 2 - Best Epoch 41 : {'accuracy': 0.8615, 'precision': 0.8361, 'recall': 0.8987, 'f1': 0.8662, 'auc': 0.9093}
Round 3 - Best Epoch 21 : {'accuracy': 0.8681, 'precision': 0.885, 'recall': 0.8547, 'f1': 0.8696, 'auc': 0.913}
Round 4 - Best Epoch 16 : {'accuracy': 0.8659, 'precision': 0.8627, 'recall': 0.8421, 'f1': 0.8523, 'auc': 0.9332}
Round 5 - Best Epoch 24 : {'accuracy': 0.8612, 'precision': 0.8438, 'recall': 0.871, 'f1': 0.8571, 'auc': 0.9107}

Early Stop Epoch Results:
Round 1 - Early Epoch 14 : {'accuracy': 0.8396, 'precision': 0.8139, 'recall': 0.8624, 'f1': 0.8374, 'auc': 0.9049}
Round 2 - Early Epoch 12 : {'accuracy': 0.8462, 'precision': 0.8257, 'recall': 0.8767, 'f1': 0.8504, 'auc': 0.9058}
Round 3 - Early Epoch 18 : {'accuracy': 0.8637, 'precision': 0.8675, 'recall': 0.8675, 'f1': 0.8675, 'auc': 0.9233}
Round 4 - Early Epoch 12 : {'accuracy': 0.8549, 'precision': 0.8206, 'recall': 0.8756, 'f1': 0.8472, 'auc': 0.9192}
Round 5 - Early Epoch 12 : {'accuracy': 0.8414, 'precision': 0.8059, 'recall': 0.8802, 'f1': 0.8414, 'auc': 0.9027}

Average Best Metrics: {'accuracy': 0.8658, 'precision': 0.8563, 'recall': 0.8704, 'f1': 0.8629, 'auc': 0.9158}
Average Early Metrics: {'accuracy': 0.8492, 'precision': 0.8267, 'recall': 0.8725, 'f1': 0.8488, 'auc': 0.9112}
```

### ckpt4
```
Best Epoch Results:
Round 1 - Best Epoch 25 : {'accuracy': 0.8747, 'precision': 0.861, 'recall': 0.8807, 'f1': 0.8707, 'auc': 0.917}
Round 2 - Best Epoch 19 : {'accuracy': 0.8571, 'precision': 0.8491, 'recall': 0.8678, 'f1': 0.8584, 'auc': 0.906}
Round 3 - Best Epoch 19 : {'accuracy': 0.8637, 'precision': 0.8707, 'recall': 0.8632, 'f1': 0.867, 'auc': 0.9209}
Round 4 - Best Epoch 31 : {'accuracy': 0.8747, 'precision': 0.88, 'recall': 0.8421, 'f1': 0.8606, 'auc': 0.9257}
Round 5 - Best Epoch 48 : {'accuracy': 0.8612, 'precision': 0.8468, 'recall': 0.8664, 'f1': 0.8565, 'auc': 0.9006}

Early Stop Epoch Results:
Round 1 - Early Epoch 12 : {'accuracy': 0.844, 'precision': 0.8483, 'recall': 0.8211, 'f1': 0.8345, 'auc': 0.9073}
Round 2 - Early Epoch 12 : {'accuracy': 0.822, 'precision': 0.8067, 'recall': 0.8458, 'f1': 0.8258, 'auc': 0.89}
Round 3 - Early Epoch 16 : {'accuracy': 0.8549, 'precision': 0.875, 'recall': 0.8376, 'f1': 0.8559, 'auc': 0.9042}
Round 4 - Early Epoch 14 : {'accuracy': 0.8374, 'precision': 0.8082, 'recall': 0.8469, 'f1': 0.8271, 'auc': 0.9159}
Round 5 - Early Epoch 15 : {'accuracy': 0.837, 'precision': 0.8389, 'recall': 0.8157, 'f1': 0.8271, 'auc': 0.9023}

Average Best Metrics: {'accuracy': 0.8663, 'precision': 0.8615, 'recall': 0.864, 'f1': 0.8626, 'auc': 0.914}
Average Early Metrics: {'accuracy': 0.8391, 'precision': 0.8354, 'recall': 0.8334, 'f1': 0.8341, 'auc': 0.9039}
```

### ckpt5
```
Best Epoch Results:
Round 1 - Best Epoch 25 : {'accuracy': 0.8725, 'precision': 0.8604, 'recall': 0.8761, 'f1': 0.8682, 'auc': 0.9153}
Round 2 - Best Epoch 35 : {'accuracy': 0.8505, 'precision': 0.8326, 'recall': 0.8767, 'f1': 0.8541, 'auc': 0.8961}
Round 3 - Best Epoch 41 : {'accuracy': 0.8747, 'precision': 0.8734, 'recall': 0.8846, 'f1': 0.879, 'auc': 0.9146}
Round 4 - Best Epoch 44 : {'accuracy': 0.8593, 'precision': 0.8222, 'recall': 0.8852, 'f1': 0.8525, 'auc': 0.9081}
Round 5 - Best Epoch 41 : {'accuracy': 0.8678, 'precision': 0.8489, 'recall': 0.8802, 'f1': 0.8643, 'auc': 0.9226}

Early Stop Epoch Results:
Round 1 - Early Epoch 16 : {'accuracy': 0.8571, 'precision': 0.8228, 'recall': 0.8945, 'f1': 0.8571, 'auc': 0.9211}
Round 2 - Early Epoch 13 : {'accuracy': 0.8352, 'precision': 0.804, 'recall': 0.8855, 'f1': 0.8428, 'auc': 0.8999}
Round 3 - Early Epoch 14 : {'accuracy': 0.8549, 'precision': 0.836, 'recall': 0.8932, 'f1': 0.8636, 'auc': 0.9211}
Round 4 - Early Epoch 16 : {'accuracy': 0.8462, 'precision': 0.8263, 'recall': 0.8421, 'f1': 0.8341, 'auc': 0.9142}
Round 5 - Early Epoch 20 : {'accuracy': 0.859, 'precision': 0.8341, 'recall': 0.8802, 'f1': 0.8565, 'auc': 0.9237}

Average Best Metrics: {'accuracy': 0.865, 'precision': 0.8475, 'recall': 0.8806, 'f1': 0.8636, 'auc': 0.9113}
Average Early Metrics: {'accuracy': 0.8505, 'precision': 0.8246, 'recall': 0.8791, 'f1': 0.8508, 'auc': 0.916}
```

### ckpt6
```
Best Epoch Results:
Round 1 - Best Epoch 31 : {'accuracy': 0.8857, 'precision': 0.8807, 'recall': 0.8807, 'f1': 0.8807, 'auc': 0.9112}
Round 2 - Best Epoch 19 : {'accuracy': 0.8725, 'precision': 0.8421, 'recall': 0.9163, 'f1': 0.8776, 'auc': 0.9164}
Round 3 - Best Epoch 23 : {'accuracy': 0.8659, 'precision': 0.865, 'recall': 0.8761, 'f1': 0.8705, 'auc': 0.9052}
Round 4 - Best Epoch 23 : {'accuracy': 0.8637, 'precision': 0.8387, 'recall': 0.8708, 'f1': 0.8545, 'auc': 0.9222}
Round 5 - Best Epoch 30 : {'accuracy': 0.8634, 'precision': 0.8475, 'recall': 0.871, 'f1': 0.8591, 'auc': 0.9164}

Early Stop Epoch Results:
Round 1 - Early Epoch 16 : {'accuracy': 0.8593, 'precision': 0.8407, 'recall': 0.8716, 'f1': 0.8559, 'auc': 0.9135}
Round 2 - Early Epoch 12 : {'accuracy': 0.8396, 'precision': 0.8565, 'recall': 0.815, 'f1': 0.8352, 'auc': 0.9057}
Round 3 - Early Epoch 12 : {'accuracy': 0.844, 'precision': 0.8439, 'recall': 0.8547, 'f1': 0.8493, 'auc': 0.9073}
Round 4 - Early Epoch 13 : {'accuracy': 0.8462, 'precision': 0.7957, 'recall': 0.8947, 'f1': 0.8423, 'auc': 0.9183}
Round 5 - Early Epoch 15 : {'accuracy': 0.8414, 'precision': 0.8008, 'recall': 0.8894, 'f1': 0.8428, 'auc': 0.9093}

Average Best Metrics: {'accuracy': 0.8702, 'precision': 0.8548, 'recall': 0.883, 'f1': 0.8685, 'auc': 0.9143}
Average Early Metrics: {'accuracy': 0.8461, 'precision': 0.8275, 'recall': 0.8651, 'f1': 0.8451, 'auc': 0.9108}
```

### ckpt7
```
Best Epoch Results:
Round 1 - Best Epoch 31 : {'accuracy': 0.8857, 'precision': 0.8705, 'recall': 0.8945, 'f1': 0.8824, 'auc': 0.9184}
Round 2 - Best Epoch 30 : {'accuracy': 0.8637, 'precision': 0.8395, 'recall': 0.8987, 'f1': 0.8681, 'auc': 0.9112}
Round 3 - Best Epoch 29 : {'accuracy': 0.8681, 'precision': 0.8718, 'recall': 0.8718, 'f1': 0.8718, 'auc': 0.9253}
Round 4 - Best Epoch 41 : {'accuracy': 0.8747, 'precision': 0.8551, 'recall': 0.8756, 'f1': 0.8652, 'auc': 0.9329}
Round 5 - Best Epoch 19 : {'accuracy': 0.8656, 'precision': 0.8824, 'recall': 0.8295, 'f1': 0.8551, 'auc': 0.9098}

Early Stop Epoch Results:
Round 1 - Early Epoch 13 : {'accuracy': 0.8484, 'precision': 0.8253, 'recall': 0.867, 'f1': 0.8456, 'auc': 0.9175}
Round 2 - Early Epoch 19 : {'accuracy': 0.8615, 'precision': 0.8417, 'recall': 0.8899, 'f1': 0.8651, 'auc': 0.907}
Round 3 - Early Epoch 14 : {'accuracy': 0.8571, 'precision': 0.8658, 'recall': 0.8547, 'f1': 0.8602, 'auc': 0.9185}
Round 4 - Early Epoch 11 : {'accuracy': 0.811, 'precision': 0.7783, 'recall': 0.823, 'f1': 0.8, 'auc': 0.8841}
Round 5 - Early Epoch 16 : {'accuracy': 0.8568, 'precision': 0.8393, 'recall': 0.8664, 'f1': 0.8526, 'auc': 0.9056}

Average Best Metrics: {'accuracy': 0.8716, 'precision': 0.8639, 'recall': 0.874, 'f1': 0.8685, 'auc': 0.9195}
Average Early Metrics: {'accuracy': 0.847, 'precision': 0.8301, 'recall': 0.8602, 'f1': 0.8447, 'auc': 0.9065}
```

### ckpt8
```
Best Epoch Results:
Round 1 - Best Epoch 45 : {'accuracy': 0.8813, 'precision': 0.8761, 'recall': 0.8761, 'f1': 0.8761, 'auc': 0.924}
Round 2 - Best Epoch 20 : {'accuracy': 0.8637, 'precision': 0.8511, 'recall': 0.8811, 'f1': 0.8658, 'auc': 0.9116}
Round 3 - Best Epoch 32 : {'accuracy': 0.8681, 'precision': 0.8655, 'recall': 0.8803, 'f1': 0.8729, 'auc': 0.9348}
Round 4 - Best Epoch 32 : {'accuracy': 0.8549, 'precision': 0.8357, 'recall': 0.8517, 'f1': 0.8436, 'auc': 0.9274}
Round 5 - Best Epoch 36 : {'accuracy': 0.859, 'precision': 0.843, 'recall': 0.8664, 'f1': 0.8545, 'auc': 0.9064}

Early Stop Epoch Results:
Round 1 - Early Epoch 15 : {'accuracy': 0.8747, 'precision': 0.8578, 'recall': 0.8853, 'f1': 0.8713, 'auc': 0.9316}
Round 2 - Early Epoch 14 : {'accuracy': 0.8308, 'precision': 0.8049, 'recall': 0.8722, 'f1': 0.8372, 'auc': 0.8989}
Round 3 - Early Epoch 13 : {'accuracy': 0.8484, 'precision': 0.834, 'recall': 0.8803, 'f1': 0.8565, 'auc': 0.9172}
Round 4 - Early Epoch 13 : {'accuracy': 0.8286, 'precision': 0.8104, 'recall': 0.8182, 'f1': 0.8143, 'auc': 0.8944}
Round 5 - Early Epoch 13 : {'accuracy': 0.837, 'precision': 0.8357, 'recall': 0.8203, 'f1': 0.8279, 'auc': 0.8988}

Average Best Metrics: {'accuracy': 0.8654, 'precision': 0.8543, 'recall': 0.8711, 'f1': 0.8626, 'auc': 0.9208}
Average Early Metrics: {'accuracy': 0.8439, 'precision': 0.8286, 'recall': 0.8553, 'f1': 0.8414, 'auc': 0.9082}
```

### ckpt9
```
Best Epoch Results:
Round 1 - Best Epoch 26 : {'accuracy': 0.8967, 'precision': 0.8869, 'recall': 0.8991, 'f1': 0.8929, 'auc': 0.9234}
Round 2 - Best Epoch 36 : {'accuracy': 0.8659, 'precision': 0.8402, 'recall': 0.9031, 'f1': 0.8705, 'auc': 0.9011}
Round 3 - Best Epoch 16 : {'accuracy': 0.8791, 'precision': 0.8776, 'recall': 0.8889, 'f1': 0.8832, 'auc': 0.929}
Round 4 - Best Epoch 36 : {'accuracy': 0.8549, 'precision': 0.8295, 'recall': 0.8612, 'f1': 0.8451, 'auc': 0.9175}
Round 5 - Best Epoch 23 : {'accuracy': 0.8436, 'precision': 0.8288, 'recall': 0.8479, 'f1': 0.8383, 'auc': 0.8972}

Early Stop Epoch Results:
Round 1 - Early Epoch 13 : {'accuracy': 0.8462, 'precision': 0.8304, 'recall': 0.8532, 'f1': 0.8416, 'auc': 0.9156}
Round 2 - Early Epoch 13 : {'accuracy': 0.8396, 'precision': 0.8632, 'recall': 0.8062, 'f1': 0.8337, 'auc': 0.9034}
Round 3 - Early Epoch 13 : {'accuracy': 0.8593, 'precision': 0.8829, 'recall': 0.8376, 'f1': 0.8596, 'auc': 0.9294}
Round 4 - Early Epoch 12 : {'accuracy': 0.8462, 'precision': 0.8062, 'recall': 0.8756, 'f1': 0.8395, 'auc': 0.9017}
Round 5 - Early Epoch 14 : {'accuracy': 0.8216, 'precision': 0.8036, 'recall': 0.8295, 'f1': 0.8163, 'auc': 0.8907}

Average Best Metrics: {'accuracy': 0.868, 'precision': 0.8526, 'recall': 0.88, 'f1': 0.866, 'auc': 0.9136}
Average Early Metrics: {'accuracy': 0.8426, 'precision': 0.8373, 'recall': 0.8404, 'f1': 0.8381, 'auc': 0.9082}
```
