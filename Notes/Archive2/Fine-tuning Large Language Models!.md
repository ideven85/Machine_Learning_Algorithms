# Fine-tuning Large Language Models!  
# Fine-tuning Large Language Models!  
  
  
The advent of large language models (LLMs) has signalled a paradigm shift in the field of artificial intelligence, offering unprecedented capabilities in natural language processing and understanding. These large language models, characterised by their use of the transformer architecture and extensive training datasets, possess a remarkable ability to comprehend and generate human language. However, the true potential of these models is realised through the process of fine-tuning, wherein they are adapted to excel in specific domains.  
The advent of large language models (LLMs) has signalled a paradigm shift in the field of artificial intelligence, offering unprecedented capabilities in natural language processing and understanding. These large language models, characterised by their use of the transformer architecture and extensive training datasets, possess a remarkable ability to comprehend and generate human language. However, the true potential of these models is realised through the process of fine-tuning, wherein they are adapted to excel in specific domains.  
  
   
   
  
In this session, you will:  
In this session, you will:  
* Explore the process of training large language models  
* Explore the process of training large language models  
* Emphasise the need for fine-tuning LLMs  
* Emphasise the need for fine-tuning LLMs  
* Perform full fine-tuning on an LLM  
* Perform full fine-tuning on an LLM  
* Explore the theory and implementation of Low Rank Adaptation (LoRA) fine-tuning (Optional)  
* Explore the theory and implementation of Low Rank Adaptation (LoRA) fine-tuning (Optional)  
  
*    
*    
  
* By the end of this session, you should have a solid understanding of the theoretical and practical aspects of fine-tuning LLMs and a few specialised techniques that can be used to address inefficiencies in the fine-tuning process.  
* By the end of this session, you should have a solid understanding of the theoretical and practical aspects of fine-tuning LLMs and a few specialised techniques that can be used to address inefficiencies in the fine-tuning process.  
  
  
  
## How Large Language Models Are Trained  In this segment, we will discuss how large language models (LLMs) are trained.  
## How Large Language Models Are Trained  In this segment, we will discuss how large language models (LLMs) are trained.  
LLMs are trained through a two-stage training process which involves the following steps:   
LLMs are trained through a two-stage training process which involves the following steps:   
* Pre-training  
* Pre-training  
* Fine-tuning.   
* Fine-tuning.   
* [Untrained LLM](Attachments/BBA31CC5-95E3-4058-B669-8DF0F2335CFC.png)  
* [Untrained LLM](Attachments/BBA31CC5-95E3-4058-B669-8DF0F2335CFC.png)  
* **Pretraining** During the pre-training stage, the LLM is exposed to a vast and diverse set of unlabelled text data. This corpus can include anything from books and articles to websites and other forms of written communication. Pre-training requires significant computational power and time because the model is being trained on a massive dataset. Besides, due the complex architecture of LLMs, especially the self-attention modules that power the LLMs’ ability to determine complex relationships between different parts of the text, we need to perform training for multiple epochs. Here, one epoch refers to one passthrough of the whole data set. The pretraining process of Large Language Models (LLMs) begins with the model in an untrained state where the initial parameters, known as weights, are set randomly.   
* **Pretraining** During the pre-training stage, the LLM is exposed to a vast and diverse set of unlabelled text data. This corpus can include anything from books and articles to websites and other forms of written communication. Pre-training requires significant computational power and time because the model is being trained on a massive dataset. Besides, due the complex architecture of LLMs, especially the self-attention modules that power the LLMs’ ability to determine complex relationships between different parts of the text, we need to perform training for multiple epochs. Here, one epoch refers to one passthrough of the whole data set. The pretraining process of Large Language Models (LLMs) begins with the model in an untrained state where the initial parameters, known as weights, are set randomly.   
* ["All happy families are"](Attachments/E35691B7-A3A4-482F-BBDC-E0B270EA01BD.png)  
* ["All happy families are"](Attachments/E35691B7-A3A4-482F-BBDC-E0B270EA01BD.png)  
  
 The fundamental architecture of an LLM is designed to process language in discrete pieces called "tokens." These tokens can be words, parts of words, or even punctuation marks—essentially the atoms of written language. The task for which the LLM is being pretrained is called "next token prediction." This means that the model is presented with a string of tokens and must predict the subsequent token in the sequence.  For example, given the phrase "The cat sat on the," the model might predict "mat" as the next token. This process is iterative and involves presenting the model with large amounts of text so that it can learn to anticipate what comes next in any given snippet of language. This training method is self-supervised. To understand what self-supervised means, let us first recall supervised and unsupervised training.   
 The fundamental architecture of an LLM is designed to process language in discrete pieces called "tokens." These tokens can be words, parts of words, or even punctuation marks—essentially the atoms of written language. The task for which the LLM is being pretrained is called "next token prediction." This means that the model is presented with a string of tokens and must predict the subsequent token in the sequence.  For example, given the phrase "The cat sat on the," the model might predict "mat" as the next token. This process is iterative and involves presenting the model with large amounts of text so that it can learn to anticipate what comes next in any given snippet of language. This training method is self-supervised. To understand what self-supervised means, let us first recall supervised and unsupervised training.   
  
* **Supervised training**: In supervised training, you train the ML model using labelled data. These labels supervise the learning process by telling the model the correct outcome in a data point. For example, an image might be labelled as ‘cat’ or ‘dog’ based on the animal being captured in that image.  
* **Supervised training**: In supervised training, you train the ML model using labelled data. These labels supervise the learning process by telling the model the correct outcome in a data point. For example, an image might be labelled as ‘cat’ or ‘dog’ based on the animal being captured in that image.  
* **Unsupervised training**: In unsupervised training, the ML model analyses unlabelled data sets. These models can identify patterns in data without guidance from a human being. In these tasks, there is no obvious target variable whose value we are trying to predict. For example, an ML model called K-means clustering divides the data set into clusters with K members each. These clusters are created based on the similarity of the features of its members.    
* **Unsupervised training**: In unsupervised training, the ML model analyses unlabelled data sets. These models can identify patterns in data without guidance from a human being. In these tasks, there is no obvious target variable whose value we are trying to predict. For example, an ML model called K-means clustering divides the data set into clusters with K members each. These clusters are created based on the similarity of the features of its members.    
## Self-supervised learning:  
## Self-supervised learning:  
  
  
### Definition:  
### Definition:  
  
Uses raw, unlabeled historical data to generate its own supervisory signals, enabling AI models to learn complex patterns without manual annotation. By transforming this data—such as masking words in text, hiding parts of images, or predicting future video frames—models learn, via "pretext tasks," to understand the structure of the information, which can then be fine-tuned for specific, downstream applications. [1, 2, 3, 4]  
Uses raw, unlabeled historical data to generate its own supervisory signals, enabling AI models to learn complex patterns without manual annotation. By transforming this data—such as masking words in text, hiding parts of images, or predicting future video frames—models learn, via "pretext tasks," to understand the structure of the information, which can then be fine-tuned for specific, downstream applications. [1, 2, 3, 4]  
  
  
### Overview  
### Overview  
Leverages the text itself to provide the supervision. Since the correct next token is part of the input data, the model uses the input to teach itself without the need for external labels. This process is performed on a massive data set. An example of a record that may be used for pretraining from the ++[Common Crawl](https://commoncrawl.org/)++ data set is given below. {'text': 'Beginners BBQ Class Taking Place in Missoula!\nDo you want to get better at making delicious BBQ? You will have the opportunity, put this on your calendar now. Thursday, September 22nd join World Class BBQ Champion, Tony Balay from Lonestar Smoke Rangers. He will be teaching a beginner level class for everyone who wants to get better with their culinary skills.\nHe will teach you everything you need to know to compete in a KCBS BBQ competition, including techniques, recipes, timelines, meat selection and trimming, plus smoker and fire information.\nThe cost to be in the class is $35 per person, and for spectators it is free. Included in the cost will be either a t-shirt or apron and you will be tasting samples of each meat that is prepared.', 'timestamp': '2019-04-25T12:57:54Z', 'url': '[https://klyq.com/beginners-bbq-class-taking-place-in-missoula/'}](https://klyq.com/beginners-bbq-class-taking-place-in-missoula/'%7D)  
Leverages the text itself to provide the supervision. Since the correct next token is part of the input data, the model uses the input to teach itself without the need for external labels. This process is performed on a massive data set. An example of a record that may be used for pretraining from the ++[Common Crawl](https://commoncrawl.org/)++ data set is given below. {'text': 'Beginners BBQ Class Taking Place in Missoula!\nDo you want to get better at making delicious BBQ? You will have the opportunity, put this on your calendar now. Thursday, September 22nd join World Class BBQ Champion, Tony Balay from Lonestar Smoke Rangers. He will be teaching a beginner level class for everyone who wants to get better with their culinary skills.\nHe will teach you everything you need to know to compete in a KCBS BBQ competition, including techniques, recipes, timelines, meat selection and trimming, plus smoker and fire information.\nThe cost to be in the class is $35 per person, and for spectators it is free. Included in the cost will be either a t-shirt or apron and you will be tasting samples of each meat that is prepared.', 'timestamp': '2019-04-25T12:57:54Z', 'url': '[https://klyq.com/beginners-bbq-class-taking-place-in-missoula/'}](https://klyq.com/beginners-bbq-class-taking-place-in-missoula/'%7D)  
  
### Key Aspects of Self-Supervised Learning on Historical Data:  
### Key Aspects of Self-Supervised Learning on Historical Data:  
* **Data Utilization:** It enables the use of vast, messy, and previously underutilized historical data (documents, sensor data, clickstreams, images) that lacks labels.  
* **Data Utilization:** It enables the use of vast, messy, and previously underutilized historical data (documents, sensor data, clickstreams, images) that lacks labels.  
* **Techniques:**  
* **Techniques:**  
    * **Contrastive Learning (e.g., SimCLR, MoCo):** Maximizes agreement between augmented views of the same data point while minimizing agreement with others.  
    * **Contrastive Learning (e.g., SimCLR, MoCo):** Maximizes agreement between augmented views of the same data point while minimizing agreement with others.  
    * **Generative Methods/Masking (e.g., BERT, Autoencoders):** Predicts missing or hidden parts of the data.  
    * **Generative Methods/Masking (e.g., BERT, Autoencoders):** Predicts missing or hidden parts of the data.  
    * **Predictive Learning:** Anticipates future data points in a sequence (e.g., forecasting).  
    * **Predictive Learning:** Anticipates future data points in a sequence (e.g., forecasting).  
* **Benefits:** Reduces dependency on costly, manual data labeling, improves generalization to new data, and supports transfer learning.  
* **Benefits:** Reduces dependency on costly, manual data labeling, improves generalization to new data, and supports transfer learning.  
* **Applications:**  
* **Applications:**  
    * **Finance:** Analyzing historical transactions to detect fraud and predict market trends.  
    * **Finance:** Analyzing historical transactions to detect fraud and predict market trends.  
    * **Healthcare:** Processing medical images and electronic health records (EHRs) to detect abnormalities.  
    * **Healthcare:** Processing medical images and electronic health records (EHRs) to detect abnormalities.  
    * **NLP:** Building language models (like GPT and BERT) that understand context by predicting missing words.  
    * **NLP:** Building language models (like GPT and BERT) that understand context by predicting missing words.  
    * **Robotics/Auto:** Training on sensor and video data to predict environmental changes and improve autonomy. [++[1](https://en.wikipedia.org/wiki/Self-supervised_learning)++, ++[2](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++, ++[3](https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning)++, ++[4](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx)++, ++[5](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)++, ++[6](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence)++, ++[7](https://www.mongodb.com/resources/basics/self-supervised-learning)++]  
    * **Robotics/Auto:** Training on sensor and video data to predict environmental changes and improve autonomy. [++[1](https://en.wikipedia.org/wiki/Self-supervised_learning)++, ++[2](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++, ++[3](https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning)++, ++[4](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx)++, ++[5](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)++, ++[6](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence)++, ++[7](https://www.mongodb.com/resources/basics/self-supervised-learning)++]  
  
    * Historically, the concept has roots in the 1990s and 2000s, with significant precursors in Hinton’s work on autoencoders. The recent resurgence is driven by the explosive availability of data and the need for more efficient, scalable AI. [++[2](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++, ++[8](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence#:~:text=Self%2Dsupervised%20learning%20has%20progressed%20over%20the%20decade,to%20acquire%20valuable%20representations%20without%20explicit%20labels.)++, ++[9](https://openreview.net/pdf?id=MRGFutr0p5e#:~:text=Self%2Dsupervised%20learning%20The%20idea%20of%20self%2Dsupervised%20learning,30%20years%20of%20exploration%20and%20research%20now.)++, ++[10](http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf)++]  
    * Historically, the concept has roots in the 1990s and 2000s, with significant precursors in Hinton’s work on autoencoders. The recent resurgence is driven by the explosive availability of data and the need for more efficient, scalable AI. [++[2](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++, ++[8](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence#:~:text=Self%2Dsupervised%20learning%20has%20progressed%20over%20the%20decade,to%20acquire%20valuable%20representations%20without%20explicit%20labels.)++, ++[9](https://openreview.net/pdf?id=MRGFutr0p5e#:~:text=Self%2Dsupervised%20learning%20The%20idea%20of%20self%2Dsupervised%20learning,30%20years%20of%20exploration%20and%20research%20now.)++, ++[10](http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf)++]  
  
  
*AI responses may include mistakes.*  
*AI responses may include mistakes.*  
  
[1] ++[https://en.wikipedia.org/wiki/Self-supervised_learning](https://en.wikipedia.org/wiki/Self-supervised_learning)++  
[1] ++[https://en.wikipedia.org/wiki/Self-supervised_learning](https://en.wikipedia.org/wiki/Self-supervised_learning)++  
  
[2] ++[https://jonathanbgn.com/2020/12/31/self-supervised-learning.html](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++  
[2] ++[https://jonathanbgn.com/2020/12/31/self-supervised-learning.html](https://jonathanbgn.com/2020/12/31/self-supervised-learning.html)++  
  
[3] ++[https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning](https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning)++  
[3] ++[https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning](https://www.ust.com/en/ust-explainers/what-is-self-supervised-learning)++  
  
[4] ++[https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx)++  
[4] ++[https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Breaking-Down-Self-Supervised-Learning-Concepts-Comparisons-and-Examples--Vmlldzo2MzgwNjIx)++  
  
[5] ++[https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)++  
[5] ++[https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)++  
  
[6] ++[https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence)++  
[6] ++[https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence)++  
  
[7] ++[https://www.mongodb.com/resources/basics/self-supervised-learning](https://www.mongodb.com/resources/basics/self-supervised-learning)++  
[7] ++[https://www.mongodb.com/resources/basics/self-supervised-learning](https://www.mongodb.com/resources/basics/self-supervised-learning)++  
  
[8] ++[https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence#:~:text=Self%2Dsupervised%20learning%20has%20progressed%20over%20the%20decade,to%20acquire%20valuable%20representations%20without%20explicit%20labels.)++  
[8] ++[https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence](https://www.finextra.com/blogposting/26343/self-supervised-learning-the-future-of-artificial-intelligence#:~:text=Self%2Dsupervised%20learning%20has%20progressed%20over%20the%20decade,to%20acquire%20valuable%20representations%20without%20explicit%20labels.)++  
  
[9] ++[https://openreview.net/pdf?id=MRGFutr0p5e](https://openreview.net/pdf?id=MRGFutr0p5e#:~:text=Self%2Dsupervised%20learning%20The%20idea%20of%20self%2Dsupervised%20learning,30%20years%20of%20exploration%20and%20research%20now.)++  
[9] ++[https://openreview.net/pdf?id=MRGFutr0p5e](https://openreview.net/pdf?id=MRGFutr0p5e#:~:text=Self%2Dsupervised%20learning%20The%20idea%20of%20self%2Dsupervised%20learning,30%20years%20of%20exploration%20and%20research%20now.)++  
  
[10] ++[http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf](http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf)++  
[10] ++[http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf](http://proceedings.mlr.press/v27/baldi12a/baldi12a.pdf)++  
  
  
  
  
Through this process, the LLM learns the structure and rules of language, absorbing not only grammar and syntax but also general knowledge that is implicitly contained within the text. However, because of the vastness of language and the breadth of knowledge to be learned, this phase is both computationally expensive and time-consuming.    
Through this process, the LLM learns the structure and rules of language, absorbing not only grammar and syntax but also general knowledge that is implicitly contained within the text. However, because of the vastness of language and the breadth of knowledge to be learned, this phase is both computationally expensive and time-consuming.    
## Fine-Tuning  
## Fine-Tuning  
  
After pre-training, the second step in training LLMs is fine-tuning. In this stage, the model is trained further, but now on a much smaller, more focused dataset that may be labelled or unlabelled, depending on the desired task. This dataset is tailored to the specific application for which the LLM will be used, such as medical language for healthcare applications or legal jargon for legal applications. Fine-tuning allows the model to adjust its pre-trained parameters to better understand and produce text that is specific to its intended use case. This stage is less resource-intensive than pre-training, both in terms of data required and computational resources, due to the more narrow scope of learning.  
After pre-training, the second step in training LLMs is fine-tuning. In this stage, the model is trained further, but now on a much smaller, more focused dataset that may be labelled or unlabelled, depending on the desired task. This dataset is tailored to the specific application for which the LLM will be used, such as medical language for healthcare applications or legal jargon for legal applications. Fine-tuning allows the model to adjust its pre-trained parameters to better understand and produce text that is specific to its intended use case. This stage is less resource-intensive than pre-training, both in terms of data required and computational resources, due to the more narrow scope of learning.  
  
Fine-tuning is the process of refining a pre-existing foundation model to enhance its performance for specific tasks or knowledge areas. For instance, OpenAI's GPT-3, a general-purpose language model, underwent fine-tuning to create ChatGPT, a variant more adept at conversational responses.  
Fine-tuning is the process of refining a pre-existing foundation model to enhance its performance for specific tasks or knowledge areas. For instance, OpenAI's GPT-3, a general-purpose language model, underwent fine-tuning to create ChatGPT, a variant more adept at conversational responses.  
  
Fine-tuning can employ both self-supervised and supervised learning techniques. Self-supervised learning continues the work of the pre-training phase, where the model still learns from unlabelled data by predicting next tokens or filling in blanks. Supervised learning involves labelled data, where the model is given explicit examples of input-output pairs to learn from. For instance, to fine-tune a model for customer service, it might be trained on transcripts of customer interactions where the correct responses are labelled.  
Fine-tuning can employ both self-supervised and supervised learning techniques. Self-supervised learning continues the work of the pre-training phase, where the model still learns from unlabelled data by predicting next tokens or filling in blanks. Supervised learning involves labelled data, where the model is given explicit examples of input-output pairs to learn from. For instance, to fine-tune a model for customer service, it might be trained on transcripts of customer interactions where the correct responses are labelled.  
  
The goals of fine-tuning are two-fold. Firstly, it may aim to increase the model's knowledge about a specialised topic, making it more informed and better able to understand queries about that topic. Secondly, it can alter the model's behaviour to make it more suitable for specific applications, such as training it to follow instructions or maintain a conversation.  
The goals of fine-tuning are two-fold. Firstly, it may aim to increase the model's knowledge about a specialised topic, making it more informed and better able to understand queries about that topic. Secondly, it can alter the model's behaviour to make it more suitable for specific applications, such as training it to follow instructions or maintain a conversation.  
  
You have now learned about how large language models are trained. Before moving forward, answer the following questions to check your understanding.  
You have now learned about how large language models are trained. Before moving forward, answer the following questions to check your understanding.  
  
**Why Fine-Tune?**    
**Why Fine-Tune?**    
  
So far in this session, you have learned about the general process for training large language models. You have also seen that fine-tuning is an integral part of the training process of LLMs and provides vital additional capabilities to our LLM as compared to the foundation model.  
So far in this session, you have learned about the general process for training large language models. You have also seen that fine-tuning is an integral part of the training process of LLMs and provides vital additional capabilities to our LLM as compared to the foundation model.  
  
You have previously interacted with LLMs in various different ways such as by prompting them, by creating applications using frameworks like Langchain and LlamaIndex, using retrieval augmented generation and so on. These approaches allow you to customise the behaviour of an LLM in different ways, but fine-tuning a model lets you achieve the same results with better consistency.  
You have previously interacted with LLMs in various different ways such as by prompting them, by creating applications using frameworks like Langchain and LlamaIndex, using retrieval augmented generation and so on. These approaches allow you to customise the behaviour of an LLM in different ways, but fine-tuning a model lets you achieve the same results with better consistency.  
  
Therefore, to answer the question “Why fine-tune?” we need to approach it from two different angles:  
Therefore, to answer the question “Why fine-tune?” we need to approach it from two different angles:  
* Why fine-tune a foundation model?  
* Why fine-tune a foundation model?  
* Prompt engineering vs. Fine-tuning  
* Prompt engineering vs. Fine-tuning  
  
* In this segment, we will consider these questions and also talk about the process of fine-tuning in more detail.  
* In this segment, we will consider these questions and also talk about the process of fine-tuning in more detail.  
  
* **Why fine-tune a foundation model?**  
* **Why fine-tune a foundation model?**  
  
* In the case of a foundation model (the outcome of the pretraining stage), the task for which it has been trained is “next token prediction”. That is, the model has been trained to predict the next piece of text that logically follows the string of text that has been input into the model. Although this is a powerful capability, it has its own limitations.  
* In the case of a foundation model (the outcome of the pretraining stage), the task for which it has been trained is “next token prediction”. That is, the model has been trained to predict the next piece of text that logically follows the string of text that has been input into the model. Although this is a powerful capability, it has its own limitations.  
  
* Let us consider the prompt “How to tie a tie?” being sent into a foundation LLM. The actual output would look something like this:  
* Let us consider the prompt “How to tie a tie?” being sent into a foundation LLM. The actual output would look something like this:  
  
*    
*    
```
How to tie a tie? This is a question that many men ask themselves. The answer is not as simple as it seems. There are many different ways to tie a tie, and each one has its own advantages and disadvantages. In this article, we will discuss the different ways to tie a tie and the pros and cons of each method. The most common way to tie a tie is the Windsor knot. This knot is easy to tie and looks good on most men. However, it can be difficult to tie if you are not familiar with the process. 
Another popular way to tie a tie is the Four-in-Hand knot. This knot is more difficult to tie than the Windsor knot, but it looks more professional. The Half Windsor knot is a variation of the Windsor knot that is less formal than the Windsor knot. It is a good choice for men who want to look more casual. 
The Pratt knot is a variation of the Windsor knot that is more formal than the Windsor knot. It is a good choice for men who want to look more professional.




```
  
  
  
Here, the output of the model is related to the topic of tying a tie. It is also well-written and informative, but it does not do the most fundamental thing that a user expects from the model at this point. Instructions on how to tie a tie. A desired output may look something like this:  
Here, the output of the model is related to the topic of tying a tie. It is also well-written and informative, but it does not do the most fundamental thing that a user expects from the model at this point. Instructions on how to tie a tie. A desired output may look something like this:  
  
   
   
```
Tying a tie can seem like a daunting task, but with a little practice, you'll be a pro in no time! Here's a step-by-step guide on how to tie a tie:

1. Start by facing a mirror and standing up straight.
2. Place the tie around your neck with the wide end on your left side and the narrow end on your right side. The tie should be hanging down about 12 inches below your neck.
3. Cross the wide end over the narrow end, so that it forms an "X" shape.
4. Take the wide end and pass it behind the narrow end.
5. Bring the wide end up and through the loop that you just created in step 3.
6. You should now have a knot starting to form at the bottom of the tie. Take the wide end and pass it through the loop again.
7. Pull the wide end gently to tighten the knot.
8. Adjust the tie so that it's centered and sits comfortably under your collar.
9. Tuck the narrow end of the tie into your shirt and you're done!




```
  
  
  
   
   
  
This example shows you that foundation LLMs are only trained to predict the next token in the sequence and not to answer questions or to maintain a conversation. This may be a desired behaviour from your chatbot and to elicit this behaviour, you will need to fine-tune your LLM.  
This example shows you that foundation LLMs are only trained to predict the next token in the sequence and not to answer questions or to maintain a conversation. This may be a desired behaviour from your chatbot and to elicit this behaviour, you will need to fine-tune your LLM.  
  
Secondly, as we discussed earlier, the foundation model is trained on a corpus that is made up of a wide range of text and has some general knowledge about the world. But it does not have domain-specific knowledge about a specialised domain. To train that knowledge into the chatbot, we will need to perform fine-tuning. To understand this better, we can take a look at the differences in outputs between two chatbots, one of which has been trained on literature about endocrinology and the other which only has general knowledge about the world.   
Secondly, as we discussed earlier, the foundation model is trained on a corpus that is made up of a wide range of text and has some general knowledge about the world. But it does not have domain-specific knowledge about a specialised domain. To train that knowledge into the chatbot, we will need to perform fine-tuning. To understand this better, we can take a look at the differences in outputs between two chatbots, one of which has been trained on literature about endocrinology and the other which only has general knowledge about the world.   
  
[Non fine-tuned LLM](Attachments/E148BF60-F290-4025-8FB5-120C0A4DA361.png)  
[Non fine-tuned LLM](Attachments/E148BF60-F290-4025-8FB5-120C0A4DA361.png)  
  
    
    
  
You can see the difference in detail in the two outputs. The output from the non fine-tuned LLM is not sure of the diagnosis and essentially recommends the patient to an endocrinologist. Whereas the fine-tuned LLM makes specific diagnoses and suggests a way forward in terms of specific tests and medication. This output is desirable and is a result of fine-tuning an LLM on endocrinology literature.  
You can see the difference in detail in the two outputs. The output from the non fine-tuned LLM is not sure of the diagnosis and essentially recommends the patient to an endocrinologist. Whereas the fine-tuned LLM makes specific diagnoses and suggests a way forward in terms of specific tests and medication. This output is desirable and is a result of fine-tuning an LLM on endocrinology literature.  
  
In conclusion, we there may be two reasons to fine-tune a foundation model:  
In conclusion, we there may be two reasons to fine-tune a foundation model:  
* To change its behaviour  
* To change its behaviour  
* To increase specialised knowledge  
* To increase specialised knowledge  
  
* Let us now look at differences between prompt engineering and fine-tuning.  
* Let us now look at differences between prompt engineering and fine-tuning.  
  
### Prompt engineering vs. fine-tuning  
### Prompt engineering vs. fine-tuning  
  
We have looked at two reasons to fine-tune a foundation model:  
We have looked at two reasons to fine-tune a foundation model:  
* To change its behaviour  
* To change its behaviour  
* To increase specialised knowledge  
* To increase specialised knowledge  
  
* But arguably, we can achieve these results by simply prompting a large language model properly. That is true and in many cases prompt engineering provides adequate performance on required tasks. In such cases, we may not need to perform fine-tuning. Therefore it is always recommended that you start approaching a problem by performing prompt engineering. You may end up solving the problem without having to fine-tune the model and even if you end up having to fine-tune the model, writing prompts to approach a problem will give you a better understanding of the problem and the data required to fine-tune the language model.  
* But arguably, we can achieve these results by simply prompting a large language model properly. That is true and in many cases prompt engineering provides adequate performance on required tasks. In such cases, we may not need to perform fine-tuning. Therefore it is always recommended that you start approaching a problem by performing prompt engineering. You may end up solving the problem without having to fine-tune the model and even if you end up having to fine-tune the model, writing prompts to approach a problem will give you a better understanding of the problem and the data required to fine-tune the language model.  
  
We can summarise the differences between prompt engineering and fine-tuning as follows.   
We can summarise the differences between prompt engineering and fine-tuning as follows.   
We can summarise the differences between prompt engineering and fine-tuning as follows.   

| Prompt Engineering                                  | Fine-tuning |
| --------------------------------------------------- | ----------- |
| •	Amount of new data input is limited by token size |             |
  
  
  
```
•	Don’t need new data to get started
•	Little upfront costs
•	Less technical knowledge required
•	Performance is limited by the size of the context window
•	Should be the first approach while solving a problem | •	Large amounts of new data can be used
•	Require large amounts of data (which can be expensive)
•	Some upfront costs
•	Some technical knowledge required
•	Performance is limited by the performance of the foundation model and the data provided
•	Should be tried if prompt engineering doesn’t give good results |



```
  
  
  
   
   
  
So far we have looked at the reasons to fine-tune a large language model by considering two starting points, a foundation model and prompt engineering. Let us now look at some more general reasons for performing fine-tuning.  
So far we have looked at the reasons to fine-tune a large language model by considering two starting points, a foundation model and prompt engineering. Let us now look at some more general reasons for performing fine-tuning.  
  
   
   
  
By fine-tuning, models can provide more **consistent responses**, aligning more closely with the expected outcomes of their tasks. This consistency is crucial in applications where users rely on precise information or where the LLM needs to maintain a specific tone or style throughout its many responses.  
By fine-tuning, models can provide more **consistent responses**, aligning more closely with the expected outcomes of their tasks. This consistency is crucial in applications where users rely on precise information or where the LLM needs to maintain a specific tone or style throughout its many responses.  
  
Another advantage of fine-tuning is the reduction in **hallucinations**, which are instances where a model generates incorrect or nonsensical information. Fine-tuning helps to ground the model's responses in reality, making them more accurate and reliable.  
Another advantage of fine-tuning is the reduction in **hallucinations**, which are instances where a model generates incorrect or nonsensical information. Fine-tuning helps to ground the model's responses in reality, making them more accurate and reliable.  
  
In terms of moderation, fine-tuning can make models better at understanding and adhering to content guidelines, thereby reducing the risk of generating inappropriate or harmful content. This is particularly important in maintaining user trust and ensuring that the models are safe to interact with.  
In terms of moderation, fine-tuning can make models better at understanding and adhering to content guidelines, thereby reducing the risk of generating inappropriate or harmful content. This is particularly important in maintaining user trust and ensuring that the models are safe to interact with.  
  
Remarkably, fine-tuning can enable smaller models to outperform larger ones on specialised tasks. A smaller model with fewer parameters, when fine-tuned, can become highly efficient at a specific job, sometimes even surpassing a larger model that hasn't been fine-tuned. This specialisation not only leads to better performance but can also result in lower computational costs. For instance, a model with 410 million parameters that has been fine-tuned for a particular domain may perform better in that domain than a much larger model with 175 billion parameters that hasn't undergone the same process.  
Remarkably, fine-tuning can enable smaller models to outperform larger ones on specialised tasks. A smaller model with fewer parameters, when fine-tuned, can become highly efficient at a specific job, sometimes even surpassing a larger model that hasn't been fine-tuned. This specialisation not only leads to better performance but can also result in lower computational costs. For instance, a model with 410 million parameters that has been fine-tuned for a particular domain may perform better in that domain than a much larger model with 175 billion parameters that hasn't undergone the same process.  
  
Finally, fine-tuning can help overcome the limitations posed by the** finite context window** of LLMs. These models can only process a certain number of tokens at a time; when the input exceeds this limit, the earliest tokens are truncated, which can lead to loss of context. Fine-tuning can mitigate this by reducing the size of the required prompt by including knowledge in the fine-tuning data set. This ensures that the most pertinent tokens are processed effectively for the task at hand. Before moving forward, answer the following questions.  
Finally, fine-tuning can help overcome the limitations posed by the** finite context window** of LLMs. These models can only process a certain number of tokens at a time; when the input exceeds this limit, the earliest tokens are truncated, which can lead to loss of context. Fine-tuning can mitigate this by reducing the size of the required prompt by including knowledge in the fine-tuning data set. This ensures that the most pertinent tokens are processed effectively for the task at hand. Before moving forward, answer the following questions.  
  
  
## How to Fine-Tune LLMs     
## How to Fine-Tune LLMs     
We can take three approaches to perform fine-tuning on LLMs:  
We can take three approaches to perform fine-tuning on LLMs:  
* Self-supervised learning  
* Self-supervised learning  
* Supervised learning  
* Supervised learning  
* Reinforcement learning with human feedback  
* Reinforcement learning with human feedback  
  
* Let’s look at these three approaches individually.  
* Let’s look at these three approaches individually.  
  
*  **Self-Supervised Learning**  
*  **Self-Supervised Learning**  
  
* Self-supervised learning focuses on the inherent structure of the data without requiring explicit labels. The training process looks very similar to the pre-training process except for the fact that the training data set contains some specialised knowledge.    
* Self-supervised learning focuses on the inherent structure of the data without requiring explicit labels. The training process looks very similar to the pre-training process except for the fact that the training data set contains some specialised knowledge.    
  
* [Pre-training](Attachments/655B5E55-4D88-424C-A4AC-60A1E28F3439.png)  
* [Pre-training](Attachments/655B5E55-4D88-424C-A4AC-60A1E28F3439.png)  
  
* The LLM continues to learn the task of next-token prediction as it did during pretraining, but now, it does so in a context designed to refine its capabilities in a specific area. For instance, by feeding the model a corpus of text from a certain author or genre, the model can pick up on and generate text with similar stylistic features. Another example as we saw earlier could be to gain knowledge in a specialised field such as endocrinology in medicine.   
* The LLM continues to learn the task of next-token prediction as it did during pretraining, but now, it does so in a context designed to refine its capabilities in a specific area. For instance, by feeding the model a corpus of text from a certain author or genre, the model can pick up on and generate text with similar stylistic features. Another example as we saw earlier could be to gain knowledge in a specialised field such as endocrinology in medicine.   
  
*  **Supervised Learning**  
*  **Supervised Learning**  
  
* Supervised learning, on the other hand, involves training on input-output pairs, which act as explicit examples for the model to learn from. This method relies heavily on the curation of a high-quality training dataset that contains examples closely aligned with the desired task. An example of this data set could be pairs of instructions and responses as given in the image below.    
* Supervised learning, on the other hand, involves training on input-output pairs, which act as explicit examples for the model to learn from. This method relies heavily on the curation of a high-quality training dataset that contains examples closely aligned with the desired task. An example of this data set could be pairs of instructions and responses as given in the image below.    
  
* [instruction](Attachments/86E56E37-62CE-4FD9-8FB6-CC94EDC20C07.png)  
* [instruction](Attachments/86E56E37-62CE-4FD9-8FB6-CC94EDC20C07.png)  
  
*  Once the data set has been curated, we need to convert it into pairs of inputs and outputs by injecting the instruction into a prompt and using the response as the output. This application of supervised learning could enable the LLM to fine-tune its abilities to respond accurately to instructions.   **Reinforcement Learning**  
*  Once the data set has been curated, we need to convert it into pairs of inputs and outputs by injecting the instruction into a prompt and using the response as the output. This application of supervised learning could enable the LLM to fine-tune its abilities to respond accurately to instructions.   **Reinforcement Learning**  
  
* Reinforcement learning introduces a reward model to guide the fine-tuning process. In this approach, the LLM learns to generate responses that are not only contextually and grammatically correct but also aligned with human preferences. The reward model typically involves human feedback, which assesses the quality and relevance of the model's responses. Over time, the LLM is trained to optimise its outputs to maximise this feedback, essentially learning to produce responses that are more likely to be favoured by users.  
* Reinforcement learning introduces a reward model to guide the fine-tuning process. In this approach, the LLM learns to generate responses that are not only contextually and grammatically correct but also aligned with human preferences. The reward model typically involves human feedback, which assesses the quality and relevance of the model's responses. Over time, the LLM is trained to optimise its outputs to maximise this feedback, essentially learning to produce responses that are more likely to be favoured by users.  
  
*    
*    
  
* After considering the three different types of fine-tuning, let’s look at the steps that we need to undertake every time we perform fine-tuning.  
* After considering the three different types of fine-tuning, let’s look at the steps that we need to undertake every time we perform fine-tuning.  
1. Choose fine-tuning task  
2. Choose fine-tuning task  
3. Prepare training data set  
4. Prepare training data set  
5. Choose a base model  
6. Choose a base model  
7. Perform fine-tuning  
8. Perform fine-tuning  
9. Evaluate model performance  
10. Evaluate model performance  
  
11. Before moving forward, answer the following questions to check your understanding.  
12. Before moving forward, answer the following questions to check your understanding.  
  
**Fine-Tuning Code**    
**Fine-Tuning Code**    
  
In this segment, we will look at the code that can be used to fine-tune a large language model.  
In this segment, we will look at the code that can be used to fine-tune a large language model.  
  
   
   
  
You can start by downloading the notebook given below and going through it. The text that follows in this segment can be used alongside the notebook as an explainer for the concepts and code covered in the notebook.  ++[Fine-tuning Large Language Models](https://cdn.upgrad.com/uploads/production/0c5f5425-cc19-4dc8-a1e1-a80f46db1e92/Fine_tuning_large_language_models.ipynb)++     
You can start by downloading the notebook given below and going through it. The text that follows in this segment can be used alongside the notebook as an explainer for the concepts and code covered in the notebook.  ++[Fine-tuning Large Language Models](https://cdn.upgrad.com/uploads/production/0c5f5425-cc19-4dc8-a1e1-a80f46db1e92/Fine_tuning_large_language_models.ipynb)++     
  
You saw this notebook being used in the live session. Let’s look at the steps that outline the tasks that we completed in this notebook.  
You saw this notebook being used in the live session. Let’s look at the steps that outline the tasks that we completed in this notebook.  
1. Installing and importing required libraries  
2. Installing and importing required libraries  
3. Comparing outputs from the two types of models  
4. Comparing outputs from the two types of models  
5. Exploring the fine-tuning data set  
6. Exploring the fine-tuning data set  
7. Data Preparation  
8. Data Preparation  
9. Training and inference  
10. Training and inference  
  
11.    
12.    
  
13. We will look at each one of these steps individually in this segment.  
14. We will look at each one of these steps individually in this segment.  
  
15.    
16.    
  
17. Before executing any code, we need to make sure that we are running this notebook in Google Colab and that we have selected the T4 GPU runtime. This is important because fine-tuning large language models requires considerable compute and memory resources and the T4 GPU is a powerful processor that provides 16 GB VRAM. This is enough to fine-tune smaller models.  
18. Before executing any code, we need to make sure that we are running this notebook in Google Colab and that we have selected the T4 GPU runtime. This is important because fine-tuning large language models requires considerable compute and memory resources and the T4 GPU is a powerful processor that provides 16 GB VRAM. This is enough to fine-tune smaller models.  
  
19.    
20.    
  
21. Let’s now look at the first step.  
22. Let’s now look at the first step.  
  
23.    
24.    
  
25. **Installing and Importing Required Libraries**  
26. **Installing and Importing Required Libraries**  
  
27. We started by installing the required libraries using the code given below:  
28. We started by installing the required libraries using the code given below:  
29. We started by installing the required libraries using the code given below:  
30. We started by installing the required libraries using the code given below:  
```
# Installing required libraries
! pip install --upgrade pip lamini --disable-pip-version-check torch torchdata transformers4.31.0 datasets --quiet accelerate0.20.3




```
  
  
  
   
   
  
This line of code is used to install the following libraries:  
This line of code is used to install the following libraries:  
* *lamini*: This library is used to quickly load and prompt large language models.  
* *lamini*: This library is used to quickly load and prompt large language models.  
* *torch*: This library provides the implementation of neural networks. It works as a dependency for other libraries  
* *torch*: This library provides the implementation of neural networks. It works as a dependency for other libraries  
* *transformers*: This library provides the implementation of large language models. We have tested our code for version 4.31.0 and hence have frozen it to that version.  
* *transformers*: This library provides the implementation of large language models. We have tested our code for version 4.31.0 and hence have frozen it to that version.  
* *accelerate*: This library improves the performance of the transformer code.  
* *accelerate*: This library improves the performance of the transformer code.  
* *datasets*: This library allows us to load and manipulate data sets efficiently.  
* *datasets*: This library allows us to load and manipulate data sets efficiently.  
  
*    
*    
  
* After installing the libraries, we imported the required methods.  
* After installing the libraries, we imported the required methods.  
```
import lamini
from google.colab import userdata
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
import pandas as pd
from datasets import Dataset




```
  
  
  
   
   
  
Let’s take a look at the methods that were imported in more detail:  
Let’s take a look at the methods that were imported in more detail:  
* import lamini  
* import lamini  
  
    * Here, we are importing the *lamini *library. This library is used to easily load, prompt, and fine-tune large language models. In our case, we will only use it to explore the behaviour of LLMs.  
    * Here, we are importing the *lamini *library. This library is used to easily load, prompt, and fine-tune large language models. In our case, we will only use it to explore the behaviour of LLMs.  
* from google.colab import userdata  
* from google.colab import userdata  
  
    * Google Colab provides a way to save secret API keys and access them inside the program. The *userdata *object is used to import the API key for the llama library.  
    * Google Colab provides a way to save secret API keys and access them inside the program. The *userdata *object is used to import the API key for the llama library.  
* import torch  
* import torch  
  
    * PyTorch provides an implementation of neural networks that is required by other libraries that are built on top of it.  
    * PyTorch provides an implementation of neural networks that is required by other libraries that are built on top of it.  
* from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer  
* from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer  
  
    * These are the components that we require from the transformers library.  
    * These are the components that we require from the transformers library.  
    * *AutoModelForCausalLM *is used to load a causal language model. All the models that we load in our notebook for the purposes of training will be loaded using this object.  
    * *AutoModelForCausalLM *is used to load a causal language model. All the models that we load in our notebook for the purposes of training will be loaded using this object.  
    * *AutoTokenizer *provides access to the tokenizer associated with a language model.  
    * *AutoTokenizer *provides access to the tokenizer associated with a language model.  
    * *TrainingArguments *is used to specify the hyperparameters used during the fine-tuning process.  
    * *TrainingArguments *is used to specify the hyperparameters used during the fine-tuning process.  
    * *Trainer *is the object that actually performs the fine-tuning.  
    * *Trainer *is the object that actually performs the fine-tuning.  
* import pandas as pd  
* import pandas as pd  
  
* from datasets import Dataset  
* from datasets import Dataset  
  
    * These libraries are required for handling data sets.  
    * These libraries are required for handling data sets.  
  
    *    
    *    
  
    * We have now looked at all the libraries that were imported in this notebook. We will talk more about each one of these libraries and their methods as and when they are used inside the code. Let’s now move on to the next part of the code where we will examine the outputs of different LLMs.  
    * We have now looked at all the libraries that were imported in this notebook. We will talk more about each one of these libraries and their methods as and when they are used inside the code. Let’s now move on to the next part of the code where we will examine the outputs of different LLMs.  
  
    *    
    *    
  
    * **Comparing outputs from the two types of models**  
    * **Comparing outputs from the two types of models**  
  
    * One of the reasons that we generally fine-tune LLMs is to introduce new behaviour. As you know foundation models are trained on the task of next-token prediction and that doesn’t lend themselves well to providing a realistic chat interface. Therefore, popular models provide base and chat fine-tuned versions of their models. For example, Llama 2 provides two models ++[Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)++ and ++[Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)++. In this section, we will explore the output that these two models provide for the same input and compare them with each other.  
    * One of the reasons that we generally fine-tune LLMs is to introduce new behaviour. As you know foundation models are trained on the task of next-token prediction and that doesn’t lend themselves well to providing a realistic chat interface. Therefore, popular models provide base and chat fine-tuned versions of their models. For example, Llama 2 provides two models ++[Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)++ and ++[Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)++. In this section, we will explore the output that these two models provide for the same input and compare them with each other.  
  
    *    
    *    
  
    * We will use the library provided by ++[Lamini](https://lamini-ai.github.io/)++ for this purpose. This library can be used to conveniently load, prompt, and fine-tune large language models. Although we are loading and prompting the two variants of Llama 2 using this library, we will perform fine-tuning using the lower-level functions provided by the *transformers *library.  
    * We will use the library provided by ++[Lamini](https://lamini-ai.github.io/)++ for this purpose. This library can be used to conveniently load, prompt, and fine-tune large language models. Although we are loading and prompting the two variants of Llama 2 using this library, we will perform fine-tuning using the lower-level functions provided by the *transformers *library.  
  
    *    
    *    
  
    * To initialise the *llama *library, we first need to make an account on Lamini and retrieve our API token from the ++[Account](https://app.lamini.ai/account)++ page. Note that this is required only for exploring the outputs of the two versions of Llama and not for the actual fine-tuning code, so you may choose to skip this step. You can then add this as a ++[secret in Google Colab](https://medium.com/@parthdasawant/how-to-use-secrets-in-google-colab-450c38e3ec75)++ and use the following code to initialise the API.  
    * To initialise the *llama *library, we first need to make an account on Lamini and retrieve our API token from the ++[Account](https://app.lamini.ai/account)++ page. Note that this is required only for exploring the outputs of the two versions of Llama and not for the actual fine-tuning code, so you may choose to skip this step. You can then add this as a ++[secret in Google Colab](https://medium.com/@parthdasawant/how-to-use-secrets-in-google-colab-450c38e3ec75)++ and use the following code to initialise the API.  
  
    *    
    *    
```
lamini.api_key = userdata.get('my_lamini_api_token')




```
  
  
  
   
   
  
After initialising the API, we can load the two models using the *BasicModelRunner()* object from the lamini library. Given below are the outputs of the two versions of Llama 2 for the question “How to be a good data scientist?”  
After initialising the API, we can load the two models using the *BasicModelRunner()* object from the lamini library. Given below are the outputs of the two versions of Llama 2 for the question “How to be a good data scientist?”  
  
   
   
  
**Chat fine-tuned version (Llama-2-7b-chat-hf)**  
**Chat fine-tuned version (Llama-2-7b-chat-hf)**  
```
Data science is a field that combines mathematics, statistics, computer science, and domain expertise in order to extract insights and knowledge from data. To be a good data scientist, one must have a strong foundation in these areas, as well as the ability to communicate complex ideas to non-technical stakeholders. Here are some key skills and traits that are important for data scientists to possess:

1. Strong analytical and problem-solving skills: Data scientists must be able to analyze complex data sets and identify patterns, trends, and insights. They must also be able to communicate their findings effectively to stakeholders.
2. Programming skills: Data scientists must be proficient in programming languages such as Python, R, or SQL, and be able to write efficient and well-structured code.
3. Statistical knowledge: Data scientists must have a strong understanding of statistical concepts such as hypothesis testing, regression analysis, and time series analysis.
4. Machine learning skills: Data scientists must be familiar with machine learning algorithms such as decision trees, clustering, and neural networks, and be able to apply them to real-world data set
5.




```
  
  
  
   
   
  
**Non chat fine-tuned version (Llama-2-7b-hf)**  
**Non chat fine-tuned version (Llama-2-7b-hf)**  
```
How to be a good data scientist? Data science is a field that is growing rapidly. It is a field that is constantly changing and evolving. There are many different ways to be a good data scientist. In this article, we will discuss some of the ways that you can be a good data scientist.
Data science is a field that is constantly changing and evolving. There are many different ways to be a good data scientist. In this article, we will discuss some of the ways that you can be a good data scientist.
Data science is a field that is constantly changing and evolving. There are many different ways to be a good data scientist. In this article, we will discuss some of the ways that you can be a good data scientist.




```
  
  
  
   
   
  
You can see that the output to our question is more coherent in the case of the chat fine-tuned version of the Llama 2 model even though the base model is the same in both cases. This is an illustration of how fine-tuning can make your LLM more user friendly and can add new functionalities into the model.    
You can see that the output to our question is more coherent in the case of the chat fine-tuned version of the Llama 2 model even though the base model is the same in both cases. This is an illustration of how fine-tuning can make your LLM more user friendly and can add new functionalities into the model.    
  
   
   
  
You have now examined the outputs of two different types of LLMs. Let’s now move on to the main task of this notebook, fine-tuning an LLM. We will start by exploring the fine-tuning data set. Before moving forward, answer the following question to check your understanding.  
You have now examined the outputs of two different types of LLMs. Let’s now move on to the main task of this notebook, fine-tuning an LLM. We will start by exploring the fine-tuning data set. Before moving forward, answer the following question to check your understanding.  
  
   
   
  
Reference Links  
Reference Links  
  
++[Fine-tuning Large Language Model](https://cdn.upgrad.com/uploads/production/0c5f5425-cc19-4dc8-a1e1-a80f46db1e92/Fine_tuning_large_language_models.ipynb)++  
++[Fine-tuning Large Language Model](https://cdn.upgrad.com/uploads/production/0c5f5425-cc19-4dc8-a1e1-a80f46db1e92/Fine_tuning_large_language_models.ipynb)++  
  
**Exploring the fine-tuning data set**  
**Exploring the fine-tuning data set**  
  
In this notebook, we will fine-tune our LLM on a question answering data set. The task on which our model will be trained is to answer questions that a customer support executive might get. We are going to use a subset of the ++[Customer Service Dataset](https://github.com/bitext/customer-support-llm-chatbot-training-dataset)++ provided by Bitext.  
In this notebook, we will fine-tune our LLM on a question answering data set. The task on which our model will be trained is to answer questions that a customer support executive might get. We are going to use a subset of the ++[Customer Service Dataset](https://github.com/bitext/customer-support-llm-chatbot-training-dataset)++ provided by Bitext.  
  
 In the notebook, we started by loading the data set into the variable *df_q_a *using the following code.  
 In the notebook, we started by loading the data set into the variable *df_q_a *using the following code.  
```
df_q_a = pd.read_csv(data_path)




```
  
  
  
   
   
  
Here, data_path refers to the address where the raw CSV file of the data set is hosted on GitHub. The data set has 5 columns, namely: *flags*, *instruction*, *category*, *intent*, and *response*. But we will only use the *instruction *and the *response *columns to train our chatbot. Let’s look at what these columns look like for the second entry in the data set.  
Here, data_path refers to the address where the raw CSV file of the data set is hosted on GitHub. The data set has 5 columns, namely: *flags*, *instruction*, *category*, *intent*, and *response*. But we will only use the *instruction *and the *response *columns to train our chatbot. Let’s look at what these columns look like for the second entry in the data set.  
```
print("question: " + df_q_a.iloc[1]["instruction"])
print("answer: " + df_q_a.iloc[1]["response"])




```
  
  
  
   
   
```
question: i need help cancelling puchase {{Order Number}}
answer: I can sense that you're seeking assistance with canceling your purchase with the purchase number {{Order Number}}. I apologize for any inconvenience caused, and I'm here to guide you through the process.

To cancel your purchase, please follow these steps:

1. Log into your account: Visit our {{Online Company Portal Info}} and sign in using your credentials.
2. Locate your order: Once logged in, navigate to the '{{Online Order Interaction}}' or '{{Online Order Interaction}}' section to find the purchase with the order number {{Order Number}}.
3. Initiate the cancellation: Upon finding your purchase, look for the option labeled '{{Online Order Interaction}}' and click on it to initiate the cancellation process.
4. Confirm the cancellation: Our system might ask for confirmation or feedback regarding the cancellation. Kindly provide the necessary information to complete the process.
5. Seek additional support: If you encounter any difficulties or require further assistance, our dedicated customer support team is available during {{Customer Support Hours}}. You can contact us at {{Customer Support Phone Number}} or use the Live Chat feature on our {{Website URL}}.

We appreciate your understanding and value your satisfaction. Should you have any more questions or concerns, feel free to reach out to us. We're here to help you.




```
  
  
  
   
   
  
As you can see, the data set consists of question and answer pairs for common queries that may arise in the context of customer support. Feel free to explore more entries in this data set to familiarise yourself with the kind of responses you should expect from the fine-tuned LLM.  
As you can see, the data set consists of question and answer pairs for common queries that may arise in the context of customer support. Feel free to explore more entries in this data set to familiarise yourself with the kind of responses you should expect from the fine-tuned LLM.  
  
   
   
  
You have now explored the fine-tuning data set. Next, we will move on to the data preparation stage.  
You have now explored the fine-tuning data set. Next, we will move on to the data preparation stage.  
  
   
   
  
**Data Preparation**  
**Data Preparation**  
  
The LLM that we are fine-tuning in this demonstration is the *pythia-70m* model provided by EleutherAI. The model contains 70 million parameters and is a small model when compared to other popular LLMs. You can learn more about this model ++[here](https://huggingface.co/EleutherAI/pythia-70m)++.   
The LLM that we are fine-tuning in this demonstration is the *pythia-70m* model provided by EleutherAI. The model contains 70 million parameters and is a small model when compared to other popular LLMs. You can learn more about this model ++[here](https://huggingface.co/EleutherAI/pythia-70m)++.   
  
   
   
  
As you know, LLMs convert text into tokens before sending them in as inputs to the model. For this purpose, LLMs provide the tokenizer that can be used to process the text as a part of the model. As tokenization is one of the most important steps in data preparation, we demonstrated the process of tokenization on the first entry in the data set in the notebook. For this, we loaded the tokenizer associated with the *pythia-70m *model using the code given below.  
As you know, LLMs convert text into tokens before sending them in as inputs to the model. For this purpose, LLMs provide the tokenizer that can be used to process the text as a part of the model. As tokenization is one of the most important steps in data preparation, we demonstrated the process of tokenization on the first entry in the data set in the notebook. For this, we loaded the tokenizer associated with the *pythia-70m *model using the code given below.  
  
   
   
```
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")




```
  
  
  
   
   
  
The tokenizer object initialised as given above, can take in a sequence of strings and can return a sequence of encoded texts for each of those strings. For example, consider the list consisting of the values in the *instruction *column of the first entry in the data set.  
The tokenizer object initialised as given above, can take in a sequence of strings and can return a sequence of encoded texts for each of those strings. For example, consider the list consisting of the values in the *instruction *column of the first entry in the data set.  
  
   
   
```
question about cancelling order {{Order Number}}




```
  
  
  
   
   
  
On passing this list to the tokenizer, we get the following output.  
On passing this list to the tokenizer, we get the following output.  
```
{'input_ids': [19751, 670, 476, 68, 3485, 1340, 12033, 13921, 11057, 599], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}




```
  
  
  
   
   
  
This dictionary contains two key-value pairs and the values in both cases are lists. Let’s look at the two key-value pairs:  
This dictionary contains two key-value pairs and the values in both cases are lists. Let’s look at the two key-value pairs:  
* *input_ids*: This key contains the actual tokens that are received from the tokenizer. The items in the list, *“19751, 670, 476, …”*, correspond to the input string “question about cancelling …”.   
* *input_ids*: This key contains the actual tokens that are received from the tokenizer. The items in the list, *“19751, 670, 476, …”*, correspond to the input string “question about cancelling …”.   
* *attention_mask*: The tokenizer produces an attention mask that tells the model which token to actually focus on. We will look at this in more detail later.  
* *attention_mask*: The tokenizer produces an attention mask that tells the model which token to actually focus on. We will look at this in more detail later.  
  
* In practice, we will tokenize sequences of strings that make up our data set. Therefore, in the notebook, we provided an example where we create a list of strings called *concatenated* and perform tokenization on this list of strings.  
* In practice, we will tokenize sequences of strings that make up our data set. Therefore, in the notebook, we provided an example where we create a list of strings called *concatenated* and perform tokenization on this list of strings.  
  
*    
*    
  
* We used the following code to create the list.  
* We used the following code to create the list.  
```
instructions = df_q_a["instruction"][0]
responses = df_q_a["response"][0]
concatenated = [instructions, responses]




```
  
  
  
   
   
  
The list of string *concatenated *contains two items and looks as follows.  
The list of string *concatenated *contains two items and looks as follows.  
```
['question about cancelling order {{Order Number}}', "I've understood you have a question regarding canceling order {{Order Number}}, and I'm here to provide you with the information you need. Please go ahead and ask your question, and I'll do my best to assist you."]




```
  
  
  
   
   
  
We then used the following code to tokenize this list of strings.  
We then used the following code to tokenize this list of strings.  
```
encoded_text = tokenizer(concatenated)




```
  
  
  
   
   
  
The output of this statement, *encoded_text *is given below.  
The output of this statement, *encoded_text *is given below.  
  
   
   
```
{'input_ids': [[19751, 670, 476, 68, 3485, 1340, 12033, 13921, 11057, 599], [42, 1849, 7192, 368, 452, 247, 1953, 5001, 14002, 272, 1340, 12033, 13921, 11057, 8503, 285, 309, 1353, 1060, 281, 2085, 368, 342, 253, 1491, 368, 878, 15, 7764, 564, 6386, 285, 1642, 634, 1953, 13, 285, 309, 1833, 513, 619, 1682, 281, 10073, 368, 15]], 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]}




```
  
  
  
   
   
  
This time also, we received two key-value pairs as the output of the *tokenizer()* function. Let's look at the key-value pairs in more detail:  
This time also, we received two key-value pairs as the output of the *tokenizer()* function. Let's look at the key-value pairs in more detail:  
* *input_ids*: Because we sent a list of two strings as input this time, the value corresponding to *input_ids* is a list of lists. The two lists in this list of lists represent the tokens for the two strings that were sent into the tokenizer. Note that because the second string was longer than the first list, the second list is also longer than the first list.  
* *input_ids*: Because we sent a list of two strings as input this time, the value corresponding to *input_ids* is a list of lists. The two lists in this list of lists represent the tokens for the two strings that were sent into the tokenizer. Note that because the second string was longer than the first list, the second list is also longer than the first list.  
* *attention_mask*: This is true for the value associated with *attention_mask* as well. It is a list of lists where the two nested lists correspond to the attention masks associated with the two strings. We will learn about attention masks later.  
* *attention_mask*: This is true for the value associated with *attention_mask* as well. It is a list of lists where the two nested lists correspond to the attention masks associated with the two strings. We will learn about attention masks later.  
  
* Notice that as the length of the two strings is different, the output of the *tokenizer()* function are lists of different sizes. But this is a problem, because our model expects token lists of the same size. To handle this problem, we employ two different kinds of strategies while preparing our data: padding and truncation.    
* Notice that as the length of the two strings is different, the output of the *tokenizer()* function are lists of different sizes. But this is a problem, because our model expects token lists of the same size. To handle this problem, we employ two different kinds of strategies while preparing our data: padding and truncation.    
  
* **Padding and Truncation**  
* **Padding and Truncation**  
  
* Padding is used to bring the length of the list of tokens up to a uniform length by adding some placeholder tokens (if the length of the list of tokens is smaller than the required length). If the length of the list of tokens is longer than the required length, then perform truncation to bring it down to the required length.  
* Padding is used to bring the length of the list of tokens up to a uniform length by adding some placeholder tokens (if the length of the list of tokens is smaller than the required length). If the length of the list of tokens is longer than the required length, then perform truncation to bring it down to the required length.  
  
* The pretrained tokenizers come with an *eos_token *(end of sentence token) which is appended at the end of the list of the list of tokens if we are doing padding.  
* The pretrained tokenizers come with an *eos_token *(end of sentence token) which is appended at the end of the list of the list of tokens if we are doing padding.  
  
* We specified the *pad_token* using the code given below.  
* We specified the *pad_token* using the code given below.  
  
*    
*    
```
tokenizer.pad_token = tokenizer.eos_token




```
  
  
  
   
   
  
We then performed padding using the following code.  
We then performed padding using the following code.  
  
   
   
```
encoded_texts_longest = tokenizer(concatenated, padding=True)
print("Using padding: ", encoded_texts_longest["input_ids"])
print("Attention mask for this piece of text: ", encoded_texts_longest["attention_mask"])




```
  
  
  
   
   
  
By setting the value of *padding* to *True*Tan increase the size of the shorter list of tokens up to the length of the longest token list. The output of this piece of code is given below.  
By setting the value of *padding* to *True*Tan increase the size of the shorter list of tokens up to the length of the longest token list. The output of this piece of code is given below.  
  
   
   
```
Using padding:  [[19751, 670, 476, 68, 3485, 1340, 12033, 13921, 11057, 599, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [42, 1849, 7192, 368, 452, 247, 1953, 5001, 14002, 272, 1340, 12033, 13921, 11057, 8503, 285, 309, 1353, 1060, 281, 2085, 368, 342, 253, 1491, 368, 878, 15, 7764, 564, 6386, 285, 1642, 634, 1953, 13, 285, 309, 1833, 513, 619, 1682, 281, 10073, 368, 15]]
Attention mask for this piece of text:  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]




```
  
  
  
   
   
  
Notice that the length of both the lists in *input_ids *is the same this time. Also, the lists corresponding to the shorter string has zeros appended to it.  
Notice that the length of both the lists in *input_ids *is the same this time. Also, the lists corresponding to the shorter string has zeros appended to it.  
  
   
   
  
We can also specify the length of the padded sequence by setting the value of *padding* to *'max_length' *and specifying the desired length in the *max_length* parameter.  
We can also specify the length of the padded sequence by setting the value of *padding* to *'max_length' *and specifying the desired length in the *max_length* parameter.  
  
Consider the example given below.   
Consider the example given below.   
  
[Before padding](Attachments/B947ABA3-278B-4F1B-84B1-1B999BE214CD.png)  
[Before padding](Attachments/B947ABA3-278B-4F1B-84B1-1B999BE214CD.png)  
  
Here, the *max_length *is specified to be 10 whereas the list of tokens for a string has a length of 8. So after padding, two instances of the *eos_token *are appended at the end of the string. In this case, the *eos_token *has a value of 0.   
Here, the *max_length *is specified to be 10 whereas the list of tokens for a string has a length of 8. So after padding, two instances of the *eos_token *are appended at the end of the string. In this case, the *eos_token *has a value of 0.   
  
   
   
  
We used the following code to demonstrate *max_length* padding in the notebook.  
We used the following code to demonstrate *max_length* padding in the notebook.  
  
   
   
```
encoded_texts_longest = tokenizer(concatenated, max_length = 30, padding='max_length')
print("Using padding: ", encoded_texts_longest["input_ids"])
print("Attention mask for this piece of text: ", encoded_texts_longest["attention_mask"])
print("Length of the list of tokens:", len(encoded_texts_longest["input_ids"][0]))




```
  
  
  
   
   
  
The output of this code cell is given below.  
The output of this code cell is given below.  
  
   
   
```
Using padding:  [[19751, 670, 476, 68, 3485, 1340, 12033, 13921, 11057, 599, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [42, 1849, 7192, 368, 452, 247, 1953, 5001, 14002, 272, 1340, 12033, 13921, 11057, 8503, 285, 309, 1353, 1060, 281, 2085, 368, 342, 253, 1491, 368, 878, 15, 7764, 564, 6386, 285, 1642, 634, 1953, 13, 285, 309, 1833, 513, 619, 1682, 281, 10073, 368, 15]]
Attention mask for this piece of text:  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Length of the list of tokens: 30




```
  
  
  
   
   
  
This is a good place to talk about the **attention masks**. There are multiple reasons because of which the tokenizer sends an attention mask along with the actual tokens, but in our context, it is being used to handle padding. As we saw, we can handle strings of different lengths by adding padding tokens at the end. This is because neural network architectures expect inputs to be of the same size. But these extra tokens are also irrelevant tokens which may reduce the models accuracy. So, the attention mask tells the model which tokens are actually relevant by assigning the value 1 to the actual tokens and the value 0 to the padding tokens. This improves the focus of the model and allows it to attention mechanism inside transformers to only consider the actual tokens corresponding to the input string.  
This is a good place to talk about the **attention masks**. There are multiple reasons because of which the tokenizer sends an attention mask along with the actual tokens, but in our context, it is being used to handle padding. As we saw, we can handle strings of different lengths by adding padding tokens at the end. This is because neural network architectures expect inputs to be of the same size. But these extra tokens are also irrelevant tokens which may reduce the models accuracy. So, the attention mask tells the model which tokens are actually relevant by assigning the value 1 to the actual tokens and the value 0 to the padding tokens. This improves the focus of the model and allows it to attention mechanism inside transformers to only consider the actual tokens corresponding to the input string.  
  
   
   
  
   
   
  
Next, let's talk about **truncation**. If the input string is very long (perhaps longer than the context window of the LLM), we will need to truncate it. We can specify the length to which the token lists must be truncated by specifying the *max_length*. While truncating, if the length of the list of tokens for a given string is longer than the specified *max_length*, we drop some tokens from the tokens list.  
Next, let's talk about **truncation**. If the input string is very long (perhaps longer than the context window of the LLM), we will need to truncate it. We can specify the length to which the token lists must be truncated by specifying the *max_length*. While truncating, if the length of the list of tokens for a given string is longer than the specified *max_length*, we drop some tokens from the tokens list.  
  
   
   
  
Consider the example of truncation the we saw in the notebook.  
Consider the example of truncation the we saw in the notebook.  
  
   
   
```
encoded_texts_truncation = tokenizer(concatenated, max_length=3, truncation=True)
print("Using truncation: ", encoded_texts_truncation)




```
  
  
  
   
   
  
The output of this code cell is as follows.  
The output of this code cell is as follows.  
  
   
   
```
Using truncation:  {'input_ids': [[19751, 670, 476], [42, 1849, 7192]], 'attention_mask': [[1, 1, 1], [1, 1, 1]]}




```
  
  
  
   
   
  
You can choose the side from which you want to truncate the list, that is, from the right side of the list or the left side.  
You can choose the side from which you want to truncate the list, that is, from the right side of the list or the left side.  
  
   
   
  
You saw an example of this in the notebook.  
You saw an example of this in the notebook.  
  
   
   
```
tokenizer.truncation_side = "left"
encoded_texts_truncation_left = tokenizer(concatenated, max_length=3, truncation=True)
print("Using left-side truncation: ", encoded_texts_truncation_left)




```
  
  
  
   
   
  
The output of this code cell is given below.  
The output of this code cell is given below.  
  
   
   
```
Using left-side truncation:  {'input_ids': [[13921, 11057, 599], [10073, 368, 15]], 'attention_mask': [[1, 1, 1], [1, 1, 1]]}




```
  
  
  
   
   
  
Note the difference in the outputs when we truncate from left side and the right side.  
Note the difference in the outputs when we truncate from left side and the right side.  
  
You also saw an example of padding and truncation being performed together as given in the code cell below.   
You also saw an example of padding and truncation being performed together as given in the code cell below.   
```
encoded_texts_both = tokenizer(concatenated, max_length=15, truncation=True, padding=True)
print("Using both padding and truncation: ", encoded_texts_both["input_ids"])




```
  
  
  
   
   
  
This code resulted in the following output.  
This code resulted in the following output.  
```
Using both padding and truncation:  [[19751, 670, 476, 68, 3485, 1340, 12033, 13921, 11057, 599, 0, 0, 0, 0, 0], [285, 1642, 634, 1953, 13, 285, 309, 1833, 513, 619, 1682, 281, 10073, 368, 15]]




```
  
  
  
   
   
  
Notice that in this case, both the token lists are 15 tokens long. The shorter list has been padded with 0s to bring the length up to 15 and the longer list has been truncated from the left hand side to get this output.  
Notice that in this case, both the token lists are 15 tokens long. The shorter list has been padded with 0s to bring the length up to 15 and the longer list has been truncated from the left hand side to get this output.  
  
   
   
  
Usually in practice, we set a value for *max_length *and set both padding and truncation to be true. You can choose the side from which you want to truncate based on the task at hand.  
Usually in practice, we set a value for *max_length *and set both padding and truncation to be true. You can choose the side from which you want to truncate based on the task at hand.  
  
   
   
  
We have now discussed tokenization in detail including the problem of differing lengths of input strings and some strategies like padding and truncation that we can employ to address those problems. Before moving forward, answer the following questions to check your understanding. For the following questions, you need to read about the different values that can be assigned to the *padding *and *truncation *parameter in the AutoTokenizer class ++[here](https://huggingface.co/docs/transformers/pad_truncation)++.  
We have now discussed tokenization in detail including the problem of differing lengths of input strings and some strategies like padding and truncation that we can employ to address those problems. Before moving forward, answer the following questions to check your understanding. For the following questions, you need to read about the different values that can be assigned to the *padding *and *truncation *parameter in the AutoTokenizer class ++[here](https://huggingface.co/docs/transformers/pad_truncation)++.  
  
ext, we will discuss how to use prompt templates to prepare our instruction-response pairs for training.  
ext, we will discuss how to use prompt templates to prepare our instruction-response pairs for training.  
  
   
   
  
In the notebook, we subsetting the data set in two ways:  
In the notebook, we subsetting the data set in two ways:  
* We picked rows that have the value of *intent* set to *'cancel_order'* to reduce the size of the data set. You can try skipping this step during training to increase the size of the data set and hence the performance of the model.  
* We picked rows that have the value of *intent* set to *'cancel_order'* to reduce the size of the data set. You can try skipping this step during training to increase the size of the data set and hence the performance of the model.  
* As we will only use the *instruction* and *response *columns, we dropped the other columns.  
* As we will only use the *instruction* and *response *columns, we dropped the other columns.  
  
* After subsetting the data set, we created a prompt template and "hydrated" that prompt template with values from the instruction and response columns using the code given below.  
* After subsetting the data set, we created a prompt template and "hydrated" that prompt template with values from the instruction and response columns using the code given below.  
  
*    
*    
```
list_of_entries = []
for i in range(0, len(df_q_a)):
  entry = {
      'question': f"### Below is an instruction that describes a task. Write a response that appropriately completes the request. \nQuestion:\n{df_q_a.iloc[i]['instruction']}\n\n### Answer:",
      'answer': df_q_a.iloc[i]['response']
  }
  list_of_entries.append(entry)




```
  
  
  
   
   
  
An example of an entry from the list *list_of_entries *is given below.  
An example of an entry from the list *list_of_entries *is given below.  
  
   
   
```
{'question': '### Below is an instruction that describes a task. Write a response that appropriately completes the request. \nQuestion:\nquestion about cancelling order {{Order Number}}\n\n### Answer:',
 'answer': "I've understood you have a question regarding canceling order {{Order Number}}, and I'm here to provide you with the information you need. Please go ahead and ask your question, and I'll do my best to assist you."}




```
  
  
  
   
   
  
Note that we have added some text before the instruction. This provides context to the LLM about the task we are expecting it to perform.  
Note that we have added some text before the instruction. This provides context to the LLM about the task we are expecting it to perform.  
  
   
   
  
Then, we concatenate the two values in each entry in *list_of_entries *before tokenizing them.  
Then, we concatenate the two values in each entry in *list_of_entries *before tokenizing them.  
  
   
   
  
We wrote a function *tokenize_function *to perform this whole task in one go.  
We wrote a function *tokenize_function *to perform this whole task in one go.  
  
   
   
```
def tokenize_function(entry):
    text = entry['question'] + " " + entry['answer']
    tokenized_inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        padding=True,
        max_length=2048
    )
    return tokenized_inputs




```
  
  
  
   
   
  
Let’s see what this code does:  
Let’s see what this code does:  
* This function takes in an entry that contains key-value pairs for *“instruction”* and *“response”*.  
* This function takes in an entry that contains key-value pairs for *“instruction”* and *“response”*.  
* The *instruction *and *response *are concatenated together and the resultant string is stored in *text*.  
* The *instruction *and *response *are concatenated together and the resultant string is stored in *text*.  
* Then we use the tokenizer to convert this string into tokens while keeping *padding *and *truncation True *to take care of strings of different sizes. Note that we have also specified *max_length *to be 2048 as that is the context window limit of our LLM.  
* Then we use the tokenizer to convert this string into tokens while keeping *padding *and *truncation True *to take care of strings of different sizes. Note that we have also specified *max_length *to be 2048 as that is the context window limit of our LLM.  
* Finally, this function returns a list called *tokenized_inputs *which contains the token lists and attention masks for the given string.  
* Finally, this function returns a list called *tokenized_inputs *which contains the token lists and attention masks for the given string.  
  
* To apply this function on all entries in the data set, we converted *list_of_entries* into a Pandas DataFrame and then used the *map()* method to get the tokenized dataset.  
* To apply this function on all entries in the data set, we converted *list_of_entries* into a Pandas DataFrame and then used the *map()* method to get the tokenized dataset.  
  
* There is one last thing that we need to do before finalizing our data set. As the LLM looks for the tokens in a column with the name *labels, *we created a new column called *'labels' *by simply copying the *input_ids* column.  
* There is one last thing that we need to do before finalizing our data set. As the LLM looks for the tokens in a column with the name *labels, *we created a new column called *'labels' *by simply copying the *input_ids* column.  
  
* After this, we performed a train-test split and reached the end of the data preparation step.  
* After this, we performed a train-test split and reached the end of the data preparation step.  
  
* Next, we can move on to the next step which is Training and Inference.  
* Next, we can move on to the next step which is Training and Inference.  
  
*    
*    
  
* **Training and Inference**  
* **Training and Inference**  
  
* To start with this stage of the project, we first wrote a function called *inference()* that performs inference given the *text*, *model*, *tokenizer*, *max_input_tokens*, and *max_output_tokens*.  
* To start with this stage of the project, we first wrote a function called *inference()* that performs inference given the *text*, *model*, *tokenizer*, *max_input_tokens*, and *max_output_tokens*.  
  
* At a high level, this function performs the following steps:  
* At a high level, this function performs the following steps:  
* Tokenize the input text  
* Tokenize the input text  
* Create an attention mask  
* Create an attention mask  
* Assign the device to be used for the computation  
* Assign the device to be used for the computation  
* Perform inference  
* Perform inference  
* Decode the output tokens  
* Decode the output tokens  
* Remove the initial prompt.   
* Remove the initial prompt.   
  
* You can find proper commentary for each line in this function in the notebook.  
* You can find proper commentary for each line in this function in the notebook.  
  
* Before performing fine-tuning, we performed inference on the model on a string and received the following output.  
* Before performing fine-tuning, we performed inference on the model on a string and received the following output.  
  
*    
*    
  
* **Input**  
* **Input**  
```
Question input (test): i need assistance with canceling purchase {{Order Number}}




```
  
  
  
   
   
  
**Correct Output from the data set**  
**Correct Output from the data set**  
```
I've grasped that you're seeking assistance with canceling purchase {{Order Number}}, and I'm here to guide you through the process. Cancelling a purchase is important, and we want to ensure a smooth experience for you. Here's what you need to do:

1. Access Your Account: Start by logging in to our {{Online Company Portal Info}}.
2. Locate Your Purchase: Once logged in, navigate to the '{{Online Order Interaction}}' or '{{Online Order Interaction}}' section.
3. Identify the Purchase: Look for the purchase associated with the order number {{Order Number}}. Click on it for more details.
4. Initiate the Cancellation: You'll find the option to '{{Online Order Interaction}}' linked with your purchase. Please select that.
5. Complete the Process: Our system may prompt you for additional information or feedback to finalize the cancellation.

If you encounter any difficulties or have any questions during the process, our dedicated team is available during {{Customer Support Hours}} at {{Customer Support Phone Number}} or through the Live Chat feature on our website at {{Website URL}}. We value your satisfaction and are committed to providing you the assistance you need.




```
  
  
  
   
   
  
**Model’s output**  
**Model’s output**  
```
Model's answer: 


The following is a list of items that you can purchase from the following items:

1. The item you purchase from the following items:

1. The item you purchase from the following items:

1. The item you purchase from the following items:

1. The item you purchase from the following items:

1. The item you purchase from the following items:

1. The item




```
  
  
  
   
   
  
Here you can clearly see that the model’s output is not very good.  
Here you can clearly see that the model’s output is not very good.  
  
   
   
  
To train the model, we initialised the *TrainingArguments()* object with appropriate values and performed training using the code given below. The training arguments in this case require some knowledge of training neural networks and is out of scope in this discussion.  
To train the model, we initialised the *TrainingArguments()* object with appropriate values and performed training using the code given below. The training arguments in this case require some knowledge of training neural networks and is out of scope in this discussion.  
```
trainer = Trainer(
    model=base_model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

training_output = trainer.train()




```
  
  
  
   
   
  
You can see from the logs of the training process that the training and validation loss are decreasing more or less consistently, which means that the model is learning.  
You can see from the logs of the training process that the training and validation loss are decreasing more or less consistently, which means that the model is learning.  
  
   
   
  
   
   
  
We have trained it for a small number of epochs due to the limitations posed by the hardware. But we can still see an improvement in the quality of the output. Let’s look at the output of the newly fine-tuned model.  
We have trained it for a small number of epochs due to the limitations posed by the hardware. But we can still see an improvement in the quality of the output. Let’s look at the output of the newly fine-tuned model.  
  
 **Input**  
 **Input**  
```
Question input (test): i need assistance with canceling purchase {{Order Number}}




```
  
  
  
   
   
  
**Correct Output from the data set**  
**Correct Output from the data set**  
```
I've grasped that you're seeking assistance with canceling purchase {{Order Number}}, and I'm here to guide you through the process. Cancelling a purchase is important, and we want to ensure a smooth experience for you. Here's what you need to do:

1. Access Your Account: Start by logging in to our {{Online Company Portal Info}}.
2. Locate Your Purchase: Once logged in, navigate to the '{{Online Order Interaction}}' or '{{Online Order Interaction}}' section.
3. Identify the Purchase: Look for the purchase associated with the order number {{Order Number}}. Click on it for more details.
4. Initiate the Cancellation: You'll find the option to '{{Online Order Interaction}}' linked with your purchase. Please select that.
5. Complete the Process: Our system may prompt you for additional information or feedback to finalize the cancellation.

If you encounter any difficulties or have any questions during the process, our dedicated team is available during {{Customer Support Hours}} at {{Customer Support Phone Number}} or through the Live Chat feature on our website at {{Website URL}}. We value your satisfaction and are committed to providing you the assistance you need.




```
  
  
  
   
   
  
**Model’s output**  
**Model’s output**  
```
I'm here to assist you with canceling purchase {{Order Number}}. Please follow these steps:

1. Sign in to Your Account: Access our platform by logging into your {{Online Company Portal Info}} using your credentials.
2. Navigate to the '{{Online Order Interaction}}' or '{{Online Order Interaction}}' section.
3. Navigate to the '{{Online Order Interaction}}' or '{{Online Order Interaction}}' section




```
  
  
  
   
   
  
This is not the best output you can expect from a fine-tuned LLM. But considering the size of the *pythia*-70m model and the small number of epochs for which we have trained the model, this is pretty good. Recall that we also subsetted our data set.   
This is not the best output you can expect from a fine-tuned LLM. But considering the size of the *pythia*-70m model and the small number of epochs for which we have trained the model, this is pretty good. Recall that we also subsetted our data set.   
  
   
   
  
With better compute resources, a better model, a data set, and a larger budget that will allow us to train models longer we will definitely get better results.  
With better compute resources, a better model, a data set, and a larger budget that will allow us to train models longer we will definitely get better results.  
  
   
   
  
In the next segment, you will learn about some improvements that you can do to your fine-tuning code.  
In the next segment, you will learn about some improvements that you can do to your fine-tuning code.  
  
  
  
**Further Improvements**     
**Further Improvements**     
  
In this segment, we will discuss some strategies that we can consider to improve the efficiency of our fine-tuning code. Specifically, we will discuss parameter efficient fine-tuning (PEFT).  
In this segment, we will discuss some strategies that we can consider to improve the efficiency of our fine-tuning code. Specifically, we will discuss parameter efficient fine-tuning (PEFT).  
  
   
   
  
PEFT refers to a set of techniques that reduce the resources required in the fine-tuning process. The two main techniques that come under this umbrella are Low-Rank Adaptation (LoRA) and Quantized Low-Rank Adaptation (qLoRA).  
PEFT refers to a set of techniques that reduce the resources required in the fine-tuning process. The two main techniques that come under this umbrella are Low-Rank Adaptation (LoRA) and Quantized Low-Rank Adaptation (qLoRA).  
  
   
   
  
The innovation that produces the massive efficiencies seen in the PEFT techniques takes advantage of the fact that matrices that represent the change in the network weights during fine-tuning have a low “rank”. Here, “rank” is the concept from linear algebra which refers to the number of linearly independent rows in a matrix. Due to the low rank, we can decompose the large matrix that represents change in weights to smaller matrices and hence reduce the number of trainable parameters drastically.  
The innovation that produces the massive efficiencies seen in the PEFT techniques takes advantage of the fact that matrices that represent the change in the network weights during fine-tuning have a low “rank”. Here, “rank” is the concept from linear algebra which refers to the number of linearly independent rows in a matrix. Due to the low rank, we can decompose the large matrix that represents change in weights to smaller matrices and hence reduce the number of trainable parameters drastically.  
  
   
   
  
You can learn more about these methods by following the links given below:  
You can learn more about these methods by following the links given below:  
1. ++[Efficient Fine-Tuning with LoRA by Databricks](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)++  
2. ++[Efficient Fine-Tuning with LoRA by Databricks](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)++  
3. ++[Low-rank Adaptation of LLMs by Chris Alexiuk - Part 1](https://www.youtube.com/watch?v=dA-NhCtrrVE)++  
4. ++[Low-rank Adaptation of LLMs by Chris Alexiuk - Part 1](https://www.youtube.com/watch?v=dA-NhCtrrVE)++  
5. ++[Low-rank Adaptation of LLMs by Chris Alexiuk - Part 2](https://www.youtube.com/watch?v=iYr1xZn26R8)++  
6. ++[Low-rank Adaptation of LLMs by Chris Alexiuk - Part 2](https://www.youtube.com/watch?v=iYr1xZn26R8)++  
  
7.    
8.    
  
9. You can also find below the notebook that contains code that uses LoRA to fine-tune the *pythia-70m* model on the same customer support data set by Bitext.  ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  This brings us to the end of our discussion about further improvements that can be made to improve the efficiency of our fine-tuning algorithm. In the next segment, you will summarise your learnings from this session.   
10. You can also find below the notebook that contains code that uses LoRA to fine-tune the *pythia-70m* model on the same customer support data set by Bitext.  ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  This brings us to the end of our discussion about further improvements that can be made to improve the efficiency of our fine-tuning algorithm. In the next segment, you will summarise your learnings from this session.   
  
11. Reference Links  
12. Reference Links  
  
13. ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  
14. ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  
15. ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  
16. ++[Fine-tuning LoRA Code](https://cdn.upgrad.com/uploads/production/9a1795ca-f565-4e65-aaa0-1da36c40d7b1/upGrad_FINAL_Fine_Tuning_LoRA_Code+(1).ipynb)++  
  
  
**Session Summary**    
**Session Summary**    
  
In this segment, you will summarise your learnings from this session. In this session, you:  
In this segment, you will summarise your learnings from this session. In this session, you:  
* Explored the process of training large language models  
* Explored the process of training large language models  
* Emphasised the necessity of fine-tuning LLMs  
* Emphasised the necessity of fine-tuning LLMs  
* Conducted complete fine-tuning on an LLM  
* Conducted complete fine-tuning on an LLM  
* Explored the theory and implementation of Low Rank Adaptation (LoRA) fine-tuning (Optional)  
* Explored the theory and implementation of Low Rank Adaptation (LoRA) fine-tuning (Optional)  
  
*    
*    
  
* You are now ready to fine-tune LLMs for different use cases. In the next segment, you will attempt the graded assessments.  
* You are now ready to fine-tune LLMs for different use cases. In the next segment, you will attempt the graded assessments.  
