# Natural Language Processing course  
  
* This is the 2025 iteration of the course, materials are added as we prepare them.  
* Lecture and seminar materials for each week are in ./week* folders, see README.md for materials and instructions  
* Any technical issues, ideas, bugs in course materials, contribution ideas - add an ++[issue](https://github.com/yandexdataschool/nlp_course/issues)++  
  
* Installing libraries and troubleshooting: ++[this thread](https://github.com/yandexdataschool/nlp_course/issues/1)++.  
  
## Syllabus  
  
* **++[week01](https://github.com/yandexdataschool/nlp_course/blob/2025/week01_embeddings)++** **Word Embeddings**  
    * Lecture: Word embeddings. Distributional semantics. Count-based (pre-neural) methods. Word2Vec: learn vectors. GloVe: count, then learn. Evaluation: intrinsic vs extrinsic. Analysis and Interpretability. ++[Interactive lecture materials and more.](https://lena-voita.github.io/nlp_course.html#preview_word_emb)++  
    * Seminar: Playing with word and sentence embeddings  
    * Homework: Embedding-based machine translation system  
* **++[week02](https://github.com/yandexdataschool/nlp_course/blob/2025/week02_lm)++** **Language Modeling**  
    * Lecture: Language Modeling: what does it mean? Left-to-right framework. N-gram language models. Neural Language Models: General View, Recurrent Models, Convolutional Models. Evaluation. Practical Tips: Weight Tying. Analysis and Interpretability. ++[Interactive lecture materials and more.](https://lena-voita.github.io/nlp_course.html#preview_lang_models)++  
    * Seminar: Build a N-gram language model from scratch  
    * Homework: Neural LMs & smoothing in count-based models.  
* **++[week03](https://github.com/yandexdataschool/nlp_course/blob/2025/week03_attention)++** **Seq2seq and Attention**  
    * Lecture: Seq2seq Basics: Encoder-Decoder framework, Training, Simple Models, Inference (e.g., beam search). Attention: general, score functions, models. Transformer: self-attention, masked self-attention, multi-head attention; model architecture. Subword Segmentation (BPE). Analysis and Interpretability: functions of attention heads; probing for linguistic structure. ++[Interactive lecture materials and more.](https://lena-voita.github.io/nlp_course.html#preview_seq2seq_attn)++  
    * Seminar: Basic sequence to sequence model  
    * Homework: Machine translation with attention  
  
* **++[week04](https://github.com/yandexdataschool/nlp_course/blob/2025/week04_transfer)++** **Transfer Learning**  
    * Lecture: What is Transfer Learning? Great idea 1: From Words to Words-in-Context (CoVe, ELMo). Great idea 2: From Replacing Embeddings to Replacing Models (GPT, BERT). (A Bit of) Adaptors. Analysis and Interpretability. ++[Interactive lecture materials and more.](https://lena-voita.github.io/nlp_course.html#preview_transfer)++  
    * Homework: fine-tuning a pre-trained BERT model  
* **++[week05](https://github.com/yandexdataschool/nlp_course/blob/2025/week05_llm)++** **Large Language Models**  
    * Lecture: Scaling laws. Emergent abilities. Open-source LLMs.  
    * Practice: hands-on with open-source LLMs  
* **++[week06](https://github.com/yandexdataschool/nlp_course/blob/2025/week06_prompting)++** **Prompting & In-Context Learning**  
    * Lecture: Prompting techniques. Chain-of-Thought reasoning. In-context learning: how and why it works. Analysis and Interpretability.  
    * Homework: manual prompt engineering and chain-of-thought reasoning  
* **++[week07](https://github.com/yandexdataschool/nlp_course/blob/2025/week07_finetuning)++** **Fine-tuning (PEFT & RLHF)**  
    * Lecture: Parameter-efficient fine-tuning (LoRA, adapters). Reinforcement Learning from Human Feedback (RLHF).  
    * Seminar + Homework  
* **++[week08](https://github.com/yandexdataschool/nlp_course/blob/2025/week08_efficiency)++** **Efficiency**  
    * Lecture: Quantization. Distillation. Pruning. Speculative decoding.  
    * Homework  
* **++[week09](https://github.com/yandexdataschool/nlp_course/blob/2025/week09_retrieval)++** **Retrieval-Augmented Generation (RAG)**  
    * Lecture: Dense retrieval. RAG architectures.  
    * Practice  
* **++[week10](https://github.com/yandexdataschool/nlp_course/blob/2025/week10_agents)++** **AI Agents**  
    * Lecture: Agent architectures. Tool use. Memory.  
    * Seminar + Homework  
* **++[week11](https://github.com/yandexdataschool/nlp_course/blob/2025/week11_interpretability)++** **Interpretability**  
    * Lecture: Probing. Mechanistic interpretability.  
    * Seminar + Homework  
* **++[week12](https://github.com/yandexdataschool/nlp_course/blob/2025/week12_multimodal)++** **Multimodal LLMs**  
* **++[week13](https://github.com/yandexdataschool/nlp_course/blob/2025/week13_llm_systems)++** **Building LLM Systems**  
* **++[week14](https://github.com/yandexdataschool/nlp_course/blob/2025/week14_agents_production)++** **AI Agents in Production**  
  
  
This is the Convolutional Models Supplementary. It contains a detailed description of convolutional models in general, as well as particular model configurations for specific tasks.a  Most of the content is copied from the corresponding parts of the main course: I gathered them here for convenience. The news parts here are Parameters: Kernel size, Stride, Padding, Bias and k-max pooling.  
  
Convolutions for Images and Translation Invariance  
  
Convolutional networks were originally developed for computer vision tasks. Therefore, let's first understand the intuition behind convolutional models for images.  
  
Imagine we want to classify an image into several classes, e.g. cat, dog, airplane, etc. In this case, if you find a cat on an image, you don't care where on the image this cat is: you care only that it is there somewhere.  
  
[Label: cat](Attachments/E033054C-8746-49D5-9A51-CFFA1036198E.png)  
  
Convolutional networks apply the same operation to small parts of an image: this is how they extract features. Each operation is looking for a match with a pattern, and a network learns which patterns are useful. With a lot of layers, the learned patterns become and more complicated: from lines in the early layers to very complicated patterns (e.g., the whole cat or dog) on the upper ones. You can look at the examples in the Analysis and Interpretability section.  
  
This property is called translation invariance: translation because we are talking about shifts in space, invariance because we want it to not matter.  
  
 The illustration is adapted from the one taken from [this cool repo](https://github.com/vdumoulin/conv_arithmetic).  
  
Convolutions for Text  
  
Well, for images it's all clear: e.g. we want to be able to move a cat because we don't care where the cat is. But what about texts? At first glance, this is not so straightforward: we can not move phrases easily - the meaning will change or we will get something that does not make much sense.  
  
However, there are some applications where we can think of the same intuition. Let's imagine that we want to classify texts, but not cats/dogs as in images, but positive/negative sentiment. Then there are some words and phrases which could be very informative "clues" (e.g. it's been great, bored to death, absolutely amazing, the best ever, etc), and others which are not important at all. We don't care much where in a text we saw bored to death to understand the sentiment, right?  
  
[An absolutely great mavie! I watched the premiere with my friends.](Attachments/83D92347-92C4-43B7-AC59-E3CED9530EEB.png)  
  
A Typical Model: Convolution+Pooling Blocks  
  
Following the intuition above, we want to detect some patterns, but we don't care much where exactly these patterns are. This behavior is implemented with two layers:  
* convolution: finds matches with patterns (as the cat head we saw above);  
* pooling: aggregates these matches over positions (either locally or globally).  
  
* A typical convolutional model for texts is shown on the figure. Usually, a convolutional layer is applied to word embedding, which is followed by a non-linearity (usually ReLU) and a pooling operation. These are the main building blocks of convolutional models: for specific tasks, the configurations can be different, but these blocks are standard.  
  
* [Typical usage](Attachments/DD59E290-BEA7-438B-9CF7-C7EDFC6BE3D8.png)  
  
* In the following, we discuss in detail the main building blocks, convolution and pooling, then consider modeling modifications.  
  
* ++Note++ that modeling modifications for specific tasks are described in the corresponding lectures of the main part of the course. We repeat applications for specific tasks here just for convenience.  
  
  
## Building Blocks: Convolution  
Convolutions in computer vision go over an image with a sliding window and apply the same operation, convolution filter, to each window. A convolution layer usually has several filters, and each filter detects a different pattern (more on this below).  
  
The illustration (taken from [this cool repo](https://github.com/vdumoulin/conv_arithmetic)) shows this process for one filter: the bottom is the input image, the top is the filter output. Since an image has two dimensions (width and height), the convolution is two-dimensional.  
  
[same_padding_no_strides.gif](Attachments/43CA6C34-09A5-450B-873A-70035BBD68A6.gif)  
  
 Convolution filter for images. The illustration is from [this cool repo](https://github.com/vdumoulin/conv_arithmetic).  
  
Differently from images, texts have only one dimension. Therefore, a convolution here is one-dimensional: look at the illustration.  
  
Convolution filter for text.  
  
### Convolution is a Linear Operation Applied to Each Window  
[BUEiE](Attachments/CFC246D6-E9E1-43CB-9144-64F971DCD603.png)  
  
**A convolution is a linear layer (followed by a non-linearity) which is applied to each input window. Formally, let us assume that**  
* **- representations of the input words, ;**  
* **(input channels) - size of an input embedding;**  
* **(kernel size) - the length of a convolution window (on the illustration, );**  
* **(output channels) - number of convolution filters (i.e., number of channels produced by the convolution).**  
  
* **Then a convolution is a linear layer . For a -sized window , the convolution takes the concatenation of these vectors**  
  
and multiplies by the convolution matrix:  
  
A convolution goes over an input with a sliding window and applies the same linear transformation to each window.  
  
Parameters: Kernel size, Stride, Padding, Bias  
  
• Kernel size: How far to look  
  
Kernel size is the number of input elements (tokens) a convolution looks at each step. For text, typical values are 2-5.  
  
[kernel size = 2](Attachments/A2E8C043-0A6F-42A1-B1DC-361D94AAAB0B.png)  
  
• Stride: How much move a filter at each step  
  
Stride tells how much to move filter at each step. For example, stride equal to 1 means that we move the filter by 1 input element (pixel for images, token for texts) at each step.  
  
[stride=1 (default)](Attachments/7F8C764D-FE16-4FF6-8B86-42B4B9C08AD0.png)  
  
• Padding: Add zero vectors to both sides  
  
Padding adds zero vectors to both sides of an input. If you are using stride>1, you may need padding - be careful!  
  
[padding=0 (default)](Attachments/A5076793-F7CF-45E3-8DAE-F1C1CE68405F.png)  
  
• Bias: The bias term in the linear operation in convolution.  
  
By default, there's no bias - only multiplication by a matrix.  
  
[Resut](Attachments/A289E03D-88AB-4E3D-84B3-6A3F9D99F2B7.png)  
  
Intuition: Each Filter Extracts a Feature  
  
Intuitively, each filter in a convolution extracts a feature.  
  
[< pad› I like](Attachments/C7B778B9-495F-4CF0-95EB-604284CB7F5B.png)  
  
• One filter - one feature extractor  
  
A filter takes vector representations in a current window and transforms them linearly into a single feature. Formally, for a window a filter computes dot product:  
  
The number  
  
(the extracted "feature") is a result of applying the filter to the window .  
  
• m filters: m feature extractors  
  
[Filter: 1](Attachments/F03C9439-AE98-450B-B79F-E569C63DD0AC.gif)  
  
One filter extracts a single feature. Usually, we want many features: for this, we have to take several filters. Each filter reads an input text and extracts a different feature - look at the illustration. The number of filters is the number of output features you want to get. With filters instead of one, the size of the convolutional layer we discussed above will become .  
  
[Filter: ml](Attachments/48E23592-9073-48AC-B1C4-6FF184220F4E.png)  
  
++This is done in parallel!++ Note that while I show you how a CNN "reads" a text, in practice these computations are done in parallel.  
## Building Blocks: Pooling  
After a convolution extracted features from each window, a pooling layer summarises the features in some region. Pooling layers are used to reduce the input dimension, and, therefore, to reduce the number of parameters used by the network.  
  
Max and Mean Pooling  
  
The most popular is max-pooling: it takes maximum over each dimension, i.e. takes the maximum value of each feature.  
  
[Filter: 2](Attachments/F021C8EE-882E-4F37-88B7-B2A7D702DE40.png)  
  
Intuitively, each feature "fires" when it sees some pattern: a visual pattern in an image (line, texture, a cat's paw, etc) or a text pattern (e.g., a phrase). After a pooling operation, we have a vector saying which of these patterns occurred in the input.  
  
Mean-pooling works similarly but computes mean over each feature instead of maximum.  
  
k-max Pooling  
  
[0.4||0.9](Attachments/35B52EA9-3A8F-470F-92AA-F6B4C9CCB883.png)  
  
k-max pooling is a generalization of max-pooling. Instead of finding one maximum feature, it selects k features with the highest values. The order of these features is preserved.  
  
It can be useful if it is important how many times a network found some pattern.  
  
Pooling and Global Pooling  
  
Similarly to convolution, pooling is applied to windows of several elements. Pooling also has the stride parameter, and the most common approach is to use pooling with non-overlapping windows. For this, you have to set the stride parameter the same as the pool size. Look at the illustration.  
  
[pooling = 2 with stride=2](Attachments/C20C4257-0237-4B06-8C44-54548AAAB082.png)  
  
The difference between pooling and global pooling is that pooling is applied over features in each window independently, while global pooling performs over the whole input. For texts, global pooling is often used to get a single vector representing the whole text; such global pooling is called max-over-time pooling, where the "time" axis goes from the first input token to the last.  
  
[Pooling](Attachments/3CC0FADB-8D75-4987-A28E-E42F4FB14D13.png)  
  
Intuitively, each feature "fires" when it sees some pattern: a visual pattern in an image (line, texture, a cat's paw, etc) or a text pattern (e.g., a phrase). After a pooling operation, we have a vector saying which of these patterns occurred in the input.  
  
[analysis_empty.png](Attachments/E0A1BCD5-8EFE-436B-B693-A2812F3C75EB.png)  
  
For more details on intuition and examples of patterns, look at the Analysis and Interpretability section.  
## Building Blocks: Residual Connections  
TL;DR: Train Deep Networks Easily!  
  
To process longer contexts you need a lot of layers. Unfortunately, when stacking a lot of layers, you can have a problem with propagating gradients from top to bottom through a deep network. To avoid this, we can use residual connections or a more complicated variant [highway connections](https://arxiv.org/pdf/1505.00387.pdf).  
  
[block with](Attachments/DA2E2E2A-E9F3-4777-94E5-CEC831F1EB7C.png)  
  
Residual connections are very simple: they add input of a block to its output. In this way, the gradients over inputs will flow not only indirectly through the block, but also directly through the sum.  
  
Highway connections have the same motivation, but a use a gated sum of input and output instead of the simple sum. This is similar to LSTM gates where a network can learn the types of information it may want to carry on from bottom to top (or, in case of LSTMs, from left to right).  
  
Look at the example of a convolutional network with residual connections. Typically, we put residual connections around blocks with several layers. A network can several such blocks - depending on your task, you may need a lot of layers to get a decent receptive field.  
  
[more blocks](Attachments/4FFF57DC-3CA1-4CE7-A8DD-B13453B56006.png)  
  
## Specific Tasks: Text Classification  
This part is a summary of the convolutional models part of the [Text Classification](https://lena-voita.github.io/nlp_course/text_classification.html) lecture in the main part of the course. For a detailed description of the text classification task, go to the main lecture.  
  
Now, when we understand how the convolution and pooling work, let's come to modeling modifications. In the case of text classification:  
  
We need a model that can produce a fixed-sized vector for inputs of different lengths.  
  
Therefore, we need to construct a convolutional model that represents a text as a single vector.  
  
The basic convolutional model for text classification is shown on the figure. Note that, after the convolution, we use global-over-time pooling. This is the key operation: it allows to compress a text into a single vector. The model itself can be different, but at some point, it has to use the global pooling to compress input in a single vector.  
  
[Standard part](Attachments/E73F18B9-4631-4D39-B57C-315411F371E8.png)  
  
• Several Convolutions with Different Kernel Sizes  
  
Instead of picking one kernel size for your convolution, you can use several convolutions with different kernel sizes. The recipe is simple: apply each convolution to the data, add non-linearity and global pooling after each of them, then concatenate the results (on the illustration, non-linearity is omitted for simplicity). This is how you get vector representation of the data which is used for classification.  
  
[renresentation of the text](Attachments/B4A05D8E-86DC-45F8-B03A-FD94F40B1146.png)  
  
This idea was used, among others, in the paper [Convolutional Neural Networks for Sentence Classification](https://www.aclweb.org/anthology/D14-1181.pdf) and many follow-ups.  
  
• Stack Several Blocks Convolution+Pooling  
  
Instead of one layer, you can stack several blocks convolution+pooling on top of each other. After several blocks, you can apply another convolution, but with global pooling this time. Remember: you have to get a single fixed-sized vector - for this, you need global pooling.  
  
Such multi-layered convolutions can be useful when your texts are very long; for example, if your model is character-level (as opposed to word-level).  
  
[Slobal Pooling →](Attachments/A3901F9C-9BA8-4F99-8018-236B97A21B1D.png)  
  
This idea was used, among others, in the paper [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf).  
## Specific Tasks: Language Modeling  
This part is a summary of the convolutional models part of the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture in the main part of the course. For a detailed description of the language modeling task, go to the main lecture.  
  
Compared to CNNs for text classification, language models have several differences. Here we discuss general design principles of CNN language models; for a detailed description of specific architectures, you can look in the [Related Papers](https://lena-voita.github.io/nlp_course/language_modeling.html#related_papers) section in the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture.  
  
[convolutions: do not want to](Attachments/57A14391-AA99-4E6B-A757-3CD47F09ADBA.png)  
  
When designing a CNN language model, you have to keep in mind the following things:  
* prevent information flow from future tokens To predict a token, a left-to-right LM has to use only previous tokens - make sure your CNN does not see anything but them! For example, you can shift tokens to the right by using padding - look at the illustration above.  
* do not remove positional information Differently from text classification, positional information is very important for language models. Therefore, do not use pooling (or be very careful in how you do it).  
* if you stack many layers, do not forget about residual connections If you stack many layers, it may difficult to train a very deep network well. To avoid this, use residual connections - look for the details below.  
  
* Receptive field: with many layers, can be large  
  
* [like the cat on a red](Attachments/A8A1E3D6-2903-4C39-A220-591DFB7DF020.png)  
  
* When using convolutional models without global pooling, your model will inevitably have a fixed-sized context. This might seem undesirable: the fixed context size problem is exactly what we didn't like in the n-gram models!  
  
* However, if for n-gram models typical context size is 1-4, contexts in convolutional models can be quite long. Look at the illustration: with only 3 convolutional layers with small kernel size 3, a network has a context of 7 tokens. If you stack many layers, you can get a very large context length.  
  
* Residual Connections: with many layers, you will need them!  
  
* If you stack many layers, you may have troubles with training a deep network. Luckily, for this you can use residual connections!  
  
* Look at the example of a convolutional network with residual connections. Typically, we put residual connections around blocks with several layers. A network can several such blocks - remember, you need a lot of layers to get a decent receptive field.  
  
* [the cat](Attachments/894D30CE-58A2-4C2A-8326-53E90E5CF897.png)  
  
[analysis_empty.png](Attachments/CF1B8996-886B-4DB3-BC4E-F58449CC60E4.png)  
## Analysis and Interpretability  
What do Convolutions Learn? Analyzing Convolutional Filters  
  
++Convolutions in Computer Vision: Visual Patterns++  
  
Convolutions were originally developed for images, and there's already a pretty good understanding of what the filters capture and how filters from different layers from a hierarchy. While lower layers capture simple visual patterns such as lines or circles, final layers can capture the whole pictures, animals, people, etc.  
  
[Lower layers](Attachments/843A29D5-92B7-4096-811F-461A2C811C0A.png)  
  
 Examples of patterns captured by convolution filters for images. The examples are from [Activation Atlas from distill.pub](https://distill.pub/2019/activation-atlas/).  
  
Convolutions for Text Classification  
  
This part is from the [Text Classification](https://lena-voita.github.io/nlp_course/text_classification.html) lecture from the main part of the course.  
  
For images, filters capture local visual patterns which are important for classification. For text, such local patterns are word n-grams. The main findings on how CNNs work for texts are:  
* convolving filters are used as ngram detectors Each filter specializes in one or several families of closely-related ngrams. Filters are not homogeneous, i.e. a single filter can, and often does, detect multiple distinctly different families of ngrams.  
* max-pooling induces a thresholding behavior Values below a given threshold are ignored when (i.e. irrelevant to) making a prediction. For example, [this paper](https://arxiv.org/pdf/1809.08037.pdf) shows that 40% of the pooled ngrams on average can be dropped with no loss of performance.  
  
* [2. When does this](Attachments/97BE4081-650D-4380-918B-008C4E47561D.png)  
  
* The simplest way to understand what a network captures is to look which patterns activate its neurons. For convolutions, we pick a filter and find those n-grams which activate this filter most.  
  
* Below are examples of the top-1 n-gram for several filters. For one of them, we also show other n-grams which lead to high activation of this filter - you can see that the n-grams have a very similar meaning.  
  
* [filter Topn-gram](Attachments/98AE9A4F-D5F5-488B-8E54-A6369E5C53D9.png)  
  
* For more details, look at the paper [Understanding Convolutional Neural Networks for Text Classification](https://arxiv.org/pdf/1809.08037.pdf).  
  
* Convolutions for Language Modeling  
  
* This part is from the [Research Thinking](https://lena-voita.github.io/nlp_course/language_modeling.html#research_thinking) section of the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture from the main part of the course.  
  
* Let's look at the examples from the EMNLP 2016 paper [Convolutional Neural Network Language Models](https://www.aclweb.org/anthology/D16-1123.pdf). For a simple convolutional LM, the authors feed the development data to a model and find ngrams that activate a certain filter most.  
  
* [have until nov.](Attachments/4981D0E1-F41F-4821-AF20-05EF1F93512F.png)  
  
* While a model for sentiment classification learned to pick things which are related to sentiment, the LM model captures phrases which can be continued similarly. For example, one kernel activates on phrases ending with a month, another - with a name; note also the "comparative" kernel firing at as ... as.  
## Convolutional Neural Networks for Text  
This is the Convolutional Models Supplementary. It contains a detailed description of convolutional models in general, as well as particular model configurations for specific tasks.  Most of the content is copied from the corresponding parts of the main course: I gathered them here for convenience. The news parts here are Parameters: Kernel size, Stride, Padding, Bias and k-max pooling.  
  
Convolutions for Images and Translation Invariance  
  
Convolutional networks were originally developed for computer vision tasks. Therefore, let's first understand the intuition behind convolutional models for images.  
  
Imagine we want to classify an image into several classes, e.g. cat, dog, airplane, etc. In this case, if you find a cat on an image, you don't care where on the image this cat is: you care only that it is there somewhere.  
  
[Label: cat](Attachments/8825C447-2C65-4226-8C5F-18371D036CA0.png)  
  
Convolutional networks apply the same operation to small parts of an image: this is how they extract features. Each operation is looking for a match with a pattern, and a network learns which patterns are useful. With a lot of layers, the learned patterns become and more complicated: from lines in the early layers to very complicated patterns (e.g., the whole cat or dog) on the upper ones. You can look at the examples in the Analysis and Interpretability section.  
  
This property is called translation invariance: translation because we are talking about shifts in space, invariance because we want it to not matter.  
  
 The illustration is adapted from the one taken from [this cool repo](https://github.com/vdumoulin/conv_arithmetic).  
  
Convolutions for Text  
  
Well, for images it's all clear: e.g. we want to be able to move a cat because we don't care where the cat is. But what about texts? At first glance, this is not so straightforward: we can not move phrases easily - the meaning will change or we will get something that does not make much sense.  
  
However, there are some applications where we can think of the same intuition. Let's imagine that we want to classify texts, but not cats/dogs as in images, but positive/negative sentiment. Then there are some words and phrases which could be very informative "clues" (e.g. it's been great, bored to death, absolutely amazing, the best ever, etc), and others which are not important at all. We don't care much where in a text we saw bored to death to understand the sentiment, right?  
  
[An absolutely great mavie! I watched the premiere with my friends.](Attachments/819644C0-9F9B-4431-B7E2-7F58BF83A6A0.png)  
  
A Typical Model: Convolution+Pooling Blocks  
  
Following the intuition above, we want to detect some patterns, but we don't care much where exactly these patterns are. This behavior is implemented with two layers:  
* convolution: finds matches with patterns (as the cat head we saw above);  
* pooling: aggregates these matches over positions (either locally or globally).  
  
* A typical convolutional model for texts is shown on the figure. Usually, a convolutional layer is applied to word embedding, which is followed by a non-linearity (usually ReLU) and a pooling operation. These are the main building blocks of convolutional models: for specific tasks, the configurations can be different, but these blocks are standard.  
  
* [Typical usage](Attachments/BC555B06-07C1-4938-A81C-E43B9590CD07.png)  
  
* In the following, we discuss in detail the main building blocks, convolution and pooling, then consider modeling modifications.  
  
* ++Note++ that modeling modifications for specific tasks are described in the corresponding lectures of the main part of the course. We repeat applications for specific tasks here just for convenience.  
## Building Blocks: Convolution  
Convolutions in computer vision go over an image with a sliding window and apply the same operation, convolution filter, to each window. A convolution layer usually has several filters, and each filter detects a different pattern (more on this below).  
  
The illustration (taken from [this cool repo](https://github.com/vdumoulin/conv_arithmetic)) shows this process for one filter: the bottom is the input image, the top is the filter output. Since an image has two dimensions (width and height), the convolution is two-dimensional.  
  
[same_padding_no_strides.gif](Attachments/DA7E28FD-FB05-4EFD-813F-9FCD339ABBF6.gif)  
  
 Convolution filter for images. The illustration is from [this cool repo](https://github.com/vdumoulin/conv_arithmetic).  
  
Differently from images, texts have only one dimension. Therefore, a convolution here is one-dimensional: look at the illustration.  
  
Convolution filter for text.  
  
Convolution is a Linear Operation Applied to Each Window  
  
[BUEiE](Attachments/CC4FF160-34B3-44D2-B1F7-657688DE9805.png)  
  
A convolution is a linear layer (followed by a non-linearity) which is applied to each input window. Formally, let us assume that  
    - representations of the input words, ;  
* (input channels) - size of an input embedding;  
* (kernel size) - the length of a convolution window (on the illustration, );  
* (output channels) - number of convolution filters (i.e., number of channels produced by the convolution).  
  
* Then a convolution is a linear layer . For a -sized window , the convolution takes the concatenation of these vectors  
  
and multiplies by the convolution matrix:  
  
A convolution goes over an input with a sliding window and applies the same linear transformation to each window.  
  
Parameters: Kernel size, Stride, Padding, Bias  
  
• Kernel size: How far to look  
  
Kernel size is the number of input elements (tokens) a convolution looks at each step. For text, typical values are 2-5.  
  
[kernel size = 2](Attachments/47962324-866B-4CC0-9552-53BAF581812E.png)  
  
• Stride: How much move a filter at each step  
  
Stride tells how much to move filter at each step. For example, stride equal to 1 means that we move the filter by 1 input element (pixel for images, token for texts) at each step.  
  
[stride=1 (default)](Attachments/B804C0A2-4131-4252-BD7D-94F6E6CDF729.png)  
  
• Padding: Add zero vectors to both sides  
  
Padding adds zero vectors to both sides of an input. If you are using stride>1, you may need padding - be careful!  
  
[padding=0 (default)](Attachments/8AEA36FF-08E2-4E0D-9680-9B86DF2A9E0B.png)  
  
• Bias: The bias term in the linear operation in convolution.  
  
By default, there's no bias - only multiplication by a matrix.  
  
[Resut](Attachments/35CDCDBF-E17A-4E69-A3D6-A7B38D713794.png)  
  
Intuition: Each Filter Extracts a Feature  
  
Intuitively, each filter in a convolution extracts a feature.  
  
[< pad› I like](Attachments/EE8E5D36-5596-48BA-9E08-B1ECF13C0037.png)  
  
• One filter - one feature extractor  
  
A filter takes vector representations in a current window and transforms them linearly into a single feature. Formally, for a window a filter computes dot product:  
  
The number  
  
(the extracted "feature") is a result of applying the filter to the window .  
  
• m filters: m feature extractors  
  
[Filter: 1](Attachments/FC21B555-21CB-4CED-942A-53A0E521D48F.gif)  
  
One filter extracts a single feature. Usually, we want many features: for this, we have to take several filters. Each filter reads an input text and extracts a different feature - look at the illustration. The number of filters is the number of output features you want to get. With filters instead of one, the size of the convolutional layer we discussed above will become .  
  
[Filter: ml](Attachments/80F9F619-6568-4A04-B726-24928C3206A5.png)  
  
++This is done in parallel!++ Note that while I show you how a CNN "reads" a text, in practice these computations are done in parallel.  
## Building Blocks: Pooling  
After a convolution extracted features from each window, a pooling layer summarises the features in some region. Pooling layers are used to reduce the input dimension, and, therefore, to reduce the number of parameters used by the network.  
  
Max and Mean Pooling  
  
The most popular is max-pooling: it takes maximum over each dimension, i.e. takes the maximum value of each feature.  
  
[Filter: 2](Attachments/5EF8AF59-93E5-47C4-8220-30DE13E8786D.png)  
  
Intuitively, each feature "fires" when it sees some pattern: a visual pattern in an image (line, texture, a cat's paw, etc) or a text pattern (e.g., a phrase). After a pooling operation, we have a vector saying which of these patterns occurred in the input.  
  
Mean-pooling works similarly but computes mean over each feature instead of maximum.  
  
k-max Pooling  
  
[0.4||0.9](Attachments/1D65D1DD-EF71-4A1B-BA03-F009F6A89992.png)  
  
k-max pooling is a generalization of max-pooling. Instead of finding one maximum feature, it selects k features with the highest values. The order of these features is preserved.  
  
It can be useful if it is important how many times a network found some pattern.  
  
Pooling and Global Pooling  
  
Similarly to convolution, pooling is applied to windows of several elements. Pooling also has the stride parameter, and the most common approach is to use pooling with non-overlapping windows. For this, you have to set the stride parameter the same as the pool size. Look at the illustration.  
  
[pooling = 2 with stride=2](Attachments/248E7C02-AD6F-4ED3-886A-E56687733AA7.png)  
  
The difference between pooling and global pooling is that pooling is applied over features in each window independently, while global pooling performs over the whole input. For texts, global pooling is often used to get a single vector representing the whole text; such global pooling is called max-over-time pooling, where the "time" axis goes from the first input token to the last.  
  
[Pooling](Attachments/9792885B-3151-4843-BD5F-2B3A1918D1BE.png)  
  
Intuitively, each feature "fires" when it sees some pattern: a visual pattern in an image (line, texture, a cat's paw, etc) or a text pattern (e.g., a phrase). After a pooling operation, we have a vector saying which of these patterns occurred in the input.  
  
[analysis_empty.png](Attachments/9ABBFF94-0748-44E5-9C76-AD41D99B44BB.png)  
  
For more details on intuition and examples of patterns, look at the Analysis and Interpretability section.  
## Building Blocks: Residual Connections  
TL;DR: Train Deep Networks Easily!  
  
To process longer contexts you need a lot of layers. Unfortunately, when stacking a lot of layers, you can have a problem with propagating gradients from top to bottom through a deep network. To avoid this, we can use residual connections or a more complicated variant [highway connections](https://arxiv.org/pdf/1505.00387.pdf).  
  
[block with](Attachments/80CE7DF3-8F00-4E7D-A4DE-8FD6F9D74530.png)  
  
Residual connections are very simple: they add input of a block to its output. In this way, the gradients over inputs will flow not only indirectly through the block, but also directly through the sum.  
  
Highway connections have the same motivation, but a use a gated sum of input and output instead of the simple sum. This is similar to LSTM gates where a network can learn the types of information it may want to carry on from bottom to top (or, in case of LSTMs, from left to right).  
  
Look at the example of a convolutional network with residual connections. Typically, we put residual connections around blocks with several layers. A network can several such blocks - depending on your task, you may need a lot of layers to get a decent receptive field.  
  
[more blocks](Attachments/81515BD2-147A-4017-828D-6332CD580850.png)  
  
## Specific Tasks: Text Classification  
This part is a summary of the convolutional models part of the [Text Classification](https://lena-voita.github.io/nlp_course/text_classification.html) lecture in the main part of the course. For a detailed description of the text classification task, go to the main lecture.  
  
Now, when we understand how the convolution and pooling work, let's come to modeling modifications. In the case of text classification:  
  
We need a model that can produce a fixed-sized vector for inputs of different lengths.  
  
Therefore, we need to construct a convolutional model that represents a text as a single vector.  
  
The basic convolutional model for text classification is shown on the figure. Note that, after the convolution, we use global-over-time pooling. This is the key operation: it allows to compress a text into a single vector. The model itself can be different, but at some point, it has to use the global pooling to compress input in a single vector.  
  
[Standard part](Attachments/97366E17-84A0-4E4D-9248-C32DF3D7AAC5.png)  
  
• Several Convolutions with Different Kernel Sizes  
  
Instead of picking one kernel size for your convolution, you can use several convolutions with different kernel sizes. The recipe is simple: apply each convolution to the data, add non-linearity and global pooling after each of them, then concatenate the results (on the illustration, non-linearity is omitted for simplicity). This is how you get vector representation of the data which is used for classification.  
  
[renresentation of the text](Attachments/3C831DBF-A97C-4425-A386-ABFA34962ED4.png)  
  
This idea was used, among others, in the paper [Convolutional Neural Networks for Sentence Classification](https://www.aclweb.org/anthology/D14-1181.pdf) and many follow-ups.  
  
• Stack Several Blocks Convolution+Pooling  
  
Instead of one layer, you can stack several blocks convolution+pooling on top of each other. After several blocks, you can apply another convolution, but with global pooling this time. Remember: you have to get a single fixed-sized vector - for this, you need global pooling.  
  
Such multi-layered convolutions can be useful when your texts are very long; for example, if your model is character-level (as opposed to word-level).  
  
[Slobal Pooling →](Attachments/664A3709-DA84-4DDB-BE56-153F0D12250E.png)  
  
This idea was used, among others, in the paper [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf).  
## Specific Tasks: Language Modeling  
This part is a summary of the convolutional models part of the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture in the main part of the course. For a detailed description of the language modeling task, go to the main lecture.  
  
Compared to CNNs for text classification, language models have several differences. Here we discuss general design principles of CNN language models; for a detailed description of specific architectures, you can look in the [Related Papers](https://lena-voita.github.io/nlp_course/language_modeling.html#related_papers) section in the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture.  
  
[convolutions: do not want to](Attachments/0641019D-4B05-4A43-83B3-E8031D33D58A.png)  
  
When designing a CNN language model, you have to keep in mind the following things:  
* prevent information flow from future tokens To predict a token, a left-to-right LM has to use only previous tokens - make sure your CNN does not see anything but them! For example, you can shift tokens to the right by using padding - look at the illustration above.  
* do not remove positional information Differently from text classification, positional information is very important for language models. Therefore, do not use pooling (or be very careful in how you do it).  
* if you stack many layers, do not forget about residual connections If you stack many layers, it may difficult to train a very deep network well. To avoid this, use residual connections - look for the details below.  
  
* Receptive field: with many layers, can be large  
  
* [like the cat on a red](Attachments/008FF288-B1FB-46B8-99CA-D5676F8A94D0.png)  
  
* When using convolutional models without global pooling, your model will inevitably have a fixed-sized context. This might seem undesirable: the fixed context size problem is exactly what we didn't like in the n-gram models!  
  
* However, if for n-gram models typical context size is 1-4, contexts in convolutional models can be quite long. Look at the illustration: with only 3 convolutional layers with small kernel size 3, a network has a context of 7 tokens. If you stack many layers, you can get a very large context length.  
  
* Residual Connections: with many layers, you will need them!  
  
* If you stack many layers, you may have troubles with training a deep network. Luckily, for this you can use residual connections!  
  
* Look at the example of a convolutional network with residual connections. Typically, we put residual connections around blocks with several layers. A network can several such blocks - remember, you need a lot of layers to get a decent receptive field.  
  
* [the cat](Attachments/600BEBBB-1AB6-4F19-B9A2-9C396BB0C12C.png)  
  
[analysis_empty.png](Attachments/019BF9A4-7357-4AD0-BD28-5F417E4B229E.png)  
## Analysis and Interpretability  
What do Convolutions Learn? Analyzing Convolutional Filters  
  
++Convolutions in Computer Vision: Visual Patterns++  
  
Convolutions were originally developed for images, and there's already a pretty good understanding of what the filters capture and how filters from different layers from a hierarchy. While lower layers capture simple visual patterns such as lines or circles, final layers can capture the whole pictures, animals, people, etc.  
  
[Lower layers](Attachments/33231FCA-4782-40D8-9C6F-0BA8C5C9AA60.png)  
  
 Examples of patterns captured by convolution filters for images. The examples are from [Activation Atlas from distill.pub](https://distill.pub/2019/activation-atlas/).  
  
Convolutions for Text Classification  
  
This part is from the [Text Classification](https://lena-voita.github.io/nlp_course/text_classification.html) lecture from the main part of the course.  
  
For images, filters capture local visual patterns which are important for classification. For text, such local patterns are word n-grams. The main findings on how CNNs work for texts are:  
* convolving filters are used as ngram detectors Each filter specializes in one or several families of closely-related ngrams. Filters are not homogeneous, i.e. a single filter can, and often does, detect multiple distinctly different families of ngrams.  
* max-pooling induces a thresholding behavior Values below a given threshold are ignored when (i.e. irrelevant to) making a prediction. For example, [this paper](https://arxiv.org/pdf/1809.08037.pdf) shows that 40% of the pooled ngrams on average can be dropped with no loss of performance.  
  
* [2. When does this](Attachments/DABD7A8F-0828-41AE-BF4D-0346D9176B0F.png)  
  
* The simplest way to understand what a network captures is to look which patterns activate its neurons. For convolutions, we pick a filter and find those n-grams which activate this filter most.  
  
* Below are examples of the top-1 n-gram for several filters. For one of them, we also show other n-grams which lead to high activation of this filter - you can see that the n-grams have a very similar meaning.  
  
* [filter Topn-gram](Attachments/C2A8E124-2939-4173-9985-642A5B9F8310.png)  
  
* For more details, look at the paper [Understanding Convolutional Neural Networks for Text Classification](https://arxiv.org/pdf/1809.08037.pdf).  
  
* Convolutions for Language Modeling  
  
* This part is from the [Research Thinking](https://lena-voita.github.io/nlp_course/language_modeling.html#research_thinking) section of the [Language Modeling](https://lena-voita.github.io/nlp_course/language_modeling.html) lecture from the main part of the course.  
  
* Let's look at the examples from the EMNLP 2016 paper [Convolutional Neural Network Language Models](https://www.aclweb.org/anthology/D16-1123.pdf). For a simple convolutional LM, the authors feed the development data to a model and find ngrams that activate a certain filter most.  
  
* [have until nov.](Attachments/9FCE4179-7BCA-4899-AF6F-E94550E36A85.png)  
  
* While a model for sentiment classification learned to pick things which are related to sentiment, the LM model captures phrases which can be continued similarly. For example, one kernel activates on phrases ending with a month, another - with a name; note also the "comparative" kernel firing at as ... as.  
