You are exactly right—the $L_2$ norm maps directly to the Gaussian distribution. Mathematically, minimizing an $L_2$ norm or $L_2$ loss is the exact probabilistic equivalent of maximizing the likelihood of a Gaussian (Normal) distribution. [1, 2, 3]
When you strip away the calculus, the squared $L_2$ norm is the exponent inside the Gaussian formula. [4]
------------------------------
## 1. The Mathematical Origin
Look at the Probability Density Function (PDF) of a standard 1D Gaussian distribution: [5]
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)$$
For a multidimensional vector $\mathbf{x}$ (an isotropic Multivariate Gaussian), the formula becomes: [6]
$$f(\mathbf{x}) = C \cdot \exp\left( -\frac{\sum (x_i - \mu_i)^2}{2\sigma^2} \right)$$
Notice the term inside the exponent: $\sum (x_i - \mu_i)^2$. This is precisely the squared $L_2$ norm ($\Vert{}\mathbf{x} - \boldsymbol{\mu}\Vert{}_2^2$) of the distance vector! [7]
------------------------------
## 2. The Log-Likelihood Connection
When algorithms optimize a model (like a neural network or a linear regression), they want to maximize the probability of the data. To make the math easier, we take the natural logarithm ($\ln$) of the Gaussian distribution. [1, 3, 4, 8, 9]
Taking the log eliminates the exponential ($\exp$): [3]
$$\ln(f(\mathbf{x})) = \ln(C) - \frac{1}{2\sigma^2} \Vert{}\mathbf{x} - \boldsymbol{\mu}\Vert{}_2^2$$
Because $\ln(C)$ and $\frac{1}{2\sigma^2}$ are constants, maximizing this log-probability is mathematically identical to minimizing the $L_2$ norm $\Vert{}\mathbf{x} - \boldsymbol{\mu}\Vert{}_2^2$. [3]
------------------------------
## 3. How This Dictates Machine Learning Rules
The intrinsic relationship between the $L_2$ norm and the Gaussian distribution serves as the mathematical foundation for several machine learning techniques:

*
* Mean Squared Error (MSE Loss): When you use $L_2$ loss to train a model, you are explicitly assuming that your model's prediction errors (residuals) are distributed like a Gaussian bell curve centered around zero. [2, 10]
* $L_2$ Regularization (Ridge / Weight Decay): Adding an $L_2$ penalty to your model's weights assumes a Gaussian prior. It means you believe the weights should naturally cluster closely around zero, preventing any single weight from exploding. [4, 6, 11, 12, 13]
* The Contrastive Connection: When contrastive learning models use $L_2$ normalization to project vectors onto a hypersphere, it forces the directional features to distribute evenly. Strikingly, recent machine learning research shows that representations learned via contrastive objectives naturally exhibit Gaussian-like concentration on the sphere's surface. [14, 15]
*

(In contrast, if you assume your data follows a Laplace distribution—which has a sharp, spiked peak at zero—the log-likelihood derivation yields the absolute-value $L_1$ norm instead.) [3, 4]
------------------------------
If you want to dive deeper into this bridge between geometry and probability, let me know if you would like to explore:

