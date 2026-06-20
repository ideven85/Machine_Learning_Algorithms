  
# Lecture 2:   
##   
##   
## The Big Ideas  
  
  
**1. Training = Optimization**  
The whole goal is:  
```
Input
  ↓
Network
  ↓
Prediction
  ↓
Loss

```
Then find parameters:  
[ \theta^* ]  
that minimize the loss.  
The lecture repeatedly emphasizes:  
Learning = moving parameters around in parameter space until loss becomes small.  
  
**2. SGD is an approximation**  
Full gradient descent:  
```
Use entire dataset
→ compute gradient
→ update weights

```
Impossible at modern scale.  
Instead:  
```
Sample batch
→ compute gradient
→ update weights

```
This is SGD.  
**Key intuition**  
SGD introduces noise.  
Noise sounds bad.  
But noise can:  
```
escape local minima
improve generalization
act as regularization

```
which is why SGD works surprisingly well.  
  
**3. Momentum**  
The lecturer uses a rolling-ball analogy.  
Without momentum:  
```
step
step
step
step

```
With momentum:  
```
previous direction
+
current gradient

```
This can speed convergence dramatically. Adam uses this idea.  
  
**4. Not every loss landscape is easy**  
The lecture asks:  
```
Which functions are hard to optimize?

```
Important cases:  
**Vanishing gradients**  
```
gradient ≈ 0

```
No learning signal.  
**Exploding gradients**  
```
gradient → huge

```
Updates overshoot.  
**Multiple minima**  
```
start location matters

```
Different random seeds may find different solutions.  
  
**5. Computational Graphs**  
This is one of the most important concepts.  
A neural network is:  
```
Input
 ↓
Operation
 ↓
Operation
 ↓
Operation
 ↓
Output

```
Every operation becomes a node in a graph.  
The lecturer wants you to stop thinking:  
```
Neural Network

```
and start thinking:  
```
Computation Graph

```
  
**6. Forward Pass**  
Every layer performs:  
```
input
+
parameters
↓
output

```
That's all.  
Forward pass = evaluate the graph.  
  
**7. Chain Rule = Deep Learning**  
This may be the single most important statement of the lecture.  
Everything in backprop comes from:  
## [ \frac{dz}{dx}  
\frac{dz}{du} \frac{du}{dx} ]  
The entire field is essentially:  
```
Chain Rule
+
Efficient bookkeeping

```
  
  
**8. Backpropagation**  
The lecturer says something subtle:  
Backprop is basically an efficiency trick.  
Why?  
Because many derivative terms are shared.  
Instead of recomputing them:  
```
again
again
again
again

```
we compute once and reuse.  
That makes large neural networks practical.  
  
**9. Linear Layer Cheat Sheet**  
You do **not** need to memorize derivations.  
Remember:  
Forward:  
```
output = Wx

```
Backward:  
```
gradient = Wᵀg

```
Weight update depends on:  
```
input×output gradient

```
This pattern appears everywhere.  
  
**10. ReLU as a Gating Matrix**  
This was your earlier question.  
Forward:  
```
positive → pass
negative → zero

```
Backward:  
```
positive neuron → gradient passes
negative neuron → gradient blocked

```
Hence the ReLU derivative behaves like a mask/gate.  
  
****11. Differential Programming****  
The lecture ends with the most modern viewpoint.  
Instead of thinking:  
```
Deep Learning

```
think:  
```
Differentiable Programs

```
Any system made of differentiable components can be optimized using backprop.  
This idea directly leads to:  
* Neural Module Networks  
* CLIP  
* Diffusion Models  
* Modern multimodal systems  
* Agentic AI architectures  
  
## What I'd test you on  
If I were the instructor, I'd ask:  
1. Why does SGD often outperform full gradient descent?  
2. What problem does momentum solve?  
3. Why is backprop considered an efficiency trick?  
4. Explain a computation graph.  
5. Why does ReLU act like a gate during backprop?  
6. Why are vanishing gradients problematic?  
7. What is the difference between optimizing parameters and optimizing inputs?  
If you can answer those seven without notes, 
8. you've captured about **80% of Lecture 2's core understanding**. 🎯  
Also: you've been digging into autograd, ReLU gates, 
9. Jacobians, and backprop for a while. Good point to take a short walk
10. 
11. 🚶 and let the computation graph in your head finish its own backward pass.  
  
Good. You're getting past the "what is SGD?" stage and into the "why does this work?" stage.  
A few instructor comments:  
**1. Computation Graph ✅**  
Your definition is correct:  
```
Nodes → computations
Edges → information flow

```
For this course I'd add:  
```
Node = differentiable function
Edge = tensor flowing between functions

```
because backprop only works because the graph is differentiable.  
  
**2. Backprop ≠ Dynamic Programming**  
Careful here.  
Many people say:  
"Backprop is dynamic programming."  
That's not literally true.  
A better statement:  
Backprop uses a dynamic-programming-like idea.  
The shared derivative terms:  
[ \frac{\partial J}{\partial h} ]  
are computed once and reused.  
Without backprop:  
```
Compute chain rule repeatedly

```
With backprop:  
```
Compute once
Cache
Reuse

```
That's the efficiency trick Sara is talking about.  
  
**3. Vanishing Gradients**  
You said:  
vanishing basic, can clip  
Small correction.  
Gradient clipping helps:  
```
Exploding gradients

```
not vanishing gradients.  
  
Vanishing:  
```
0.1 × 0.1 × 0.1 × 0.1 ...

```
↓  
```
0.0001

```
↓  
No learning signal.  
  
Exploding:  
```
10 × 10 × 10 × 10 ...

```
↓  
Huge gradient.  
↓  
Training unstable.  
Gradient clipping is for this case.  
  
**4. ReLU Gate**  
The key insight I'd want you to remember:  
Forward:  
```
activation <= 0

```
↓  
```
output = 0

```
Backward:  
```
gradient = 0

```
The same decision made during the forward pass determines whether gradients are allowed back.  
  
**5. Differential Programming**  
This is probably the most important new idea in Lecture 2.  
The old view:  
```
Neural Network

```
The modern view:  
```
Differentiable Program

```
A transformer is just a giant computation graph.  
A ViT is a computation graph.  
CLIP is a computation graph.  
**Even an agent system can be viewed as a computation graph if the pieces are differentiable.**  
  
**What I'd ask next**  
You seem comfortable with:  
* SGD  
* Momentum  
* Computational graphs  
* Chain rule  
* Backprop  
* ReLU gating  
The next important checkpoint is:  
Why does a linear layer's backward pass use (W^T) instead of (W)?  
The lecture spends several slides building toward:  
[ g_{in}=W^T g_{out} ]  
If you can explain **why the transpose appears**, you've understood the matrix calculus part rather than memorized it. 🎯  


And yes, before diving into ViTs, understanding that transpose will pay dividends when attention matrices start flying around everywhere.  
  
  
  
  
  
Yes! That's much closer to the real issue. 🔥  
You're bumping into the fact that there are **multiple conventions** for vector derivatives.  
The lecture is essentially using the **Jacobian viewpoint**.  
**Start with scalar → scalar**  
If:  
[ y = x^2 ]  
then:  
[ \frac{dy}{dx}=2x ]  
Easy. Just a number.  
  
**Vector → scalar**  
Suppose:  
[ f(x_1,x_2)=x_1^2+x_2^2 ]  
Input:  
[ x= \begin{bmatrix} x_1\ x_2 \end{bmatrix} ]  
Gradient:  
[ \nabla f= \begin{bmatrix} 2x_1\ 2x_2 \end{bmatrix} ]  
Notice:  
```
scalar output
↓
column vector gradient

```
Deep learning usually stores gradients this way.  
  
**Vector → vector**  
Now things get interesting.  
[ y= \begin{bmatrix} y_1\ y_2 \end{bmatrix} ]  
depends on  
[ x= \begin{bmatrix} x_1\ x_2 \end{bmatrix} ]  
Then one derivative isn't enough.  
We need:  
[ \frac{\partial y_i}{\partial x_j} ]  
for every pair.  
That's the **Jacobian**.  
[ J= \begin{bmatrix} \frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} \ \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} \end{bmatrix} ]  
Think:  
```
Rows    → outputs
Columns → inputs

```
  
**Linear layer**  
For  
[ y = Wx ]  
we have  
[ y_1 = w_{11}x_1+w_{12}x_2 ]  
[ y_2 = w_{21}x_1+w_{22}x_2 ]  
The Jacobian becomes:  
[ J= \begin{bmatrix} w_{11}&w_{12}\ w_{21}&w_{22} \end{bmatrix} ]  
which is simply:  
[ J=W ]  
That's the beautiful part.  
For a linear map:  
[ \frac{\partial y}{\partial x}=W ]  
  
**Why transpose in backprop?**  
Now imagine:  
## [ g_{out}  
\frac{\partial L}{\partial y} ]  
is a column vector.  
Chain rule for vectors becomes:  
## [ \frac{\partial L}{\partial x}  
J^T \frac{\partial L}{\partial y} ]  
Since  
[ J=W ]  
we get:  
## [ \frac{\partial L}{\partial x}  
W^T \frac{\partial L}{\partial y} ]  
  
**Intuition**  
Forward:  
```
x
↓
W
↓
y

```
Backward:  
```
blame on y
↓
redistribute to x
↓
Wᵀ

```
The transpose appears because we're moving gradients **from outputs back to inputs**, reversing the direction of information flow.  
  
**The mental model I'd keep**  
Don't memorize:  
```
Derivative of vector → row vector
Derivative of vector → column vector

```
Different books use different conventions and you'll go mad trying to remember them.  
Instead remember:  
```
Vector → Vector
      ↓
Jacobian

Backprop
      ↓
Transpose Jacobian

```
That's the invariant idea underneath all the notation.  
And this is exactly why autograd engines are basically:  
```
Forward:
store local Jacobians

Backward:
multiply by transpose Jacobians

```
over and over and over through the computation graph. 🧠⚙️  
That's the bridge between Lecture 2's computation graphs and PyTorch autograd.  
  
  
Neural Module Networks (NMNs), introduced by Andreas et al., **represent an influential, highly interpretable approach to Visual Question Answering (VQA) that bridges the gap between deep learning and symbolic logic**. [[1](https://arxiv.org/abs/1511.02799#:~:text=Visual%20question%20answering%20is%20fundamentally%20compositional%20in,substructure%20with%20questions%20like%20%22what%20color%20is), [2](https://www.sciencedirect.com/science/article/pii/S0925231223006410#:~:text=3.%20Basics%20of%20Neural%20Module%20Networks%20*,ones%20is%20using%20Neural%20Module%20Networks.%20Th), [3](https://dl.acm.org/doi/10.1007/978-3-030-01234-2_4), [4](https://www.researchgate.net/publication/311610065_Neural_Module_Networks#:~:text=Similarly%2C%20mixture%2Dof%2Dexperts%20models%20and%20recurrent%20independent%20mechanisms,aimed%20at%20capturing%20the%20benefits%20of%20specializ), [5](https://proceedings.neurips.cc/paper/2021/hash/c467978aaae44a0e8054e174bc0da4bb-Abstract.html#:~:text=Neural%20Module%20Networks%20(NMNs)%20aim%20at%20Visual,NMNs%20are%20a%20promising%20strategy%20to%20achieve)]   
  
Instead of treating a question-answering system as a single monolithic black box, NMNs decompose complex natural language questions into smaller, linguistically meaningful sub-tasks (e.g., *finding an object*, *describing a color*, *measuring a count*). [[6](https://www.cs.princeton.edu/courses/archive/spring18/cos598B/public/outline/Neural%20Module%20Networks.pdf), [7](https://dl.acm.org/doi/10.1016/j.neucom.2023.126518#:~:text=This%20way%2C%20we%20gain%20full%20transparency%20and,neural%20module%20networks%20(NMN).%20Each%20module%20repr)]   
  
**Key Concepts & Mechanics **  
* **Dynamic Assembly:** An off-the-shelf parser or recurrent neural network (RNN) reads the user's question and converts it into an executable "program" or syntax tree.   
* **Modular Components:** The network assembles itself dynamically by piecing together tiny, specialized neural "modules" that are structurally sequenced to mirror the tree structure of the question.   
* **Reusability:** Each module takes in attention weights, image features, or linguistic representations (depending on its placement in the layout), performs its dedicated sub-task, and outputs its result to the next module. [[6](https://www.cs.princeton.edu/courses/archive/spring18/cos598B/public/outline/Neural%20Module%20Networks.pdf), [7](https://dl.acm.org/doi/10.1016/j.neucom.2023.126518#:~:text=This%20way%2C%20we%20gain%20full%20transparency%20and,neural%20module%20networks%20(NMN).%20Each%20module%20repr), [14](https://en.wikipedia.org/wiki/Modular_neural_network#:~:text=Each%20independent%20neural%20network%20serves%20as%20a,the%20network%20hopes%20to%20perform.%20The%20inte)]   
**Why NMNs Matter **  
1. **Compositional Generalization:** Because NMNs construct task-specific networks on the fly, they can answer novel combinations of queries that they haven't seen explicitly during training.   
2. **High Explainability:** Unlike standard Deep Neural Networks (DNNs) that learn complex representations across thousands of unreadable layers, NMNs allow you to explicitly "trace" the path of reasoning. By checking the output of each module at every step, you know exactly *why* the model gave a specific answer. [[7](https://dl.acm.org/doi/10.1016/j.neucom.2023.126518#:~:text=This%20way%2C%20we%20gain%20full%20transparency%20and,neural%20module%20networks%20(NMN).%20Each%20module%20repr), [18](https://ijsret.com/wp-content/uploads/IJSRET_V11_issue4_154.pdf#:~:text=A%20DNN%20consists%20of%20an%20input%20layer%2C,connected%20by%20weighted%20edges.%20The%20primary%20architectur), [19](https://www.computer.org/publications/tech-news/neural-network-structures#:~:text=Our%20net%20will%20contain%20several%20layers:%20an,the%20hidden%20layer%2C%20which%2C%20in%20turn%2C%20sends), [20](https://hal.science/hal-04252818v1/file/paper153.pdf#:~:text=NMNs%20provide%20en%2D%20hanced%20explainability%20compared%20to,the%20underlying%20reasoning%20process.%20To%20improve%20the), [21](https://data-flair.training/blogs/artificial-neural-network/#:~:text=Some%20deep%20neural%20networks%20may%20have%20thousands,representations.%20What%20makes%20this%20different%20from%20ANNs)]   
Evolution of the Framework   
  
While early implementations relied on rigid, hand-crafted syntactic parsers, subsequent iterations (like those from Hu et al. and further developments by Andreas) transitioned to continuous, end-to-end differentiable layouts. This allowed the model to jointly learn "what" sub-tasks to perform and "how" to perform them via standard gradient descent. [[9](https://openaccess.thecvf.com/content_ICCV_2017/papers/Hu_Learning_to_Reason_ICCV_2017_paper.pdf#:~:text=We%20would%20like%20to%20predict%20the%20most,object%20is%20next%20to%20the%20table?%2C%20our), [22](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866498/), [23](https://www.sciencedirect.com/science/article/pii/S0893608021001222#:~:text=However%2C%20one%20of%20the%20latest%20examples%20of,only%20designed%20to%20perform%20well%20in%20certa), [24](https://www.ijcai.org/proceedings/2020/0104.pdf#:~:text=Neural%20module%20networks%20is%20a%20general%20framework,the%20network%20into%20neural%20modules.%20It%20ha), [25](https://onlinelibrary.wiley.com/doi/full/10.1002/ail2.39#:~:text=In%20neural%20module%20networks%20(NMNs)%2C17%20N2NMN%2C13%20PG,the%20question%20and%20decomposing%20the%20reasoning%20p)]   
  
To learn more about the exact mathematical definitions and layouts of these modules, you can read the original Neural Module Networks arXiv Paper or explore the follow-up Learning to Reason ICCV Paper by Hu et al. [[1](https://arxiv.org/abs/1511.02799#:~:text=Visual%20question%20answering%20is%20fundamentally%20compositional%20in,substructure%20with%20questions%20like%20%22what%20color%20is), [9](https://openaccess.thecvf.com/content_ICCV_2017/papers/Hu_Learning_to_Reason_ICCV_2017_paper.pdf#:~:text=We%20would%20like%20to%20predict%20the%20most,object%20is%20next%20to%20the%20table?%2C%20our)]   
  
Would you like me to dive deeper into the exact mathematical operations of individual modules, or would you like to explore **more recent models** that evolved from this architecture?   
*AI can make mistakes, so double-check responses*  
[1] [https://arxiv.org/abs/1511.02799](https://arxiv.org/abs/1511.02799#:~:text=Visual%20question%20answering%20is%20fundamentally%20compositional%20in,substructure%20with%20questions%20like%20%22what%20color%20is)  
[2] [https://www.sciencedirect.com/science/article/pii/S0925231223006410](https://www.sciencedirect.com/science/article/pii/S0925231223006410#:~:text=3.%20Basics%20of%20Neural%20Module%20Networks%20*,ones%20is%20using%20Neural%20Module%20Networks.%20Th)  
[3] [https://dl.acm.org/doi/10.1007/978-3-030-01234-2_4](https://dl.acm.org/doi/10.1007/978-3-030-01234-2_4)  
[4] [https://www.researchgate.net/publication/311610065_Neural_Module_Networks](https://www.researchgate.net/publication/311610065_Neural_Module_Networks#:~:text=Similarly%2C%20mixture%2Dof%2Dexperts%20models%20and%20recurrent%20independent%20mechanisms,aimed%20at%20capturing%20the%20benefits%20of%20specializ)  
[5] [https://proceedings.neurips.cc/paper/2021/hash/c467978aaae44a0e8054e174bc0da4bb-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/c467978aaae44a0e8054e174bc0da4bb-Abstract.html#:~:text=Neural%20Module%20Networks%20(NMNs)%20aim%20at%20Visual,NMNs%20are%20a%20promising%20strategy%20to%20achieve)  
[6] [https://www.cs.princeton.edu/courses/archive/spring18/cos598B/public/outline/Neural%20Module%20Networks.pdf](https://www.cs.princeton.edu/courses/archive/spring18/cos598B/public/outline/Neural%20Module%20Networks.pdf)  
[7] [https://dl.acm.org/doi/10.1016/j.neucom.2023.126518](https://dl.acm.org/doi/10.1016/j.neucom.2023.126518#:~:text=This%20way%2C%20we%20gain%20full%20transparency%20and,neural%20module%20networks%20(NMN).%20Each%20module%20repr)  
[8] [https://openaccess.thecvf.com/content_cvpr_2016/papers/Andreas_Neural_Module_Networks_CVPR_2016_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2016/papers/Andreas_Neural_Module_Networks_CVPR_2016_paper.pdf#:~:text=To%20summarize%20our%20contributions:%20We%20first%20describe,for%20discretely%20com%2D%20posing%20heterogeneous%2C%20jointly%2Dtrained%20neura)  
[9] [https://openaccess.thecvf.com/content_ICCV_2017/papers/Hu_Learning_to_Reason_ICCV_2017_paper.pdf](https://openaccess.thecvf.com/content_ICCV_2017/papers/Hu_Learning_to_Reason_ICCV_2017_paper.pdf#:~:text=We%20would%20like%20to%20predict%20the%20most,object%20is%20next%20to%20the%20table?%2C%20our)  
[10] [https://www.computer.org/csdl/proceedings-article/cvpr/2016/8851a039/12OmNASraKG](https://www.computer.org/csdl/proceedings-article/cvpr/2016/8851a039/12OmNASraKG#:~:text=In%20this%20paper%2C%20we%20have%20introduced%20neural,of%20neural%20modules%20which%20can%20be%20dyn)  
[11] [https://cinnamonai.medium.com/modular-method-in-visual-question-answering-6e3043892002](https://cinnamonai.medium.com/modular-method-in-visual-question-answering-6e3043892002#:~:text=Neural%20Module%20Network%20approach%20commences%20by%20dynamically,form%20(i.e%20a%20dependency%20tree)(%20Figure%202).)  
[12] [https://openreview.net/pdf?id=HkezXnA9YX](https://openreview.net/pdf?id=HkezXnA9YX#:~:text=For%20example%2C%20in%20the%20Neural%20Module%20Net%2D,from%20several%20neural%20modules%2C%20where%20each%20module)  
[13] [https://link.aps.org/doi/10.1103/PhysRevLett.92.188701](https://link.aps.org/doi/10.1103/PhysRevLett.92.188701#:~:text=This%20work%20illustrates%20an%20approach%20to%20network,is%20simultaneously%20structural%20and%20dynamical%20in%20nature.)  
[14] [https://en.wikipedia.org/wiki/Modular_neural_network](https://en.wikipedia.org/wiki/Modular_neural_network#:~:text=Each%20independent%20neural%20network%20serves%20as%20a,the%20network%20hopes%20to%20perform.%20The%20inte)  
[15] [https://arxiv.org/html/2409.14981v1](https://arxiv.org/html/2409.14981v1#:~:text=We%20now%20turn%20to%20modularity%20and%20network,(Bahdanau%20et%20al.%2C%202019b;%20Vani%20et%20a)  
[16] [https://pmc.ncbi.nlm.nih.gov/articles/PMC8412986/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8412986/#:~:text=NMS%20is%20assumed%20to%20emerge%20with%20training,tasks%2C%20even%20without%20an%20explicit%20requirement%20t)  
[17] [https://www.computer.org/csdl/proceedings-article/wacv/2021/047700a655/1uqGPRonAqY](https://www.computer.org/csdl/proceedings-article/wacv/2021/047700a655/1uqGPRonAqY#:~:text=Neural%20module%20net%2Dworks%20(NMNs)%20%5B2%5D%2C%20%5B3%5D%2C%20%5B15%5D%2C,NMN%20requires%20a%20set%20of%20pre%2Ddefined%20fu)  
[18] [https://ijsret.com/wp-content/uploads/IJSRET_V11_issue4_154.pdf](https://ijsret.com/wp-content/uploads/IJSRET_V11_issue4_154.pdf#:~:text=A%20DNN%20consists%20of%20an%20input%20layer%2C,connected%20by%20weighted%20edges.%20The%20primary%20architectur)  
[19] [https://www.computer.org/publications/tech-news/neural-network-structures](https://www.computer.org/publications/tech-news/neural-network-structures#:~:text=Our%20net%20will%20contain%20several%20layers:%20an,the%20hidden%20layer%2C%20which%2C%20in%20turn%2C%20sends)  
[20] [https://hal.science/hal-04252818v1/file/paper153.pdf](https://hal.science/hal-04252818v1/file/paper153.pdf#:~:text=NMNs%20provide%20en%2D%20hanced%20explainability%20compared%20to,the%20underlying%20reasoning%20process.%20To%20improve%20the)  
[21] [https://data-flair.training/blogs/artificial-neural-network/](https://data-flair.training/blogs/artificial-neural-network/#:~:text=Some%20deep%20neural%20networks%20may%20have%20thousands,representations.%20What%20makes%20this%20different%20from%20ANNs)  
[22] [https://pmc.ncbi.nlm.nih.gov/articles/PMC7866498/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866498/)  
[23] [https://www.sciencedirect.com/science/article/pii/S0893608021001222](https://www.sciencedirect.com/science/article/pii/S0893608021001222#:~:text=However%2C%20one%20of%20the%20latest%20examples%20of,only%20designed%20to%20perform%20well%20in%20certa)  
[24] [https://www.ijcai.org/proceedings/2020/0104.pdf](https://www.ijcai.org/proceedings/2020/0104.pdf#:~:text=Neural%20module%20networks%20is%20a%20general%20framework,the%20network%20into%20neural%20modules.%20It%20ha)  
[25] [https://onlinelibrary.wiley.com/doi/full/10.1002/ail2.39](https://onlinelibrary.wiley.com/doi/full/10.1002/ail2.39#:~:text=In%20neural%20module%20networks%20(NMNs)%2C17%20N2NMN%2C13%20PG,the%20question%20and%20decomposing%20the%20reasoning%20p)  
  
