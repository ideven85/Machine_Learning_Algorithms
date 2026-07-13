from typing import *
import abc
import torch


# This is our Module API
class Module(abc.ABC):
    device: Optional[torch.device]  # Parameters should live on this device!
    inputs: Tuple[torch.Tensor, ...]

    def __init__(self, device=None):
        self.device = device

    @abc.abstractmethod
    def parameters(self) -> Iterator[torch.Tensor]:
        r"""
        Returns an iterator over the *parameters* of this module.

        Subclass needs to implement this.
        """

    @abc.abstractmethod
    def forward(self, *inputs: torch.Tensor) -> torch.Tensor:
        r"""
        Returns the output of applying this module on tensors `inputs`, each of
        which is a *batched* tensor.

        In most cases, the module takes a single input tensor (e.g., linear
        layer and ReLU layers). However, multiple inputs are useful when the
        module computes a loss between a prediction and groundtruth target.

        Subclass needs to implement this.
        """

    def __call__(self, *inputs: torch.Tensor) -> torch.Tensor:
        r"""
        Simply calls forward, and stores inputs at `self.inputs`, which may be
        useful for computing gradients in `backward`.
        """
        self.inputs = inputs
        return self.forward(*inputs)

    @abc.abstractmethod
    def backward(self, dLdout: torch.Tensor) -> torch.Tensor:
        r"""
        This is our manual backprop.

        Given, `dLdOut` as $dL / d output$, for some loss `L`, we compute
        1. For each parameter `p` of this module, compute $d L /d p$, stored at `p.grad`.
        2. $dL / d self.inputs[0]$, to be passed to the previous layer. Only
           needs to compute derivative of the first input.

        Note that $dL / d *$ should always be a tensor of same shape as *. E.g.,
        $d L /d p$ (i.e., `p.grad`) should always be of the same shape as `p`.

        Subclass needs to implement this.
        """

    def zero_grad(self):
        r"""
        Clear any previous computed gradients.
        """
        for p in self.parameters():
            p.grad = None


class Linear(Module):
    def __init__(self, in_features: int, out_features: int, device=None):
        super().__init__(device)
        self.in_features = in_features
        self.out_features = out_features
        self.weight = (
            torch.randn(out_features, in_features, device=device) / in_features
        )  # weight matrix
        self.bias = torch.zeros(out_features, device=device)  # bias vector

    def parameters(self) -> Iterator[torch.Tensor]:
        return [self.weight, self.bias]

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x           shape: [b, in_features]
        # self.weight shape: [out_features, in_features]
        # self.bias   shape: [out_features]
        #
        # output should have shape: [b, out_features]
        #
        # FIXME
        pass

    def backward(self, dLdout: torch.Tensor) -> torch.Tensor:
        # self.inputs[0] shape: [b, in_features]
        # dLdout         shape: [b, out_features]
        # self.weight    shape: [out_features, in_features]
        # self.bias      shape: [out_featurs]
        #
        # FIXME
        # Note that you should *not* modify `dLdout` or `self.inputs` inplace.
        pass

    def __repr__(self) -> str:
        return f"Linear(in={self.in_features}, out={self.out_features})"


class ReLU(Module):
    def parameters(self) -> Iterator[torch.Tensor]:
        return []

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x.clamp(min=0)

    def backward(self, dLdout: torch.Tensor) -> torch.Tensor:
        # self.inputs[0]  shape: [b, d]
        # dLdout          shape: [b, d]
        #
        # FIXME
        # Note that you should *not* modify `dLdout` or `self.inputs` inplace.
        pass

    def __repr__(self) -> str:
        return "ReLU()"


class CrossEntropyLoss(Module):
    def parameters(self) -> Iterator[torch.Tensor]:
        return []

    def forward(self, logits: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        # logits    shape: [b, num_classes]
        # target    shape: [b], containing *integers* in [0, 1, ..., num_classes - 1]
        #
        # For each logits in the batch
        #   p = softmax(logits)
        #   loss = -log(p[target])
        # Total loss is averaged across the entire batch.
        b = logits.shape[0]
        return (
            -logits.softmax(dim=-1)
            .log()[torch.arange(b, device=self.device), target]
            .mean()
        )  # scalar, shape: []

    def backward(self, dLdout: torch.Tensor) -> torch.Tensor:
        logits, target = self.inputs
        # logits    shape: [b, num_classes]
        # target    shape: [b], containing *integers* in [0, 1, ..., num_classes - 1]
        # dLdout    shape: []
        #
        # FIXME
        # Note that you should *not* modify `dLdout` or `self.inputs` inplace.
        # Compute dL / d logits
        pass

    def __repr__(self) -> str:
        return "CrossEntropyLoss()"


import doctest

doctest.testmod(verbose=True)
