from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

import nltk
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import copy

import numpy as np
import sklearn
import torch
import torch.nn.functional as F
import torchvision
import tqdm
from sklearn.metrics import confusion_matrix
from torch import nn, optim
from torch.utils.data import DataLoader, Subset
from torchvision import transforms
import torch.optim as optim

file = "shakespeare.txt"
with open(file, "r") as f:
    dialogues = f.read()

all_dialogues = dialogues.split("\n\n")


def tokenize(s):
    return nltk.word_tokenize(s)


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


class DialogueDataset:
    def __init__(self, tokenizer: MyTokenizer, lines: List[str], max_N: int):
        # tokenizer    an instance of MyTokenizer
        # lines        a list of strings. each element in an example in the dataset
        # max_N        the maximum number of tokens allowed per example. More than this will be truncated
        self.lines = lines
        self.tokenizer = tokenizer
        self.max_N = max_N

    def __len__(self) -> int:
        return len(self.lines)

    # def __iter__(self):
    #     for line in self.lines:
    #         yield self.tokenizer.encode(line)[: self.max_N]

    def __getitem__(self, idx: int) -> torch.Tensor:
        # returns the example at int encoded by the tokenizer
        # truncates the example if it is more than max_N tokens
        return self.tokenizer.encode(self.lines[idx])[: self.max_N]

    # def __getitems__(self,indices:int):
    #     return [self.__getitem__(idx) for idx in indices]


def collate_fn(examples: List[torch.Tensor]):
    """
    # examples        a batch of tensors containing token ids (maybe of different lengths)
    # Outputs a dictionary containing
    #   input_ids     a single tensor with all of the examples padded (from the right) to the max
    #                 length within the batch. shape:(B, max length within examples)
    #   input_mask    a tensor indicating which tokens are padding and should be ignored. 0 if padding
    #                 and 1 if not. shape: (B, max length within examples)
    """
    new_input_ids = tok.pad_examples(examples)
    attn_mask = torch.ones(new_input_ids.shape)  # 1s should not be ignored

    # causal attention mask
    attn_mask[new_input_ids == tok.tok_to_id[tok.pad]] = (
        0  # should be ignored if it is a padded
    )
    return {"input_ids": new_input_ids, "input_mask": attn_mask}


ds = DialogueDataset(tok, all_dialogues, max_N=200)

train_dl = DataLoader(ds, batch_size=16, num_workers=0, collate_fn=collate_fn)
BATCH_SIZE = 16
BUFFER_SIZE = 4


torch.autograd.set_detect_anomaly(True)
device = (
    torch.accelerator.current_accelerator().type
    if torch.accelerator.is_available()
    else "cpu"
)
import os

num_workers = min(0, os.cpu_count())
import logging

# Configure logging to write directly to a file
logging.basicConfig(
    filename="vit.log",
    filemode="a",  # 'a' appends to the file, 'w' overwrites it on every run
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
import gc

import torch


def clean_memory_cache():

    if torch.mps.is_available():
        print(
            f"Before Clearing, Available memory: {torch.mps.driver_allocated_memory() / 1024 / 1024:.2f} MB"
        )
        gc.collect()
        torch.mps.empty_cache()
    elif torch.cuda.is_available():
        print(
            f"Before Clearing, Available memory: {torch.cuda.memory_allocated() / 1024 / 1024:.2f} MB"
        )
        gc.collect()
        torch.cuda.empty_cache()
    else:
        gc.collect()
        return


@dataclass(init=True)
class TrainResult:
    """
    A collection containing everything we need to know about the training results
    """

    train_losses: List[float]
    train_accs: List[float]
    val_accs: List[float]
    val_losses: List[float]


result = TrainResult(train_losses=[], train_accs=[], val_accs=[], val_losses=[])


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


def print_variance(name: str, data: torch.Tensor):
    # Compute variance across features/neurons and average across the batch
    neuron_variance = torch.mean(torch.var(data.detach().float(), dim=-1))
    print(f"{name}: Variance = {neuron_variance.item():.6f}")


class MultiHeadedAttention(nn.Module):
    def __init__(self, dim: int, n_hidden: int, num_heads: int):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.n_hidden = n_hidden
        self.scale = n_hidden**-0.5

        self.qkv_projection = nn.Linear(dim, num_heads * n_hidden * 3, bias=False)
        self.W0 = nn.Linear(num_heads * n_hidden, dim)

    def forward(
        self,
        x: torch.Tensor,
        attn_mask: Optional[torch.Tensor] = None,
        layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        use_cache: bool = False,
    ) -> Tuple[torch.Tensor, Optional[Tuple[torch.Tensor, torch.Tensor]]]:
        B, T, _ = x.shape

        qkv = (
            self.qkv_projection(x)
            .reshape(B, T, self.num_heads, 3 * self.n_hidden)
            .transpose(1, 2)
        )
        q, k, v = qkv.chunk(3, dim=-1)

        if layer_past is not None:
            past_k, past_v = layer_past
            k = torch.cat([past_k, k], dim=-2)
            v = torch.cat([past_v, v], dim=-2)

        present = (k, v) if use_cache else None

        # --- THE BROADCASTING FIX ---
        if attn_mask is not None:
            # If mask is (B, T, T), expand to (B, 1, T, T)
            if attn_mask.dim() == 3:
                attn_mask = attn_mask.unsqueeze(1)
            # If mask is (T, T), expand to (1, 1, T, T)
            elif attn_mask.dim() == 2:
                attn_mask = attn_mask.unsqueeze(0).unsqueeze(0)

        # When using an explicit attn_mask, is_causal MUST be False
        is_causal = (attn_mask is None) and (T > 1) and (layer_past is None)

        context = F.scaled_dot_product_attention(
            q, k, v, attn_mask=attn_mask, is_causal=is_causal
        )

        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(B, T, self.num_heads * self.n_hidden)
        )
        output = self.W0(context)
        return output, present


class AttentionResidual(nn.Module):
    def __init__(self, dim: int, attn_dim: int, mlp_dim: int, num_heads: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)

        self.attn = MultiHeadedAttention(dim, attn_dim, num_heads)
        # self.attn = OptimizedAttentionLayer(dim,attn_dim, num_heads)
        # LayerNorm applied inside the FFN sequence only
        self.norm2 = nn.LayerNorm(dim)
        self.ffn = nn.Sequential(
            # nn.LayerNorm(dim),
            nn.Linear(dim, mlp_dim),
            nn.GELU(),
            nn.Linear(mlp_dim, dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        attn_mask: Optional[torch.Tensor] = None,
        layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        use_cache: bool = False,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Attention block with residual connection (no norm)
        attn_out, alphas = self.attn(
            x=self.norm1(x),
            attn_mask=attn_mask,
            layer_past=layer_past,
            use_cache=use_cache,
        )
        x = x + attn_out

        # FFN block with residual connection (norm is first layer inside self.ffn)
        x = x + self.ffn(self.norm2(x))
        return x, alphas


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
        return_attn: bool = False,
        layer_past: Optional[List[Tuple[torch.Tensor, torch.Tensor]]] = None,
        use_cache: bool = False,
    ) -> Tuple[
        torch.Tensor,
        Optional[torch.Tensor],
        Optional[List[Tuple[torch.Tensor, torch.Tensor]]],
    ]:
        presents = [] if use_cache else None

        for i, layer in enumerate(self.layers):
            # Extract layer-specific cache safely
            past_kv = layer_past[i] if layer_past is not None else None

            x, present_kv = layer(
                x,
                attn_mask=attn_mask,
                layer_past=past_kv,
                use_cache=use_cache,
            )
            if use_cache:
                presents.append(present_kv)

        return x, None, presents


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
        return_attn: bool = False,
        layer_past: Optional[List[Tuple[torch.Tensor, torch.Tensor]]] = None,
        use_cache: bool = False,
    ):
        B, T = input_ids.shape

        # Offset positions by the number of cached tokens
        past_length = layer_past[0][0].shape[-2] if layer_past is not None else 0
        pos_ids = torch.arange(
            past_length, past_length + T, dtype=torch.long, device=input_ids.device
        ).unsqueeze(0)

        embs = self.token_embeddings(input_ids) + self.pos_embeddings(pos_ids)

        # Causal mask is only needed for sequences longer than 1 when NOT using cache
        if layer_past is None and T > 1:
            causal_attn_mask = (
                torch.tril(torch.ones(T, T, device=input_ids.device))
                .unsqueeze(0)
                .repeat(B, 1, 1)
            ) == 1
        else:
            causal_attn_mask = None

        x, alphas, presents = self.transformer(
            embs,
            attn_mask=causal_attn_mask,
            return_attn=return_attn,
            layer_past=layer_past,
            use_cache=use_cache,
        )
        out = self.head(x)

        # Return presents ONLY when caching is explicitly requested
        if use_cache:
            return out, alphas, presents
        return out, alphas

    def key_value_cached_generation(self, input_ids: torch.Tensor, num_tokens: int):
        with torch.no_grad():
            # 1. Pre-fill: process prompt, obtain initial cache
            out, _, cache = self.forward(input_ids, use_cache=True)
            new_token = torch.argmax(out[:, [-1]], dim=-1)
            input_ids = torch.cat([input_ids, new_token], dim=1)

            # 2. Decode: pass only the single newest token and update cache
            for _ in range(num_tokens - 1):
                out, _, cache = self.forward(
                    new_token, layer_past=cache, use_cache=True
                )
                new_token = torch.argmax(out[:, [-1]], dim=-1)
                input_ids = torch.cat([input_ids, new_token], dim=1)

        return input_ids


class DialogueLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.criterion = nn.CrossEntropyLoss(reduction="none")

    def forward(
        self, logits: torch.Tensor, input_ids: torch.Tensor, inp_mask: torch.Tensor
    ):
        """
        # logits      the logits produced by DialogueGPT. shape: (B x T x V)
        # input_ids   the token ids. shape: (B x T)
        # inp_mask    a 0/1 mask of which tokens are padding tokens and should be ignored. shape: (B x T)

        TODO: Implement the language model loss. For logits[i], we want to supervise the i+1 token_id with the cross entropy loss. We thus will not supervise the start token (input_ids[0]) or use the last logit vector (logits[-1]). Return the average of the losses for each token in the batch, making sure to ignore tokens corresponding to the padding (use inp_mask).
        """
        loss = 0

        # start_token = input_ids[0]
        relevant_logits = logits[:, :-1, :]
        # print(f"{logits.shape=},{relevant_logits.shape=}")
        relevant_tokens = input_ids[:, 1:]
        shift_mask = inp_mask[:, 1:]
        relevant_logits = relevant_logits.permute(0, 2, 1)
        # print(f"{relevant_logits.shape=}")

        loss = self.criterion(relevant_logits, relevant_tokens)
        shift_mask = shift_mask.to(dtype=loss.dtype, device=loss.device)
        loss *= shift_mask

        return torch.sum(loss) / torch.clamp(torch.sum(shift_mask), min=1e-9)


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
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

    NUM_EPOCHS = 80

    optimizer = optim.AdamW(
        model.parameters(), lr=0.0001, weight_decay=0
    )  # implement in homework
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS)

    # Ensure optimizer starts completely clean before the epoch loop begins
    optimizer.zero_grad()

    for epoch in range(NUM_EPOCHS):
        loss_meter = AverageMeter()

        # Wrap your loader securely
        for step, inp_dict in tqdm.tqdm(
            enumerate(train_dl), desc=f"Training at {epoch}", total=len(train_dl)
        ):
            inp_ids, inp_mask = inp_dict["input_ids"], inp_dict["input_mask"]

            inp_ids = inp_ids.to(device).long()
            inp_mask = inp_mask.to(device)

            # 1. Forward Pass
            outputs, _ = model(input_ids=inp_ids)

            # 2. FIX: Scale the loss down by BUFFER_SIZE to normalize gradients
            loss = criterion(outputs, inp_ids, inp_mask)
            scaled_loss = loss / BUFFER_SIZE

            # 3. Backward Pass (Accumulates gradients safely)
            scaled_loss.backward()

            # Track the true unscaled loss in your meter
            loss_meter.update(loss.item(), len(inp_dict["input_ids"]))

            # 4. FIX: Step the optimizer on buffer limit OR at the final step of the dataset
            if (step + 1) % BUFFER_SIZE == 0 or (step + 1) == len(train_dl):
                optimizer.step()
                optimizer.zero_grad()  # Resets the buffer for the next accumulation block

                # OPTIONAL: If your scheduler decays per-step instead of per-epoch,
                # place `scheduler.step()` right here.

        # 5. Step scheduler at the epoch level (if using an epoch-based scheduler)
        scheduler.step()

        # 6. Safe Text Generation Example (Switched to eval/inference mode to protect memory buffers)
        model.eval()
        with torch.inference_mode():
            # Ensure your start prompt token matches your vocabulary bounds
            inp = tok.encode("").unsqueeze(0).to(device)
            generated_output = model.key_value_cached_generation(inp, 10)
            print(f"\n[Generated Sample]: {tok.decode(generated_output[0][1:].cpu())}")

        model.train()  # Switch back to training mode for the next epoch loop
        clean_memory_cache()

        print(
            f"Train Epoch: {epoch}, Loss: {loss_meter.calculate():0.4f}, LR: {scheduler.get_last_lr()[0]}"
        )


if __name__ == "__main__":
    main()
