from dataclasses import dataclass
from typing import List

import torch


@dataclass
class TrainResult:

    train_acc: List[float]

    test_acc: List[float]

    train_loss: List[float]

    test_loss: List[float]

    val_acc: List[float]

    val_loss: List[float]


def train_and_evaluate():
    pass


@torch.no_grad()
def evaluate():
    pass
