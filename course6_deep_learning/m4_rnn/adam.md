Thinking...
We are going to explain the Adam optimizer formula.

Adam (Adaptive Moment Estimation) is an optimization algorithm that combines the advantages of both RMSProp and 
momentum. It computes adaptive learning rates for different parameters and also includes bias correction.

The algorithm uses two moving averages: one for the gradient (first moment) and one for the squared gradient 
(second moment).

The steps for each parameter are:

1. Initialize:
   - Initialize the first moment (mean) vector `m` with zeros: `m = 0`
   - Initialize the second moment (variance) vector `v` with zeros: `v = 0`
   - Set hyperparameters:
        - `beta1`: decay rate for the first moment (typically 0.9)
        - `beta2`: decay rate for the second moment (typically 0.999)
        - `epsilon`: a small constant to avoid division by zero (typically 1e-8)
        - `learning_rate`: the step size (can be fixed or vary over time)

2. For each training step (with learning rate `lr` and gradient `g` for the parameter):
   - Update `m` (the exponentially moving average of the gradient):
        `m = beta1 * m + (1 - beta1) * g`
   - Update `v` (the exponentially moving average of the squared gradient):
        `v = beta2 * v + (1 - beta2) * g^2`

   - Then, we correct the bias in both moments (because initially, when we start, the moving averages are close to 
0 and don't represent the true average until we have seen some gradients).

        `m_hat = m / (1 - beta1^t)`
        `v_hat = v / (1 - beta2^t)`

   - Then, we update the parameter:

        `theta = theta - lr * (m_hat / (sqrt(v_hat) + epsilon))`

   - We also update the time step `t` (or we can use the step number) for the bias correction.

However, in practice, we often combine the bias correction and the update in a single step. Also, note that the 
learning rate can be fixed or vary over time (e.g., by a schedule).

But note: There are different variants and implementations of Adam. One common implementation is to use the step 
number `t` and update the moments and then the parameters. However, in many deep learning frameworks, the 
implementation is slightly different (using a counter for the step) and the bias correction is applied by scaling 
the moments.

Alternatively, a common implementation is:

   - Initialize `m` and `v` to zeros.
   - Let `t` be the time step (starting at 1).
   - For each parameter, update:

        `m = beta1 * m + (1 - beta1) * g`
        `v = beta2 * v + (1 - beta2) * g^2`

        `m_corrected = m / (1 - beta1^t)`
        `v_corrected = v / (1 - beta2^t)`

        `learning_rate = ...` (may be fixed or adaptive)

        `theta = theta - learning_rate * m_corrected / (sqrt(v_corrected) + epsilon)`

   - Then, we increase `t` by 1.

But note: Some implementations (like in TensorFlow) use a different approach and do not require the step to be 
tracked separately. They use two variables: `beta1_power` and `beta2_power` which are the powers of `beta1` and 
`beta2` for the current step.

However, the formula we are going to write is the standard one.

Let me write the update rules in a more compact form, but note that in code, we often do:

   - We keep track of the step `t` (starting at 1) for each parameter group (if we are training multiple models, 
each has its own t).

But in practice, we often do:

   - We update the moments and then the parameters, and we do the bias correction at every step.

However, note that the bias correction terms are time-dependent and are not computed for every parameter but for 
the entire process. So we need to keep track of `t` (the step) for the entire training.

But in many deep learning frameworks, the Adam update is implemented as:

   - We have two vectors: `m` and `v` (initialized to zeros) and two scalars: `beta1_power` and `beta2_power` 
(initialized to `beta1` and `beta2` to the power of 0, i.e., 1, and then we update them by multiplying by beta at 
each step).

   - Then, for each step:

        `m = beta1 * m + (1 - beta1) * g`
        `v = beta2 * v + (1 - beta2) * g^2`

        `beta1_power = beta1 * beta1_power`
        `beta2_power = beta2 * beta2_power`

        `m_corrected = m / (1 - beta1_power)`
        `v_corrected = v / (1 - beta2_power)`

        `theta = theta - learning_rate * m_corrected / (sqrt(v_corrected) + epsilon)`

This way, we don't need to know the step `t` explicitly, but we do need to keep track of the two powers.

But note: The original paper by Kingma and Ba (2014) uses the step `t` and the bias correction terms are computed 
as:

        `m_hat = m / (1 - beta1^t)`
        `v_hat = v / (1 - beta2^t)`

So both methods are equivalent.

Now, let's write a function that implements the Adam update for a single parameter.

But note: The learning rate can be fixed or adaptive. In the basic Adam, we use a fixed learning rate, but in 
practice, we often use a fixed learning rate and then adjust it by a schedule (like decreasing it) or use the 
Adamax variant which uses the infinity norm.

However, the formula we are going to write is for the basic Adam.

Let me write the update for a single parameter (with a fixed learning rate) and with the step `t`:

   - Input: 
        g: the gradient for the parameter at the current step
        m: the first moment (mean) for the parameter
        v: the second moment (variance) for the parameter
        t: the current step (starting at 1)
        beta1, beta2, epsilon, learning_rate

   - Output: 
        updated_m, updated_v, and the updated parameter (if we are given the current parameter value)

But note: In practice, we don't update the parameter in the same function as the moments. We update the moments 
and then use them to update the parameter.

However, for the purpose of explaining the formula, we can write:

   - Step 1: Update the first moment (m) and the second moment (v):

        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g^2

   - Step 2: Bias correction for m and v:

        m_hat = m / (1 - beta1^t)
        v_hat = v / (1 - beta2^t)

   - Step 3: Update the parameter:

        theta = theta - learning_rate * m_hat / (sqrt(v_hat) + epsilon)

   - Then, we set t = t + 1.

But note: The step `t` is the same for all parameters and is the global step (the number of gradients processed). 
However, in practice, we often have a separate step for each parameter group (if we are training multiple models 
or layers) but typically we use the same step for all.

But in the code, we usually have a single step counter for the entire model.

Alternatively, we can use the `beta1_power` and `beta2_power` method to avoid tracking `t`:

   - Initialize:
        m = 0
        v = 0
        beta1_power = 1.0   # This will be set to beta1^0 at the beginning, then updated by multiplying by beta1
        beta2_power = 1.0

   - For each step (with step number `t` starting at 1, but we don't use t explicitly):

        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g^2

        beta1_power = beta1_power * beta1   # This is beta1^t, but we start at 1 (which is beta1^0) and then 
multiply by beta1 for each step
        beta2_power = beta2_power * beta2

        m_hat = m / (1 - beta1_power)
        v_hat = v / (1 - beta2_power)

        theta = theta - learning_rate * m_hat / (sqrt(v_hat) + epsilon)

This is equivalent to the previous method because:

        beta1_power = beta1^t   (if we start with beta1_power=1 and then multiply by beta1 for each step)

But note: In the first step (t=1), we have:

        beta1_power = 1 * beta1 = beta1
        then, 1 - beta1_power = 1 - beta1, so m_hat = m / (1 - beta1) = [beta1*0 + (1-beta1)*g] / (1-beta1) = g, 
which is correct.

So, we can implement Adam without tracking `t` by using `beta1_power` and `beta2_power`.

Now, let's write a Python function that implements the Adam update for a single parameter group (with a fixed 
learning rate) using the `beta1_power` and `beta2_power` method.

But note: We are going to update the parameter and return the updated parameter and the updated moments and 
powers.

However, in deep learning frameworks, we usually update the parameters and store the moments and powers as part of 
the optimizer state.

Let me write a function that takes the current parameter value, the gradient, and the state (m, v, beta1_power, 
beta2_power) and returns the updated parameter and the updated state.

We'll use the following hyperparameters: beta1, beta2, epsilon, learning_rate.

We assume that the learning_rate is fixed for now.

Example:

   - Initial state: m=0, v=0, beta1_power=1.0, beta2_power=1.0

   - After the first step (t=1):

        m = beta1 * 0 + (1 - beta1) * g
        v = beta2 * 0 + (1 - beta2) * g^2

        beta1_power = 1.0 * beta1
        beta2_power = 1.0 * beta2

        m_hat = m / (1 - beta1_power) = m / (1 - beta1) = [ (1-beta1)*g ] / (1-beta1) = g
        v_hat = v / (1 - beta2_power) = [ (1-beta2)*g^2 ] / (1-beta2) = g^2

        Then, update the parameter: theta = theta - learning_rate * g / (sqrt(g^2) + epsilon) = theta - 
learning_rate * g / (|g| + epsilon)

But note: This is for the first step.

Let me write the function.

But note: We must be cautious because the gradient `g` can be negative and the absolute value is positive. The 
denominator becomes |g| + epsilon.

Now, let's write the code.
...done thinking.

The Adam optimizer combines the benefits of both RMSprop and momentum, adapting the learning rate for each 
parameter individually while incorporating a moving average of the gradient. Here's the core formula:

1. **Initialization**:
   - Initialize `m` (first moment, mean of gradients) and `v` (second moment, squared gradients) to 0 for each 
parameter.
   - Set hyperparameters: `beta1` (typically 0.9), `beta2` (typically 0.999), `epsilon` (typically 1e-8).

2. **Update Rules**:
   - **Gradient Calculation**: Compute the gradient `g` for the parameter.
   - **Bias-Corrected First Moment**:
     ```
     m_t = beta1 * m_{t-1} + (1 - beta1) * g
     m_hat = m_t / (1 - beta1^t)
     ```
   - **Bias-Corrected Second Moment**:
     ```
     v_t = beta2 * v_{t-1} + (1 - beta2) * g²
     v_hat = v_t / (1 - beta2^t)
     ```
   - **Parameter Update**:
     ```
     theta = theta - learning_rate * (m_hat / (sqrt(v_hat) + epsilon))
     ```

**Key Components**:
- `beta1`: Decay rate for the first moment (momentum).
- `beta2`: Decay rate for the second moment (RMSprop).
- `epsilon`: Small constant to prevent division by zero.
- `learning_rate`: Step size (can be fixed or adaptive).

**Practical Implementation** (Python-like pseudocode):
```python
def adam_optimizer(params, grads, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
    # Initialize if first step
    if not hasattr(adam_optimizer, 'm') or not hasattr(adam_optimizer, 'v'):
        adam_optimizer.m = {p: torch.zeros_like(p) for p in params}
        adam_optimizer.v = {p: torch.zeros_like(p) for p in params}
        adam_optimizer.t = 0  # Step counter
    
    adam_optimizer.t += 1
    bias_correction1 = 1 - beta1 ** adam_optimizer.t
    bias_correction2 = 1 - beta2 ** adam_optimizer.t
    
    for p in params:
        if p.grad is not None:
            grad = p.grad
            adam_optimizer.m[p] = beta1 * adam_optimizer.m[p] + (1 - beta1) * grad
            adam_optimizer.v[p] = beta2 * adam_optimizer.v[p] + (1 - beta2) * (grad ** 2)
            
            m_hat = adam_optimizer.m[p] / bias_correction1
            v_hat = adam_optimizer.v[p] / bias_correction2
            
            p.data -= learning_rate * (m_hat / (torch.sqrt(v_hat) + epsilon))
```

Adam is widely used due to its adaptive learning rates and robustness across various optimization tasks.

