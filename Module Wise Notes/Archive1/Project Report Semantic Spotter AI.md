## Project Report: Semantic Spotter AI  
**Domain:** Insurance (HDFC Life Policy Documents) **Core Technologies:** LlamaIndex, OpenAI (GPT-3.5/GPT-4), ChromaDB, Cross-Encoder Reranking  
  
**1. Executive Summary**  
  
The Semantic Spotter AI project delivers a highly accurate, Retrieval-Augmented Generation (RAG) system tailored for the insurance domain. By ingesting complex HDFC Life policy documents, the system empowers users to query dense legal jargon and receive precise, conversational, and citation-backed answers. The architecture emphasizes low-latency retrieval and high-fidelity responses through strategic caching, semantic reranking, and rigorous automated evaluation.  
  
**2. Problem Statement**  
  
Traditional methods of navigating insurance policy documents, claim guidelines, and coverage details are time-consuming and prone to human error. Policyholders and agents often struggle to extract specific clauses from lengthy PDFs.  
  
**The Goal:** Build a robust generative search system capable of effectively answering complex questions directly from a localized knowledge base of seven HDFC insurance policy documents. **The Framework Choice:** LlamaIndex was selected over heavier orchestration frameworks (like LangChain) because it is explicitly tailored for high-performance search and retrieval. It offers highly efficient data connectors, rapid indexing of large data volumes, and a lighter operational footprint optimized specifically for document Q&A pipelines.  
  
**3. System Architecture & Flowchart**  
  
The system is built on a modular, multi-layered RAG architecture ensuring both speed and accuracy.  
  
Plaintext  
  
Plaintext  
  
```
+-----------------+       +-------------------+       +--------------------+
|                 |       |                   |       |                    |
|  HDFC Policy    | ----> | LlamaIndex Parser | ----> | Text Chunks (Nodes)|
|  Documents (PDF)|       | (Data Ingestion)  |       |                    |
|                 |       |                   |       |                    |
+-----------------+       +-------------------+       +--------------------+
                                                                |
                                                                v
                                                      +--------------------+
                                                      |                    |
                                                      | OpenAI Embeddings  |
                                                      | (text-ada-002)     |
                                                      |                    |
                                                      +--------------------+
                                                                |
                                                                v
+-----------------+       +-------------------+       +--------------------+
|                 |       |                   |       |                    |
|  User Query     | ----> |  DiskCache Layer  | ----> |  ChromaDB Vector   |
|                 |       |  (Cache Check)    |       |  Store Index       |
|                 |       |                   |       |                    |
+-----------------+       +-------------------+       +--------------------+
                                                                |
                                                                v
                                                      +--------------------+
                                                      |                    |
                                                      | Cross-Encoder      |
                                                      | Reranker           |
                                                      |                    |
                                                      +--------------------+
                                                                |
                                                                v
+-----------------+       +-------------------+       +--------------------+
|                 |       |                   |       |                    |
| Final Answer &  | <---- | GPT-3.5/GPT-4 LLM | <---- | Top-K Relevant     |
| Citations       |       | (Synthesis)       |       | Context Nodes      |
|                 |       |                   |       |                    |
+-----------------+       +-------------------+       +--------------------+



```
  
  
[3. Design](Attachments/AEB1FAF3-9ACF-4951-A374-31128C9068E9.jpeg)  
  
[3. Design](Attachments/AEB1FAF3-9ACF-4951-A374-31128C9068E9.jpeg)  
[3. Design](Attachments/AEB1FAF3-9ACF-4951-A374-31128C9068E9.jpeg)  
  
**4. Implementation Details**  
* **Data Ingestion:** Processed 217 pages across 7 PDFs using LlamaIndex's SimpleDirectoryReader.  
* **Chunking & Indexing:** Implemented SentenceSplitter with a chunk size of 512 and an overlap of 100 to maintain contextual continuity. Embeddings were generated using OpenAI's text-embedding-ada-002.  
* **Storage:** Utilized VectorStoreIndex with a pluggable design pattern, defaulting to memory or ChromaDB for persistent storage.  
* **Retrieval & Reranking:** Initial retrieval fetches the top 10 nodes, which are then passed through a SentenceTransformerRerank model (cross-encoder/ms-marco-MiniLM-L-2-v2) to distill the top 3 most semantically relevant nodes.  
* **Synthesis:** GPT-3.5-turbo processes the refined nodes alongside custom prompt templates (text_qa_template and refine_template) to generate the final user response, appending exact document file names and page labels for transparency.  
  
* **5. Caching and Evaluation Pipeline**  
* **5. Caching and Evaluation Pipeline**  
* **Latency Optimization:** A diskcache layer intercepts user queries. If a query has been asked previously, the system serves the cached response instantly, saving API costs and compute time.  
* **Automated Evaluation:** For quality assurance, the system integrates a GPT-4 driven evaluation suite. It scores every non-cached response on three critical metrics:  
    1. *Faithfulness:* Does the answer strictly adhere to the retrieved context?  
    2. *Relevancy:* Does the answer directly address the user's query?  
    3. *Correctness:* Is the synthesized information factually accurate?  
  
    4. **6. Challenges Faced & Solutions**  
1. **Issue 1: Redundant Embedding Generation**  
    * *Solution:* A cache layer was added to ChromaDB to prevent re-embedding the same data across multiple runs. This optimized the retrieval process and protected the vector database from server overload.  
2. **Issue 2: Suboptimal Context Retrieval**  
    * *Solution:* Standard vector similarity sometimes retrieved tangentially related passages. A Cross-Encoder-based Reranker was introduced to act as a secondary filter, dramatically improving the relevance of the context window sent to the LLM.  
3. **Issue 3: Verifying Generative Accuracy**  
    * *Solution:* LLM hallucinations are a major risk in the insurance domain. GPT-4 was integrated specifically as an evaluator state-of-the-art model to score outputs. This was paired with an interactive human-in-the-loop feedback pipeline during testing to manually verify output quality.  
  
    * **7. Future Enhancements**  
* **Model Agnosticism:** Integrate a pluggable LLM layer to easily select between OpenAI, Google Gemini, and Anthropic Claude models.  
* **Database Expansion:** Expand the Vector Store factory to support enterprise-scale databases like Pinecone, Weaviate, or Redis.  
* **Feature Expansion:** Add multi-modal capabilities (e.g., parsing tables and images within the PDFs) and a graphical user interface (GUI) using Streamlit.  
  
1. Running the project  
