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
        self.device_numbers = len(config.device_ids)
        print(f"batch size: {batch_size}, device_number: {self.device_numbers}")
        if(batch_size // self.device_numbers * self.device_numbers != batch_size):
            print("batch size can not be devided by device number, please set a reasonal params.")
            sys.exit()
        self.register_buffer("negatives_mask", (
            ~torch.eye(int(batch_size * 2 / self.device_numbers), int(batch_size * 2 / self.device_numbers), dtype=bool).to(device)).float())  # 主对角线为0，其余位置全为1的mask矩阵
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
        print("output1:")
        print(output1.shape)
        output2 = self.bert(input_ids_2, attention_mask=attention_mask_2)[1]
        print("output2:")
        print(output2.shape)
        z_i = F.normalize(output1, dim=1)  # (bs, dim)  --->  (bs, dim)
        print("z_i:")
        print(z_i.shape)
        z_j = F.normalize(output2, dim=1)  # (bs, dim)  --->  (bs, dim)
        print("z_j:")
        print(z_j.shape)

        representations = torch.cat([z_i, z_j], dim=0)  # repre: (2*bs, dim)
        print("representations:")
        print(representations.shape)
        similarity_matrix = F.cosine_similarity(representations.unsqueeze(1), representations.unsqueeze(0),
                                                dim=2)  # simi_mat: (2*bs, 2*bs)
        print("similarity_matrix:")
        print(similarity_matrix.shape)

        sim_ij = torch.diag(similarity_matrix, int(self.batch_size / self.device_numbers))  # bs
        print("sim_ij:")
        print(sim_ij.shape)
        sim_ji = torch.diag(similarity_matrix, int(-self.batch_size / self.device_numbers))  # bs
        print("sim_ji:")
        print(sim_ji.shape)
        positives = torch.cat([sim_ij, sim_ji], dim=0)  # 2*bs
        print("positives:")
        print(positives.shape)

        nominator = torch.exp(positives / self.temperature)  # 2*bs
        print("nominator:")
        print(nominator.shape)
        denominator = self.negatives_mask * torch.exp(similarity_matrix / self.temperature)  # 2*bs, 2*bs
        print("denominator:")
        print(denominator.shape)

        loss_partial = -torch.log(nominator / torch.sum(denominator, dim=1))  # 2*bs
        print("loss_partial:")
        print(loss_partial.shape)
        loss = torch.sum(loss_partial) / int(2 * self.batch_size / self.device_numbers)
        print("model_loss:")
        print(loss.shape)
        return loss




