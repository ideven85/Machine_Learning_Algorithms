from functools import wraps

import torch
import torch.nn as nn
from typing import Tuple, Union, Optional, List, Any
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

from projects.llm_from_scratch.AttentionHead import AttentionHead


class MultiHeadedAttention(nn.Module):
    def __init__(self, dim: int, n_hidden: int, num_heads: int):
        # dim: the dimension of the input
        # n_hidden: the hidden dimensions for the attention layer
        # num_heads: the number of attention heads
        super().__init__()
        self.H = num_heads
        # TODO: set up your parameters for multi-head attention. You should initialize
        #       num_heads attention heads (see nn.ModuleList) as well as a linear layer
        #       that projects the concatenated outputs of each head into dim
        #       (what size should this linear layer be?)

        # ======= Answer START ========
        # self.attention = AttentionHead(dim=dim,n_hidden=n_hidden)
        self.linear_list = nn.ModuleList(
            [AttentionHead(dim, n_hidden) for _ in range(num_heads)]
        )
        self.dim = dim

        # 2. Final linear projection layer
        # Maps concatenated outputs (num_heads * n_hidden) back to original dim
        self.W0 = nn.Linear(n_hidden * num_heads, dim)

        # ======= Answer  END ========

    # todo in parallel
    # def forward(
    #     self, x: torch.Tensor, attn_mask: Optional[torch.Tensor]
    # ) -> Tuple[torch.Tensor, torch.Tensor]:
    #     # x                the inputs. shape: (B x T x dim)
    #     # attn_mask        an attention mask. If None, ignore. If not None, then mask[b, i, j]
    #     #                  contains 1 if (in batch b) token i should attend on token j and 0
    #     #                  otherwise. shape: (B x T x T)
    #     #
    #     # Outputs:
    #     # attn_output      the output of performing multi-headed self-attention on x.
    #     #                  shape: (B x T x dim)
    #     # attn_alphas      the attention weights of each of the attention heads.
    #     #                  shape: (B x Num_heads x T x T)
    #
    #     A,Z,W0 = None, None,None
    #
    #     # TODO: Compute multi-headed attention. Loop through each of your attention heads
    #     #       and collect the outputs. Concatenate them together along the hidden dimension,
    #     #       and then project them back into the output dimension (dim). Return both
    #     #       the final attention outputs as well as the alphas from each head.
    #
    #     # ======= Answer START ========
    #     print(f"x={x}length={len(x)},type={type(x)} in Multi Attention Head\n\n------------")

    def forward(
        self, x: torch.Tensor, attn_mask: Optional[torch.Tensor]
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        Z_concat = []
        A_concat = []
        head_outputs = []
        head_alphas = []
        print(f"\n\n In Multi headed Attention: {x.shape=}")
        for head in self.linear_list:
            #     Z,A = head(x,attn_mask=attn_mask)
            #     Z_concat.append(Z)
            #     A_concat.append(A)
            # # 4. Concatenate outputs from all heads along the last (hidden) dimension
            # # Resulting shape: (B, T, num_heads * n_hidden)
            # A=torch.cat(A_concat,dim=-1)
            # Z=self.W0(A)
            # Ah=torch.stack(Z_concat,dim=1)
            # return Z,Ah
            out, alpha = head(x, attn_mask=attn_mask)
            print(f"Multi Headed Attention: {out.shape=},{alpha.shape=}")

            head_outputs.append(out)  # Each item shape: (B, T, n_hidden)
            head_alphas.append(alpha)  # Each item shape: (B, T, T)

        # 4. Concatenate outputs from all heads along the last (hidden) dimension
        # Resulting shape: (B, T, num_heads * n_hidden)

        concatenated_heads = torch.cat(head_outputs, dim=-1)
        # concatenated_heads=concatenated_heads.transpose(0,1)

        # 5. Project the concatenated representation back to 'dim'
        # Resulting shape: (B, T, dim)
        print(f"Multi Headed Attention: {concatenated_heads.shape=}")
        attn_output = self.W0(concatenated_heads)
        print(
            f"Multi Headed Attention: {attn_output.shape=} With output head successful\n\n-----------"
        )

        # 6. Stack attention weights from all heads along a new head dimension
        # Resulting shape: (B, num_heads, T, T)

        attn_alphas = torch.stack(head_alphas, dim=1)
        print(f"{attn_alphas.shape=}")
        print("Multi Headed Attention Successful\n\n\n--------------------------")
        return attn_output, attn_alphas
