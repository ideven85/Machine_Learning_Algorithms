**Self-supervision through Random Segments with Autoregressive Coding (RandSAC)**  
[Tianyu Hua](https://arxiv.org/search/cs?searchtype=author&query=Hua,+T), [Yonglong Tian](https://arxiv.org/search/cs?searchtype=author&query=Tian,+Y), [Sucheng Ren](https://arxiv.org/search/cs?searchtype=author&query=Ren,+S), [Michalis Raptis](https://arxiv.org/search/cs?searchtype=author&query=Raptis,+M), [Hang Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+H), [Leonid Sigal](https://arxiv.org/search/cs?searchtype=author&query=Sigal,+L)  
Inspired by the success of self-supervised autoregressive representation learning in natural language (GPT and its variants), and advances in recent visual architecture design with Vision Transformers (ViTs), in this paper, we explore the effect various design choices have on the success of applying such training strategies for visual feature learning. Specifically, we introduce a novel strategy that we call Random Segments with Autoregressive Coding (RandSAC). In RandSAC, we group patch representations (image tokens) into hierarchically arranged segments; within each segment, tokens are predicted in parallel, similar to BERT, while across segment predictions are sequential, similar to GPT. We illustrate that randomized serialization of the segments significantly improves the performance and results in distribution over spatially-long (across-segments) and -short (within-segment) predictions which are effective for feature learning. We illustrate the pertinence of these design choices and explore alternatives on a number of datasets (e.g., CIFAR10, CIFAR100, ImageNet). While our pre-training strategy works with a vanilla Transformer, we also propose a conceptually simple, but highly effective, addition to the decoder that allows learnable skip-connections to encoder  
  
′  
s feature layers, which further improves the performance.  
  
**"Self-supervision through Random Segments with Autoregressive Coding"** **refers to RandSAC, a novel self-supervised learning framework introduced by Tianyu Hua et al. at ICLR** [0.6.2, 0.6.7]. The core premise of the framework is to adapt the powerful autoregressive pre-training strategies used in natural language processing (like **GPT**) to visual feature learning using **Vision Transformers (ViTs)** [ 0.6.2 ].   
  
Here is a breakdown of how the architecture works, its core mechanics, and why it is effective:   
  
1. The Core Architecture (Hybrid BERT + GPT)   
  
Traditional visual autoregressive models (like Image GPT) serialize dense image pixels or tokens linearly in a fixed raster order (left-to-right, top-to-bottom) [0.6.10]. This is incredibly computationally expensive and struggles with spatial relationships [ 0.6.10 ].   
  
**RandSAC solves this by grouping image patch tokens into hierarchically arranged, non-overlapping segments [ 0.6.2 ,  0.6.10 ] (e.g., splitting an image into spatial grids or 2 × 2 blocks [0.6.8]): **  
* **Within a segment (BERT-style):** The tokens are predicted in **parallel** [ 0.6.2 ].   
* **Across segments (GPT-style):** The segments themselves are predicted **sequentially** (autoregressively) [ 0.6.2 ].   
  
  
2. Randomized Serialization   
  
Instead of forcing the model to learn segments in a rigid, fixed sequence, RandSAC applies **randomized serialization** [ 0.6.2 ]. The order of the segments is completely scrambled during pre-training [ 0.6.8 , 0.6.9].   
  
**This dynamic ordering forces the model to capture two vital types of contextual information [ 0.6.2 ]: **  
* **Spatially-short dependencies:** Learning local context within a single parallelized segment [ 0.6.2 ].   
* **Spatially-long dependencies:** Learning global context by bridging predictions across distant segments [ 0.6.2 ].   
  
  
3. Learnable Skip-Connections   
  
While RandSAC functions effectively on a vanilla Vision Transformer, the authors introduced a highly potent addition to the decoder: **learnable skip-connections** from the encoder's feature layers [ 0.6.2 ]. This allows the representation layers to pass critical structural information forward, significantly boosting downstream feature representation and linear probing accuracy [ 0.6.2 , 0.6.4].   
  
Why it matters   
  
Unlike contrastive self-supervised learning methods (like SimCLR or MoCo), which require heavy data augmentations and suffer from an "object-centric bias," RandSAC doesn't make rigid assumptions about image invariances [ 0.6.8 ]. This makes the learned representations highly transferable to dense downstream tasks like **semantic segmentation** and object detection, achieving top-tier linear probing performance on benchmarks like ImageNet [ 0.6.4 ,  0.6.8 ].   
  
Are you looking to **implement this architecture** in PyTorch/Jax, or are you exploring how its **attention masking** operates technically? Let me know, and we can dive deeper!   
  
  
*AI can make mistakes, so double-check responses*  
