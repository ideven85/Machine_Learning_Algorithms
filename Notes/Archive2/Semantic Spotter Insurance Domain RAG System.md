  
  
## Semantic Spotter: Insurance Domain RAG System  
## Semantic Spotter: Insurance Domain RAG System  
**1. Project Goal**  
**1. Project Goal**  
  
The objective of this project is to build a robust Generative Search system capable of effectively and accurately answering questions based on various HDFC insurance policy documents. This Retrieval-Augmented Generation (RAG) application is built leveraging the LlamaIndex framework.  
The objective of this project is to build a robust Generative Search system capable of effectively and accurately answering questions based on various HDFC insurance policy documents. This Retrieval-Augmented Generation (RAG) application is built leveraging the LlamaIndex framework.  
  
**2. Data Source**  
**2. Data Source**  
  
The knowledge base consists of seven HDFC insurance documents in PDF format, contained within a single directory:  
  
The knowledge base consists of seven HDFC insurance documents in PDF format, contained within a single directory:  
The knowledge base consists of seven HDFC insurance documents in PDF format, contained within a single directory:  
* HDFC-Life-Easy-Health-101N110V03-Policy-Bond-Single-Pay.pdf  
* HDFC-Life-Easy-Health-101N110V03-Policy-Bond-Single-Pay.pdf  
* HDFC-Life-Group-Poorna-Suraksha-101N137V02-Policy-Document.pdf  
* HDFC-Life-Group-Poorna-Suraksha-101N137V02-Policy-Document.pdf  
* HDFC-Life-Group-Term-Life-Policy.pdf  
* HDFC-Life-Group-Term-Life-Policy.pdf  
* HDFC-Life-Sampoorna-Jeevan-101N158V04-Policy-Document.pdf  
* HDFC-Life-Sampoorna-Jeevan-101N158V04-Policy-Document.pdf  
* HDFC-Life-Sanchay-Plus-Life-Long-Income-Option-101N134V19-Policy-Document.pdf  
* HDFC-Life-Sanchay-Plus-Life-Long-Income-Option-101N134V19-Policy-Document.pdf  
* HDFC-Life-Smart-Pension-Plan-Policy-Document-Online.pdf  
* HDFC-Life-Smart-Pension-Plan-Policy-Document-Online.pdf  
* HDFC-Surgicare-Plan-101N043V01.pdf  
* HDFC-Surgicare-Plan-101N043V01.pdf  
  
* **3. Architecture Description**  
* **3. Architecture Description**  
* **3. Architecture Description**  
* **3. Architecture Description**  
* **Documents:** Ingestion of the seven HDFC insurance PDFs.  
* **Documents:** Ingestion of the seven HDFC insurance PDFs.  
* **Embeddings & Vector DB:** OpenAI embeddings are used to index the insurance documents into a Vector Database for efficient semantic retrieval.  
* **Embeddings & Vector DB:** OpenAI embeddings are used to index the insurance documents into a Vector Database for efficient semantic retrieval.  
* **Query Engine:** The LlamaIndex Query Engine module handles semantic search. It utilizes a Retriever and a SentenceTransformer reranker (cross-encoder/ms-marco-MiniLM-L-2-v2) to extract the top-k most relevant nodes from the embeddings.  
* **Query Engine:** The LlamaIndex Query Engine module handles semantic search. It utilizes a Retriever and a SentenceTransformer reranker (cross-encoder/ms-marco-MiniLM-L-2-v2) to extract the top-k most relevant nodes from the embeddings.  
* **LLM:** The retrieved top-k documents, along with the user's query, are passed to the LLM to generate an accurate, context-aware response.  
* **LLM:** The retrieved top-k documents, along with the user's query, are passed to the LLM to generate an accurate, context-aware response.  
* **Caching:** A caching layer improves read operation latency. Recent similar searches are stored in the cache; if a user query hits the cache, it is served immediately. If not, it routes through the standard query engine and LLM pipeline.  
* **Caching:** A caching layer improves read operation latency. Recent similar searches are stored in the cache; if a user query hits the cache, it is served immediately. If not, it routes through the standard query engine and LLM pipeline.  
* **Metadata:** Alongside the generated response, the system returns document citations (references) and similarity scores to establish transparency and improve user confidence.  
* **Metadata:** Alongside the generated response, the system returns document citations (references) and similarity scores to establish transparency and improve user confidence.  
* **Reranking:** The cross-encoder model reranks the initially retrieved documents based on deeper semantic scoring to ensure the best context is sent to the LLM.  
* **Reranking:** The cross-encoder model reranks the initially retrieved documents based on deeper semantic scoring to ensure the best context is sent to the LLM.  
* **Evaluation:** GPT-4 is utilized as an evaluator to assess the pipeline based on three core metrics: relevancy, faithfulness, and correctness.  
* **Evaluation:** GPT-4 is utilized as an evaluator to assess the pipeline based on three core metrics: relevancy, faithfulness, and correctness.  
  
* **4. Solution Strategy**  
* **4. Solution Strategy**  
  
* The system is designed to fulfill the following core requirements:  
* The system is designed to fulfill the following core requirements:  
* Provide users with accurate, conversational responses directly derived from the insurance policy knowledge base.  
* Provide users with accurate, conversational responses directly derived from the insurance policy knowledge base.  
* Process and respond to complex user queries with high precision.  
* Process and respond to complex user queries with high precision.  
* Supply exact citations and page references to the original documents for every generated response, allowing users to verify the information.  
* Supply exact citations and page references to the original documents for every generated response, allowing users to verify the information.  
  
* **5. Tools Used**  
* **5. Tools Used**  
  
* LlamaIndex is the primary orchestration framework, selected for its powerful query engine, rapid data processing capabilities, and low-code implementation.  
* LlamaIndex is the primary orchestration framework, selected for its powerful query engine, rapid data processing capabilities, and low-code implementation.  
* LlamaIndex is the primary orchestration framework, selected for its powerful query engine, rapid data processing capabilities, and low-code implementation.  
* LlamaIndex is the primary orchestration framework, selected for its powerful query engine, rapid data processing capabilities, and low-code implementation.  
* **VectorStoreIndex:** For creating the primary index.  
* **VectorStoreIndex:** For creating the primary index.  
* **Reranker:** SentenceTransformerRerank using cross-encoder/ms-marco-MiniLM-L-2-v2.  
* **Reranker:** SentenceTransformerRerank using cross-encoder/ms-marco-MiniLM-L-2-v2.  
* **Caching:** Diskcache.  
* **Caching:** Diskcache.  
* **Core LLM & Embeddings:** OpenAI.  
* **Core LLM & Embeddings:** OpenAI.  
* **Evaluation:** OpenAI GPT-4.  
* **Evaluation:** OpenAI GPT-4.  
  
* **6. Why LlamaIndex?**  
* **6. Why LlamaIndex?**  
  
* LlamaIndex generally operates with a lower overhead for RAG tasks compared to alternatives like LangChain. It offers up to 40% faster retrieval and a lighter footprint by focusing strictly on efficient, structured data indexing. While LangChain is highly suited for complex, multi-step agent workflows, LlamaIndex excels at raw, speed-optimized data retrieval.  
* LlamaIndex generally operates with a lower overhead for RAG tasks compared to alternatives like LangChain. It offers up to 40% faster retrieval and a lighter footprint by focusing strictly on efficient, structured data indexing. While LangChain is highly suited for complex, multi-step agent workflows, LlamaIndex excels at raw, speed-optimized data retrieval.  
  
* **LlamaIndex Profile (Low Overhead - Specialized):**  
* **LlamaIndex Profile (Low Overhead - Specialized):**  
* **LlamaIndex Profile (Low Overhead - Specialized):**  
* **LlamaIndex Profile (Low Overhead - Specialized):**  
* **Focus:** Data ingestion, indexing, and retrieval.  
* **Focus:** Data ingestion, indexing, and retrieval.  
* **Performance:** Faster retrieval times leveraging pre-built indexing strategies.  
* **Performance:** Faster retrieval times leveraging pre-built indexing strategies.  
* **Complexity:** Lower complexity with high-level abstractions, enabling rapid prototyping.  
* **Complexity:** Lower complexity with high-level abstractions, enabling rapid prototyping.  
* **Best for:** Document Q&A, data-intensive search, and straightforward RAG pipelines.  
* **Best for:** Document Q&A, data-intensive search, and straightforward RAG pipelines.  
  
* **Key Features of LlamaIndex:**  
* **Key Features of LlamaIndex:**  
* **Key Features of LlamaIndex:**  
* **Key Features of LlamaIndex:**  
* Data connectors that easily ingest various data sources and formats.  
* Data connectors that easily ingest various data sources and formats.  
* Capabilities to synthesize data across heterogeneous documents.  
* Capabilities to synthesize data across heterogeneous documents.  
* Native integrations with vector stores, tracing tools, and LLMs.  
* Native integrations with vector stores, tracing tools, and LLMs.  
  
* **7. Challenges & Fixes**  
* **7. Challenges & Fixes**  
* **Issue #1: Redundant Embedding Generation.** * *Fix:* A cache layer was implemented in ChromaDB to prevent the re-embedding of previously processed data. This protects the server from being overloaded and significantly speeds up retrieval.  
* **Issue #1: Redundant Embedding Generation.** * *Fix:* A cache layer was implemented in ChromaDB to prevent the re-embedding of previously processed data. This protects the server from being overloaded and significantly speeds up retrieval.  
* **Issue #2: Suboptimal Context Retrieval.** * *Fix:* A Cross-Encoder based Reranker was introduced to refine the selection of retrieved passages. This drastically improved the accuracy and relevance of the context fed to the LLM.  
* **Issue #2: Suboptimal Context Retrieval.** * *Fix:* A Cross-Encoder based Reranker was introduced to refine the selection of retrieved passages. This drastically improved the accuracy and relevance of the context fed to the LLM.  
* **Issue #3: Verifying Answer Correctness.** * *Fix:* Verifying generative output is inherently difficult. We implemented an automated evaluation pipeline using GPT-4 to score the accuracy and relevance of the answers. This was paired with a human-in-the-loop feedback system for absolute quality assurance.  
* **Issue #3: Verifying Answer Correctness.** * *Fix:* Verifying generative output is inherently difficult. We implemented an automated evaluation pipeline using GPT-4 to score the accuracy and relevance of the answers. This was paired with a human-in-the-loop feedback system for absolute quality assurance.  
  
* **8. Future Improvements**  
* **8. Future Improvements**  
* **8. Future Improvements**  
* **8. Future Improvements**  
* [ ] Integrate additional selectable LLMs (Gemini, Claude AI, Hugging Face models, etc.).  
* [ ] Integrate additional selectable LLMs (Gemini, Claude AI, Hugging Face models, etc.).  
* [ ] Expand application features (e.g., conversational memory, UI enhancements).  
* [ ] Expand application features (e.g., conversational memory, UI enhancements).  
* [ ] Add support for multiple selectable Vector Stores (Pinecone, Weaviate, Milvus, etc.).  
