# Generative Modeling  
  
# Deep generative models I  
  
## Overview  
  
• Math background  
• Fundamentals of generative modeling  
• Density functions, energy functions, and samplers  
• Autoregressive models  
• Diffusion models  
• Generative adversarial networks  
  
  
Neural Networks as probability distributions:  
  
  
Say regression as a neural network mean is outcome and loss is l2 norm which comes from Gaussian distribution  
  
Deep generative models are a class of machine learning models that are capable of generating new data samples that resemble a given dataset. They learn the underlying distribution of the data and use this knowledge to create new instances that are similar to the original data but not identical to any specific  
training examples. Do this by making a generator, a stochastic function ( a mathematical function that yields a random variable or incorporates statistical noise rather than a single fixed output has D**ual nature:** For any fixed input value (such as time t), a stochastic function acts as a **random variable**. For any fixed experimental run or realization, it acts as a **determinate function**.  
  
  
  
A common strategy in unsupervised learning is to define a mapping between the data examples x and a set of unseen latent variables z. These latent variables capture un-derlying structure in the dataset and usually have a lower dimension than the original data; in this sense, a latent variable z can be considered a compressed version of a data example x that captures its essential qualities (figures 1.9  
  
  
  
## Discriminative vs Generative Models  
  
#shenshen  Slides with understanding deep learning book could have been enough.. need more brain and more effort in understanding these slides like I did for 6.390 where I used to spend 10 hours or more per 1 concept.. with Deep learning book now udl..  
  
![Discriminative v.s. Generative Models](Attachments/D28F6103-2058-4744-9813-4715F70EC4D2.heic)  
discriminative:  
* "feature/sample" x to "label" y   
* one "desired" output   
  
generative:   
* "label" y to "feature/sample" x  
* Many possible outcomes  
  
## Framing the distinction  
  
discriminative-> P(y|x)-> y=0 nothing y=1, we get an output  
  
Generative: from label to features can be modeled as p(x|y) reverse of above such that p(x|y)=0 is one set of negative outputs ? and P(y|x)=1 if positive set??  
  
  
  
  
  
  
Examples  
  
  
  
  
  
  
  
  
![Model the task as p(z | 3)](Attachments/BD316FB9-AD06-48DB-AC64-41A30EC56AD4.heic)  
  
  
  
  
![Model the task as p(= | g)](Attachments/FF67D88C-4611-4B40-8592-02D2C55F7D8C.heic)  
  
  
![Model the task as p(= |B)](Attachments/3F79F223-1C3C-453A-A613-B4F5D23DDE42.heic)  
![Model the task as p(z | s)](Attachments/DAF880EB-E367-458D-8A66-FA0E3A3B2AEB.heic)  
  
  
  
  
  
##   
## What do we mean by modeling p(x|y)  
  
![What do we mean by modeling p(= | y)](Attachments/10EAA56E-A25C-46E1-9DB0-FC8A61F198B9.heic)  
  
argmax p(x|y) is given by density function where we want to minimize KL divergence or calculate MLE or max likelihood  
![po (z):](Attachments/E1C10387-100C-4A21-9DD3-C12F72A8078A.heic)  
  
  
### We care less about the exact value of p(x | y)  
  
We want to generate new data, sampling from given data we   
  
![What do we mean by modeling p(a | g)](Attachments/1F781BE1-35EB-4DB6-A73C-59FEA53133C3.heic)  
  
### Learning Data Generators  
  
-   Generative models that can estimate p(x | y) is called "explicit generative models"  Direct Approach  
-   Generative models that do not directly estimate p(x | y) is called "implicit generative models" Indirect Approach  
![Learning data generators](Attachments/1DCE1E47-4231-47E0-80BF-B82A719D6F6B.heic)  
  
  
![Why is this hard?](Attachments/FA6FBB4E-F469-4E2D-9786-4263CEB9D000.heic)  
![Why is this hard?](Attachments/722DD0B1-7668-478E-9E3A-30B13D6155D1.heic)  
  
## How to factorize it into easy low dimensional calculation for efficient computation..  
  
## ![Learning to represent probabilistic distributions](Attachments/3B2B3616-BE28-4466-A21B-A151C2AB5E5D.heic)  
##  just use chain rule..  
  
  
![Conditional Distribution Modeling](Attachments/36E38C9E-D316-4877-9363-2DB58BC7590C.heic)  
  
  
![Conditional Distribution Modeling](Attachments/37916E95-D2B4-4404-973A-D528ED893ECF.heic)  
  
  
  
![Conditional Distribution Modeling](Attachments/4FA9037D-35AB-4B61-9C59-09C329C53FEF.heic)  
![Conditional Distribution Modeling](Attachments/34E980B2-2DF7-44E5-8676-97F91D5A825B.heic)  
![Conditional Distribution Modeling](Attachments/1D02DC13-2FFB-41AB-8890-79087312B10A.heic)  
![Modeling each conditional distribution with a neural network](Attachments/09BA3D9C-BBE7-483A-B955-B1B3C95067E7.heic)  
![Conditional Distribution Modeling](Attachments/5CA78705-F09B-4C7D-A61B-C7890B9B2DF8.heic)  
  
Note:  
*   parameterizing p(A, B, C) vs. parameterizing p(C | A, B)?  
*   P(A, B, C) has 3 variables  
*   p(C | A, B) has 1 variable and 2 conditions (conditions are network inputs)->  Low dimensional  
*     
* ![Dependency Graphs](Attachments/791A01FD-2B26-4D50-920C-FE96B2AAD5B4.heic)  
* weight sharing?  
*   conceptually, each p has its own weights  
*   weight sharing implies** inductive biases-> Assumption built in**  
  
  
  
## Generative Modelling  
  
Two approaches direct and indirect->  
  
Consider defining a distribution Pr(z) over the latent variable z in these models. New examples can now be  
generated by  
1.   drawing from this distribution   
2. mapping the sample to the data space x.  
  
  
 Accordingly, these are termed generative models (see figure 14.1).  
  
  
  
  
  
  
  
  
Generative adversarial networks (chapter 15) learn to generate data examples x∗ rom latent variables z, using a loss that encourages the generated samples to be indistinguishable from real examples (figure 14.2a).  
  
  
Normalizing flows, variational autoencoders, and diffusion models (chapters 16–18) are probabilistic generative models. In addition to generating new examples, they assign a probability Pr(x|ϕ) to each data point x. This will depend on the model parameters ϕ, and in training, we maximize the probability of the observed data {xi}, so the loss is the sum of the negative log-likelihoods (figure 14.2b):  
  
  
L[ϕ] =− ∑ log Pr(xi|ϕ).  
  
  
## Energy based   
  
logits or likelihood of a value to be given by this score.. unnormalized probability..  
rest maths..  
  
  
  
  
  
  
  
 called boltzman distribution after normalizing  
  
  
  
  
  
# Diffusion  
  
  
* ![Outline](Attachments/DD8311D1-216E-4884-B2E8-1E2E7B5B107E.heic)  
  
  
  
  
![koverso (Generative) Process](Attachments/B5CBBB76-3223-4582-A474-8F9E01D44185.heic)  
![1. Forward Process](Attachments/A8E990E1-2DA9-4249-965E-161A209E7E93.heic)  
#shenshen read properly all slides..  
  
![For fixed (8,) cr) € (0,1), let](Attachments/24B2B647-6B0C-4A44-991F-333DD5746FE1.heic)  
  
  
## Fixed Data vs Dynamic  
  
Intuition  
  
* Real-world data is constantly changing. Because data isn't static, AI models can't stay relevant for long if they don't engage in continuous learning.++[1](https://docs.google.com/document/d/17TDSGdcTIxf3Zkrp3lVe1NuSbXAdNwfER3mN19RFJfU/edit)++  
* Generative AI needs to keep up. To avoid producing stale or irrelevant content, models must continuously update their "conceptual dictionary" to incorporate new trends without losing their grasp on older styles.++[1](https://docs.google.com/document/d/17TDSGdcTIxf3Zkrp3lVe1NuSbXAdNwfER3mN19RFJfU/edit)++  
* Compression depends on flexibility.** When compressing data, **if a model's dictionary is fixed, encountering novel data will cause the signal to distort. Models need to shift their focus (centroids) over time to handle these new data types.++[1](https://docs.google.com/document/d/17TDSGdcTIxf3Zkrp3lVe1NuSbXAdNwfER3mN19RFJfU/edit)++  
* The "Catastrophic Forgetting" hurdle. This is the big technical challenge: when a model gets better at new concepts, it often completely loses its ability to handle historical data, leading to scrambled or corrupted outputs.++[1](https://docs.google.com/document/d/17TDSGdcTIxf3Zkrp3lVe1NuSbXAdNwfER3mN19RFJfU/edit)++  
* **The solution is a gentle update. To fix this, you shouldn't change your dictionary vectors drastically for every new batch of data. Instead, update them smoothly and conservatively—using something like an exponential moving average—to blend new information into the model's existing memory without erasing it.++[1](https://docs.google.com/document/d/17TDSGdcTIxf3Zkrp3lVe1NuSbXAdNwfER3mN19RFJfU/edit)++**  
Would you like me to explain more about the technical side of the "Catastrophic Forgetting" solution or help you solve the quiz questions mentioned in the text?  
  
The document outlines how AI models must evolve to handle real-world data, which is never static. Here are the details on the two primary objectives and the core technical challenge of keeping those models functional over time:1. The Generative Objective (Creating Synthetic Data)  
  
When the goal is to generate new designs, speech, or video, the model relies on a "conceptual dictionary"—a learned representation of concepts it has seen before.  
* The Problem: If the dictionary is "frozen" (static), the model cannot capture new trends, products, or styles. As the real world evolves, the model's outputs become stale, irrelevant, or simply "out of date."  
* The Strategy: To remain effective, the system must continuously incorporate new concepts into its dictionary. The challenge here is "assimilation"—adding new knowledge without deleting the established patterns it already knows.  
2. **The Compression Objective (Downsampling Data Streams)**  
  
In data compression (like high-fidelity media codecs), the goal is to represent a signal (like an image or audio) using as few tokens as possible without losing quality.  
* The Problem: Compression relies on a dictionary of known data patterns. If the model encounters a novel data type not in its dictionary, "reconstruction loss" spikes. This causes the signal to break down, resulting in visual or auditory distortion.  
* The Strategy: To maintain fidelity, both the compressor and the dictionary must be dynamic. As the incoming data stream changes (e.g., video trends shifting), the model's means—the core representative vectors in the dictionary—must shift to match the new vocabulary of the data. means-> centroids-> of clustering.. Reconstruction loss  
3. The Core Challenge: Catastrophic Forgetting  
  
This is the "Golden Problem" of continuous learning. When you try to update a model, you often create a trade-off:  
* What happens: When a model is updated to master new data, the dictionary vectors often drift entirely toward that new information.  
* The Result: The model "forgets" how to handle historical data. If the decoder tries to reconstruct an image based on an older, now-overwritten concept, it produces scrambled noise or corrupted outputs.  
The Proposed Solution: Gentle Updating  
  
The document suggests that you shouldn't drastically change dictionary vectors for every new batch of data. Instead, use a running, exponential moving average. This approach:  
* Updates vectors by only a tiny percentage toward new data.  
* Blends new information into the existing memory slowly.  
* Prevents the "hard overwrite" that leads to catastrophic forgetting, keeping the model's past knowledge intact while still adapting to the present.  
  
  
Would you like me to expand on the quiz questions regarding **VAEs (Variational Autoencoders) or** the "Catastrophic Forgetting" mechanism?  
  
# VAEs (Variational Autoencoders)   
