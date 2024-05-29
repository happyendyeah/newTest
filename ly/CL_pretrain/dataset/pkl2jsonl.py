import pandas as pd
import json

with open(r"C:\Users\yeren\Desktop\ly\APPA\dataset\data_new_transformed_diff_project\data_new2000T_code_diff_project_test_0.pkl", 'rb') as f:
    train_texts_1, train_texts_2, train_labels = pd.read_pickle(f)

with open(r"C:\Users\yeren\Desktop\ly\APPA\dataset\data_new_transformed_diff_project\data_new2000T_code_diff_project_test_0.jsonl", 'w') as f:
    for i in range(len(train_texts_1)):
        json.dump({"text_1": train_texts_1[i], "text_2": train_texts_2[i], "text_3": train_labels[i]}, f)
        f.write("\n")