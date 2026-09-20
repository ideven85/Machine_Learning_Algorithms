import torch

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.mps.is_available() else "cpu"
)

x = torch.rand(3, 4)

dummy = torch.nn.Linear(in_features=x.shape[-1], out_features=1)

print(dummy(x).shape)

print(device)
