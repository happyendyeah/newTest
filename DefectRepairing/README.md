filter_patches目录中中是Patch_sim中提到的139个patch，经过去重处理后剩余130个，数据如下：
```
Total entries: 139
Unique entries: 130
Number of duplicates: 9
Line numbers: [38, 42] : Patch181 and Patch185
Line numbers: [9, 71] : Patch151 and Patch23
Line numbers: [78, 79] : Patch30 and Patch31
Line numbers: [87, 88] : Patch44 and Patch45
Line numbers: [28, 97] : Patch170 and Patch55
Line numbers: [104, 105] : Patch65 and Patch66
Line numbers: [121, 122] : Patch82 and Patch83
Line numbers: [124, 127] : Patch88 and Patch90
Line numbers: [94, 137] : Patch51 and PatchHDRepair7
```
Patch_sim内容存放在patch_sim.jsonl文件中，去重后的存放在deduplicated_patch_sim.jsonl文件中

new2000T的数据汇总后存放在data_total.jsonl中，共2268个，经过去重处理后剩余2228个，去重后的存放在deduplicated_data.jsonl文件中，数据如下：
```
Total entries: 2268
Unique entries: 2228
Number of duplicates: 37Total entries: 2268
Unique entries: 2228
Number of duplicates: 37
Line numbers: [205, 573]
Line numbers: [71, 629]
......
Line numbers: [872, 2259]
```

在data_total.jsonl中删去patch_sim内容：
```
Total entries in file PatchSim: 130
Total entries in file new2000T: 2228
Repeat in both files: 81
Total entries in both files after deduplicating: 2277
entries in file new2000T after remove PatchSim: 2147
```
result.jsonl中存了2147个数据，当作下一步的训练集。

hhc给了我另一个完整版本的2147数据，在2147_patch文件夹下，但是我使用Patch_Sim的方式进行patch处理后发现其与上述result.jsonl文件中的数据只有600多条相同，其余均不同。

大致查看后发现大概率是由于hhc版本的数据删除了大部分注释，导致数据与result.json文件有所不同。

将hhc版本的数据与patch_sim的130个数据做交集，发现其中有一个重复的内容：
```
Total entries in file PatchSim: 130
Total entries in file hhc: 2147
Repeat in both files: 1
Total entries in both files after deduplicating: 2276
entries in file hhc after remove PatchSim: 2146
repeat content:('k = 1 . 0 / k ; tmp = mu + k * sigma ; if ( tmp < upper ) { upper = ( ( int ) Math . ceil ( tmp ) ) - 1 ; } }', 'k = 1 . 0 / k ; tmp = mu + k * sigma ; if ( tmp < upper ) { tmp = mu + ( k * sigma ) ; } }', 0)
```

跑了四组实验：
1. 使用ly之前的数据new2000T构成的2147条数据为训练集，patch_sim的130条数据为测试集，在CL预训练基础上进行训练，结果如下：
   
   `Accuracy: 0.876923 -- Precision: 0.750000 -- Recall: 0.642857 -- F1: 0.692308 -- AUC: 0.931723`
   
2. 使用ly之前的数据new2000T构成的2147条数据为训练集，patch_sim的130条数据为测试集，直接进行训练，结果如下：
   
   `Accuracy: 0.869231 -- Precision: 0.761905 -- Recall: 0.571429 -- F1: 0.653061 -- AUC: 0.860294`
   
3. 使用hhc提供的原数据，进行diff等处理，构成2147条数据作为训练集（未剔除重复的一条数据），patch_sim的130条数据为测试集，在CL预训练基础上进行训练，结果如下：

   `Accuracy: 0.884615 -- Precision: 0.809524 -- Recall: 0.607143 -- F1: 0.693878 -- AUC: 0.869398`

4. 使用hhc提供的原数据，进行diff等处理，构成2147条数据作为训练集（未剔除重复的一条数据），patch_sim的130条数据为测试集，直接进行训练，结果如下：

   `Accuracy: 0.853846 -- Precision: 0.680000 -- Recall: 0.607143 -- F1: 0.641509 -- AUC: 0.825980`

在处理数据过程中又遇到了一些问题：
hhc给的这个2147数据没有进行去重，去重之后，以及山区与patch_sim重复的一条数据后，剩余2082条数据。
做了DA之后共有8453条数据。
现在正在跑的实验：
1. 使用hhc提供的原数据进行DA扩增，之后进行diff等处理并去重，构成8453条数据作为训练集，patch_sim的130条数据作为测试集，在CL预训练基础上进行训练，结果待更新：
   数据处理存在错误，结果作废。

现在整理了一下手头的数据：
| 数据集名称 | 条数 | 去重后条数 | 去除patchsim条数 | 去除patchsim做DA后的条数| 来源               | 数据格式 |
|-----------|------|-----------|-----------------|-----------|-----------------------|----------|
| new2000T  | 2268 | 2228      | 2147            |  /        | yl处理好的数据集构建而来| 处理好的pkl文件，无法进行筛选等操作|
| 2277      | 2277 | 2205      | 2106            | 10230     | hhc第一次给我的数据集   | 包含buggy.java和fixed.java的完整数据集，可做DA |
| 2146      | 2147 | 2081      | 2081            | 9778      | hhc第二次给我的数据集   | 包含buggy.java和fixed.java的完整数据集，可做DA |
| 2274      | 2274 | 未作去重   | 2172            | 12590     | 2277删除3条数据后的数据集，与论文数据对应 | 与2277相同 |

现在在跑的实验：
1. 2274数据集不做DACL跑patchsim测试集

   `Accuracy: 0.869231 -- Precision: 0.689655 -- Recall: 0.714286 -- F1: 0.701754 -- AUC: 0.887605 `
   
2. 2274数据集做DACL跑patchsim测试集

   `Accuracy: 0.892308 -- Precision: 0.750000 -- Recall: 0.750000 -- F1: 0.750000 -- AUC: 0.914216 `

3. 2274数据集做DACL跑patchsim测试集（只保留Chart，Lang，Math，Time，共7478条数据）

   `Accuracy: 0.892308 -- Precision: 0.733333 -- Recall: 0.785714 -- F1: 0.758621 -- AUC: 0.931022`
