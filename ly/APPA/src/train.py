import numpy as np
from transformers import AutoTokenizer, AdamW
from torch.utils.data import DataLoader
import torch
import os
import shutil
from pathlib import Path

from DataLoader import MyDataset
from Model import Model
from test import test
from configs import Config
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_curve, auc, accuracy_score, recall_score, precision_score

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


def load(model, PATH):
    checkpoint = torch.load(PATH)
    model.module.load_state_dict(checkpoint['model_state_dict'], False)
    print("加载further pretrained模型成功")
    return model

result_label = []
result_index = []
result_pred = []
result_labels = []
result_indexs = []
result_preds = []
tmp_index = []
tmp_pred = []
tmp_label = []
accs = [0,0,0,0,0]
prcs = [0,0,0,0,0]
rcs =[0,0,0,0,0]
f1s = [0,0,0,0,0]
aucs = [0,0,0,0,0]

def evl(model, test_loader):
    tmp_index.clear()
    tmp_pred.clear()
    tmp_label.clear()
    y_true = []
    y_score = []
    with torch.no_grad():
        for batch in test_loader:
            input_ids_1 = batch['input_ids_1'].to(device)
            attention_mask_1 = batch['attention_mask_1'].to(device)
            input_ids_2 = batch['input_ids_2'].to(device)
            attention_mask_2 = batch['attention_mask_2'].to(device)
            labels = batch['labels'].to(device)
            
            out = torch.sigmoid(model(input_ids_1, attention_mask_1, input_ids_2, attention_mask_2))

            y_true.append(labels.item())
            y_score.append(out.item())
            
            eval_index = batch['index'].numpy()[0]
            tmp_index.append(eval_index)
            eval_label = batch['labels'].numpy()[0]
            tmp_label.append(eval_label)
            if out.item() >= 0.5:
                tmp_pred.append(1)
            else:
                tmp_pred.append(0)
            

    fpr, tpr, thresholds = roc_curve(y_true=y_true, y_score=y_score, pos_label=1)
    auc_ = auc(fpr, tpr)
    y_pred = [1 if p >= 0.5 else 0 for p in y_score]
    acc = accuracy_score(y_true=y_true, y_pred=y_pred)
    prc = precision_score(y_true=y_true, y_pred=y_pred)
    rc = recall_score(y_true=y_true, y_pred=y_pred)
    f1 = 2 * prc * rc / (prc + rc)
    print('Accuracy: %f -- Precision: %f -- Recall: %f -- F1: %f -- AUC: %f' % (acc, prc, rc, f1, auc_))
    return acc, prc, rc, f1, auc_


def train(model, train_loader, test_loader, optim, loss_function, max_epoch, start_epoch, data_id):
    max_acc = 0
    print('-------------- start training ---------------', '\n')
    for epoch in range(max_epoch):
        # 从start_epoch开始
        if epoch < start_epoch:
            continue
        print("========= epoch:", epoch, '==============')
        step = 0
        losses = []
        for batch in train_loader:
            step += 1
            # 清空优化器
            optim.zero_grad()
            input_ids_1 = batch['input_ids_1'].to(device)
            attention_mask_1 = batch['attention_mask_1'].to(device)
            input_ids_2 = batch['input_ids_2'].to(device)
            attention_mask_2 = batch['attention_mask_2'].to(device)
            labels = batch['labels'].to(device)
            # 将数据输入模型，计算loss
            out = model(input_ids_1, attention_mask_1, input_ids_2, attention_mask_2)
            loss = loss_function(out, labels.float())

            print('[', step, '/', len(train_loader), ']', "loss:", format(loss.item(), '.3f'))
            losses.append(loss.item())

            # 反向传播
            loss.backward()
            optim.step()
        # 输出本次epoch的loss均值
        print(np.mean(losses))
        # test(model,test_loader,device=config.device)

        # 验证
        if epoch % 1 == 0:
            model.eval()
            acc, prc, rc, f1, auc = evl(model=model, test_loader=test_loader)
            model.train()
            if max_acc < acc:
                iint = int(i)
                accs[iint] = acc
                prcs[iint] = prc
                rcs[iint] = rc
                f1s[iint] = f1
                aucs[iint] = auc
                max_acc = acc
                result_index = tmp_index.copy()
                result_pred = tmp_pred.copy()
                result_label = tmp_label.copy()
                save(model, optim, config.model_save_path + "_" + data_id, epoch)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(result_index)
    print(result_pred)
    print(result_label)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    result_indexs.extend(result_index)
    result_preds.extend(result_pred)
    result_labels.extend(result_label)

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
            train_texts_1, train_texts_2, train_labels = pd.read_pickle(f)
            train_texts_1 = list(train_texts_1)
            train_texts_2 = list(train_texts_2)
            train_labels = list(train_labels)
            train_texts_1 = [text.lower() for text in train_texts_1]
            train_texts_2 = [text.lower() for text in train_texts_2]
            train_index = [idx + 1 for idx in range(len(train_labels))]
            # 过拟合检测/正确补丁检测
            train_labels = [0 if label == 1 else 1 for label in train_labels]
        with open(data_test_path, 'rb') as f:
            test_texts_1, test_texts_2, test_labels = pd.read_pickle(f)
            test_texts_1 = list(test_texts_1)
            test_texts_2 = list(test_texts_2)
            test_labels = list(test_labels)
            test_texts_1 = [text.lower() for text in test_texts_1]
            test_texts_2 = [text.lower() for text in test_texts_2]
            test_index = [idx + 1 for idx in range(len(test_labels))]
            # 过拟合检测/正确补丁检测
            test_labels = [0 if label == 1 else 1 for label in test_labels]
        print("训练集:", len(train_labels))
        print("测试集:", len(test_labels))

        tokenizer_func = {'headTail': tokenizer_head_tail, 'head': tokenizer_head, 'tail': tokenizer_tail, 'mid': tokenizer_mid}
        train_dataset = MyDataset(tokenizer_func[config.cutMethod], tokenizer, max_length, train_texts_1, train_texts_2, train_labels, train_index)
        test_dataset = MyDataset(tokenizer_func[config.cutMethod], tokenizer, max_length, test_texts_1, test_texts_2, test_labels, test_index)

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
            model = load(model, config.pretrained_model_path)
        # 训练模式
        model.train()
        # 训练次数
        max_epoch = config.num_epoch
        # 开始训练是第几轮
        start_epoch = config.start_epoch
        # 优化器
        optim = AdamW(model.parameters(), lr=5e-5)
        # 损失函数
        loss_function = torch.nn.BCEWithLogitsLoss()
        
        # 开始训练
        train(model=model, train_loader=train_loader, test_loader=test_loader, optim=optim, loss_function=loss_function,
              max_epoch=max_epoch, start_epoch=start_epoch, data_id=str(i))

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Final:', sum(accs)/5, sum(prcs)/5, sum(rcs)/5, sum(f1s)/5, sum(aucs)/5)
#        print(sum(accs), sum(prcs), sum(rcs), sum(f1s), sum(aucs))
        print('结果序号',result_indexs)
        print('标签', result_labels)
        print('预测', result_preds)






