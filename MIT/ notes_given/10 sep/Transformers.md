  
# Transformers  
  
## Outline  
  
1. Transformers high-level intuition and architecture  
2. Attention mechanism  
  
3. Multi-head attention  
  
4. (Applications)  
  
#   
# Transformers high-level intuition and architecture  
  
  
To date, the cleverest thinker of all time was  
  
To date, the cle **ve** rest thinker of **all** time was  
##   
## Word Embeddings  
  
### Overview  
  
Word embeddings are vector representations of words used in machine learning models. Count-based methods, like co-occurrence counts and PPMI, capture word meaning by analyzing word contexts in a corpus. Word2Vec, a prediction-based method, learns word vectors by training them to predict surrounding words in a sliding window context.  
  
Word2Vec is trained using gradient descent, updating parameters for each central word and its context words. T**he Skip-Gram model predicts context words from a central word, while the CBOW model predicts the central word from context vectors. Negative sampling is used to improve training efficiency by updating only a subset of context vectors.**  
  
The text discusses word embeddings, focusing on Word2Vec and GloVe models. It compares their approaches, highlighting Word2Vec’s skip-gram with negative sampling and GloVe’s combination of count-based and prediction methods. The text also explores evaluation methods for word embeddings, including intrinsic evaluation (e.g., word similarity and analogy tasks) and extrinsic evaluation (e.g., real-world tasks like text classification).  
  
The text explores the geometry of learned semantic spaces and the possibility of a linear mapping between languages. It also discusses the importance of context words in Word2Vec training and how subword information can be incorporated into embeddings. Additionally, it touches on detecting semantic change in words across different text corpora.  
  

| Representation | Description | Pros | Cons |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------- |
| One-hot Vectors | Words represented as vectors with a 1 at the index of the word and 0s elsewhere. To account for unknown words (the ones which are not in the vocabulary), usually a vocabulary contains a special token UNK. Alternatively, unknown tokens can be ignored or assigned a zero vector. Like 1 added in Naive bayes to remove 0. LDA Algorithm | Simple representation of categorical features. | High dimensionality for large vocabularies, do not capture word meanings. |
  
  
  
### ++Latent Semantic Analysis++  
  
  
* **LSA Definition:** A topic model that analyzes a collection of documents and uses cosine similarity between document vectors to measure document similarity.  
* **LSA Application:** Applies Singular Value Decomposition (SVD) to a term-document matrix where elements are computed using various weighting schemes like co-occurrence or tf-idf.  
* **[LSA Visualization:](https://en.wikipedia.org/wiki/Latent_semantic_analysis)**[ Wikipedia page](https://en.wikipedia.org/wiki/Latent_semantic_analysis) provides an animation of the topic detection process within a document-word matrix.  
  
  
  
  
  
### Distributional Semantics  
  
* Context Window Method**:** Defines contexts as each word in an L-sized window and uses word-context co-occurrence to generate embeddings.  
* PPMI Method**:** Uses Positive Pointwise Mutual Information (PPMI) to measure the association between word and context, considered state-of-the-art for pre-neural models.  
* **LSA for Document[ Analysis](http://lsa.colorado.edu/papers/JASIS.lsi.90.pdf):** Analyzes a collection of documents to generate document vectors, allowing for document similarity measurement using cosine similarity.  
  
  
  
![To date, the cleverest thinker of all time was](Attachments/323F717D-7763-42CC-90BF-FA4C619FDD35.png)  
  
### Sentences Example  
  
Mole 3 types  
American shrew **mole**->  Animal  
One **mole **of carbon dioxide-> Atom  
Take a biopsy of the **mole**-> Biological Term  
### Embedding or called tokenization:  
  
![tokenization.mp4](Attachments/A6A954D5-51BA-4E79-A824-DD42510ECE42.mp4)  
![To date, the cleverest thinker of all time was](Attachments/4E663704-C6AC-48BE-88F4-F60B01A6EB96.png)  
n*d embeddings  
  
**Loss**  
Cross Entropy loss-> Logistic Classification loss-> Cross Entropy, #todo start implementing.. or nothing will stick in head..-> Log loss.. the more complex the problem gets.. simpler meanings will be lost.. start implementing smaller.. then larger.. then see bottlenecks.. hyperparameter tuning taught blindly.. just told.. never said alternative way..   
  
  
  
###   
  
  
  
**Do nat capture context(Meaning)-> some form of embedding**  
![American shrew mole](Attachments/85982205-B7D3-4F19-8B5D-720519168B8C.png)  
  
  
  
  
## Attention  
  
**TO CAPTURE SEMANTICS**  
  
****Using many repetitions of attention layer and multi layer perceptron in parallel.. ****  
  
  
  
Bottleneck is? Iterations is 1 second? Cannot answer, have not understood...  
  
![auto-regressive.mp4](Attachments/7C89BC89-26C4-4635-8BCE-A567267279A5.mp4)  
  
  
  
  
Termed AutoRegressive  
  
  
![One mole of curba dimile](Attachments/2D71212A-3C86-4629-903C-26A05DD35348.png)  
  
###  Weight Adjustment by attention mechanism  
![Attention High Level Parallel Overview.mov](Attachments/AAA54C53-E30E-4A5F-B02E-0FC050B512D1.mov)  
  
Embeddings getting closer example  
  
![attention-drag1.mp4](Attachments/AAD8B23B-9E1C-4EDA-92C4-88F827C3D844.mp4)  
![RECURRENT NEURAL NETWORK](Attachments/0205B165-B294-4E61-B6FC-A77FF5C970A8.png)  
  
  
**Transformer “learned embedding W”**  
* **W (token embedding matrix)** is a **learned lookup table**: token id → **vector**.  
* It’s **static per token** (same token → same vector before context).  
* Then attention + layers turn it into **contextual vectors**.  
  
  
**RNN hidden state (hₜ)**  
* **hₜ is a contextual embedding**, produced **dynamically** each time step:  
    * **hₜ = f(hₜ₋₁, xₜ; θ)** (depends on history + current input).  
* It’s **not a parameter** like W; it’s a **value computed during the forward pass**. same as feedforward W but learnt  
* It acts as the model’s **running summary** (“memory”), which your deck describes as output being fed into the next step.  
**So what’s the equivalent of W in an RNN?**  
* The **input embedding matrix** (often also called **Wₑ**) that maps tokens to vectors **before** the RNN.  
* The **hidden state** is closer to a Transformer layer’s **hidden states** (contextual embeddings), not the embedding table.  
  
*   
* **Sequence → embeddings (before activation)**  
    * Discrete inputs (tokens, steps) are first mapped using a **learned embedding matrix Wₑ**.  
    * This is a **linear lookup/projection**, no non‑linearity yet.  
* **What this embedding represents**  
    * A **dense vector** encoding input meaning/features.  
    * Same role as **token embeddings in Transformers**.  
* **Then activation happens**  
    * The embedded input is combined with the **previous hidden state** using learned weights.  
    * Only **after this linear combination** do we apply **tanh / ReLU / gates**.  
* **Key distinction**  
    * **Embedding Wₑ** → *learned parameters*, static per token  
    * **Hidden state hₜ** → *computed embedding*, dynamic and contextual  
**One‑line summary:**  
**One‑line summary:**  
RNNs also learn **embeddings first**, then use activations to turn them into **context‑aware hidden states**.  
  
* **What the feedback loop is**  
    * The **previous hidden state (hₜ₋₁)** is fed back as **input** to the next step.  
    * This makes the model **stateful** across time.  
* **Where it sits in the flow**  
    * **Sequence → embedding (Wₑxₜ)**  
    * **Embedding + previous hidden state** → linear transform  
    * **Activation / gates** → new hidden state **hₜ**  
    * **hₜ loops back** to the next time step.  
* **What it achieves**  
    * Creates **memory** without storing the whole sequence.  
    * Allows later outputs to depend on **earlier inputs**.  
* **Key distinction**  
    * **Embedding Wₑ**: learned, static parameters  
    * **Hidden state hₜ**: dynamic embedding **carried forward via feedback**  
**One‑line summary:**  
The feedback loop turns per‑step embeddings into a **context‑aware sequence representation**  
  
## Transformer blocks  
  
  
![cleverest](Attachments/7DA639BF-3AFA-4D99-9942-B2B62DFBAAA5.png)  
  
Each token is contributing in parallel, and getting transformed by every transformer block   
![input embedding](Attachments/6D26C1E8-EF15-4D44-A276-FEE16F072C0A.png)  
  
n tokens-> input embedding in R^d space  
n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
  
##   
![output embedding](Attachments/17407970-ED28-407F-9F89-8F0312ECE68B.png)  
  
  
  
  
  
  
## Inside Transformer blocks  
  
Contains attention layer and (neural network or multi layer perceptron).. why terming is different here?  
![cleverest](Attachments/26350385-8B04-44BF-88F7-A176BE323EB5.png)  
MLP-> Neuron Weights <- Loss->delta(L)  
q,k,v embedding of each xi, is learnt and finally represented as Wq,Wk,Wv-> Topics Left how it is learnt..  
Attention Layer-> Wq,Wk,Wv,W0->W(query),W(key),W(value),W0(Bias)->(W)->☝️ adjusted by cross entropy loss  
  
  
### ATTENTION Mechanism in 1 Transformer block  
  
  
  
  
**Projection?**  
![attention layer](Attachments/2346662C-465D-4D5C-B8A2-8C1E19901B24.png)  
  
  
  
![attention layer](Attachments/F5A9AD33-4052-497C-ACC2-0362EC61599D.png)  
  
Most important bits in an attention layer:  
1. (query, key, value) projection  
2. attention mechanism   
3. x->x1...xd..    
4. (q,k,v)  embeddings projection->  
5. Learnt weights represented by-> Wq,WkWv  
6. ![21](Attachments/441FD3F3-849C-4B04-BEC4-CB56A3BDC21C.png)  
  
### Attention Mechanism  
  
x->xi,  
Embeddings (q,k,v)-> Learnt weights Wq,Wk,Wv  
  
![1. (query, key, value) projection](Attachments/840563D3-45F5-4C0B-A2A9-43198294882F.png)  
  
  
  
  
![Screen Recording 2026-03-26 at 7.24.00 AM.mov](Attachments/04177EAE-7AB3-4B9C-8D9E-E2BA2829CC26.mov)  
  
  
  
W(query)-> Prompt or input-> a query to be perfomed  
W(key)-> Like dictionary in python, to be compared  
  
#todo 2 days for NLP, 3 days for GENAI or less including transformers,stable diffusion, vision transformers everything.. learn this first, optional topics-> reinforcement learning, building llm from scratch will also be asked.. 1 more evaluating search systems.. RAG.. Covered..  
W(value)->to contribute-> not output..  
![1. (query, key, value) projection](Attachments/0DCC9915-CFF7-42D4-A55A-054F8ACABF86.png)  
  
  
Wq,Wk,Wv are learnt projections in attention layer  
  
![1. (query, key, value) projection](Attachments/64EFF587-7A81-48ED-A5B1-6C4159BB648D.png)  
  
  
### Why learning these projections  
  
Wq-> Learns How to ask (or prompt)  
Wk-> Learns How to listen (or compared)  
Wv -> Learns How to speak (or contribute)  
  
  
![1. (query, key, value) projection](Attachments/A87103E2-5648-438A-A229-6D2C6CB5DF85.png)  
![1. (query, key, value) projection](Attachments/3B06C4B7-9068-4326-8FB8-D29C94DFFAF4.png)  
  
  
  
  
  
  
![1. (query, key, value) projection](Attachments/7E292632-C237-4E55-8BCE-F04399C492E5.png)  
*  W q,Wk,Wv->R(d*dk), Rd-> Input dimensions,dk->key's dimensions-> which is to be compared..  
*   
* project the d-dimensional word-embedding space to dk-dimensional (qkv) space (typically dk < d) in what form? mathematically..? dk<d-> Because of noise in words or words like the, is or common words..  
  
  
![1. (query, key, value) projection](Attachments/ADD67446-AD6F-4BD0-943E-0D8483E52B3D.png)  
Wq,Wk,Wv  
  
each (q,k,v) transformed contributes to output embedding  
q¡ = Wq†x¡ (Transpose) for i, qi query->Wq(T) Learnt Query multplied by xi for all i , similar weight sharing for keys and values  
  
n tokens-> input embedding in R^d space  
n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
  
**parallel and structurally identical processing..**  
  
![2. Attention mechanism](Attachments/FD164DDE-A479-4BAD-BDE2-53879FDA8AEE.png)  
  
  
(q,k,v)->z-> projected by attention mechanism, which is context aware, a mixture of everyone's values, weighted by relevance...  
   
  
# Attention Mechanism  
![22 date](Attachments/9688EAEF-F2F5-4825-A918-29285ADDAD61.png)  
  
  
![I2 date](Attachments/A942B2E1-AE7D-456E-9D8A-B26B6DF81A15.png)  
  
  
## Attention Head  
## ![Attention head](Attachments/988533F0-5FAA-42F6-B5C9-C9142188E021.png)  
  
  
How, Representation->  
1. Compact Matrix form  
2. Each z is transformed into a row,  
3. By stacking each individual vector  
![Attention head - compact matrix form](Attachments/FD5A2CFC-A960-4082-9FC0-F4830F72C6D5.png)  
![Attention head - compact matrix form](Attachments/D32C272B-2BED-48FF-B329-C92CC1A25BB2.png)  
![attention mechanism](Attachments/32781D9F-3AA5-42EA-AC77-41692CA6C249.png)  
![Screenshot 2026-03-28 at 12.53.54 PM.png](Attachments/719AE9BD-3C8E-40BA-800B-C6603076E99D.png)  
![Screenshot 2026-03-28 at 12.55.38 PM.png](Attachments/F9E8DD2C-6850-458E-ACA0-7243C74EE4ED.png)  
  
  
# Multi Head Attention  
  
Each x¡ contributes to each transformer block/layer parallelly..   
  
  
![attention mechanism](Attachments/FDEEABA1-4854-4C34-8CB2-5931CBE362DF.png)  
![Multi-head Attention](Attachments/ED532221-5687-4B4A-9E48-C6888A4ED34D.png)  
![Multi-head Attention](Attachments/B031E5B9-36F7-4FF6-A754-21ACC196702D.png)  
![attention mechanism](Attachments/37B88830-7AEF-4F95-99E2-5B8CF14C14AA.png)  
  
  
![Attention head - compact matrix form](Attachments/02836336-23DE-4880-A87D-7A84ED6847F5.png)  
  
#todo Hidden State would mean-> Memory, means-> Embedded value, which is not used like in RNN?  
**** A-> Attention formula softmax(QK†/√dk)-> ****  
****Z-> A*V-> Called Attention Head..****  
![Multi-head Attention](Attachments/E59E947F-7F80-41F7-A2FF-6D4231CB8B10.png)  
![Multi-head Attention](Attachments/B04D53E4-2614-4F0D-86B0-B0B085F9C0D9.png)  
![Shape Example](Attachments/DEDF10B7-0D74-4418-87C5-863F41A51FCD.png)  
![Some practical techniques commonly needed when training auto-regressive transfor](Attachments/A4CCF5FB-8FE8-4969-9B88-E2D6BF816C7B.png)  
  
  
# Upgrad  
  
rofessor Raghuram then explained the steps in building such as the autofill tool:  
1. **Extract data:** Extract all sentences from the data set that begin with "not well, working from."  
2. **Identify common completions:** Identify the most common completions in these sentences. For example, "home" appears 100 times, "room" appears 50 times, and a typo "H" appears 6 times.  
3. **Build a probability model:** Calculate the probability of each word being the next one in the sequence.  
4. **Random sampling:** Use this probability distribution to predict the next word. Most of the time, "home" will be the predicted word, but sometimes, "room" or "H" may also appear.  
However, this simple statistical model has limitations. For example, if someone types "I'm not well, operating from," the model will not predict "home" because it has not seen "operating from" before. The model lacks semantic understanding and, so, will be unable to recognize that “operating” is similar to "working."  
   
To overcome these limitations, researchers have developed more advanced models that better understand semantics and context. These advancements eventually led to the creation of powerful models, which excel in handling complex language tasks and understanding context.  
  
Welcome to the session titled “**Encoder-Decoder Architecture**.”  
   
In the previous session, you explored different NLP models, noting their limitations in capturing context-specific meanings, which can lead to issues in tasks such as sentiment analysis. This session builds on that by introducing more advanced models that are designed to better capture contextual information.  
   
The Encoder-Decoder architecture is a powerful model used in natural language processing to transform sequences, such as sentences, from one form to another. It is especially effective for tasks requiring context preservation, such as language translation and text summarization. By encoding input data into a fixed representation, the model can generate meaningful output sequences, even with complex and long sentences.  
   
# Encoder Decoder  
  
In this session, you will:  
* Explore the encoder-decoder architecture, a popular model for capturing contextual information in sentences  
* Implement an encoder-decoder model for converting a sentence from source language to target language  
* Understand the challenges associated with standard encoder-decoder models when handling long sentences  
*  and how we can improve the model's performance  
* Explore graphical illustrations to understand how the proposed model works  
* Understand the mathematics behind the process and learn how to train an encoder-decoder model with attention  
* Implement encoder-decoder model with attention for converting a sentence from source language to target language  
   
As explained in the video, the encoder-decoder architecture is a popular framework for sequence-to-sequence tasks such as sentiment analysis. As the name suggests, the encoder-decoder architecture consists of two components - the Encoder and Decoder. The Encoder converts a sentence into a vector representation. The decoder uses this vector to perform the desired task, such as sentiment classification or translation.  
   
This architecture uses a recurrent neural network (RNN) to handle context and generate accurate assessments. An RNN processes the context of a sentence sequentially. If you are not familiar with RNNs, visit ++[this link](https://www.ibm.com/topics/recurrent-neural-networks)++.  
 The professor then explained how this model works with the help of the example sentence “The movie is good.”  
  
   
  
RNN-> Context passed sequentially-> (Embedding)-> Before applying activation fn..->   
  
As explained in the video, the encoder-decoder architecture is a popular framework for sequence-to-sequence tasks such as sentiment analysis. As the name suggests, the encoder-decoder architecture consists of two components - the Encoder and Decoder. The Encoder converts a sentence into a vector representation. The decoder uses this vector to perform the desired task, such as sentiment classification or translation.  
   
This architecture uses a recurrent neural network (RNN) to handle context and generate accurate assessments. An RNN processes the context of a sentence sequentially. If you are not familiar with RNNs, visit ++[this link](https://www.ibm.com/topics/recurrent-neural-networks)++.  
 The professor then explained how this model works with the help of the example sentence “The movie is good.”  
  
[Rnn.pdf](Attachments/8ED1479F-DEC1-42BE-B8DC-978D84490DB2.pdf)  
![context](Attachments/66BFE574-934B-47B3-818D-DBE1D833FFB5.png)  
  
1. In the **Encoder**, RNN processes the word “The,” performs matrix operations, and generates a context.   
2. This context is passed along with the next word "movie" to the next RNN cell.   
3. Each RNN cell takes the previous context and the current word to generate a new context.   
4. This process continues for each word in the sentence, with all RNN cells sharing the same weights, allowing the model to handle sentences of any length.  
5. The final output is a rich vector representation of the sentence, capturing its context and meaning.  
6. This vector is then fed into the **Decoder**, which uses a feed-forward neural network to classify sentiment, such as positive or negative.  
Initially, the model might not be accurate, but through training and adjusting weights based on feedback, it learns to improve its predictions. While RNNs can struggle with long sentences because recent words might overshadow earlier ones, more advanced architectures such as LSTMs or bidirectional LSTMs can help mitigate this issue.  
 This encoder-decoder setup provides a more dynamic and context-sensitive representation of words than the static representations used in Word2Vec, enhancing performance in natural language tasks.  
  
for nlp->  
 encoder encodes the sentence into a context  
and decoder-> uses the context and generates target sentence  
