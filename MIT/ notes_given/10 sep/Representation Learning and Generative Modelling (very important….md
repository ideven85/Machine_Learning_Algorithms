# Representation Learning and Generative Modelling (very important)  
  
## Overview  
  
Neural networks are, generally speaking, differentiable with respect to their inputs. If we want to find out what kind of input would cause a certain behavior — whether that’s an internal neuron firing or the final output behavior — we can use derivatives to iteratively tweak the input towards that goal  
[3]  
.  
  
[Two basic approaches: 1) compression, 2) prediction](Attachments/7947B176-740F-4378-A0EB-7430E9C552D9.tiff.png)  
  
  
  
### Applications  
  
What **type of data** you are reconstructing (images, text, numerical features)?  
If you want to use it for **dimension reduction** or **anomaly detection**, recommender systems etc..  
  
  
## Embeddings  
  
[Deep neural nets transform datapoints, layer by layer](Attachments/59CC6702-8FF6-4597-B689-5E965E3CF495.png)  
  
[Deep neural nets transform datapoints, layer by layer](Attachments/AA34991A-19D2-4AAA-80BD-C89E4ADC0BE0.png)  
  
[Good representations are:](Attachments/0B21A173-3AF9-45FC-83CE-C099B0D6D17A.png)  
  
  
  
  
## Adapting  
  
  
Question-> Input-> Songs.. Predict sentiment  
Training/Pretraining->Classify into genres Testing-> Preference Prediction   
[Training](Attachments/01F5BDE4-50A5-4C28-9C0B-4C08C8331F81.png)  
  
**Adapting->**  
also called **** transfer learning****-> freeze final layer and continue training for all weights..   
[Training](Attachments/9ACF9ACB-25A3-43F9-9591-2F638E7A1720.png)  
Output-> f' a new model  
  
  
## FineTuning  
  
  
Initialize Adapted model f' to original model and continue training for model f also to new target data..   
[Training](Attachments/65E444BC-B40E-4472-BCBE-CCFA5CD9959B.png)  
  
  
## Finetuning pipeline  
  
## First pretrain on large, finetune on smaller data and test on it   
[Pretraining](Attachments/4AA12327-214A-485B-A750-B84F23BA1FDF.png)  
  
  
## Auto Encoder  
  
  
  
An autoencoder is a neural network that is trained to attempt to copy its input  
to its output.  
  
Internally, it has a hidden layer hthat describes a code used to  
represent the input. The network may be viewed as consisting of two parts: an  
encoder function h= f(x) and a decoder that produces a reconstruction r= g(h).  
**g -> Identity guessing**  
  
This architecture is presented in figure 14.1. If an autoencoder succeeds in simply  
learning to set g(f(x)) = xeverywhere, then it is not especially useful. Inverse of f,  
[Auto-encoder](Attachments/39B11B59-F157-4743-8E4E-57FCBBBAAE9C.png)  
  
**Representation Space/Latent Space**  
[Data space:](Attachments/DC025143-9B02-4D53-9160-E94DB77112A5.png)  
[Data space](Attachments/0768A2E9-FAD0-4E65-BD22-51F8C91AF470.tiff.png.png)  
[In autoencoder](Attachments/367C0AD5-3079-4A91-90D0-F379DFDE1C1E.tiff.png.png)  
**Masking: recons**  
[In autoencoder](Attachments/D198B390-F8B8-4DDD-9BF6-5A982285826C.tiff.png.png)  
**truction**  
  
  
Masked AutoEncoder as  
  
  
Spatiotemporal representation is the process of extracting and modeling features from data containing both spatial (location) and temporal (time) components, crucial for video understanding, remote sensing, and movement tracking. It involves techniques like  ++[3D convolutional neural networks](https://www.google.com/search?client=safari&rls=en&q=3D+convolutional+neural+networks&ie=UTF-8&oe=UTF-8&ved=2ahUKEwiY-LSFgKyTAxWARmwGHSkCMSoQgK4QegQIARAC)++  and  ++[graph-based modeling](https://www.google.com/search?client=safari&rls=en&q=graph-based+modeling&ie=UTF-8&oe=UTF-8&ved=2ahUKEwiY-LSFgKyTAxWARmwGHSkCMSoQgK4QegQIARAD)++  to analyze, classify, or predict dynamic patterns over space and time.   
Agnostic (data)  
In computing, a device or software program is said to be **agnostic** or **data agnostic** if the method or ++format++ of data transmission is irrelevant to the  device  or program's function. This means that the device or program can receive data in multiple formats or from multiple sources, and still process that data effectively. Definition Many devices or programs need data to be presented in a specific format to process the data. For example, ++Apple Inc++ devices generally require applications to be downloaded from their ++App Store++.[1] This is a non data-agnostic method, as it uses a specified file type, downloaded from a specific location, and does not function unless those requirements are met. Non data-agnostic devices and programs can present problems. For example, if your file contains the right type of data (such as text), but in the wrong format, you may have to create a new file and enter the text manually in the proper format in order to use that program. Various file conversion programs exist because people need to convert their files to a different format in order to use them effectively.[2][3][4][5] Implementation Data agnostic devices and programs work to solve these problems in a variety of ways. Devices can treat files in the same way whether they are downloaded over the internet or transferred over a ++USB++ or other cable. Devices and programs[6] can become more data-agnostic by using a generic storage format to ++create, read, update and delete++ files. Formats like ++XML++ and ++JSON++ can store information in a data agnostic manner. For example, ++XML++ is data agnostic in that it can save any type of information. However, if you use Data Transform Definitions (DTD) or XML Schema Definitions (XSD) to define what data should be placed where, it becomes non-data agnostic; it produces an error if the wrong type of data is placed in a field. Once you have your data saved in a generic storage format, this source can act as an entity synchronization layer. The generic storage format can interface with a variety of different programs, with the data extraction method formatting the data in a way that the specific program can understand. This allows two programs that require different data formats to access the same data. Multiple devices and programs can ++create, read, update and delete++ (CRUD) the same information from the same storage location without formatting errors. When multiple programs are accessing the same records, they may have different defined fields for the same type of concept. Where the fields are differently labelled but contain the same data, the program pulling the information can ensure the correct data is used. If one program contains fields and information that another does not, those fields can be saved to the record and pulled for that program, but ignored by other programs. As the entity synchronization layer is data agnostic, additional fields can be added without worrying about recoding the whole database, and concepts created in other programs (that do not contain that field) are fine. Since the information formatting is imposed on the data by the program extracting it, the format can be customized to the device or program extracting and displaying that data. The information extracted from the entity synchronization layer can therefore be dynamically rendered to display on the user's device, regardless of the device or program being used. Having data agnostic devices and programs allows you to transfer data easily between them, without having to convert that data. Companies like Great Ideaz[7] provide data agnostic services by storing the data in an entity synchronization layer. This acts as a compatibility layer, as ++TSQL++ statements can retrieve, update, sort, and write data regardless of the format employed. It also allows you to synchronize data between multiple applications, as the applications can all pull data from the same location. This prevents compatibility problems between different programs that have to access the same data, as well as reducing data replication. Benefits  
[(a) agnostic, S0%](Attachments/DD76269B-70AB-4A77-B18F-65CC8999E09A.png)  
  
  
  
  
[1. Masking](Attachments/F38C07D5-C7C9-4A60-96BD-17EEBB01CC11.png)  
   
[00000-C-А ДДАДА](Attachments/975676A4-3A0F-497E-A03B-DD385D512973.png)  
   
[1• Masking](Attachments/488A8D0E-FC70-4808-B709-F601C97F95E8.png)  
[e.g. image classification (done in the contrastive way)](Attachments/B9A2E011-DD8D-4379-A0F7-A993D0C85E91.png)  
[1. Masking](Attachments/3A76F3E9-D0E0-4CA9-A925-1C6CA77CA1A8.png)  
  
  
# Contrastive Learning  
  
Augment Data one similar one opposite in this..  
  
[2. Contrastive learning](Attachments/04AD0814-89F1-456D-BE0E-15BAAC36D72C.png)  
  
**2. Contrastive learning**  
  
## Overview  
  
Contrastive learning is a self-supervised machine learning technique that teaches models to distinguish between similar and dissimilar data points without needing labeled data. It works by pulling representations of similar items (positive pairs) closer together and pushing different items (negative pairs) further apart in a shared .  
  
  
The goal of contrastive representation learning is to learn such an embedding space  
in which similar sample pairs stay close to each other while dissimilar ones are far  
apart. Contrastive learning can be applied to both supervised and unsupervised  
settings. When working with unsupervised data, contrastive learning is one of the  
most powerful approaches in self-supervised learning.  
  
## Contrastive Training Objectives  
  
In early versions of loss functions for contrastive learning, only one positive and one  
negative sample are involved. The trend in recent training objectives is to include  
multiple positive and negative pairs in one batch.  
  
[2. Contrastive learning](Attachments/510ECA57-E11A-4E8B-9BDB-5A03C1CB2353.png)  
  
### Augment then reconstruct  
  
  
By minimizing contrastive loss  
  
[2. Contrastive learning](Attachments/AD9F0282-60E8-47AC-86E8-785FF511618F.png)  
  
## Contrastive Loss  
  
  
  
  
  
  
### Triplet Loss  
  
  
Triplet loss was originally proposed in the FaceNet (Schroff et al. 2015) paper and  
was used to learn face recognition of the same person at different poses and angles.  
  
  
Given one anchor input x x+ x− we select one positive sample and one negative ,  
x+ x x− meaning that and belong to the same class and is sampled from another  
different class. Triplet loss learns to minimize the distance between the anchor x  
and x+ x x− positive and maximize the distance between the anchor and negative at the  
same time with the following equation:  
  
[distance of dissimilar pairs) » distance of similar pairs)](Attachments/8208C729-729E-493D-8222-C776E5046370.png)  
  
  
find the most dissimilar(hard) negative example.. -> same pca generalization.. maximize variance  
  
Say  
  
[Triplet network](Attachments/77A96621-714F-4B6D-88C5-9FB4DFB75762.png)  
  
  
  
  
  
  
  
### NCE  
  
Noise Contrastive Estimation, short for NCE, is a method for estimating parameters  
of a statistical model, proposed by Gutmann & Hyvarinen in 2010. The idea is to run  
logistic regression to tell apart the target data from noise. Read more on how NCE is  
used for learning word embedding here  
  
  
  
[common setup](Attachments/8343F356-C8B9-4735-A62A-91DE30D86EF5.png)  
  
  
## Algorithm  
  
  
Idea: Push an entire batch instead of one..  
  
What is t-Distributed Stochastic Neighbor Embedding (t-SNE)?  
++[t-SNE](https://www.geeksforgeeks.org/machine-learning/ml-t-distributed-stochastic-neighbor-embedding-t-sne-algorithm/)++ is a non-linear dimensionality reduction technique specifically designed for visualizing high-dimensional data in 2D or 3D spaces. It works by modeling focuses pairwise similarities between data points in the high-dimensional space and optimizing their representation in a lower-dimensional space to preserve these similarities.  
* Unlike PCA t-SNE focuses on maintaining local relationships by minimizing the ++[Kullback–Leibler divergence](https://www.geeksforgeeks.org/machine-learning/kullback-leibler-divergence/)++ (KL divergence) between the high-dimensional and low-dimensional distributions of data points making it highly effective to find clusters and patterns in complex datasets.  
* However it takes a lot of time to run the results and it doesn't work well with very large datasets.  
* t-SNE is primarily used for exploratory data analysis and visualization rather than feature reduction or preprocessing.  
  
  
  
Finding pairs most dissimilar  
  
  
[Which pairs should we present?](Attachments/19704B41-9E1A-4550-B830-108C11E2EB35.png)  
  
## Self Supervised Learning..  
  
### Invariance  
  
In contrastive learning, data augmentation is the fundamental mechanism used to define the actual learning task. It dictates what the model considers "similar" and forces it to learn meaningful representations without human labels.  
Here is how data augmentation drives contrastive learning:  
**1. Creating Positive Pairs and Learned Invariance** To train a contrastive model (like SimCLR), a stochastic data augmentation module takes a single data example and applies random transformations to create two different, correlated "views" of it. These two views form a **positive pair**. The model's objective is to pull these positive pairs together in the latent space while pushing them apart from **negative pairs** (which are simply other random images in the training batch).  
By forcing the model to recognize that a heavily cropped, color-shifted image is still the exact same concept as a rotated, blurry version of that image, you are teaching the model **learned invariance**. The network learns to ignore superficial perturbations induced by the augmentations and instead focuses on the core semantic structure of the data.  
**2. The Crucial Role of Composition** Research shows that applying a single type of augmentation is not enough to learn good representations. The **composition of multiple augmentations** is absolutely critical.  
Specifically, combining **random cropping and resizing with random color distortion** is essential. If you only use random cropping, two different patches from the same image will usually share the exact same color distribution. A neural network will exploit this by taking a "shortcut"—it will simply match the color histograms of the two patches to solve the task, completely failing to learn generalizable features like shapes or objects. Composing cropping with heavy color distortion destroys this shortcut, forcing the network to actually understand the image content.  
**3. Contrastive vs. Supervised Learning Needs** Interestingly, unsupervised contrastive learning requires **significantly stronger data augmentation** than standard supervised learning. While applying aggressive color distortions might actually hurt the performance of a supervised model, it substantially improves the quality of the representations learned by contrastive models. Because the entire pretext task relies on matching augmented views, making those views drastically different creates a harder, more enriching challenge for the network.  
  
  
Neural networks learn semantics—the underlying abstract concepts, objects, and meaning within data—by being forced to solve highly constrained tasks where superficial memorization is impossible. Instead of relying on explicit human labels, modern systems acquire semantic understanding through three primary mechanisms:  
**1. Predicting the Hidden (Masked Autoencoding)**  
One of the most powerful ways models learn semantics is by being forced to reconstruct heavily corrupted data. In approaches like Masked Autoencoders (MAEs) or language models like BERT, the system hides a massive portion of the input—such as masking out 75% of an image's patches or hiding words in a sentence—and asks the network to predict what is missing.  
If a model only hides a tiny portion of an image, it can cheat by just copying the local textures or colors of adjacent pixels. However, when 75% of the image is gone, the network is forced to understand the global structure, or the **"gestalt" of objects and scenes**, to successfully infer plausible missing patches. Through this process of minimizing prediction errors, the network discovers that high-level concepts (like specific objects or grammatical rules) are the most reliable statistical predictors of the missing data. **The model discovers human-like semantics simply because those concepts are the only tools predictive enough to solve the masking task**.  
**2. Forced Invariance (Contrastive Learning)**  
Models also learn semantics by learning what *not* to care about. In contrastive learning, a model is given a single image and applies drastic random augmentations to create two different "views" (e.g., cropping one piece of the image, and taking another piece while heavily distorting its colors and blurring it).  
The model is then tasked with pulling these two drastically different views together in its representation space while pushing them apart from other random images. If the model only looked at superficial details—like the distribution of pixel colors—it would take a "shortcut" and fail to understand the image. By composing heavy distortions (like aggressive cropping combined with color dropping), the model's shortcut is destroyed. To match the two images, **the network is forced to learn "invariance" to superficial perturbations**, stripping away the noise to find the core semantic identity (e.g., "a dog") that remains constant across both views.  
**3. Aligning with Human Language (Multimodality)**  
Finally, models can learn semantics by directly anchoring their representations to human language. Words essentially act as the "atoms" of concepts, serving as symbols that denote specific sets of ideas.  
Models like CLIP leverage the massive amount of paired image and text data on the internet to learn a joint multimodal space. By training an image encoder and a text encoder to simply predict which text caption pairs with which image across hundreds of millions of examples, the visual model begins to map raw pixels directly onto the deep semantic structures already present in language. Because natural language is incredibly broad and generic, this form of supervision allows the model to learn a massive dictionary of semantic concepts, giving it the ability to perform "zero-shot" transfers to entirely new tasks without ever needing bespoke training data.  
  
  
No, **invariance does not mean that the label is known**.  
In representation learning, **invariance** simply means that a model's internal representation remains unchanged (stable) even when the input data undergoes superficial changes or transformations.  
If a model has learned a good invariant representation of a "dog," it will output the exact same semantic mathematical vector whether the picture of the dog is translated, scaled, rotated, zoomed in, or shifted in color. The model has learned to **ignore irrelevant information and focus only on the core semantic identity**.  
While labels *can* be used to teach a model invariance, they are not strictly necessary. Here is how invariance works with and without known labels:  
**1. Learning Invariance WITHOUT Labels (Self-Supervised)**  
As we discussed with contrastive learning models like SimCLR, a network can learn invariance entirely on its own without a human ever providing a label.  
* It takes a single unlabeled image and applies random data augmentations (like cropping, blurring, and color-jittering) to create two corrupted "views".  
* By forcing the network to pull these two visually different views together in its representation space, the network learns to be **invariant to the perturbations induced by the augmentations**. It learns that the underlying concept remains the same despite the visual noise.  
* **2. Learning Invariance WITH Labels (Supervised)**  
* When you *do* have known labels (such as in Supervised Contrastive Learning), you can teach the network an even broader type of invariance.  
* Instead of just pulling together two augmented crops of the *exact same* image, the model can use the known label to pull together two completely *different* images that share the same class (e.g., pulling a picture of a Chihuahua and a picture of a Golden Retriever together because they are both labeled "dog").  
* This teaches the model **class-level invariance**, forcing it to ignore specific breed details or backgrounds and focus purely on the abstract concept that unites them.  
* In both cases, invariance is the mechanism of **Concentration (Alignment)**—pulling similar concepts tightly together in the representation space so that the model becomes blind to meaningless variations.  
  
  
If you only have text data, you are working within the realm of **unimodal self-supervised learning**. In fact, text-based representation learning actually pioneered the deep learning concepts that were later adapted for computer vision.  
Because human language is already a highly compressed, information-dense representation of the world, models do not need to look at images to learn complex concepts. Instead, they learn the structure of the world entirely through the relationships between words.  
Here is how representation learning works when you only have text:  
**1. Predicting the Hidden (Masked Language Modeling)**  
Instead of removing patches of an image, text models hide words. The most famous example of this is **BERT (Bidirectional Encoder Representations from Transformers)**.  
* **The Task:** BERT takes a sequence of text, randomly masks out a percentage of the tokens (typically 15%), and forces the neural network to predict the original vocabulary IDs of those missing words.  
* **The Concept:** To successfully guess a missing word, the network cannot just read left-to-right; it must deeply fuse both the left and right context of the sentence. This is the exact same "predicting the hidden" concept as visual Masked Autoencoders, but because words are highly semantic, the model quickly learns deep grammar and factual relationships.  
* **2. Predicting the Future (Autoregressive Modeling)**  
* Instead of filling in the blanks, models like the **GPT (Generative Pre-trained Transformer)** family learn by strictly guessing what comes next.  
* **The Task:** The model is fed a sequence of text and must predict the very next token, reading only from left to right.  
* **The Concept:** If you scale this simple task up to billions of parameters and train it on a massive crawl of the entire internet, the model is forced to internalize the complexities of the world. To accurately guess the next word, it must implicitly learn factual knowledge, syntax, sentiment analysis, math, and even computer code.  
* **3. Text-to-Text Similarity (Contrastive & Relational Learning)**  
* You can also apply similarity-based learning entirely within the text modality to understand how different concepts relate:  
* **Word Embeddings:** Classic algorithms like word2vec map individual words into a continuous vector space where words that appear in similar contexts are pushed together.  
* **Neural Information Retrieval:** As we discussed with search engines, **Dual-Encoders** take a text query and a text document, encode them independently, and use dot-product similarity to pull matching text pairs together and push irrelevant ones apart. Advanced models like **ColBERT** do this by keeping fine-grained token-level representations to accurately compare the nuances between the two texts.  
* **Sentence Relationships:** To teach a model how larger ideas connect, BERT uses a "Next Sentence Prediction" (NSP) task. It is given two sentences (A and B) and must predict whether B logically follows A in the original document or if it is just a random sentence.  
* In short, when you only have text, you rely on the fact that humans have already compressed the physical world into discrete symbols (words). By forcing a machine to play fill-in-the-blank or guess-the-next-word on billions of sentences, you force it to reverse-engineer the human thoughts that generated those symbols in the first place.  
  
  
Large Language Models (LLMs) are famously recognized as both **"zero-shot learners"** and **"few-shot learners"** (the latter being the exact title of the seminal GPT-3 paper, *Language Models are Few-Shot Learners*).  
The reason they possess these incredible capabilities comes down to two main factors rooted in representation learning:  
* **Massive Self-Supervised Pre-Training:** Historically, neural networks were treated as "blank slates" that required massive amounts of task-specific labeled data to learn anything. Modern LLMs, however, undergo massive self-supervised pre-training on web-scale text. By simply trying to predict the next word in a sequence (autoregressive modeling) or fill in missing words (masked language modeling), the network is forced to learn deep semantics, grammar, and world knowledge. This creates a highly robust, general-purpose representation of the world.  
* **The "Text-to-Text" Interface:** Because LLMs use a standardized text-in, text-out framework, their architecture is entirely task-agnostic. This means that researchers no longer need to build specialized, heavily-engineered output layers or gather thousands of specific labels for every new task.  
* Instead of retraining the model's weights to teach it a new task, you can simply use natural language to reference the visual or linguistic concepts it has already learned. By providing a prompt (zero-shot) or demonstrating a new skill quickly with a few examples (few-shot or in-context learning), the model can immediately transfer its vast pre-trained knowledge to synthesize the correct output.  
* In short, LLMs are zero-shot and few-shot learners because their pre-training does the heavy lifting of understanding the world, allowing them to solve new problems with little to no specific training data.  
  
  
Point of so many losses and examples?  
  
HyperSphere, Margin Classifier-> SVM non linear transformation..  
Gaussian in 3d?  
  
  
Invariance  
  
embedding space. Example-> Clustering we did in machine learning.. but this topic should be here only which in all books is..  
  
  
Observations are trained now to correct observation..  
Similar observations are pushed together dissimilar are pulled apart  
  
  
  
  
  
  
  
  
  
## [2. Contrastive learning](Attachments/FD0DE8DB-3877-4A0D-B3DC-F06D13B1F237.png)  
1. ImageNet top-1 accuracy of linear classifiers trained on representations learned with different self-supervised methods (pretrained on ImageNet). Our method, SimCLR, is shown in bold.  
  
[2. Contrastive learning](Attachments/8A691940-8F57-433F-8389-FF8E3EEE626A.png)  
  
Predictive..  
  
First generate different augmentations of data-> Image-> Cropping, Rotating, Blurring.. Goal to cluster similar items together and push dissimilar apart in self supervised way..Self supervised-> Already know labels of augmented data.. learn from them.. push them together, dissimilar-> pull them apart..  
LLMs are trained in this way..  
  
  
[2. Contrastive learning](Attachments/01A66130-5C94-4657-8F73-D1EDBFE14F47.png)  
[eg. video, audio, images](Attachments/60AD5758-3A65-4468-81C4-AC0F56D9A95B.png)  
  
  
  
## Multi Modality Prediction  
[Self-supervised learning](Attachments/4B579178-E4DE-4869-9D37-EA1756672E99.tiff.png)  
  
[3. Multi-modality](Attachments/44C89893-BB7F-43B4-B8F1-AC6D39C2FED8.png)  
  
  
[Pretext task:](Attachments/57635DF7-9B0E-4699-BE50-BB2711F1E9C2.tiff.png)  
  
**Imputation->  Predict missing data**  
  
[Imputation: one pretext task to rule them all?](Attachments/1AE0DB13-B20E-4A5C-84CA-FBECF7FA264E.tiff.png)  
[Screenshot 2026-08-16 at 2.26.30 PM.png](Attachments/D196A3C4-A0C3-4BEE-80B4-D3596D6E0541.png)  
[e.g. image classification (done in the contrastive way)](Attachments/74F75BAE-EC39-4144-8F2D-2EE5B1EC2309.png)  
[e.g. image classification (done in the contrastive way)](Attachments/8698CFD5-0D2C-48D9-BAD5-10CB9969C8B1.png)  
  
[e.g. image classification (done in the contrastive way)](Attachments/2038A24E-D102-49BC-A671-749D9F8448BA.png)  
  
[e.g. image classification (done in the contrastive way)](Attachments/D516926C-432B-4EF3-A49D-2A4A1A837DDA.png)  
  
  
[Summary](Attachments/0F0E44B2-ACDE-45DC-90E5-AFBBD5A934DF.png)  
  
  
  
  
[Betore diving in, let us present the basic problem statement and the notation we](Attachments/962BF2BC-0D80-4044-9894-69988401CB2D.png)  
  
  
**Mapping data to a representation..then reconstructing back **  
  
### Depends on our choice we can build representations that is larger than our input  
  
[Data space](Attachments/E8C26FA9-DF77-44A4-A302-2E290A188C31.png)  
  
  
  
  
Why learn representations, we can use it for many tasks.. termed transfer it to other tasks or transfer learning from representations of 1 to another  
  
  
**PCA and k means(clustering) are very important models, everything else in representation learning is just a generalization of them**  
  
**Clustering-> Basically learns a latent space z.. or in 1 dimensional integers..**  
  
## Compression Methods  
  
  
  
  
# AutoEncoder  
  
  
**Overview**  
  
**Dimensionality->R^n->R^m->R-^n**  
**m<n.. in autoencoder architecture**  
**R**  
** PCA**  
  
**Autoencoder, Contrastive Learning-> Learn Representations by compression**  
  
**Autoencoders are deep learning versions of PCA**  
**Another method guess?  is deep learning version of k means **  
  
  
  
  
  
**Maths Revision**  
  
**MSE Loss Dervivation**  
  
In linear regression, error terms should be Gaussian with **a mean of zero and constant variance (homoscedasticity)**, and they must be **independent (uncorrelated)** of each other and the predictor variables.  
  
**Core Properties of Error Terms**  
  
**Zero mean:** The average value of the errors across the data must equal zero.  
**Constant variance (Homoscedasticity):** The spread of the errors must stay the same across all values of the input variables.  
**Independence (No Autocorrelation):** One error value must not predict or relate to another error value.  
**Normal distribution:** The errors should follow a bell-shaped curve around the regression line. [1, 2, 3]  
  
**Loss Functions and Error Assumptions**  
  
**Mean Squared Error (MSE):** Using MSE implicitly assumes that the reconstruction errors are **Gaussian** with a mean of zero and constant variance. Minimizing MSE is mathematically identical to maximizing the likelihood of a Gaussian distribution. [2, 3, 4]  
**Binary Cross-Entropy:** Used when input data is normalized between 0 and 1. This assumes the reconstruction errors follow a **Bernoulli (binomial)** distribution rather than a Gaussian one. [5, 6]  
**Absolute Error (MAE / L1):** Using MAE implicitly assumes that the reconstruction errors follow a **Laplace**distribution, which has fatter tails than a Gaussian curve.  
  
  
## Overview  
  
  
Latent-> Not yet existing  
[What is a representation?](Attachments/F47DE9E7-7A89-4F8F-BD9E-71165F5B6B0D.tiff.png)  
**The Inductive Bias:** The assumptions baked into the model architecture  
Embedding->Neural Network every layer is an abstraction(embedding) of the data.  
PCA-> Pick some  vectors such that it captures maximum variance so that data is as less disentangled as possible.. Means correlation between data is as less as possible.. Covariance Meaning?  
[image](Attachments/27B6459F-8CD2-4DFD-8CB3-F89D72833395.tiff.png)  
  
Latent Space-> An Embedding Space  
  
AutoEncoder-> Space where objective is L2 norm(derived by gaussian(N(0,1)) between two points is minima  
  
## Auto Encoder Loss Function  
  
  
  
In an autoencoder, the equivalent assumptions about error terms depend entirely on the **loss function** you choose to train the network. Because autoencoders are neural networks, they do not strictly require Gaussian errors to function, but their training math is deeply connected to these concepts. [1]  
  
## Key Differences from Linear Regression  
  
* **Independence:** Autoencoder errors do not need to be independent. The network can capture highly complex, non-linear relationships, meaning errors are often correlated across features.  
* **Variance:** Standard autoencoders do not enforce constant variance. However, **Variational Autoencoders (VAEs)**explicitly force the latent space errors to follow a standard Gaussian distribution with zero mean and unit variance using a regularization penalty (KL divergence). [7]  
  
  
  
In representation learning, **the core goal is to automatically discover the underlying features, patterns, or structuresfrom raw data and transform them into dense vector formats (embeddings) that make downstream machine learning tasks easier to solve**  
Instead of manually designing features (like hand-crafting edges in images or keywords in text), the model learns the representation itself. [6, 7, 8]  
  
  
  
  
1. Compression-> AutoEncoders, Contrastive  
2. Prediction-> Masking, 2 more..  
  
  
  
3. **The Bottleneck (Compression):** Forcing data through a low-dimensional space (like an autoencoder's hidden layer) to strip away noise and retain only the most critical information. [9, 10, 11, 12, 13]  
4. **The Objective Function (Loss):** The mathematical rules guiding what the representation cares about (e.g., using **MSE** to preserve exact pixel layouts, or **Contrastive Loss** to preserve semantic meaning).  
5. Prediction  
## 🌟 What Makes a "Good" Representation?  
A high-quality learned representation generally satisfies these properties:  
  
* **Expressiveness:** It captures a massive amount of information in a relatively small vector. [20, 21, 22]  
* **Disentanglement:** It separates distinct real-world factors into independent dimensions. For example, in a face representation, one dimension controls skin tone, another controls glasses, and another controls lighting. [23, 24, 25]  
* **Invariance:** It remains unchanged by irrelevant transformations. A picture of a cat should yield a similar "cat vector" whether the cat is flipped upside down, brightly lit, or placed in the corner of the frame. [26, 27, 28]  
* **Smoothness:** Similar concepts sit close together in the vector space. Moving slightly in the latent space should result in a smooth, logical change in semantic meaning. [29, 30, 31]  
  
## 🛠️ Common Paradigms & Their Loss Functions  
Representation learning changes drastically based on how the model is trained: [32]  

| Paradigm | Objective / Approach | Common Loss Functions |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Generative |  |  |
| (e.g., Autoencoders, VAEs) | Reconstruct the exact input from the compressed latent code. | MSE (for continuous data) or Binary Cross-Entropy. |
| Contrastive |  |  |
| (e.g., SimCLR, CLIP) | Push representations of similar items closer together and pull dissimilar items far apart. | InfoNCE Loss, Triplet Loss, Cosine Embedding Loss. |
| Masked / Predictive |  |  |
| (e.g., BERT, Masked Autoencoders) | Hide a portion of the input (text or image pixels) and force the model to predict the missing pieces using surrounding context. | Cross-Entropy (for tokens) or MSE(for patches). |
  
  
## 🔗 Connecting the Dots (Regression → Autoencoders → Representation)  
Your questions trace a perfect evolutionary line in machine learning:  
  
1. **Linear Regression:** Learns direct mapping weights assuming simple **Gaussian** errors.  
2. **Autoencoders:** Expand this by forcing data through a non-linear network to minimize **MSE** (which inherently assumes Gaussian reconstruction errors).  
3. **Representation Learning:** Takes that autoencoder bottleneck and generalizes it. It proves that the "compressed code" created by minimizing that loss is often far more valuable for classification, clustering, or generation than the raw data ever was. [33, 34, 35]  
4. Are you currently designing a representation learning pipeline? I can help you pick the best approach if you share your **data type** (e.g., text, graphs, audio, or images) or your ultimate **downstream goal** (e.g., anomaly detection, classification, or search/retrieval). [36, 37, 38, 39, 40]  
  
#diary**-> just revise daily and practice now.. there will be some bad pain days.. for the next month.. do not waste time.. do projects now.. esp after physio.. there can be pain.. no wasting time.. let's see..**  
  
  
**Architecture tradeoff-> they are good at learning some representations bad at others like shape vs colors.. good representation of colors bad at shapes, why colors are just pixels.. shapes are not..**  
  
**L2 Autoencoders-> **  
  
**Neural Networks are representation learners..**  
  
  
** Earlier layers generate representations.. later are finetuned for that task.. can be transferred(Transfer learning) by freezing those layers.. basically.. **  
  
**is_trainable=False.. syntax depends on framework used..**  
  
**basically this.. **  
  
**From Data to representations-> called Encoding or Encoder.. **  
**from representation to data-> Generative Modeling->  called decoding or Decoder**  
**methods.. many..**  
**Identity-> Autoencoder**  
**with loss-> Variational Autoencoder..**  
**Now practice..**  
  
  
When embeddings are generated by a neural network, they are clustered into groups which is a generalization of linear clustering..  
  
## Latent embedding Space  
  
  
  
  
Yeah, equivalent of PCA. OK, right. So you're on to this. What is PCA doing? PCA can be understood as trying to  
maximize the variance I'm capturing in the signal via some linear orthogonal transformation of the vector.  
And if I'm maximizing the variance, I'm able to best reconstruct. And that actually is exactly equivalent to the L2  
reconstruction objective. So PCA can be understood as doing essentially the same thing.  
So if they're both linear, we'll just replace it with the encoders of matrix W. The decoder is a matrix Wg, and the  
encoders matrix Wf. And we're trying to say, if I pass encode, decode, I will obtain my original data matrix again.  
That's the objective of an autoencoder written with linear f and g.  
And PCA is a variant of this, where we assume that the encoder and decoder are the same matrix W. And they  
have this property that it's an orthogonal matrix, so that's the constraint. It's a slightly different setting, but it's  
almost the same.  
And so this is the objective that PCA tries to minimize. It tries to find W such that this transformation will result in  
decoding back to the original data. So you can work through the math.  
If you're more familiar with PCA maximize the variance in the projected space, then you can work out that this  
thing under this condition is equivalent to minimize the variance in x minus the variance in the transformed  
version of x. And then we can maximize and change the sign to be plus instead of minus. And then we can  
remove this term because this term doesn't depend on W, and we're maximizing over w.  
And then this is just maximize the variance captured in the reconstructions. And that might be more familiar PCA  
that you're used to. And what can be proven is that the embeddings learned by a linear autoencoder span the  
same subspace as embeddings learned by PCA. So this is the rough the rough argument there.  
So vanilla, most intro statistical model that you can think of, the most standard one that's been around for  
hundreds of years, I believe, or quite a long time, PCA. Well, an autoencoder, the very best representation  
learning method in the family of reconstruction based representation learning is just nonlinear PCA. That's a  
generalization of PCA to nonlinear representations.  
  
  
[PDF 5]  
  
Representation Space:  
  
is thought be Gaussian N(0,1)  
  
distance between two clusters-> Maths is for gaussian it is L2 Norm.. Derivation see your notes or ask chatgpt..  
  
min(Expected value of (x¡-x¡)^2))  
  
[PDF 6]  
L2 Norm-> euclidean norm  
  
I cannot learn formulae but proofs are easier to conceptualize 10 years later..  
  
[PDF 4]  
  
learning by compression  
  
## Clustering K means or Vector Quantized  
  
  
  
  
[PDF 2]  
  
So let's look at clustering now. So clustering is the problem of taking data and assigning each data point to a  
cluster. So a representation-learning lens on clustering is you're learning an encoder that doesn't output a  
vector. It outputs an integer. So for every data point, I output an integer, which is the cluster assignment. It still  
is an encoder. It's still representation learning.  
So at inference time, if I just apply my learned encoder that outputs integers to some data points, it will tell me,  
this is the third class. And I'll color that red. And that has identified clusters So clustering is learning an encoder  
to integers.  
  
  
[VQ nets](Attachments/7D476BF5-633E-4152-91D7-5C3624FA4922.tiff.png)  
[PDF 3]  
So why is clustering a good representation? So from the representation-learning angle, **clustering is learning a**  
**function f that outputs an integer, will represent the integers of one-hot code, in this example here**.  
## I will map every image like this to this cluster, and I can just label it arbitrarily with a  
## word.  
  
  
  
So we can think of it as a vector embedding, but it's just a one-hot vector embedding that's isomorphic with the integers, for a finite set of integers.  
So. what's the best representation that-- this is another subjective statement. What's the best representation  
that humans have come up with so far? What do you think? What's the best representation that the human brain  
has discovered? Yeah?  
  
  
  
  
**And clustering is the problem of making up new words for things**. That's one way of understanding it, right? A  
word is like a symbol that at least-- there might be some linguists that would quibble about this, but one rough  
definition of word is it's just like it is a symbol that denotes a set, and that's what clustering is doing.  
  
  
  
  
** Language has more structure beyond the words, but this is but words are an important part of it. So clustering is the representation learning problem of finding new words for concepts.**  
[PDF]  
  
  
  
Representation earning is generalizing these concepts concepts of PCA and k means  
  
  
So what does k-means do? k-means finds k different clusters in your data. And each cluster is represented with  
what's called the mean or centroid, which is just going to be the average of all the data points in that cluster. So it maps data  
points to integers. And it does that in such a way that each data point is as close as possible to the mean of the data points in the cluster it is assigned to. So here's the representation learning view of k-means. I'm going to train an encoder that will output one-hot  
codes. And then my decoder will just be-- think of it like a lookup table. It takes in a one-hot code, and it outputs  
a vector. And it's trying to output the vector that will reconstruct the input as best as possible.  
If I only can output a single vector for every item in a cluster, every item in the cluster goes to the same one-hot  
code. So now I can decode that into just a single vector. Think of g as a matrix W applied to a one-hot code. It  
selects a row of that matrix.  
What is going to be the decoder that minimizes the Euclidean distance reconstruction error, the L2 reconstruction  
error? What is the name for the vector that minimizes the distance to all points in a set, the L2 distance? Yeah?  
he mean, OK. I think a lot of that, maybe some of you don't. But, yes, the vector that minimizes the L2 distance  
to a set of other points is the mean of those other points.  
  
  
  
  
  
  
  
  
  
You can show that.  
So that means that k-means is an L2 autoencoder. The only difference from the other autoencoder that I showed  
you is that the hypothesis space doesn't have a low-dimensional bottleneck. It has an integer bottleneck, OK?  
So that's just a mapping of k-means onto autoencoders. They're the same model with a different hypothesis  
space. k-means, this hypothesis space is not differentiable. It has some properties that can be exploited, some  
structure that can be exploited.  
So we optimize it with a different algorithm than SGD. And that's where you might have encountered the  
**expectation maximization me**thod for doing k-means and so forth. And, yeah, that's just because this problem  
has some special structure.  
And then the deep learning version of k-means is called a **vector quantized autoencoder.** So a vector quantized  
autoencoder is exactly the same as k-means, except that f is non-linear instead of linear. And there's a whole  
bunch of variations on VQ models. There's VQGAN, VQVAE, et cetera, et cetera. These have bells and whistles,  
but this is the gist of it.  
I'm trying to learn an encoding into a set of integers and a decoding that minimizes reconstruction error. And f  
will be a deep network, or little f in little g are both going to be deep neural networks. So you can read up on  
exactly how that method works, but it's just k-means with deep nets. Yeah?  
  
#diary First learn concepts.. but remember terms.. to be able to answer interview questions.. like today's interview.. human in the loop.. in llamaindex.. Import all your notes..  
## Representing by Prediction  
  
Label Prediction..  
Given half features construct rest  
  
**Same Self Supervised Learning**  
  
  
So now rather than learning representations by compressing data, we're going to try to learn representations by  
predicting held-out data. And this is actually the kind I started this lecture with. I said that we could just pre-train  
a network on music classification. That's a prediction problem, and it induces an OK representation for music  
classification.  
But we're instead going to do something else, which is we'll say, we didn't want labels. We don't want to be we  
don't want a representation that is tied to a specific task. So we don't want to have to have humans label some  
narrow task. We do something much more generic that doesn't require annotations or task specificity.  
And one way to do that is we say, we're not going to predict labels. We're going to predict the raw data itself. And  
this is called self-supervised learning.  So it's called self-supervised learning because it's using the machinery of supervised learning, meaning predict y from x, except that we define y as being some part of the raw data as  
opposed to some label. So this is like an autoencoder, except I'm predicting half of the data from the other half of the data. And  
interestingly, this works really well. This tends to work a lot better than autoencoders.  
  
**Example**  
  
So here's an example of this setup. This is the colorization problem I showed you before. Try to predict the colors  
from a black and white image?  
And this is a self-supervised method that tries to predict part of the raw data, the color channels, from another  
part of the raw data, the black and white channel. So we can now take that model that's just trained to do this  
self-supervised prediction of the missing colors.  
  
Now it's free labels because color images have the colors built in. I just took the color image. I split it into the  
luminance channel and the color channels. So it's cheap. It's easy to run this on just raw, unlabeled data.  
Now I can investigate, did this system actually learn a meaningful representation? So we'll do the deep net  
electrophysiology. I'll poke my probe in there and ask, what are the neurons sensitive to?  
  
So here, I guess I'll ask the class. What do you think? Remember when I talked about the Zeiler and Fergus  
model, I said that they were like face selective neurons, and dog face selective neurons, and other things. What  
do you think the neurons will be sensitive to for predicting colors?  
And let's look at layer five of a network, so deep inside the network. What do you all think? Yeah, over here?  
  
  
Yeah, different classes of objects have different colors. If I know something's strawberry, I can say it's probably  
red. So knowing the object category tells me a lot about the color. Anything else? So, yes, it turns out objects is  
one of the answers.  
  
So here are our three different neurons. And this is looking at the feature maps. And we're just shading-- we're  
blacking out all the parts of the feature maps where the activations are below a threshold. So this is like, where  
are the neurons firing at some convolutional layer 5 of this network?  
  
And, yeah, on lower layers, it is textures and other things like this. But the interesting thing is that it doesn't  
really matter how you train these networks. If you train them to predict classes, if you train them to predict  
colors, if you train them to inpaint missing pixels, just pick the right half of the image from the left half, the units  
that carve the world at its joints, that are predictive of everything, turn out to be objects and semantics and the  
words that humans have.  
  
So it's like words are not arbitrary. We have the words we have because they're very predictive statistically of  
missing data. So this is discovery of semantic words without any semantic labels.  
  
And this has been the big finding over the last decade that led to this revolution in how we do deep learning,  
which was the move from supervised learning to self-supervised learning. So the self-supervised learning is-- we used to try to do what's called unsupervised learning, which is just learn from raw, unlabeled data. But then we  
switch it into the mathematical machinery of supervised learning by just predicting some fake labels, which are  
just raw data, which you call pretext labels or pretext tasks from the data itself.  
  
And there's so many different ways of doing this learning by prediction. So you could just predict class labels.  
That would be called supervised learning of representations. You could predict the next frame in a video, the  
future. You could predict the next pixel in a sequence and the same thing for any other data modality, too.  
So the two on the right are self-supervised because no human had to provide the label target. It's the next frame in the video, the raw data. It's the next pixel in a sequence.  
  
  
  
  
And as you probably know,  
[6.390 IntroML (Spring26) - Lecture 8 Representation Learning Slides 3]  
the way that language models work is they predict the next word in a sequence, so  
they're mostly in the family of this type of learning. And most people still call language models self-supervised  
because they're just predicting the raw data. It happens the raw data is semantic and is words, but in that  
context, it's not like they're predicting the sentiment. They're just predicting the next word.  
So all of these self-supervised tasks can be understood as something we call imputation, which just means take  
  
your data-- it could be a matrix, a tensor, some data object. A video would be like time by x by y. A sentence  
would be time by the content at that time, the word at that time.  
And mask part of it, and put that into an encoder. Decode it to predict the masked part of that input. So masked  
prediction or imputation is the standard pretext tasks that people like to use these days to learn representations.  
So spatial imputation, just predict the next pixel from the previous pixel. Temporal imputation-- predict the next  
frame from the previous frame. Channel imputation-- predict the colors from the black and white and, again, on  
other modalities, you can do the same.  
  
**Prediction by masking**  
  
Yeah, you can do this in a way that frames it just like an autoencoder, again, but it will be called now a masked  
autoencoder. So masked autoencoder is you take your data, you mask random chunks of it. And the little  
interesting trick is that in masked autoencoder is applied to images.  
You're using a vision transformer. And the vision transformer already tokenized the image into the first--  
remember, we talked about vision transform. We said that we are going to create a set of tokens by chopping the  
image into patches and then mapping those patches to vector embeddings or tokens that then get processed.  
And so they just said, well, what if I just remove some of the tokens, and then I predict the missing tokens?  
And the really interesting thing about the attention architecture is that I can mask different ratios. I can only  
keep four of these tokens, but then the attention mechanism will scale in a way that is proportional to the  
number of tokens. Each token will attend to each other token.  
So if I have four, it will be four attending to four. And it will output predictions for four. If I have eight, it will be  
eight attending to eight. So it has this nice kind of architectural invariance to the number of tokens you put in.  
And then I decode. I just have some blank tokens I put into another transformer. And then I have trained it so  
that those blank tokens get filled in with the prediction of the pixels in the missing tokens, or the prediction of the data in the missing tokens.  
  
**Vision**  
  
[Masked Autoencoder (MAE)](Attachments/C549B1E2-FAAA-4242-AE58-1D2C992A0EDD.png)  
**Text**  
  
  
And masked autoencoders are just a new name for another model which was very popular called BERT. So there are differences.  
[Bidirectional Transformers (BERT)](Attachments/A068E32D-BF0D-4A27-ABF0-8411F9780DBB.png)  
  
Engineering this to work on language versus vision is a very important difference but,  
conceptually, they're almost the same thing.  
Mask LM  
Uses Byte Pair Tokens  
  
Bidirectional Transformers  
  
[Bidirectional Transformers (BERT)](Attachments/DC56B6B5-9D23-438E-8A24-CC087422B9E3.png)  
So BERT was a language model that was very popular some years ago. It's gone a bit out of fashion, but BERT is  
roughly the same thing on text. So I just take my text. I tokenize it. I mask some of the tokens. I run it through a  
transformer, and I predict all the tokens. So I'm now doing masked prediction with language. some tokens in between.. maskingWe introduce a new language representation model called BERT, which stands for **Bidirectional Encoder Representations from Transformers. **Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement), and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).  
  
**Popular Works best Guess and reason why**  
  
I only thought difference between masking in between words vs masking final word.. Real question is masking vs autoencoder..  
  
And the autoregressive models that try to predict the next word in a sentence are just the same, except they're  
only masking the final word as opposed to interleaving words. And th  
[Masked prediction often works better than autoencoding](Attachments/541FE586-767C-41B7-9AEE-A056141A695F.png)  
  
at has some advantages in that I can  
decode in sequential order as opposed to in out-of-time order. So, yeah, question? final token  
Works by Conditional likelihood..  
  
  
  
AUDIENCE:  
  
Why is BERT getting out of fashion?  
  
Why is BERT getting out of fashion? So I think it's because masking the final token, naturally, can be used for  
generating sentences autoregressively, which we talked about before. If I mask the interleaving, then it's like I'm  
generating words out of temporal order. positional encoding instead of masking  
  
  
So if I'm talking with a human, time is an axis that is important and not symmetric with other axes. I have to  
answer the question after the question has been asked by the person I'm talking to. And so having these causal  
attention mechanisms for the masking is in causal order. I'm only masking the future in conditioning on the past.  
It just fits into language models, which operate in causal order.  
  
And once that became popular, the biggest models were all masking only the tokens in the future, given the  
tokens in the past  
  
  
  
And because those were the biggest models, they just worked the best. But if I want to learn a  
sentence embedding, I bet the BERT method is still going to work better if scaled the same amount.  
  
  
  
  
  
OK, so here's an interesting empirical finding. This is going back to that colorization paper, but it's been shown in  
a lot of work, which is that masked prediction just tends to always work better than autoencoding.  
So if I I'm going to look at the accuracy, I'm going to look at the representations at each layer of an autoencoder  
versus a masked prediction network, for colorization in this case. And I'm going to assess performance seeing  
how well I can linearly classify given the representation on that layer.  
Imagenet categories, in this case, is like a probe, just like we were doing with the shapes, where we had the  
nearest neighbor probe. Now we have a linear classifier probe. So here's what happens.  
As I go deeper in the network, you get this separation, where autoencoding learns an OK representation, but  
masked prediction learns a representation which is more semantic. It linearly decodes ImageNet categories  
better. And this is something that I thought I had a good explanation for, and then I realized I don't.  
  
## Final Project why masked prediction works better than autoencoding  
  
[Masked prediction often works better than autoencoding](Attachments/E492EBA2-D162-49C7-A55F-E03FB8344F73.png)  
  
  
  
So I'm going to call it ongoing science and leave it as a puzzle for the class. And maybe this would be a good final  
project. Why does masked prediction work better than autoencoding? So here are three hypotheses to think  
about.  
  
[Masked prediction often works better than autoencoding](Attachments/FDAB6734-EA87-45A0-A1D0-E1CC4AFF46AF.png)  
So one is that autoencoding controls compression via dimensional bottleneck. Masked prediction controls  
compression by the non-overlap between the outputs you're predicting and the inputs you're conditioning on.  
  
  
So  
the only thing that's useful for predicting the outputs is the mutual information between the inputs and the  
outputs. And if these are separate, then I will just forget all the stuff that's specific to the inputs that's not  
relevant for the output. So that's how it does compression.  
So it could be that just controlling compression via dimensional bottlenecks is really hard to make work. It's very  
finicky. It requires an architecture that has constraints on the dimensionality of the embeddings.  
  
  
  
And we know that low-dimensional things, anything with low dimension and deep learning just is hard. It interacts with optimization in weird ways and interacts with BatchNorm and LayerNorm in weird ways. So low-dimensional embeddings have some bad properties, and maybe it's just really hard to use dimensionality of the embeddings as the way to learn a good representation.  
  
[Hypothesis 1: It's hard to control compression via a dimensional bottleneck.](Attachments/0F3FC0F8-CF64-4623-A815-AE1768112001.png)  
Hypothesis two is autoencoders are learning shortcuts. So in order for me to reconstruct the signal-- imagine this.  
What if I had an autoencoder with skip connections, with residual connections?  
Would that be a good idea?  
  
What would be wrong with that, autoencoder f, g, but they just have some residual  
connections in between f and g?  
  
F=f((g(x))-> Identity..=I  
If residual-> (f+f(f(g(x)-> embedding..-> skip connection +g(x))..? it will skip the embedding  
  
  
  
AUDIENCE: Not forcing this low-dimensional representation.  
PHILLIP ISOLA: Yeah. It skips the bottleneck. So there's all these little gotchas like that. And it could be that autoencoders just  
have this tendency to copy the local information that they're processing. And that will be a decent solution, even  
though it would be better for them to capture global properties in order to reconstruct the entire signal.  
And then maybe math prediction is closer to the prediction problems we actually care about.  
[• Hypothesis 1: It's hard to control compression via a dimensional bottleneck.](Attachments/68214040-09C0-4E31-890F-B9BB80129E72.png)  
  
So somehow it's closer to the actual use case. We're going to try to predict the future from the past or something like this.  
So I don't know. I asked Kaiming, who's a professor here who was the first author of "The Masked Autoencoder" paper. And he said, well, at the end of the day, it's just empiricism. So masked prediction works better than  
autoencoding. And I think it's a really interesting question, theoretically why that should be the case. Yeah?  
AUDIENCE: [INAUDIBLE] beginning of the lecture, you said that in the scope of representation learning, you think this  
framework of [INAUDIBLE] is simplest and will win out. I was wondering if you could talk about why you think that  
is?  
  
  
  
Yeah, so ultimately, it just goes back to some first principle argument that I can't really prove. But there are  
arguments along the lines of Occam's razor(Occam's razor is the problem-solving principle that recommends searching for explanations constructed with the smallest possible set of elements. It is also known as the principle of parsimony or the law of parsimony.) and formalisms of that the compression is somehow equivalent to prediction. And the most compressed representation will make the most accurate predictions about the future.  
And autoencoders are just a simple embodiment of the idea of take your data, compress it as much as possible,  
and remove all redundancies. And it just seems, from first principles, if compression is all you need, then  
autoencoders are all you need. I think there's more to say about that  
  
. I don't have time right now.  
So, yeah, still an open question. I'll end with I think this is a nice idea that Yann LeCun put out some years ago,  
which is that intelligence is like this cake.  
  
## Summary  
  
Masked Autoencoders (MAE) mask random image patches and reconstruct pixels. BERT masks random text tokens and predicts missing words using both sides. Autoregressive models mask future tokens and predict the next word using only past context. They differ in data types, training goals, and context flow. [1, 2, 3, 4, 5] Key Differences   

| Masking Type | Data Type | Masking Strategy | Context Use | Objective | Key Papers |
| ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- | -------------------- |
| Masked Autoencoders (MAE) | Vision (images split into patches). | Random high masking (often 75% of patches). | Bidirectional (sees all unmasked patches around the target). | Reconstruct raw pixel values of missing patches. | [6, 7, 8, 9, 10] |
| BERT Language Masking | Text (words or sub-word tokens). | Random moderate masking (usually 15% of tokens). | Bidirectional (sees left and right context of the masked word). | Predict the exact original token ID (classification task). | [11, 12, 13, 14, 15] |
| Autoregressive Future Token Masking | Text or sequential data. | Casual lower-triangular mask hiding all future tokens (t+1 and beyond). | Unidirectional (sees only past and current tokens). | Predict the single next token in the sequence. | [16, 17, 18, 19, 20] |
  

| Masking Type | Data Type | Masking Strategy | Context Use | Objective | Key Papers |
| ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- | -------------------- |
| Masked Autoencoders (MAE) | Vision (images split into patches). | Random high masking (often 75% of patches). | Bidirectional (sees all unmasked patches around the target). | Reconstruct raw pixel values of missing patches. | [6, 7, 8, 9, 10] |
| BERT Language Masking | Text (words or sub-word tokens). | Random moderate masking (usually 15% of tokens). | Bidirectional (sees left and right context of the masked word). | Predict the exact original token ID (classification task). | [11, 12, 13, 14, 15] |
| Autoregressive Future Token Masking | Text or sequential data. | Casual lower-triangular mask hiding all future tokens (t+1 and beyond). | Unidirectional (sees only past and current tokens). | Predict the single next token in the sequence. | [16, 17, 18, 19, 20] |
  
  
  
  
Would you like to explore how these affect fine-tuning performance or the math behind the attention masks for one of these models?   
A lot of you may have seen this, where the bulk of the cake is representation learning.  
  
[How Much Information is the Machine Given during Learning?](Attachments/366FB134-DA83-4A36-A0CA-763CC503BB79.png)  
  
  
You spend a lot of data and a lot of time coming up with a really good representation of the world in a self-  
supervised way or an unsupervised way, not tied to any specific task. So self-supervision is about not having  
labels, but it's also about not being narrow and tied to a task. It's just generally compress the universe into  
something that's predictive of the future and is compact.  
And then the icing and the cherry are all the rest of machine learning-- supervised learning, adaptation, post-  
training, reinforcement learning. So he's making the point that representation learning is the bulk of intelligence,  
and I agree with that point. So I will end th  
  
  
So BERT was a language model that was very popular some years ago. It's gone a bit out of fashion, but BERT is roughly the same thing on text. So I just take my text. I tokenize it. I mask some of the tokens. I run it through a  
transformer, and I predict all the tokens. So I'm now doing masked prediction with language.  
  
  
And the autoregressive models that try to predict the next word in a sentence are just the same, except they're  
only masking the final word as opposed to interleaving words. And that has some advantages in that I can  
decode in sequential order as opposed to in out-of-time order. So, yeah, question?  
  
  
  
# Similarity Based Learning  
  
  
  
  
  
## Outline  
Vector databases chroma, pincecone are based on this  
1. Information retrieval (IR), as an application area of representation learning  
2. Contrastive learning  
3. Approximate nearest-neighbor (ANN) search  
4. Neural IR Paradigms: Cross-Attention, Dual-Encoders, Late Interaction  
  
  
Why learn representations?  
  
  
• To improve generalization  
• To do more learning from limited high-quality data (transfer learning)  
• To **organize information** by exploiting geometric similarity, vector databases are based on this..  
