import numpy as np
from torch import nn, Tensor
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
import torch
from sklearn.metrics.pairwise import *

class Model(torch.nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        temperature = 0.5
        device = config.device
        self.register_buffer("temperature", torch.tensor(temperature).to(device))  # 超参数 温度


        # bert 预训练模型
        self.bert = AutoModel.from_pretrained(config.model_path)
        if config.freeze_bert:
            for p in self.bert.parameters():
                p.requires_grad=False
        else:
            for param in self.bert.parameters():
                param.requires_grad = True  # 使参数可更新


    def forward(self, input_ids_1=None, attention_mask_1=None, input_ids_2=None, attention_mask_2=None, input_ids_3=None, attention_mask_3=None):
        output1 = self.bert(input_ids_1, attention_mask=attention_mask_1)
        output2 = self.bert(input_ids_2, attention_mask=attention_mask_2)
        output3 = self.bert(input_ids_3, attention_mask=attention_mask_3)

        vec1 = output1[1]
        vec2 = output2[1]
        vec3 = output3[1]
        return vec1, vec2, vec3




