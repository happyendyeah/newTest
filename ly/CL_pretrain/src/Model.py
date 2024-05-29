import numpy as np
from torch import nn, Tensor
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
import torch
from sklearn.metrics.pairwise import *

class Model(torch.nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        batch_size = config.train_batch_size
        temperature = 0.5
        device = config.device
        self.register_buffer("temperature", torch.tensor(temperature).to(device))  # 超参数 温度
        self.register_buffer("negatives_mask", (
            ~torch.eye(batch_size * 2, batch_size * 2, dtype=bool).to(device)).float())  # 主对角线为0，其余位置全为1的mask矩阵
        self.splicingMethod = config.splicingMethod
        self.batch_size = batch_size
        # bert 预训练模型
        self.bert = AutoModel.from_pretrained(config.model_path)
        if config.freeze_bert:
            for p in self.bert.parameters():
                p.requires_grad=False
        else:
            for param in self.bert.parameters():
                param.requires_grad = True  # 使参数可更新


    def forward(self, input_ids_1, attention_mask_1, input_ids_2, attention_mask_2):

        # [bs, 768]
        output1 = self.bert(input_ids_1, attention_mask=attention_mask_1)[1]
        # print(output1.shape)
        output2 = self.bert(input_ids_2, attention_mask=attention_mask_2)[1]
        z_i = F.normalize(output1, dim=1)  # (bs, dim)  --->  (bs, dim)
        z_j = F.normalize(output2, dim=1)  # (bs, dim)  --->  (bs, dim)

        representations = torch.cat([z_i, z_j], dim=0)  # repre: (2*bs, dim)
        similarity_matrix = F.cosine_similarity(representations.unsqueeze(1), representations.unsqueeze(0),
                                                dim=2)  # simi_mat: (2*bs, 2*bs)

        sim_ij = torch.diag(similarity_matrix, self.batch_size)  # bs
        sim_ji = torch.diag(similarity_matrix, -self.batch_size)  # bs
        positives = torch.cat([sim_ij, sim_ji], dim=0)  # 2*bs

        nominator = torch.exp(positives / self.temperature)  # 2*bs
        denominator = self.negatives_mask * torch.exp(similarity_matrix / self.temperature)  # 2*bs, 2*bs

        loss_partial = -torch.log(nominator / torch.sum(denominator, dim=1))  # 2*bs
        loss = torch.sum(loss_partial) / (2 * self.batch_size)
        return loss




