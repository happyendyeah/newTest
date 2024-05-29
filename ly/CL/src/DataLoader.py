from torch.utils.data import Dataset
import torch


def remove_context(buggy_code, fixed_code):
    buggy_code = buggy_code.strip().split(" ")
    fixed_code = fixed_code.strip().split(" ")
    length1 = len(buggy_code)
    length2 = len(fixed_code)
    offset_head = 0
    offset_tail = 0
    while offset_head < min(length1, length2):
        if buggy_code[offset_head] == fixed_code[offset_head]:
            offset_head += 1
        else:
            break
    while offset_tail < min(length1, length2):
        if buggy_code[length1 - 1 - offset_tail] == fixed_code[length2 - 1 - offset_tail]:
            offset_tail += 1
        else:
            break
    s1 = ""
    s2 = ""
    if offset_head + offset_tail < length1:
        s1 = ' '.join(buggy_code[offset_head:length1 - offset_tail]).strip()
    if offset_head + offset_tail < length2:
        s2 = ' '.join(fixed_code[offset_head:length2 - offset_tail]).strip()
    return s1, s2


class MyDataset(Dataset):
    def __init__(self, func, tokenizer, max_length, texts_1, texts_2, texts_3):
        self.tokenizer = tokenizer
        self.func = func
        self.max_length = max_length
        self.texts_1 = texts_1
        self.texts_2 = texts_2
        self.texts_3 = texts_3

    def _encode(self, text):
        return self.func(text, self.tokenizer, self.max_length)

    def __getitem__(self, idx):
        text_1 = self.texts_1[idx]
        text_2 = self.texts_2[idx]
        text_3 = self.texts_3[idx]
        encoding_1 = self._encode(text_1)
        encoding_2 = self._encode(text_2)
        encoding_3 = self._encode(text_3)

        item = dict()
        for key, val in encoding_1.items():
            if key.startswith("token_type_ids"):
                continue
            item[key + '_1'] = torch.tensor(val)
        for key, val in encoding_2.items():
            if key.startswith("token_type_ids"):
                continue
            item[key + '_2'] = torch.tensor(val)
        for key, val in encoding_3.items():
            if key.startswith("token_type_ids"):
                continue
            item[key + '_3'] = torch.tensor(val)
        return item

    def __len__(self):
        return len(self.texts_1)
