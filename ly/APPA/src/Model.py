import numpy as np
from torch import nn, Tensor
from transformers import AutoModel, AutoTokenizer
import torch
from sklearn.metrics.pairwise import *

class Model(torch.nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        self.splicingMethod = config.splicingMethod

        # bert 预训练模型
        self.bert = AutoModel.from_pretrained(config.model_path)
        if config.freeze_bert:
            for p in self.bert.parameters():
                p.requires_grad=False
        else:
            for param in self.bert.parameters():
                param.requires_grad = True  # 使参数可更新
        # lstm 模型
        input_time = {'cat': 2, 'add': 1, 'sub': 1, 'mul': 1, 'mix': 5, 'max_pooling': 1, 'mean_pooling': 1}
        self.lstm = nn.LSTM(input_size=config.input_size * input_time[self.splicingMethod], hidden_size=config.hidden_size, num_layers=config.num_layers, batch_first=True,
                            dropout=config.dropout, bias=True, bidirectional=True)
        self.lstm.flatten_parameters()
        # dropout
        self.dropout = nn.Dropout(config.dropout)
        # linear 全连接层：双向LSTM要*2
        self.fc = nn.Linear(config.hidden_size * 2,
                            config.num_classes)  # 自定义全连接层 ，输入数（输入的最后一个维度），输出数（多分类数量），bert模型输出的最后一个维度是1024，这里的输入要和bert最后的输出统一

    def add(self, text1, text2):
        return torch.add(text1, text2)

    def subtraction(self, text1, text2):
        return torch.sub(text1, text2)

    def multiplication(self, text1, text2):
        return torch.mul(text1, text2)
        
    def max_pooling(self, text1, text2):
        return torch.max(text1, text2)
        
    def mean_pooling(self, text1, text2):
        return torch.mean(text1, text2)

    def cosion(self, text1, text2):
        return torch.cosine_similarity(text1, text2)

    def euclid(self, text1, text2):
        return torch.pairwise_distance(text1, text2)

    def cat_features(self, text1, text2):
        addition = self.add(text1, text2)
        subtract = self.subtraction(text1, text2)
        multiple = self.multiplication(text1, text2)
        cos = self.cosion(text1, text2).unsqueeze(1)
        eu = self.euclid(text1, text2).unsqueeze(1)
        
        fe = torch.cat((text1, text2, addition, subtract, multiple), dim=2)
        return fe

    def forward(self, input_ids_1, attention_mask_1, input_ids_2, attention_mask_2):

        # 输入bert，得到词向量向量
        output1 = self.bert(input_ids_1, attention_mask=attention_mask_1)[0]
        output2 = self.bert(input_ids_2, attention_mask=attention_mask_2)[0]

#        print(output1.shape)
#        print(output2.shape)

        # 将两个向量进行拼接，格式为[t1,t2,t1-t2,t1*t2]
        if self.splicingMethod == 'cat':
            output = torch.cat((output1, output2), dim=2)
        elif self.splicingMethod == 'add':
            output = self.add(output1, output2)
        elif self.splicingMethod == 'sub':
            output = self.subtraction(output1, output2)
        elif self.splicingMethod == 'mul':
            output = self.multiplication(output1, output2)
        elif self.splicingMethod == 'mix':
            output = self.cat_features(output1, output2)
        elif self.splicingMethod == 'max_pooling':
            output = self.max_pooling(output1, output2)
        elif self.splicingMethod == 'mean_pooling':
            output = self.max_pooling(output1, output2)
#        print(output.shape)

        # 将词向量输入lstm
        out, _ = self.lstm(output)

        # 将lstm输入进行dropout，其输入输出shape相同
        out = self.dropout(out)

        # 全连接
#        print(out.shape)
        out = out[:, -1, :]  # 只要序列中最后一个token对应的输出，（因为lstm会记录前边token的信息）
#        print(out.shape)
        out = self.fc(out).squeeze(-1)
#        print(out.shape)
#        print(1/0)
        return out



