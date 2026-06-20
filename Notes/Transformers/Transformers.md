  
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
  
  
  
![To date, the cleverest thinker of all time was](Attachments/2C06DDB1-8720-49FA-91A1-56ADCEFD8503.png)  
  
### Sentences Example  
  
Mole 3 types  
American shrew **mole**->  Animal  
One **mole **of carbon dioxide-> Atom  
Take a biopsy of the **mole**-> Biological Term  
### Embedding or called tokenization:  
  
![tokenization.mp4](Attachments/B15198FE-9C10-4D9A-8573-25C783FF2DA4.mp4)  
![To date, the cleverest thinker of all time was](Attachments/AF5EEBBC-C9B1-495E-A29A-A1D7A921F56E.png)  
n*d embeddings  
  
**Loss**  
Cross Entropy loss-> Logistic Classification loss-> Cross Entropy, #todo start implementing.. or nothing will stick in head..-> Log loss.. the more complex the problem gets.. simpler meanings will be lost.. start implementing smaller.. then larger.. then see bottlenecks.. hyperparameter tuning taught blindly.. just told.. never said alternative way..   
  
  
  
###   
  
  
  
**Do nat capture context(Meaning)-> some form of embedding**  
![American shrew mole](Attachments/409D46C4-362C-45FF-A09D-EF2702042CEA.png)  
  
  
  
  
## Attention  
  
**TO CAPTURE SEMANTICS**  
  
****Using many repetitions of attention layer and multi layer perceptron in parallel.. ****  
  
  
  
Bottleneck is? Iterations is 1 second? Cannot answer, have not understood...  
  
![auto-regressive.mp4](Attachments/DEED3D16-3394-4B1E-9DE4-C38BA66773D5.mp4)  
  
  
  
  
Termed AutoRegressive  
  
  
![One mole of curba dimile](Attachments/53960833-4579-4A03-8745-A4875CCC95EE.png)  
  
###  Weight Adjustment by attention mechanism  
![Attention High Level Parallel Overview.mov](Attachments/87CA6475-FC93-4D10-9BBD-189B474F3DEE.mov)  
  
Embeddings getting closer example  
  
![attention-drag1.mp4](Attachments/144734A9-52E7-41EE-8F88-D83608E37E1D.mp4)  
  
  
## Transformer blocks  
  
  
![cleverest](Attachments/8E52D029-5252-4715-BCFF-E4CFBABB3B13.png)  
  
Each token is contributing in parallel, and getting transformed by every transformer block   
![input embedding](Attachments/28E706DF-EDB3-4A5E-813D-CC754FD8C82D.png)  
  
n tokens-> input embedding in R^d space  
n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
  
##   
![output embedding](Attachments/148C62D5-F7AB-49C3-83F7-90F5BF7E8A04.png)  
  
  
  
  
  
  
## Inside Transformer blocks  
  
Contains attention layer and (neural network or multi layer perceptron).. why terming is different here?  
![cleverest](Attachments/C1F2C9FF-F045-4025-9F6E-B9C28CDA7DA7.png)  
MLP-> Neuron Weights <- Loss->delta(L)  
q,k,v embedding of each xi, is learnt and finally represented as Wq,Wk,Wv-> Topics Left how it is learnt..  
Attention Layer-> Wq,Wk,Wv,W0->W(query),W(key),W(value),W0(Bias)->(W)->☝️ adjusted by cross entropy loss  
  
  
### ATTENTION Mechanism in 1 Transformer block  
  
  
  
  
**Projection?**  
![attention layer](Attachments/7280E371-7DE1-4862-BB01-EDA04AB36B58.png)  
  
  
  
![attention layer](Attachments/988FBF3F-77BB-41C1-995C-A74F3F8127AF.png)  
  
Most important bits in an attention layer:  
1. (query, key, value) projection  
2. attention mechanism   
3. x->x1...xd..    
4. (q,k,v)  embeddings projection->  
5. Learnt weights represented by-> Wq,WkWv  
6. ![21](Attachments/3338BB0B-3BDF-4B66-9435-F29BEF328DB9.png)  
  
### Attention Mechanism  
  
x->xi,  
Embeddings (q,k,v)-> Learnt weights Wq,Wk,Wv  
  
![1. (query, key, value) projection](Attachments/42341004-4219-4ECC-85A9-6D4680C5FDBA.png)  
  
  
  
  
![Screen Recording 2026-03-26 at 7.24.00 AM.mov](Attachments/B7FBEC0B-EAEF-44C3-B341-97DB14D97AC1.mov)  
  
  
  
W(query)-> Prompt or input-> a query to be perfomed  
W(key)-> Like dictionary in python, to be compared  
  
#todo 2 days for NLP, 3 days for GENAI or less including transformers,stable diffusion, vision transformers everything.. learn this first, optional topics-> reinforcement learning, building llm from scratch will also be asked.. 1 more evaluating search systems.. RAG.. Covered..  
W(value)->to contribute-> not output..  
![1. (query, key, value) projection](Attachments/72EBB05E-504B-43AB-85DF-5C8B4BE7190F.png)  
  
  
Wq,Wk,Wv are learnt projections in attention layer  
  
![1. (query, key, value) projection](Attachments/D180930C-8EE9-42CD-8D8C-EE178E516844.png)  
  
  
### Why learning these projections  
  
Wq-> Learns How to ask (or prompt)  
Wk-> Learns How to listen (or compared)  
Wv -> Learns How to speak (or contribute)  
  
  
![1. (query, key, value) projection](Attachments/FEEB6121-6B8B-4AA3-AC2E-DAD7A0DF9D14.png)  
![1. (query, key, value) projection](Attachments/1BDE38E0-5682-4C9D-8958-CCF824C024AD.png)  
  
  
  
  
  
  
![1. (query, key, value) projection](Attachments/08984D2C-A17B-448E-9795-ED93DED38CC9.png)  
*  W q,Wk,Wv->R(d*dk), Rd-> Input dimensions,dk->key's dimensions-> which is to be compared..  
*   
* project the d-dimensional word-embedding space to dk-dimensional (qkv) space (typically dk < d) in what form? mathematically..? dk<d-> Because of noise in words or words like the, is or common words..  
  
  
![1. (query, key, value) projection](Attachments/CA6E5703-F3F4-45FB-8247-C5677D79B1D4.png)  
Wq,Wk,Wv  
  
each (q,k,v) transformed contributes to output embedding  
q¡ = Wq†x¡ (Transpose) for i, qi query->Wq(T) Learnt Query multplied by xi for all i , similar weight sharing for keys and values  
  
n tokens-> input embedding in R^d space  
n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
  
**parallel and structurally identical processing..**  
  
![2. Attention mechanism](Attachments/33C64F42-85EB-4B8C-8CBA-B625C354F8EC.png)  
  
  
(q,k,v)->z-> projected by attention mechanism, which is context aware, a mixture of everyone's values, weighted by relevance...  
   
  
# Attention Mechanism  
![22 date](Attachments/2B91A4B1-960C-4F1F-B1C2-0D62A5916CA4.png)  
  
  
![I2 date](Attachments/C582C44D-C6EC-4AFD-B19F-17B473B712B0.png)  
  
  
## Attention Head  
## ![Attention head](Attachments/DF3C2BD8-9DF1-49E2-B9CE-9D6233507975.png)  
  
  
How, Representation->  
1. Compact Matrix form  
2. Each z is transformed into a row,  
3. By stacking each individual vector  
![Attention head - compact matrix form](Attachments/A60F3D27-D9F7-46BF-9DC8-AB868DB72550.png)  
![Attention head - compact matrix form](Attachments/598A4037-B3A2-4631-B859-EF0DC0DC26B7.png)  
![attention mechanism](Attachments/CC23820C-9F2D-4422-AB72-D33B61F94A91.png)  
![Screenshot 2026-03-28 at 12.53.54 PM.png](Attachments/6B7FF3B4-517F-4C16-94C2-1F8FCEF36933.png)  
![Screenshot 2026-03-28 at 12.55.38 PM.png](Attachments/6A7B2F45-2FCE-434C-9CF6-FCA4508F84E2.png)  
  
  
# Multi Head Attention  
  
Each x¡ contributes to each transformer block/layer parallelly..   
  
  
![attention mechanism](Attachments/39E7A520-06B9-4FF8-91A6-70177D74B8E3.png)  
![Multi-head Attention](Attachments/85A68386-820A-4E4F-989B-5ADDBC01F694.png)  
![Multi-head Attention](Attachments/888DBBC3-F650-4E5C-BCC3-443BCEC79E87.png)  
![attention mechanism](Attachments/89125A4F-CCDE-4474-92AA-0CAD2F47DD96.png)  
  
  
![Attention head - compact matrix form](Attachments/CC289F85-905A-4A5D-ADE9-4B31385C5068.png)  
  
#todo Hidden State would mean-> Memory, means-> Embedded value, which is not used like in RNN?  
**** A-> Attention formula softmax(QK†/√dk)-> ****  
****Z-> A*V-> Called Attention Head..****  
![Multi-head Attention](Attachments/9EEBE2A9-A1CC-4486-82EC-670A24EBD0A9.png)  
![Multi-head Attention](Attachments/F1031B54-625F-4CD3-A013-EBA805F92C8E.png)  
![Shape Example](Attachments/A59DC2CA-CFAB-4AFF-90A3-F78B40788383.png)  
![Some practical techniques commonly needed when training auto-regressive transfor](Attachments/D201D975-33C7-43E3-9637-A2A6EDDC4ADB.png)  
  
