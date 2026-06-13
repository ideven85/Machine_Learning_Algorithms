# Feature Visualization in Neural Networks  
  
#todo   
  
There is a growing sense that neural networks need to be interpretable to humans. The field of neural network interpretability has formed in response to these concerns. As it matures, two major threads of research have begun to coalesce:** feature visualization and attribution.**  
  
1. **Feature visualization** answers questions about what a network — or parts of a network — are looking for **by generating examples.**  
2. **Attribution** studies what part of an example is responsible for the network activating a particular way.  
  
This article focuses on feature visualization. While feature visualization is a powerful tool, actually getting it to work involves a number of details. In this article, we examine the major issues and explore common approaches to solving them. We find that remarkably simple methods can produce high-quality visualizations. Along the way we introduce a few tricks for exploring variation in what neurons react to, how they interact, and how to improve the optimization process.  
  
  
**Feature Visualization by Optimization**  
Neural networks are, generally speaking, differentiable with respect to their inputs. If we want to find out what kind of input would cause a certain behavior — whether that’s an internal neuron firing or the final output behavior — we can use derivatives to iteratively tweak the input towards that goal  
  
Starting from random noise, we optimize an image to activate a particular neuron  
  
**Optimization Objectives**  
What do we want examples of? This is the core question in working with examples, regardless of whether we’re searching through a dataset to find the examples**, or optimizing images->  to create them from scratch.** We have a wide variety of options in what we search for:  
[Feature Visualization](https://distill.pub/2017/feature-visualization/)  
f we want to understand individual features, we can search for examples where they have high values — either for a *neuron* at an individual position, or for an entire *channel*. We used the channel objective to create most of the images in this article.  
If we want to understand a *layer* as a whole, we can use the DeepDream objective  
[4]  
, searching for images the layer finds “interesting.”'  
Optimization also has the advantage of flexibility. For example, if we want to study how neurons jointly represent information, we can easily ask how a particular example would need to be different for an additional neuron to activate. This flexibility can also be helpful in visualizing how features evolve as the network trains. If we were limited to understanding the model on the fixed examples in our dataset, topics like these ones would be much harder to explore  
On the other hand, there are also significant challenges to visualizing features with optimization. In the following sections we’ll examine techniques to get diverse visualizations, understand how neurons interact, and avoid high frequency artifacts.  
  
