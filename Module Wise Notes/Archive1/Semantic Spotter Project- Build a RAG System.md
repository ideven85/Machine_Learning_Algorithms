**Semantic Spotter Project- Build a RAG System**  
  
## 1. Project Goal  
Build a project in the insurance domain. The goal of the project will be to build a robust generative search system capable of effectively and accurately answering questions from various policy documents. Using LlamaIndex to build the generative search application.  
  
  
## 2. Data Source  
Seven HDFC insurance documents in Pdf format provides inside a single folder.  
* a. HDFC-Life-Easy-Health-101N110V03-Policy-Bond-Single-Pay.pdf  
* b. HDFC-Life-Group-Poorna-Suraksha-101N137V02-Policy-Document.pdf  
* c. HDFC-Life-Group-Term-Life-Policy.pdf  
* d. HDFC-Life-Sampoorna-Jeevan-101N158V04-Policy-Document.pdf  
* e. HDFC-Life-Sanchay-Plus-Life-Long-Income-Option-101N134V19-Policy-Document.pdf  
* f. HDFC-Life-Smart-Pension-Plan-Policy-Document-Online.pdf  
* g. HDFC-Surgicare-Plan-101N043V01.pdf  
  
## Design  
[3. Design](Attachments/FB9FA1B1-256C-408A-BF46-EBB24742FEAB.jpeg)  
  
[3. Design](Attachments/FB9FA1B1-256C-408A-BF46-EBB24742FEAB.jpeg)  
  
Descriptions about the Architecture:  
  
* Documents: List of seven HDFC insurance documents provides inside a single folder.  
  
* Open API embedding: OpenAPI embedding as Vector DB for indexing insurance documents in the form of embedding.  
  
* Query Engine: We are using Query Engine Module of Llammaindex for performing semantic Search. Query Engine will use internally Retriever and SentenceTransformerRerank- model="cross-encoder/ms-marco-MiniLM-L-2-v2 retrieve top-k relevant nodes from embedding.  
  
* LLM: top k-documents along with user query will be passed to LLM to generate the accurate response.  
  
* Caching:" Caching is being used to improve the read operation. Recent similar search will be store in Caching and user query first will be served from Cache. If user query not found in cache, then query will be forwarded to query engine and then LLM to generate the response.  
  
* Meta data: Along with Response we are also returning docs reference and similarly score to improve the user confidence towards the implemented RAG system.  
  
* SentenceTransformerRerank- model="cross-encoder/ms-marco-MiniLM-L-2-v2 Is being used to rerank the query based on semantic score.  
  
* Evaluation- LLM-gpt4 is used for evaluation on matrices relevancy ,faithfulness and correctness.  
  
**4. Solution Strategy**  
  
**4. Solution Strategy**  
**4. Solution Strategy**  
* Build a solution which should solve the following requirements:  
* Users would get responses from insurance policy knowledge base.  
* If user want to perform a query system must be able to response to query accurately.  
* If they want to refer to the original page from which the bot is responding, the bot should provide a citation as well.  
  
* **5. Tools used**  
* LlamaIndex has been used due to its powerful query engine, fast data processing ,easier and faster implementation using fewer lines of code.  
  
* Vectorstoreindex is used to create index.  
* -SentenceTransformerRerank model="cross-encoder/ms-marco-MiniLM-L-2-v2" is used to Rerank.  
* -Diskcache  
* openAI API key  
* -LLM- gpt-4 for evaluation  
  
* **6. Why LlamaIndex?**  
  
* LlamaIndex generally has lower operational overhead for Retrieval-Augmented Generation (RAG) tasks, offering up to 40% faster retrieval and a lighter footprint by focusing on efficient, structured data indexing. In contrast, LangChain serves as a heavier, "orchestration-first" framework with higher overhead, suited for complex, multi-step agent workflows rather than raw, speed-optimized data retrieval.   
  
* LlamaIndex Overhead (Low - Specialized)   
* LlamaIndex Overhead (Low - Specialized)   
* Focus: Data ingestion, indexing, and retrieval.  
* Performance: Faster retrieval times due to pre-built indexing strategies.  
* Complexity: Lower, with higher-level abstractions that allow faster prototyping for RAG.  
* Best for: Document Q&A, data-intensive search, and straightforward RAG pipelines.   
  
* LlamaIndex reduces overhead when your primary goal is building high-performance RAG with large datasets.  
  
* **Key Feature of LlamaIndex:**  
* **Key Feature of LlamaIndex:**  
* Data connectors allow ingestion from various data sources and formats.  
* It can synthesize data from multiple documents or heterogeneous data sources.  
* It provides numerous integrations with vector stores, ChatGPT plugins, tracing tools, LangChain, and more.  
  
[Image](Attachments/7DC0D798-553E-4B94-BDA1-6597EE2FF0E3.jpeg)  
  
[Image](Attachments/7DC0D798-553E-4B94-BDA1-6597EE2FF0E3.jpeg)  
[Image](Attachments/7DC0D798-553E-4B94-BDA1-6597EE2FF0E3.jpeg)  
  
* **7. Generative Search Response from Insurance documents :**  
* **7. Generative Search Response from Insurance documents :**  
```
￼



```
  
  
```




```
  
  
```
We have attached custom query generative search results.



```
  
  
[8. Multiple Query Response](Attachments/ACE81D15-144B-436F-965C-1D9F6B8B2DD7.jpeg)  
  
[8. Multiple Query Response](Attachments/ACE81D15-144B-436F-965C-1D9F6B8B2DD7.jpeg)  
  
[Image](Attachments/7A81E02F-BACB-4DD9-9345-B271995819A2.jpeg)  
  
[Image](Attachments/7A81E02F-BACB-4DD9-9345-B271995819A2.jpeg)  
[Image](Attachments/7A81E02F-BACB-4DD9-9345-B271995819A2.jpeg)  
  
**9. ️ Challenges/Issues Faced with fixes**  
* [Issue #1] (Cache layer was added in ChromaDB to prevent re-embedding of the data. This was done to avoid overloading the ChromaDB server with data and to make the retrieval process more efficient.)  
* [Issue #2] (Cross Encoder based Reranker was added to better select the most relevant passages from the document. This was done to improve the quality of the answers to the user queries.)  
* [Issue #3] (Verifying the correctness of the answers given by the model was a challenge. We used GPT-4 to verify the answers provided by the model since it is a state-of-the-art model. This was done to ensure that the answers provided by the model are accurate and relevant. We also included a human feedback system to verify the correctness of the answers provided by the model. This was done to ensure that the answers provided by the model are accurate and relevant.)  
  
* **11. Future Improvements**  
* **11. Future Improvements**  
* Add more selectable GPT models to the project(Gemini, Claude AI, Huggingface models etc).  
* Add more features to the project.  
* Add more selectable Vector Store to the project(Pinecone, Weaviate, Redis etc).  
