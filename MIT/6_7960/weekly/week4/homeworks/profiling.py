import torch
import torch.nn as nn

# 1. Setup simple linear operation
linear_layer = nn.Linear(in_features=4096, out_features=4096)
x = torch.randn(1024, 4096)

# 2. Run the profiler with the TensorBoard trace handler
with torch.profiler.profile(
        activities=[torch.profiler.ProfilerActivity.CPU], # Add .CUDA here if using a GPU
        schedule=torch.profiler.schedule(wait=1, warmup=1, active=3, repeat=1),
        on_trace_ready=torch.profiler.tensorboard_trace_handler('./log/linear_profile'),
        record_shapes=True,
        profile_memory=True
) as prof:

    # Run a few iterations to satisfy the scheduler (wait, warmup, active)
    for step in range(5):
        y = linear_layer(x)
        prof.step()  # Crucial: signals the profiler to advance steps
