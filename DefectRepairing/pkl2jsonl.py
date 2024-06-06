import pandas as pd
import json

buggy_code = []
fixed_code = []
labels = []
# for i in range(5):
#     with open(rf"C:\Users\yeren\Desktop\ly\APPA\dataset\New2000T\data_new2000T_code_train_{str(i)}.pkl", 'rb') as f:
#         train_texts_1, train_texts_2, train_labels = pd.read_pickle(f)
#         buggy_code.extend(train_texts_1)
#         fixed_code.extend(train_texts_2)
#         labels.extend(train_labels)

#     # with open(rf"C:\Users\yeren\Desktop\ly\APPA\dataset\New2000T\data_new2000T_code_train_{str(i)}.jsonl", 'w') as f:
#     #     for i in range(len(train_texts_1)):
#     #         json.dump({"buggy_code": train_texts_1[i], "fixed_code": train_texts_2[i], "label": train_labels[i]}, f)
#     #         f.write("\n")

# with open(rf"C:\Users\yeren\Desktop\ly\APPA\dataset\New2000T\data_new2000T_code.jsonl", 'w') as f:
#     for i in range(len(buggy_code)):
#         json.dump({"buggy_code": buggy_code[i], "fixed_code": fixed_code[i], "label": labels[i]}, f)
#         f.write("\n")

path = r"C:\Users\yeren\Desktop\DefectRepairing\train.pkl"

with open(path, 'rb') as f:
    train_texts_1 = pd.read_pickle(f)

with open(path[:-3]+"jsonl", 'w') as f:
    for i in range(len(train_texts_1)):
        json.dump(train_texts_1[i], f)
        f.write("\n")