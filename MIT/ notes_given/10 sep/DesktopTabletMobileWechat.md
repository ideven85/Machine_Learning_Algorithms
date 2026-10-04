  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
DesktopTabletMobile/Wechat  
**Transformers**  
**Outline**  
1. Transformers high-level intuition and architecture  
2. Attention mechanism  
3. Multi-head attention  
4. (Applications)  
  
**Transformers high-level intuition and architecture**  
To date, the cleverest thinker of all time was  
To date, the cle **ve** rest thinker of **all** time was  
  
**Word Embeddings**  
**Overview**  
Word embeddings are vector representations of words used in machine learning models. Count-based methods, like co-occurrence counts and PPMI, capture word meaning by analyzing word contexts in a corpus. Word2Vec, a prediction-based method, learns word vectors by training them to predict surrounding words in a sliding window context.  
Word2Vec is trained using gradient descent, updating parameters for each central word and its context words. T**he Skip-Gram model predicts context words from a central word, while the CBOW model predicts the central word from context vectors. Negative sampling is used to improve training efficiency by updating only a subset of context vectors.**  
The text discusses word embeddings, focusing on Word2Vec and GloVe models. It compares their approaches, highlighting Word2Vec’s skip-gram with negative sampling and GloVe’s combination of count-based and prediction methods. The text also explores evaluation methods for word embeddings, including intrinsic evaluation (e.g., word similarity and analogy tasks) and extrinsic evaluation (e.g., real-world tasks like text classification).  
The text explores the geometry of learned semantic spaces and the possibility of a linear mapping between languages. It also discusses the importance of context words in Word2Vec training and how subword information can be incorporated into embeddings. Additionally, it touches on detecting semantic change in words across different text corpora.  

| Representation | Description | Pros | Cons |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------- |
| One-hot Vectors | Words represented as vectors with a 1 at the index of the word and 0s elsewhere. To account for unknown words (the ones which are not in the vocabulary), usually a vocabulary contains a special token UNK. Alternatively, unknown tokens can be ignored or assigned a zero vector. Like 1 added in Naive bayes to remove 0. LDA Algorithm | Simple representation of categorical features. | High dimensionality for large vocabularies, do not capture word meanings. |
  
  
**++Latent Semantic Analysis++**  
* **LSA Definition:** A topic model that analyzes a collection of documents and uses cosine similarity between document vectors to measure document similarity.  
* **LSA Application:** Applies Singular Value Decomposition (SVD) to a term-document matrix where elements are computed using various weighting schemes like co-occurrence or tf-idf.  
* **++[LSA Visualization:](https://en.wikipedia.org/wiki/Latent_semantic_analysis)++**++[ Wikipedia page](https://en.wikipedia.org/wiki/Latent_semantic_analysis)++ provides an animation of the topic detection process within a document-word matrix.  
* **Distributional Semantics**  
* Context Window Method**:** Defines contexts as each word in an L-sized window and uses word-context co-occurrence to generate embeddings.  
* PPMI Method**:** Uses Positive Pointwise Mutual Information (PPMI) to measure the association between word and context, considered state-of-the-art for pre-neural models.  
* **LSA for Document++[ Analysis](http://lsa.colorado.edu/papers/JASIS.lsi.90.pdf)++:** Analyzes a collection of documents to generate document vectors, allowing for document similarity measurement using cosine similarity.  
* [Attachment.png](Attachments/15B195AE-0F74-49A2-9241-A8B7BD9699E2.png)  
* **Sentences Example**  
* Mole 3 types American shrew **mole**-> Animal One **mole **of carbon dioxide-> Atom Take a biopsy of the **mole**-> Biological Term  
* **Embedding or called tokenization:**  
* [Attachment.png](Attachments/B681EC7B-0C2F-40EC-A64E-8CE22C440943.png)  
*    
* [Attachment.png](Attachments/7297BD48-C903-4D9E-BC95-AE1D530FBF6C.png)  
*  n*d embeddings  
* **Loss** Cross Entropy loss-> Logistic Classification loss-> Cross Entropy, #todo start implementing.. or nothing will stick in head..-> Log loss.. the more complex the problem gets.. simpler meanings will be lost.. start implementing smaller.. then larger.. then see bottlenecks.. hyperparameter tuning taught blindly.. just told.. never said alternative way..  
  
**Do nat capture context(Meaning)-> some form of embedding**   
[Attachment.png](Attachments/D0277356-97EB-494D-B568-AB1174102DB7.png)  
**Attention**  
**TO CAPTURE SEMANTICS**  
****Using many repetitions of attention layer and multi layer perceptron in parallel.. ****  
Bottleneck is? Iterations is 1 second? Cannot answer, have not understood...  
[Attachment.png](Attachments/602109B7-CDF7-461E-B55D-453D5C3D1362.png)  
Termed AutoRegressive  
[Attachment.png](Attachments/C4C9E1D0-50D5-4C1E-BD22-4989AD112C19.png)  
**Weight Adjustment by attention mechanism**  
[Attachment.png](Attachments/729BA96D-5500-4AEE-9F86-312C61D3816A.png)  
Embeddings getting closer example  
[Attachment.png](Attachments/D2CDA397-070B-4C54-AB54-72553785C19C.png)  
**Transformer blocks**  
[Attachment.png](Attachments/66DC3726-7739-4A04-BCA7-795FCC61000D.png)  
Each token is contributing in parallel, and getting transformed by every transformer block   
[Attachment.png](Attachments/0522BD6F-8C9E-4541-9D80-8DB7AB0BB182.png)  
n tokens-> input embedding in R^d space n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
  
[Attachment.png](Attachments/C4FF95AC-1979-469D-BAEC-BAFA9798A413.png)  
**Inside Transformer blocks**  
Contains attention layer and (neural network or multi layer perceptron).. why terming is different here?   
[Attachment.png](Attachments/C202F9E7-D328-49DB-8F3E-8339D5C7E081.png)  
 MLP-> Neuron Weights <- Loss->delta(L) q,k,v embedding of each xi, is learnt and finally represented as Wq,Wk,Wv-> Topics Left how it is learnt.. Attention Layer-> Wq,Wk,Wv,W0->W(query),W(key),W(value),W0(Bias)->(W)->☝️ adjusted by cross entropy loss  
**ATTENTION Mechanism in 1 Transformer block**  
**Projection?**   
[Attachment.png](Attachments/C4476480-5B84-4A06-98BE-4DCDC4B8DAAE.png)  
[Attachment.png](Attachments/9EC1291B-7884-4812-985B-863817106F80.png)  
Most important bits in an attention layer:  
1. (query, key, value) projection  
2. attention mechanism  
3. x->x1...xd..  
4. (q,k,v) embeddings projection->  
5. Learnt weights represented by-> Wq,WkWv  
6. [Attachment.png](Attachments/B6FB11F3-EDFD-46B0-99C5-0572ABBA9200.png)  
7. **Attention Mechanism**  
8. x->xi, Embeddings (q,k,v)-> Learnt weights Wq,Wk,Wv  
9. [Attachment.png](Attachments/6D2A1791-9B63-48E9-BFED-A849FA71E88E.png)  
10. [Attachment.png](Attachments/737F788A-D5F4-406F-802C-32A86DA99806.png)  
11. W(query)-> Prompt or input-> a query to be perfomed W(key)-> Like dictionary in python, to be compared  
12. #todo 2 days for NLP, 3 days for GENAI or less including transformers,stable diffusion, vision transformers everything.. learn this first, optional topics-> reinforcement learning, building llm from scratch will also be asked.. 1 more evaluating search systems.. RAG.. Covered.. W(value)->to contribute-> not output..   
13. [Attachment.png](Attachments/86994BDD-ACAB-4A2A-94F9-6614D742622D.png)  
14. Wq,Wk,Wv are learnt projections in attention layer  
15. [Attachment.png](Attachments/1BAFFF4A-17DE-4C28-AFA3-F0D8CC76C9E7.png)  
16. **Why learning these projections**  
17. Wq-> Learns How to ask (or prompt) Wk-> Learns How to listen (or compared) Wv -> Learns How to speak (or contribute)  
18. [Attachment.png](Attachments/8C532858-469B-4244-9C8F-2CC0964C1A78.png)  
19.    
20. [Attachment.png](Attachments/5FD1023B-D7AD-487E-9A16-E86E134DC8DA.png)  
21. [Attachment.png](Attachments/24B52A79-FF4E-46F8-AEB6-4D3531704A88.png)  
* W q,Wk,Wv->R(d*dk), Rd-> Input dimensions,dk->key's dimensions-> which is to be compared..  
  
* project the d-dimensional word-embedding space to dk-dimensional (qkv) space (typically dk < d) in what form? mathematically..? dk Because of noise in words or words like the, is or common words..  
* [Attachment.png](Attachments/BC24B03B-D41A-45AE-ADF9-90B7B7EBED9E.png)  
*  Wq,Wk,Wv  
* each (q,k,v) transformed contributes to output embedding q¡ = Wq†x¡ (Transpose) for i, qi query->Wq(T) Learnt Query multplied by xi for all i , similar weight sharing for keys and values  
* n tokens-> input embedding in R^d space n tokens transformed block by block within a shared d dimensional word embedding space, contribution is parallel that is why weights are shared.. contribution is sequential of 1 embedding to each transformer block, but parallelly contributed to output  
* **parallel and structurally identical processing..**  
* [Attachment.png](Attachments/463A45D7-64E7-41E1-9A05-BFA19424CBF9.png)  
* (q,k,v)->z-> projected by attention mechanism, which is context aware, a mixture of everyone's values, weighted by relevance...  
* **Attention Mechanism**  
* [Attachment.png](Attachments/027CD91A-FE51-43BC-8EF7-8EDB36D8DFDB.png)  
* [Attachment.png](Attachments/68EBAFC5-5DB7-4B54-B726-2D31FB3B7518.png)  
* **Attention Head**  
* [Attachment.png](Attachments/87990CC0-B500-48FD-98A3-281522DAF7C9.png)  
* How, Representation->  
1. Compact Matrix form  
2. Each z is transformed into a row,  
3. By stacking each individual vector   
4. [Attachment.png](Attachments/B2CBDAE3-0B40-4E23-82AA-A06CA7471E42.png)  
5.    
6. [Attachment.png](Attachments/FF058F80-A503-4BF8-8EC5-0904E6664EDF.png)  
7.    
8. [Attachment.png](Attachments/846E361A-509E-4FE1-B8E3-CF862749B666.png)  
9.    
10. [Attachment.png](Attachments/8203DEF1-67FE-4DC0-B678-1C9E3C9A387C.png)  
11.    
12. [Attachment.png](Attachments/16EAB456-6F21-4F19-89F0-26D3513DDF51.png)  
13. **Multi Head Attention**  
14. Each x¡ contributes to each transformer block/layer parallelly..  
15. [Attachment.png](Attachments/CFF8B8FA-232F-424E-9FCC-124D73E6DF0F.png)  
16.    
17. [Attachment.png](Attachments/F4AE7FFC-B1DE-4DDC-A427-A386FDABC12D.png)  
18.    
19. [Attachment.png](Attachments/76545C6D-CE2C-44A2-ABC1-4EC0B062DC71.png)  
20.    
21. [Attachment.png](Attachments/4616A801-C736-4A10-9C16-1D0F8067B5D2.png)  
22. [Attachment.png](Attachments/9C3B0796-5EA3-40D6-8F0A-930ECF7AAE58.png)  
23. #todo Hidden State would mean-> Memory, means-> Embedded value, which is not used like in RNN? **** A-> Attention formula softmax(QK†/√dk)-> **** ***Z-> AV-> Called Attention Head..****   
24. [Attachment.png](Attachments/8A9FA5A4-F609-43E7-B93F-0FA4CD3B1917.png)  
25.    
26. [Attachment.png](Attachments/BD11660B-8A89-42FA-B41C-69B2D846A7F1.png)  
27.    
28. [Attachment.png](Attachments/112A590F-0DF0-4D57-828A-76A264E2884A.png)  
29.    
30. [Attachment.png](Attachments/A33A9065-A684-4406-9CD2-4FFB457BD447.png)  
