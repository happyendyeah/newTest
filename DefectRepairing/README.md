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