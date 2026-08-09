import os
import torch

size = int(os.path.getsize("best_model_10.pt"))
print(f"Model 2 Size {os.path.getsize('best_model_10.pt'):.4f}")
if size > 1000:
    model = torch.load("best_model_10.pt", weights_only=False)
    print(model.get_submodule("conv1").weight.shape)
