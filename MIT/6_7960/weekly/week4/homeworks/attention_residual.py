# these are already implemented for you!

class FFN(nn.Module):
    def __init__(self, dim: int, n_hidden: int):
        # dim       the dimension of the input
        # n_hidden  the width of the linear layer

        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, n_hidden),
            nn.GELU(),
            nn.Linear(n_hidden, dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x         the input. shape: (B x T x dim)

        # Outputs:
        # out       the output of the feed-forward network: (B x T x dim)
        # print("\n\n\nIn FFN-------------------------")
        print(f"{x.shape=}")
        out = self.net(x)
        # print(f"Out={out.shape=}")
        return out
class AttentionResidual(nn.Module):
    def __init__(self, dim: int, attn_dim: int, mlp_dim: int, num_heads: int):
        # dim       the dimension of the input
        # attn_dim  the hidden dimension of the attention layer
        # mlp_dim   the hidden layer of the FFN
        # num_heads the number of heads in the attention layer
        super().__init__()

        self.attn = MultiHeadedAttentionParallel(dim, attn_dim, num_heads)
        self.ffn = FFN(dim, mlp_dim)

    def forward(
            self, x: torch.Tensor, attn_mask=False
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # x                the inputs. shape: (B x T x dim)
        # attn_mask        an attention mask. If None, ignore. If not None, then mask[b, i, j]
        #                  contains 1 if (in batch b) token i should attend on token j and 0
        #                  otherwise. shape: (B x T x T)
        #
        # Outputs:
        # attn_output      shape: (B x T x dim)
        # attn_alphas      the attention weights of each of the attention heads.
        #                  shape: (B x Num_heads x T x T)
        # print("\n\n--------- Attention Residual")
        Z, A = self.attn(x=x, attn_mask=attn_mask)
        # Z,A = attn_out,alphas

        # print("\n\n  In Attention Residual")
        # print(f"{Z.shape=}\t,{x.shape=}\t.{A.shape=}\n")
        x = Z + x
        x = self.ffn(x) + x
        # print(f"{x.shape=}\n\n--------------")
        return x, A