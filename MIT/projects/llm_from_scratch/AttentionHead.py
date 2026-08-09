from functools import wraps

import torch
import torch.nn as nn
from typing import Tuple, Union, Optional, List, Any
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

import math


class AttentionHead(nn.Module):
    def __init__(self, dim: int, n_hidden: int):
        # dim: the dimension of the input
        # n_hidden: the dimension of the keys, queries, and values

        super().__init__()

        self.W_K = nn.Linear(dim, n_hidden)  # W_K weight matrix
        self.W_Q = nn.Linear(dim, n_hidden)  # W_Q weight matrix
        self.W_V = nn.Linear(dim, n_hidden)  # W_V weight matrix
        self.n_hidden = n_hidden
        self.dim = dim
        self.temp = torch.tensor([])
        self.temp2 = torch.tensor([])
        self.temp3 = torch.tensor([])

        print(self.count_params())
        # self.calculate_shapes()

    def count_params(self):
        return sum(p.view(-1).shape[0] for p in self.parameters())

    # def calculate_shapes(self):
    #     print("Attention Matrix shape",self.temp.shape)
    #     print(f"Before Normalizing Attention Head: {self.temp2.shape}")
    #     print(f"Attention Head final shape: {self.temp3.shape}")

    # todo
    def calc_attention_mask(self, inp, mask: Optional[torch.Tensor] = None):
        if not mask:
            return inp
        else:
            first = mask[0, :, 1]
            second = mask[0, :, 2]
            for i in first:
                for j in second:
                    if j == 0:
                        inp = -inp
            return inp

    # def forward(
    #     self, x: torch.Tensor, attn_mask: Optional[torch.Tensor]=None
    # ) -> Tuple[torch.Tensor, torch.Tensor]:
    #     """
    #     # x                the inputs. shape: (B x T x dim)
    #     # attn_mask        an attention mask. If None, ignore. If not None, then mask[b, i, j]
    #     #                  contains 1 if (in batch b) token i should attend on token j and 0
    #     #                  otherwise. shape: (B x T x T)
    #     #
    #     # Outputs:
    #     # attn_output      the output of performing self-attention on x. shape: (Batch x Num_tokens x n_hidden)
    #     # alpha            the attention weights (after softmax). shape: (B x T x T)
    #     #
    #     """
    #     print(f"Attention Mask:{attn_mask}")
    #
    #     A, Z = None, None
    #     """
    #     #todo : Compute self attention on x.
    #     #       (1) First project x to the query Q, key K, value V.
    #     #       (2) Then compute the attention weights alpha as:
    #     #                  alpha = softmax(QK^T/sqrt(n_hidden))
    #     #           Make sure to take into account attn_mask such that token i does not attend on token
    #     #           j if attn_mask[b, i, j] == 0. (Hint, in such a case, what value should you set the weight
    #     #           to before the softmax so that after the softmax the value is 0?)
    #     #       (3) The output is a linear combination of the values (weighted by the alphas):
    #     #                  out = alpha V
    #     #       (4) return the output and the alpha after the softmax
    #
    #     # ======= Answer START ========
    #     """
    #     print(f"x={type(x)},{x.shape if type(x) is torch.tensor else len(x)} in attention head")
    #     Q = self.W_Q(x).T
    #     K = self.W_K(x).T
    #     V = self.W_V(x).T
    #     print(f"Without Transpose:{self.W_Q(x).shape}")
    #     print(f"{Q.shape=},{K.shape=},{V.shape=}")
    #     #print(f"{(Q@K.T).shape=}\n\n\n-------------")
    #     #print(f"{torch.matmul(Q,K.T).shape}")
    #     A = torch.matmul(Q,K.transpose(dim0=1,dim1=2))
    #     print(f"{A.shape=}")
    #     self.temp = A
    #     #print(A.shape) # dim*dim
    #     #todo -> causal masking auto regressive.. for time based
    #     # if not attn_mask:
    #     #     out = alpha
    #     # else:
    #     #     first = attn_mask[0,:,1]
    #     #     second = attn_mask[0,:,2]
    #     #     for i in first:
    #     #         for j in second:
    #     #             if j==0:
    #     #                 out=-alpha
    #
    #     #mask = self.calc_attention_mask(A,attn_mask)
    #     #print(self.calculate_shapes())
    #     if attn_mask is not None:
    #         Z=A+attn_mask
    #     else:
    #         Z=A
    #     self.temp2 = Z
    #     #print(f"Masking score: {inp.shape}")
    #
    #     Z = torch.softmax(Z/n_hidden**.5,dim=-1)
    #     print(f"before multiplication{Z.shape=}")
    #     Z = torch.matmul(Z,V)
    #     #print(f"Checking shape along dim 1: {torch.softmax(Z,dim=1).shape}")
    #     print(f"{Z.shape=}")
    #
    #     self.temp3 = Z
    #     #self.calculate_shapes()
    #
    #
    #
    #
    #
    #
    #     #attn_output = torch.softmax(attn_scores,dim=-1)
    #
    #     # ======= Answer  END ========
    #     print("Attention Head Successful!")
    #     print(f"Attention output shape={A.shape}, Z={Z.shape} calculated for attention head\n\n------------")
    #
    #     return A,Z

    def forward(
        self, x: torch.Tensor, attn_mask: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # x shape: (B, T, dim)

        # 1. Project inputs to Q, K, V (Keep 3D structure intact)
        Q = self.W_Q(x)  # (B, T, n_hidden)
        K = self.W_K(x)  # (B, T, n_hidden)
        V = self.W_V(x)  # (B, T, n_hidden)

        # 2. Compute attention scores matrix
        # Transpose the last two dimensions of K to match (B, n_hidden, T)
        scores = torch.matmul(Q, K.transpose(-2, -1))  # Shape: (B, T, T)

        # 3. Apply the Attention Mask safely before Softmax
        if attn_mask is not None:
            # Everywhere mask is 0, fill scores with a massive negative number
            scores = scores.masked_fill(attn_mask == 0, float("-inf"))

        # 4. Normalize and apply Softmax to get Alpha weights
        alpha = torch.softmax(
            scores / math.sqrt(self.n_hidden), dim=-1
        )  # Shape: (B, T, T)

        # 5. Compute the final context vector
        # (B, T, T) x (B, T, n_hidden) -> (B, T, n_hidden)
        attn_output = torch.matmul(alpha, V)

        # 6. Return strictly in the order requested by your docstring/parent class
        return attn_output, alpha

    # def backward(self):
