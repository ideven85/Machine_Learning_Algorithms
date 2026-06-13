To truly understand how **LSTMs (Long Short-Term Memory)** and **GRUs (Gated Recurrent Units)** work, we have to look at the problem they were invented to solve: the failure of the standard Recurrent Neural Network (RNN).

In a standard RNN, data flows sequentially through time. However, because the network performs the exact same matrix multiplications step after step, gradients flowing back through time get multiplied repeatedly. This causes them to either blow up exponentially or completely vanish to zero (**Vanishing Gradient Problem**). In practice, a standard RNN completely forgets what it saw just 10 or 20 steps ago.

LSTMs and GRUs fix this by introducing internal **gates**—mathematical operations that control exactly how much information is allowed to be written, forgotten, or read at any given time step.

---

## 1. Long Short-Term Memory (LSTM)

An LSTM maintains an internal "information highway" called the **Cell State ($C_t$)**. Information can flow down this highway with almost no modification, preventing gradients from vanishing over hundreds of steps.

An LSTM regulates this cell state using three distinct gating mechanisms:

### Step 1: The Forget Gate ($f_t$)

Decides what information to throw away from the previous cell state. It looks at the current input ($x_t$) and the previous hidden state ($h_{t-1}$), running them through a sigmoid activation function ($\sigma$).


$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$

* If $f_t = 0$, the model completely wipes out that memory.
* If $f_t = 1$, the model preserves the memory perfectly.

### Step 2: The Input Gate ($i_t$) & Candidate State ($\tilde{C}_t$)

Decides what brand-new information to add to the cell state.

* The **Input Gate ($i_t$)** acts as a filter determining *which* values to update:

$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$


* The **Candidate State ($\tilde{C}_t$)** generates a vector of new prospective values using a `tanh` function:

$$\tilde{C}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$



### Step 3: Updating the Cell State ($C_t$)

The old cell state ($C_{t-1}$) is multiplied by the forget gate, and the new candidate information is added, scaled by the input gate:


$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$

### Step 4: The Output Gate ($h_t$)

Decides what the final visible **Hidden State ($h_t$)** should be for this time step. The updated cell state is pushed through a `tanh` layer and scaled by the output gate:


$$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$

$$h_t = o_t \odot \tanh(C_t)$$

---

## 2. Gated Recurrent Unit (GRU)

Invented in 2014 by Cho et al., the GRU is a streamlined, more efficient version of the LSTM. It merges the Cell State and Hidden State into a single vector ($h_t$) and uses only **two gates**, making it computationally lighter and faster to train while retaining almost identical performance.

### Step 1: The Update Gate ($z_t$)

Combines the functionalities of the LSTM's forget and input gates. It decides how much historical context to keep versus how much new content to bring in.


$$z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)$$

### Step 2: The Reset Gate ($r_t$)

Determines how much of the past hidden state to completely forget when computing a new candidate memory.


$$r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)$$

### Step 3: The Candidate Hidden State ($\tilde{h}_t$)

Computes the current prospective content. If the reset gate $r_t$ is close to 0, it ignores the past context completely, acting like a fresh start:


$$\tilde{h}_t = \tanh(W \cdot [r_t \odot h_{t-1}, x_t] + b)$$

### Step 4: Final Hidden State Update ($h_t$)

The update gate $z_t$ linearly interpolates between the past state and the new candidate state:


$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$

---

## Key Comparison: LSTM vs. GRU

| Property | LSTM | GRU |
| --- | --- | --- |
| **State Vectors** | Two vectors: Cell State ($C_t$) and Hidden State ($h_t$) | One vector: Hidden State ($h_t$) |
| **Gating Mechanisms** | 3 Gates (Forget, Input, Output) | 2 Gates (Update, Reset) |
| **Parameter Count** | Higher (Slower compute, prone to overfitting on small data) | Lower (Faster iterations, highly efficient) |
| **Expressivity** | Can maintain separate long-term vs. short-term tracks | Blends tracks linearly |

Would you like to walk through a quick vectorized tensor dimension example to see how the shapes map when processing a batch of sequences?