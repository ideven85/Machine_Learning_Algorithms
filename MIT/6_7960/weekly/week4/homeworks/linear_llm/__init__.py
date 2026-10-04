import os
import gc
import logging
from dataclasses import dataclass
from typing import Optional, Tuple, List

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import tqdm
import nltk
import numpy as np
# --- Environment & Diagnostics Setup ---
# Disable anomaly detection for standard training runs

import torchmetrics
from torchmetrics import MeanMetric
from torchmetrics.classification import MulticlassAccuracy
from torchmetrics.text import Perplexity
from typing import Dict, Any
torch.autograd.set_detect_anomaly(False)

device = (
    torch.accelerator.current_accelerator().type
    if torch.accelerator.is_available()
    else "cpu"
)

num_workers = min(2, os.cpu_count() or 1)

logging.basicConfig(
    filename="llm.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def clean_memory_cache():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    elif torch.backends.mps.is_available():
        torch.mps.empty_cache()


@dataclass
class TrainResult:
    train_losses: List[float]
    train_accs: List[float]
    val_accs: List[float]
    val_losses: List[float]


class AverageMeter:
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0.0
        self.avg = 0.0
        self.sum = 0.0
        self.count = 0.0

    def update(self, val: float, n: int = 1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count if self.count > 0 else 0.0

    def calculate(self) -> float:
        return self.avg

file = "shakespeare.txt"
with open(file, "r") as f:
    dialogues = f.read()

all_dialogues = dialogues.split("\n\n")
def tokenize(s):
    return nltk.word_tokenize(s)
# --- Dataset and Collation ---


class MyTokenizer:
    def __init__(self, raw_text: str):
        # raw_text     contains the text from which we will build our vocabulary

        self.start = "<START>"  # token that starts every example
        self.pad = "<PAD>"  # token used to pad examples to the same length
        self.unk = "<UNK>"  # token used if encountering a word not in our vocabulary

        vocab = np.unique(tokenize(raw_text))
        vocab = np.concatenate([np.array([self.start, self.pad, self.unk]), vocab])

        self.vocab = vocab  # array of tokens in order
        self.tok_to_id = {w: i for i, w in enumerate(vocab)}  # mapping of token to ID
        self.id_to_token = {i: w for i, w in enumerate(vocab)}
        self.vocab_size = len(self.vocab)  # size of vocabulary

    def __len__(self):
        return self.vocab_size

    def encode(self, s: str) -> torch.Tensor:
        # s           input string
        #
        # Output
        # id_tensor   a tensor of token ids, starting with the start token.t

        id_tensor = torch.from_numpy(
            np.array(
                [self.tok_to_id[self.start]]
                + [self.tok_to_id[w] for w in tokenize(s) if w in self.tok_to_id],
                dtype=np.int32,
                )
        )

        # TODO: tokenize the input using word_tokenize. Return a tensor  of the token ids, starting with the token id for the start token.
        # ============ ANSWER START ===========
        # encoded_string = tokenize(s)
        # token_ids =
        # token_ids.append(self.tok_to_id[self.start])
        # token_ids.extend(
        #     [self.tok_to_id[w] for w in encoded_string if w in self.tok_to_id.keys()]
        # )
        # id_tensor = np.array(token_ids)

        # id_tensor = torch.from_numpy(id_tensor)
        # ============ ANSWER END =============

        return id_tensor

    def decode(self, toks: torch.Tensor) -> str:
        # toks         a list of token ids
        #
        # Output
        # decoded_str  the token ids decoded back into a string (join with a space)

        # TODO: convert the token ids back to the actual corresponding words.
        # Join the tokens with a space and return the full string
        # ============ ANSWER START ===========
        return " ".join(
            [
                self.id_to_token[int(token)]
                for token in toks
                if token in self.tok_to_id.values()
            ]
        ).rstrip()

        # ============ ANSWER END =============

        # return decoded_str

    def pad_examples(self, tok_list: List[torch.Tensor]) -> torch.Tensor:
        # Pads the tensors to the right with the pad token so that they are the same length.
        #
        # tok_list       a list of tensors containing token ids (maybe of different lengths)
        #
        # Output
        # padded_tokens  shape: (len(tok_list), max length within tok_list)
        return torch.nn.utils.rnn.pad_sequence(
            tok_list, batch_first=True, padding_value=self.tok_to_id[self.pad]
        )


tok = MyTokenizer(dialogues)

class DialogueDataset(Dataset):
    def __init__(self, tokenizer, lines: List[str], max_N: int):
        self.lines = lines
        self.tokenizer = tokenizer
        self.max_N = max_N

    def __len__(self) -> int:
        return len(self.lines)

    def __getitem__(self, idx: int) -> torch.Tensor:
        encoded = self.tokenizer.encode(self.lines[idx])[: self.max_N]
        return torch.tensor(encoded, dtype=torch.long)


def get_collate_fn(tokenizer):
    def collate_fn(examples: List[torch.Tensor]):
        new_input_ids = tokenizer.pad_examples(examples)
        if not isinstance(new_input_ids, torch.Tensor):
            new_input_ids = torch.tensor(new_input_ids, dtype=torch.long)

        attn_mask = torch.ones(new_input_ids.shape, dtype=torch.float32)
        pad_id = tokenizer.tok_to_id[tokenizer.pad]
        attn_mask[new_input_ids == pad_id] = 0.0

        return {"input_ids": new_input_ids, "input_mask": attn_mask}
    return collate_fn

class DialogueCollateFn:
    """Picklable collate callable for DataLoader multiprocessing."""

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.pad_id = tokenizer.tok_to_id[tokenizer.pad]

    def __call__(self, examples: List[torch.Tensor]) -> dict:
        new_input_ids = self.tokenizer.pad_examples(examples)
        if not isinstance(new_input_ids, torch.Tensor):
            new_input_ids = torch.tensor(new_input_ids, dtype=torch.long)

        attn_mask = torch.ones(new_input_ids.shape, dtype=torch.float32)
        attn_mask[new_input_ids == self.pad_id] = 0.0

        return {"input_ids": new_input_ids, "input_mask": attn_mask}
# --- Model Components ---
from typing import Optional, Tuple
import torch
import torch.nn as nn
import torch.nn.functional as F


class LinearMultiAttentionHead(nn.Module):
    """Linear Multi-Head Attention module with kernel feature maps.

    This module implements Kernel Linear Attention (Katharopoulos et al., 2020),
    which replaces the softmax operator with an explicit, non-negative feature map
    $\phi(x) = \text{ELU}(x) + 1$. By leveraging the associative property of matrix
    multiplication, attention computation achieves linear time and memory complexity
    $\mathcal{O}(N \cdot d^2)$ with respect to sequence length $N$.

    The module natively supports three operational execution modes:
        1. **Non-Causal Global Attention**: Bidirectional attention for vision or
           encoder architectures (e.g., ViT, BERT). Computes $Q (K^T V)$ in $\mathcal{O}(N)$
           time.
        2. **Causal Training Mode**: Autoregressive attention computed using
           cumulative prefixes (`torch.cumsum`) in $\mathcal{O}(N)$ parallel time.
        3. **Recurrent Inference Mode**: Constant-time $\mathcal{O}(1)$ autoregressive
           decoding per step by maintaining a fixed-size state tuple $(S_t, z_t)$
           independent of sequence length.

    Attributes:
        dim (int): Total input and output feature dimension ($D$).
        num_heads (int): Number of parallel attention heads ($H$).
        n_hidden (int): Feature dimensionality per head ($d_k = d_v$).
        eps (float): Epsilon scalar added to the denominator for numerical stability.
        qkv_proj (nn.Linear): Unified projection layer mapping $D \to 3 \times H \times d$.
        out_proj (nn.Linear): Output linear layer mapping concatenated heads $H \times d \to D$.

    Example:
        >>> # Bidirectional / Encoder usage (e.g., Vision Transformer)
        >>> attn = LinearMultiAttentionHead(dim=128, n_hidden=32, num_heads=4)
        >>> x = torch.randn(2, 50, 128)  # (Batch, Seq_Len, Dim)
        >>> out, _ = attn(x, is_causal=False)
        >>> out.shape
        torch.Size([2, 50, 128])

        >>> # Autoregressive generation with constant-memory recurrent state
        >>> prompt = torch.randn(1, 10, 128)
        >>> out, cache = attn(prompt, is_causal=True, use_cache=True)
        >>> # Single step decode
        >>> next_token = torch.randn(1, 1, 128)
        >>> next_out, cache = attn(next_token, layer_past=cache, use_cache=True)
        >>> next_out.shape
        torch.Size([1, 1, 128])
    """

    def __init__(
            self,
            dim: int,
            n_hidden: int,
            num_heads: int,
            eps: float = 1e-6,
    ) -> None:
        """Initializes the LinearMultiAttentionHead module.

        Args:
            dim (int): Dimensionality of the input feature space.
            n_hidden (int): Projected hidden dimension per individual head.
            num_heads (int): Total number of parallel attention heads.
            eps (float, optional): Small constant preventing zero-division in
                the kernel normalization denominator. Defaults to 1e-6.
        """
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.n_hidden = n_hidden
        self.eps = eps

        # Fused linear layer for Q, K, and V projections
        self.qkv_proj = nn.Linear(dim, num_heads * n_hidden * 3, bias=False)
        self.out_proj = nn.Linear(num_heads * n_hidden, dim)

    @staticmethod
    def feature_map(x: torch.Tensor) -> torch.Tensor:
        """Applies an element-wise non-negative kernel feature map.

        Computes $\phi(x) = \text{ELU}(x) + 1.0$, guaranteeing that all kernel values
        are strictly non-negative ($\phi(x) \ge 0$), which is required to prevent
        the normalization denominator from evaluating to zero or negative quantities.

        Args:
            x (torch.Tensor): Unnormalized projection tensor of arbitrary shape.

        Returns:
            torch.Tensor: Non-negative transformed feature tensor with the same
                shape and dtype as the input.
        """
        return F.elu(x) + 1.0

    def forward(
            self,
            x: torch.Tensor,
            is_causal: bool = False,
            layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
            use_cache: bool = False,
    ) -> Tuple[torch.Tensor, Optional[Tuple[torch.Tensor, torch.Tensor]]]:
        """Executes the linear multi-head attention forward pass.

        Args:
            x (torch.Tensor): Input sequence tensor of shape `(batch_size, seq_len, dim)`.
            is_causal (bool, optional): If `True`, enables causal autoregressive masking,
                restricting queries to attend only to current and past positions. Ignored
                if `layer_past` is provided. Defaults to `False`.
            layer_past (Optional[Tuple[torch.Tensor, torch.Tensor]], optional): Recurrent
                state tuple `(S_prev, z_prev)` from the previous autoregressive generation
                step:
                    - `S_prev`: Matrix state of shape `(batch_size, num_heads, n_hidden, n_hidden)`.
                    - `z_prev`: Normalizer state of shape `(batch_size, num_heads, n_hidden)`.
                Providing this argument puts the module into single-step recurrent
                decoding mode. Defaults to `None`.
            use_cache (bool, optional): If `True`, computes and returns the updated
                recurrent memory state tuple for subsequent autoregressive decoding steps.
                Defaults to `False`.

        Returns:
            Tuple[torch.Tensor, Optional[Tuple[torch.Tensor, torch.Tensor]]]: A tuple containing:
                - **output** (`torch.Tensor`): The projected multi-head attention representation
                  of shape `(batch_size, seq_len, dim)`.
                - **present** (`Optional[Tuple[torch.Tensor, torch.Tensor]]`): The updated
                  recurrent state `(S_t, z_t)` if `use_cache=True`, or `None` otherwise.
        """
        B, T, _ = x.shape

        # 1. Project inputs and reshape to: (B, num_heads, T, n_hidden)
        qkv = (
            self.qkv_proj(x)
            .reshape(B, T, self.num_heads, 3 * self.n_hidden)
            .transpose(1, 2)
        )
        q, k, v = qkv.chunk(3, dim=-1)

        # 2. Map queries and keys to non-negative kernel representations
        phi_q = self.feature_map(q)  # (B, H, T, n_hidden)
        phi_k = self.feature_map(k)  # (B, H, T, n_hidden)

        present = None

        # ------------------------------------------------------------------
        # Mode 1: Recurrent Step Generation with KV Cache (O(1) Step Cost)
        # ------------------------------------------------------------------
        if layer_past is not None:
            prev_S, prev_z = layer_past

            # Extract instantaneous step tokens: (B, H, n_hidden)
            k_t = phi_k.squeeze(2)
            v_t = v.squeeze(2)

            # Recurrent transition: S_t = S_{t-1} + (k_t^T @ v_t)
            dS = torch.einsum("bhd,bhe->bhde", k_t, v_t)
            dz = k_t

            S = prev_S + dS
            z = prev_z + dz
            present = (S, z) if use_cache else None

            # Compute output token: O_t = (q_t @ S_t) / (q_t @ z_t)
            q_t = phi_q.squeeze(2)
            num = torch.einsum("bhd,bhde->bhe", q_t, S)       # (B, H, n_hidden)
            den = (q_t * z).sum(dim=-1, keepdim=True)         # (B, H, 1)

            context = (num / (den + self.eps)).unsqueeze(2)   # (B, H, 1, n_hidden)

        # ------------------------------------------------------------------
        # Mode 2: Parallel Causal Attention via Prefix Cumsum (O(N) Training)
        # ------------------------------------------------------------------
        elif is_causal:
            # Outer products across all timesteps: (B, H, T, n_hidden, n_hidden)
            outer = torch.einsum("bhtd,bhte->bhtde", phi_k, v)
            S = torch.cumsum(outer, dim=2)                     # (B, H, T, d, d)
            z = torch.cumsum(phi_k, dim=2)                     # (B, H, T, d)

            if use_cache:
                # Store terminal step state for subsequent iterative decoding
                present = (S[:, :, -1], z[:, :, -1])

            # Numerator: O_i = sum_{j<=i} phi(q_i) @ (phi(k_j)^T @ v_j)
            num = torch.einsum("bhtd,bhtde->bhte", phi_q, S)

            # Denominator: D_i = phi(q_i) @ sum_{j<=i} phi(k_j)
            den = (phi_q * z).sum(dim=-1, keepdim=True)
            context = num / (den + self.eps)

        # ------------------------------------------------------------------
        # Mode 3: Bidirectional Non-Causal Attention (Associative Q @ (K^T @ V))
        # ------------------------------------------------------------------
        else:
            # Memory state: (B, H, n_hidden, n_hidden)
            kv = torch.matmul(phi_k.transpose(-2, -1), v)

            # Numerator: (B, H, T, n_hidden)
            num = torch.matmul(phi_q, kv)

            # Denominator: phi(Q) @ (sum_j phi(K_j))^T -> (B, H, T, 1)
            k_sum = phi_k.sum(dim=-2, keepdim=True)
            den = torch.matmul(phi_q, k_sum.transpose(-2, -1))

            context = num / (den + self.eps)

        # 3. Concatenate all heads and apply final linear projection W_O
        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(B, T, self.num_heads * self.n_hidden)
        )
        output = self.out_proj(context)

        return output, present



class AttentionResidual(nn.Module):
    def __init__(self, dim: int, attn_dim: int, mlp_dim: int, num_heads: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)

        # Instantiate Linear Attention Head
        self.attn = LinearMultiAttentionHead(
            dim=dim,
            n_hidden=attn_dim,
            num_heads=num_heads,
        )

        self.norm2 = nn.LayerNorm(dim)
        self.ffn = nn.Sequential(
            nn.Linear(dim, mlp_dim),
            nn.GELU(),
            nn.Linear(mlp_dim, dim),
        )

    def forward(
            self,
            x: torch.Tensor,
            is_causal: bool = True,
            layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
            use_cache: bool = False,
    ) -> Tuple[torch.Tensor, Optional[Tuple[torch.Tensor, torch.Tensor]]]:
        # Pass inputs, causal flag, and optional cache into linear attention
        attn_out, present = self.attn(
            x=self.norm1(x),
            is_causal=is_causal,
            layer_past=layer_past,
            use_cache=use_cache,
        )
        x = x + attn_out
        x = x + self.ffn(self.norm2(x))
        return x, present
class Transformer(nn.Module):
    def __init__(
            self, dim: int, attn_dim: int, mlp_dim: int, num_heads: int, num_layers: int
    ):
        super().__init__()
        self.layers = nn.ModuleList(
            [
                AttentionResidual(dim, attn_dim, mlp_dim, num_heads)
                for _ in range(num_layers)
            ]
        )

    def forward(
            self,
            x: torch.Tensor,
            attn_mask: Optional[torch.Tensor] = None,
            layer_past: Optional[List[Tuple[torch.Tensor, torch.Tensor]]] = None,
            use_cache: bool = False,
    ) -> Tuple[torch.Tensor, Optional[List[Tuple[torch.Tensor, torch.Tensor]]]]:
        presents = [] if use_cache else None

        for i, layer in enumerate(self.layers):
            past_kv = layer_past[i] if layer_past is not None else None
            x, present_kv = layer(
                x,
                attn_mask=attn_mask,
                layer_past=past_kv,
                use_cache=use_cache,
            )
            if use_cache:
                presents.append(present_kv)

        return x, presents


class DialogueGPT(nn.Module):
    def __init__(
            self,
            vocab_size: int,
            max_N: int,
            dim: int,
            attn_dim: int,
            mlp_dim: int,
            num_heads: int,
            num_layers: int,
    ):
        super().__init__()
        self.token_embeddings = nn.Embedding(vocab_size, dim)
        self.pos_embeddings = nn.Embedding(max_N, dim)
        self.transformer = Transformer(
            dim=dim,
            attn_dim=attn_dim,
            mlp_dim=mlp_dim,
            num_heads=num_heads,
            num_layers=num_layers,
        )
        self.head = nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim, vocab_size))

    def forward(
            self,
            input_ids: torch.Tensor,
            layer_past: Optional[List[Tuple[torch.Tensor, torch.Tensor]]] = None,
            use_cache: bool = False,
    ):
        B, T = input_ids.shape

        past_length = layer_past[0][0].shape[-2] if layer_past is not None else 0
        pos_ids = torch.arange(
            past_length, past_length + T, dtype=torch.long, device=input_ids.device
        ).unsqueeze(0)

        embs = self.token_embeddings(input_ids) + self.pos_embeddings(pos_ids)

        # Causal mask across full prompt sequence length
        if layer_past is None and T > 1:
            causal_attn_mask = (
                                   torch.tril(torch.ones(T, T, device=input_ids.device))
                                   .unsqueeze(0)
                                   .expand(B, -1, -1)
                               ) == 1
        else:
            causal_attn_mask = None

        x, presents = self.transformer(
            embs,
            attn_mask=causal_attn_mask,
            layer_past=layer_past,
            use_cache=use_cache,
        )
        logits = self.head(x)

        if use_cache:
            return logits, presents
        return logits

    @torch.inference_mode()
    def key_value_cached_generation(self, input_ids: torch.Tensor, num_tokens: int):
        # 1. Pre-fill: process prompt, obtain initial cache
        out, cache = self.forward(input_ids, use_cache=True)
        new_token = torch.argmax(out[:, [-1], :], dim=-1)
        input_ids = torch.cat([input_ids, new_token], dim=1)

        # 2. Decode: pass single newest token and update cache
        for _ in range(num_tokens - 1):
            out, cache = self.forward(new_token, layer_past=cache, use_cache=True)
            new_token = torch.argmax(out[:, [-1], :], dim=-1)
            input_ids = torch.cat([input_ids, new_token], dim=1)

        return input_ids


class DialogueLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.criterion = nn.CrossEntropyLoss(reduction="none")

    def forward(
            self, logits: torch.Tensor, input_ids: torch.Tensor, inp_mask: torch.Tensor
    ):
        relevant_logits = logits[:, :-1, :].permute(0, 2, 1)  # (B, V, T-1)
        relevant_tokens = input_ids[:, 1:]                   # (B, T-1)
        shift_mask = inp_mask[:, 1:].to(logits.dtype)         # (B, T-1)

        loss = self.criterion(relevant_logits, relevant_tokens)
        masked_loss = loss * shift_mask

        return torch.sum(masked_loss) / torch.clamp(torch.sum(shift_mask), min=1e-9)


# --- Training Execution ---
def save_checkpoint(state: Dict[str, Any],
                    is_best: bool,
                    checkpoint_dir: str = "checkpoints",
                    filename: str = "last_checkpoint.pt",
                    best_filename: str = "best_checkpoint.pt")-> None:
    """Saves model weights, optimizer/scheduler states,
     and torchmetrics results."""
    os.makedirs(checkpoint_dir, exist_ok=True)
    filepath = os.path.join(checkpoint_dir,filename)
    torch.save(state,filepath)

    if is_best:
        best_filepath = os.path.join(checkpoint_dir,best_filename)
        torch.save(state,best_filepath)
        print(
            f"[*] Best model saved at Epoch {state['epoch']} | "
            f"Val Loss: {state['metrics']['val_loss']:.4f} | "
            f"Val PPL: {state['metrics']['val_ppl']:.2f} | "
            f"Val Acc: {state['metrics']['val_acc'] * 100:.2f}%"
        )

def load_checkpoint(
        checkpoint_path: str,
        model: torch.nn.Module,
        optimizer: Optional[torch.optim.Optimizer] = None,
        scheduler: Optional[torch.optim.lr_scheduler._LRScheduler] = None,
        device: str = "cpu",
) -> int:
    """Loads weights and states from an existing checkpoint to resume training.

    Args:
        checkpoint_path (str): Path to the saved `.pt` checkpoint file.
        model (torch.nn.Module): The model to restore weights into.
        optimizer (Optional[Optimizer], optional): Optimizer to restore state into.
        scheduler (Optional[_LRScheduler], optional): Scheduler to restore state into.
        device (str, optional): Computation device. Defaults to "cpu".

    Returns:
        int: The next epoch number to resume training from.
    """
    if not os.path.isfile(checkpoint_path):
        print(f"[!] No checkpoint found at '{checkpoint_path}'. Starting from scratch.")
        return 0

    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])

    if optimizer is not None and "optimizer_state_dict" in checkpoint:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

    if scheduler is not None and "scheduler_state_dict" in checkpoint:
        scheduler.load_state_dict(checkpoint["scheduler_state_dict"])

    start_epoch = checkpoint.get("epoch", -1) + 1
    loss = checkpoint.get("loss", float("inf"))
    print(f"[+] Loaded checkpoint from '{checkpoint_path}' (Resuming at epoch {start_epoch}, prior loss: {loss:.4f})")
    return start_epoch
CHECKPOINT_DIR = "checkpoints"
RESUME_CHECKPOINT = os.path.join(CHECKPOINT_DIR, "last_checkpoint.pt")

def main():
    pad_id = tok.tok_to_id[tok.pad]
    train_loss_metric = MeanMetric().to(device)
    train_acc_metric = MulticlassAccuracy(
        num_classes=tok.vocab_size, ignore_index=pad_id
    ).to(device)
    train_ppl_metric = Perplexity(ignore_index=pad_id).to(device)

    val_loss_metric = MeanMetric().to(device)
    val_acc_metric = MulticlassAccuracy(
        num_classes=tok.vocab_size, ignore_index=pad_id
    ).to(device)
    val_ppl_metric = Perplexity(ignore_index=pad_id).to(device)
    BATCH_SIZE = 16
    BUFFER_SIZE = 4
    NUM_EPOCHS = 80

    ds = DialogueDataset(tok, all_dialogues, max_N=200)
    train_dl = DataLoader(
        ds,
        batch_size=BATCH_SIZE,

        collate_fn=DialogueCollateFn(tok),
        pin_memory=torch.cuda.is_available(),
    )

    model = DialogueGPT(
        vocab_size=tok.vocab_size,
        max_N=200,
        dim=128,
        attn_dim=64,
        mlp_dim=128,
        num_heads=3,
        num_layers=6,
    ).to(device)

    criterion = DialogueLoss()
    optimizer = optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.01)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS, eta_min=1e-6)

    result = TrainResult(train_losses=[], train_accs=[], val_accs=[], val_losses=[])

    CHECKPOINT_DIR = "checkpoints"
    RESUME_CHECKPOINT = os.path.join(CHECKPOINT_DIR, "last_checkpoint.pt")

    best_val_loss = float("inf")
    start_epoch = 0

    if os.path.exists(RESUME_CHECKPOINT):
        start_epoch = load_checkpoint(
            RESUME_CHECKPOINT,
            model=model,
            optimizer=optimizer,
            scheduler=scheduler,
            device=device,
        )
        best_path = os.path.join(CHECKPOINT_DIR, "best_checkpoint.pt")
        if os.path.exists(best_path):
            ckpt_data = torch.load(best_path)
            best_val_loss = ckpt_data.get("metrics", {}).get("val_loss", float("inf"))

    for epoch in range(start_epoch, NUM_EPOCHS):
        # -------------------------------------------------------------
        # 1. Training Phase
        # -------------------------------------------------------------
        model.train()
        train_loss_metric.reset()
        train_acc_metric.reset()
        train_ppl_metric.reset()
        optimizer.zero_grad()

        pbar = tqdm.tqdm(enumerate(train_dl), desc=f"Train Epoch {epoch:02d}", total=len(train_dl))
        for step, batch in pbar:
            inp_ids = batch["input_ids"].to(device, non_blocking=True)
            inp_mask = batch["input_mask"].to(device, non_blocking=True)

            logits = model(inp_ids)
            loss = criterion(logits, inp_ids, inp_mask)

            # Gradient accumulation
            (loss / BUFFER_SIZE).backward()

            if (step + 1) % BUFFER_SIZE == 0 or (step + 1) == len(train_dl):
                optimizer.step()
                optimizer.zero_grad()

            # Update training metrics on shifted targets (next-token prediction)
            shift_logits = logits[:, :-1, :].contiguous()
            shift_targets = inp_ids[:, 1:].contiguous()
            # Overwrite masked positions with pad_id for torchmetrics ignore_index
            shift_targets = torch.where(inp_mask[:, 1:] == 1, shift_targets, pad_id)

            train_loss_metric.update(loss.item(), weight=inp_ids.size(0))
            train_acc_metric.update(shift_logits.argmax(dim=-1), shift_targets)
            train_ppl_metric.update(shift_logits, shift_targets)

            pbar.set_postfix(
                loss=f"{train_loss_metric.compute().item():.4f}",
                acc=f"{train_acc_metric.compute().item() * 100:.1f}%",
            )

        scheduler.step()

        # Compute final epoch training metrics
        epoch_train_loss = train_loss_metric.compute().item()
        epoch_train_acc = train_acc_metric.compute().item()
        epoch_train_ppl = train_ppl_metric.compute().item()

        # -------------------------------------------------------------
        # 2. Validation Phase (Optional / Recommended)
        # -------------------------------------------------------------
        model.eval()
        val_loss_metric.reset()
        val_acc_metric.reset()
        val_ppl_metric.reset()

        # If you have a val_dl, iterate over it (or use train_dl subset for tracking)
        if "val_dl" in locals():
            with torch.no_grad():
                for batch in val_dl:
                    v_ids = batch["input_ids"].to(device)
                    v_mask = batch["input_mask"].to(device)
                    v_logits = model(v_ids)
                    v_loss = criterion(v_logits, v_ids, v_mask)

                    v_shift_logits = v_logits[:, :-1, :].contiguous()
                    v_shift_targets = torch.where(v_mask[:, 1:] == 1, v_ids[:, 1:], pad_id)

                    val_loss_metric.update(v_loss.item(), weight=v_ids.size(0))
                    val_acc_metric.update(v_shift_logits.argmax(dim=-1), v_shift_targets)
                    val_ppl_metric.update(v_shift_logits, v_shift_targets)

            epoch_val_loss = val_loss_metric.compute().item()
            epoch_val_acc = val_acc_metric.compute().item()
            epoch_val_ppl = val_ppl_metric.compute().item()
        else:
            # Default fallback to train loss if no validation set is defined
            epoch_val_loss = epoch_train_loss
            epoch_val_acc = epoch_train_acc
            epoch_val_ppl = epoch_train_ppl

        # -------------------------------------------------------------
        # 3. Save Checkpoint with Metrics Payload
        # -------------------------------------------------------------
        is_best = epoch_val_loss < best_val_loss
        if is_best:
            best_val_loss = epoch_val_loss

        checkpoint_payload = {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "scheduler_state_dict": scheduler.state_dict(),
            "metrics": {
                "train_loss": epoch_train_loss,
                "train_acc": epoch_train_acc,
                "train_ppl": epoch_train_ppl,
                "val_loss": epoch_val_loss,
                "val_acc": epoch_val_acc,
                "val_ppl": epoch_val_ppl,
            },
        }

        save_checkpoint(
            state=checkpoint_payload,
            is_best=is_best,
            checkpoint_dir=CHECKPOINT_DIR,
        )

        print(
            f"\n[Epoch {epoch:02d} Summary] "
            f"Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc * 100:.2f}% | Train PPL: {epoch_train_ppl:.2f} || "
            f"Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc * 100:.2f}% | Val PPL: {epoch_val_ppl:.2f}"
        )

        clean_memory_cache()

main()