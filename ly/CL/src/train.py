import numpy as np
from transformers import AutoTokenizer, AdamW
from torch.utils.data import DataLoader
import torch
import os
import shutil
from pathlib import Path
import numpy as np
from torch import nn, Tensor
import torch.nn.functional as F
from tqdm import tqdm
from DataLoader import MyDataset
from Model import Model
from test import test
from configs import Config
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_curve, auc, accuracy_score, recall_score, precision_score

temperature = 10
tau1 = 1
tau2 = 1

def tokenizer_head_tail(text, tokenizer, max_length):
    encoding = tokenizer(text, padding=True)
    if len(encoding['input_ids']) > max_length:
        half_length = int(max_length / 2)
        encoding['input_ids'] = encoding['input_ids'][:half_length] + encoding['input_ids'][-half_length:]
        #        encoding['token_type_ids'] = encoding['token_type_ids'][:half_length] + encoding['token_type_ids'][-half_length:]
        encoding['attention_mask'] = encoding['attention_mask'][:half_length] + encoding['attention_mask'][
                                                                                -half_length:]
        # encoding.pop('token_type_ids')
    else:
        encoding['input_ids'] = encoding['input_ids'] + [0 for i in range(len(encoding['input_ids']), max_length)]
        encoding['attention_mask'] = encoding['attention_mask'] + [0 for i in
                                                                   range(len(encoding['attention_mask']), max_length)]
        # encoding.pop('token_type_ids')
    return encoding


def tokenizer_head(text, tokenizer, max_legnth):
    encoding = tokenizer(text, padding=True)
    if len(encoding['input_ids']) > max_legnth:
        encoding['input_ids'] = encoding['input_ids'][:max_legnth - 1] + encoding['input_ids'][-1:]
        #        encoding['token_type_ids'] = encoding['token_type_ids'][:max_legnth-1] + encoding['token_type_ids'][-1:]
        encoding['attention_mask'] = encoding['attention_mask'][:max_legnth - 1] + encoding['attention_mask'][-1:]
        # encoding.pop('token_type_ids')
    else:
        encoding['input_ids'] = encoding['input_ids'] + [0 for i in range(len(encoding['input_ids']), max_length)]
        encoding['attention_mask'] = encoding['attention_mask'] + [0 for i in
                                                                   range(len(encoding['attention_mask']), max_length)]
        # encoding.pop('token_type_ids')
    return encoding


def tokenizer_tail(text, tokenizer, max_legnth):
    encoding = tokenizer(text, padding=True)
    if len(encoding['input_ids']) > max_legnth:
        encoding['input_ids'] = encoding['input_ids'][:1] + encoding['input_ids'][-max_legnth + 1:]
        #        encoding['token_type_ids'] = encoding['token_type_ids'][:max_legnth-1] + encoding['token_type_ids'][-1:]
        encoding['attention_mask'] = encoding['attention_mask'][:1] + encoding['attention_mask'][-max_legnth + 1:]
        # encoding.pop('token_type_ids')
    else:
        encoding['input_ids'] = encoding['input_ids'] + [0 for i in range(len(encoding['input_ids']), max_length)]
        encoding['attention_mask'] = encoding['attention_mask'] + [0 for i in
                                                                   range(len(encoding['attention_mask']), max_length)]
        # encoding.pop('token_type_ids')
    return encoding

def tokenizer_mid(text, tokenizer, max_legnth):
    encoding = tokenizer(text, padding=True)
    if len(encoding['input_ids']) > max_legnth:
        encoding['input_ids'] = encoding['input_ids'][(len(encoding['input_ids']) - max_length) // 2: (len(encoding['input_ids']) + max_length) // 2]
        #        encoding['token_type_ids'] = encoding['token_type_ids'][:max_legnth-1] + encoding['token_type_ids'][-1:]
        encoding['attention_mask'] = encoding['attention_mask'][(len(encoding['input_ids']) - max_length) // 2: (len(encoding['input_ids']) + max_length) // 2]
        # encoding.pop('token_type_ids')
    else:
        encoding['input_ids'] = encoding['input_ids'] + [0 for i in range(len(encoding['input_ids']), max_length)]
        encoding['attention_mask'] = encoding['attention_mask'] + [0 for i in
                                                                   range(len(encoding['attention_mask']), max_length)]
        # encoding.pop('token_type_ids')
    return encoding


def save(model, optimizer, PATH, index):
    # 先删除文件夹，再新建文件夹，可以起到清空的作用
    if os.path.exists(PATH):
        shutil.rmtree(PATH)
    os.makedirs(PATH)
    # 保存模型参数
    torch.save({
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': optimizer.state_dict()
    }, os.path.join(PATH, 'checkpoint' + str(index)))
    print("保存模型参数")


def load(model, PATH, index):
    checkpoint = torch.load(os.path.join(PATH, 'checkpoint' + str(index)))
    model.module.load_state_dict(checkpoint['model_state_dict'])
    print("从checkpoint" + str(index) + "加载模型成功")
    return model


def train(model, train_loader, test_loader, optim, loss_function, max_epoch, start_epoch, data_id):
    mac_acc = 0
    print('-------------- start training ---------------', '\n')
    for epoch in range(max_epoch):
        # 从start_epoch开始
        if epoch < start_epoch:
            continue
        print("========= epoch:", epoch, '==============')
        step = 0
        losses = []
        model.train()
        for batch in train_loader:
            step += 1
#            if step == 37:
#                continue
            # 清空优化器
            optim.zero_grad()

            input_ids_1 = batch['input_ids_1'].to(device)
            attention_mask_1 = batch['attention_mask_1'].to(device)
            input_ids_2 = batch['input_ids_2'].to(device)
            attention_mask_2 = batch['attention_mask_2'].to(device)
            input_ids_3 = batch['input_ids_3'].to(device)
            attention_mask_3 = batch['attention_mask_3'].to(device)
            # 将数据输入模型，计算loss
            # [bs, 768]
            vec1, vec2, vec3 = model(input_ids_1, attention_mask_1, input_ids_2, attention_mask_2, input_ids_3, attention_mask_3)
            # [bs]
#            con_positive = (F.cosine_similarity(vec1, vec2) + 0.00001) * temperature
#            con_negative = (F.cosine_similarity(vec1, vec3) + 0.00001) * temperature
#            con_loss = -torch.nn.LogSoftmax(dim=0)(con_positive / (con_positive + con_negative))
            con_loss = 2 - F.cosine_similarity(vec1, vec2) * tau1 + F.cosine_similarity(vec1, vec3) * tau2
            # num
            con_loss = torch.mean(con_loss, dim=0)
            loss = con_loss
            print('[', step, '/', len(train_loader), ']', "loss:", format(loss.item(), '.3f'))
            losses.append(loss.item())
            # 反向传播
            loss.backward()
            optim.step()
        # 输出本次epoch的loss均值
        tr_loss = np.mean(losses)
        # test(model,test_loader,device=config.device)

        # 验证
#        model.eval()
        cos_right = []
        cos_wrong = []
        with torch.no_grad():
            for batch in test_loader:

                input_ids_1 = batch['input_ids_1'].to(device)
                attention_mask_1 = batch['attention_mask_1'].to(device)
                input_ids_2 = batch['input_ids_2'].to(device)
                attention_mask_2 = batch['attention_mask_2'].to(device)
                input_ids_3 = batch['input_ids_3'].to(device)
                attention_mask_3 = batch['attention_mask_3'].to(device)
                # 将数据输入模型，计算loss
                vec1, vec2, vec3 = model(input_ids_1, attention_mask_1, input_ids_2, attention_mask_2, input_ids_3, attention_mask_3)
                cos_right.append(F.cosine_similarity(vec1, vec2))
                cos_wrong.append(F.cosine_similarity(vec1, vec3))

        temp_best_accuracy = 0
        temp_best_f1 = 0
        temp_best_recall = 0
        temp_best_precision = 0
        temp_P = 0
        temp_N = 0
        temp_TP = 0
        temp_TN= 0
        temp_best_threshold = 0
        P = len(cos_right)
        N = len(cos_wrong)
        for i in tqdm(range(0, 1000)):
            TP = 0
            TN = 0
            threshold = i / 1000
            for i in cos_right:
                if i >= threshold:
                    TP += 1
            for i in cos_wrong:
                if i < threshold:
                    TN += 1
            accuracy = (TN + TP) / (N + P)
            if N - TN + TP == 0:
                continue
            correct_recall = TP / P
            precision = TP / (TP + N - TN)
            if precision + correct_recall == 0:
                continue
            F1 = 2 * precision * correct_recall / (precision + correct_recall)
            if accuracy > temp_best_accuracy:
                temp_best_accuracy = accuracy
                temp_best_f1 = F1
                temp_best_recall = correct_recall
                temp_best_precision = precision
                temp_P = P
                temp_N = N
                temp_TP = TP
                temp_TN = TN
                temp_best_threshold = threshold

        print("eval_loss", temp_P, temp_N, temp_TP, temp_TN)

        result = {'accuracy': temp_best_accuracy, 'recall': temp_best_recall, 'precision': temp_best_precision, 'F1': temp_best_f1,
                  'global_step': epoch, 'threshold': temp_best_threshold,
                  'train_loss': round(tr_loss, 3)}
        print(result)
        if temp_best_accuracy > mac_acc:
            mac_acc = temp_best_accuracy
            save(model, optim, config.model_save_path + "_" + data_id, epoch)



if __name__ == '__main__':
    # 配置类
    config = Config()
    # 分词器
    tokenizer = AutoTokenizer.from_pretrained(config.model_path)
    # 模型最长输入
    max_length = config.max_length
    
    # 加载数据
    for i in range(0, 5):
        data_train_path = config.data_train_path + str(i) + '.pkl'
        data_test_path = config.data_test_path + str(i) + '.pkl'
        with open(data_train_path, 'rb') as f:
            train_buggy, train_fixed_c, train_fixed_inc = pd.read_pickle(f)
            train_buggy = list(train_buggy)
            train_fixed_c = list(train_fixed_c)
            train_fixed_inc = list(train_fixed_inc)
            train_buggy = [x.lower() for x in train_buggy]
            train_fixed_c = [x.lower() for x in train_fixed_c]
            train_fixed_inc = [x.lower() for x in train_fixed_inc]

        with open(data_test_path, 'rb') as f:
            test_buggy, test_fixed_c, test_fixed_inc = pd.read_pickle(f)
            test_buggy = list(test_buggy)
            test_fixed_c = list(test_fixed_c)
            test_fixed_inc = list(test_fixed_inc)
            test_buggy = [x.lower() for x in test_buggy]
            test_fixed_c = [x.lower() for x in test_fixed_c]
            test_fixed_inc = [x.lower() for x in test_fixed_inc]
        print("训练集:", len(train_buggy))
        print("测试集:", len(test_buggy))

        tokenizer_func = {'headTail': tokenizer_head_tail, 'head': tokenizer_head, 'tail': tokenizer_tail, 'mid': tokenizer_mid}
        train_dataset = MyDataset(tokenizer_func[config.cutMethod], tokenizer, max_length, train_buggy, train_fixed_c, train_fixed_inc)
        test_dataset = MyDataset(tokenizer_func[config.cutMethod], tokenizer, max_length, test_buggy, test_fixed_c, test_fixed_inc)

        # 生成训练和测试Dataloader
        train_loader = DataLoader(train_dataset, batch_size=config.train_batch_size, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=config.test_batch_size, shuffle=True)

        # 模型
        model = Model(config)
        # 定义GPU/CPU
        device = config.device
        model.to(device)
        # 多GPU并行
        model = torch.nn.DataParallel(model, device_ids=config.device_ids)
        #    model = torch.nn.DataParallel(model)
        # 加载已有模型参数
        if config.start_epoch > 0:
            model = load(model, config.model_save_path, config.start_epoch - 1)
        # 训练模式
        model.train()
        # 训练次数
        max_epoch = config.num_epoch
        # 开始训练是第几轮
        start_epoch = config.start_epoch
        # 优化器
        optim = AdamW(model.parameters(), lr=1e-5)
        # 损失函数
        loss_function = torch.nn.BCEWithLogitsLoss()
        
        # 开始训练
        train(model=model, train_loader=train_loader, test_loader=test_loader, optim=optim, loss_function=loss_function,
              max_epoch=max_epoch, start_epoch=start_epoch, data_id=str(i))






