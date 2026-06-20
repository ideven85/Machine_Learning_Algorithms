# What is LangChain?  
# What is LangChain?  
  
  
Large language models (LLMs) have revolutionized natural language processing (NLP), enabling various applications, from conversational assistants to content generation and analysis. However, working with LLMs can be challenging, requiring developers to navigate complex prompting, data integration, and memory management tasks. This is where LangChain comes into play, a powerful open-source Python framework designed to simplify the development of **++[LLM-powered applications.](https://www.analyticsvidhya.com/blog/2023/07/building-llm-powered-applications-with-langchain/)++**  
Large language models (LLMs) have revolutionized natural language processing (NLP), enabling various applications, from conversational assistants to content generation and analysis. However, working with LLMs can be challenging, requiring developers to navigate complex prompting, data integration, and memory management tasks. This is where LangChain comes into play, a powerful open-source Python framework designed to simplify the development of **++[LLM-powered applications.](https://www.analyticsvidhya.com/blog/2023/07/building-llm-powered-applications-with-langchain/)++**  
  
LangChain addresses the difficulties of building sophisticated LLM applications by providing modular, easy-to-use components for connecting language models with external data sources and services. It abstracts away the complexities of LLM integration, enabling developers to focus on building impactful applications that leverage the full potential of these advanced language models.  
LangChain addresses the difficulties of building sophisticated LLM applications by providing modular, easy-to-use components for connecting language models with external data sources and services. It abstracts away the complexities of LLM integration, enabling developers to focus on building impactful applications that leverage the full potential of these advanced language models.  
  
As the importance of **++[LLMs](https://www.analyticsvidhya.com/blog/2023/03/an-introduction-to-large-language-models-llms/)++** continues to grow in various domains, LangChain plays a crucial role in democratizing their use and empowering developers to create innovative solutions that can transform industries.  
As the importance of **++[LLMs](https://www.analyticsvidhya.com/blog/2023/03/an-introduction-to-large-language-models-llms/)++** continues to grow in various domains, LangChain plays a crucial role in democratizing their use and empowering developers to create innovative solutions that can transform industries.  
  
Here is the comprehensive LangChain Guide for you!  
Here is the comprehensive LangChain Guide for you!  
  
## Overview  
## Overview  
* LangChain simplifies building LLM-powered apps with its modular, open-source Python framework.  
* LangChain simplifies building LLM-powered apps with its modular, open-source Python framework.  
* It integrates LLMs and external services, enabling complex workflows and easy development.  
* It integrates LLMs and external services, enabling complex workflows and easy development.  
* Quick setup – install via pip, connect to LLMs like OpenAI, and start coding.  
* Quick setup – install via pip, connect to LLMs like OpenAI, and start coding.  
* Process documents by reading, splitting text into chunks, and creating embeddings.  
* Process documents by reading, splitting text into chunks, and creating embeddings.  
* Store embeddings in vector stores like Chroma for efficient similarity search.  
* Store embeddings in vector stores like Chroma for efficient similarity search.  
## Table of contents  
## Table of contents  
1. Getting Started with LangChain  
2. Getting Started with LangChain  
    * Hello World example with LangChain  
    * Hello World example with LangChain  
    * Ingesting Data from Various Sources  
    * Ingesting Data from Various Sources  
    * Text Splitting and Chunking Techniques:  
    * Text Splitting and Chunking Techniques:  
3. Vector Store and Retrieval Mechanisms  
4. Vector Store and Retrieval Mechanisms  
5. Building Chains  
6. Building Chains  
7. Agents: Elevating LLM Capabilities  
8. Agents: Elevating LLM Capabilities  
    * Agent  
    * Agent  
    * Define Tools  
    * Define Tools  
9. Bind Tools to LLM  
10. Bind Tools to LLM  
    * Create the Agent  
    * Create the Agent  
    * Adding Memory  
    * Adding Memory  
11. Memory Management in LangChain  
12. Memory Management in LangChain  
    * Importance of Memory in MultiStep Workflows  
    * Importance of Memory in MultiStep Workflows  
    * Types of Memory  
    * Types of Memory  
13. ConversationBufferMemory Example and Implementation  
14. ConversationBufferMemory Example and Implementation  
15. Real-world Applications and Case Studies  
16. Real-world Applications and Case Studies  
17. Future of LangChain and LLMs  
18. Future of LangChain and LLMs  
19. Potential Impact of LLMs on Various Industries  
20. Potential Impact of LLMs on Various Industries  
21. Ethical Considerations and Responsible AI Practices  
22. Ethical Considerations and Responsible AI Practices  
23. Conclusion  
24. Conclusion  
25. Frequently Asked Questions  
26. Frequently Asked Questions  
  
## What is LangChain?  
## What is LangChain?  
  
LangChain is an open-source orchestration framework for building applications using large language models (LLMs). Available in both Python and JavaScript-based libraries, LangChain provides a centralized development environment and set of tools to simplify the process of creating LLM-driven applications like chatbots and virtual agents.  
LangChain is an open-source orchestration framework for building applications using large language models (LLMs). Available in both Python and JavaScript-based libraries, LangChain provides a centralized development environment and set of tools to simplify the process of creating LLM-driven applications like chatbots and virtual agents.  
  
Serving as a generic interface for integrating with various LLMs, LangChain’s modular design allows developers and data scientists to dynamically compare different prompts and even different foundation models with minimal need to rewrite code. This flexibility also enables building programs that utilize multiple LLMs together, such as one model for interpreting user queries and another for generating responses.   
Serving as a generic interface for integrating with various LLMs, LangChain’s modular design allows developers and data scientists to dynamically compare different prompts and even different foundation models with minimal need to rewrite code. This flexibility also enables building programs that utilize multiple LLMs together, such as one model for interpreting user queries and another for generating responses.   
  
The way I see it, LangChain is filling an important gap – providing a common framework to build upon, so that innovators and creators don’t have to reinvent the wheel every time they want to leverage the power of LLM.   
The way I see it, LangChain is filling an important gap – providing a common framework to build upon, so that innovators and creators don’t have to reinvent the wheel every time they want to leverage the power of LLM.   
  
## How Does LangChain Work?  
## How Does LangChain Work?  
  
The core idea behind LangChain is to provide a modular, flexible framework for building applications that utilize large language models (LLMs). At the heart of LangChain are a few key concepts:  
The core idea behind LangChain is to provide a modular, flexible framework for building applications that utilize large language models (LLMs). At the heart of LangChain are a few key concepts:  
  
LLMs  
LLMs  
  
At the core of LangChain is the ability to seamlessly integrate with a variety of large language models (LLMs) from different providers, such as OpenAI, Anthropic, and Google. LangChain provides a standardized interface to interact with these powerful AI models, abstracting away the complexities of working with each vendor’s unique APIs and input/output formats.  
At the core of LangChain is the ability to seamlessly integrate with a variety of large language models (LLMs) from different providers, such as OpenAI, Anthropic, and Google. LangChain provides a standardized interface to interact with these powerful AI models, abstracting away the complexities of working with each vendor’s unique APIs and input/output formats.  
  
Chains  
Chains  
  
LangChain’s Chains are the basic building blocks for creating complex workflows and processing pipelines. A Chain is a sequence of operations that can be performed on the outputs of an LLM. For example, you might have a Chain that first uses an LLM to extract key information from user input, then passes that to another LLM to generate a relevant response. Chaining multiple LLM-powered steps together enables developers to tackle increasingly sophisticated natural language tasks.  
LangChain’s Chains are the basic building blocks for creating complex workflows and processing pipelines. A Chain is a sequence of operations that can be performed on the outputs of an LLM. For example, you might have a Chain that first uses an LLM to extract key information from user input, then passes that to another LLM to generate a relevant response. Chaining multiple LLM-powered steps together enables developers to tackle increasingly sophisticated natural language tasks.  
  
**Also Read: ++[A Comprehensive Guide to Using Chains in Langchain](https://www.analyticsvidhya.com/blog/2023/10/a-comprehensive-guide-to-using-chains-in-langchain/)++**  
**Also Read: ++[A Comprehensive Guide to Using Chains in Langchain](https://www.analyticsvidhya.com/blog/2023/10/a-comprehensive-guide-to-using-chains-in-langchain/)++**  
  
## Agents  
## Agents  
  
Building on the Chains concept, LangChain introduces higher-level abstractions called Agents. Agents are self-contained units that can leverage Chains and other LangChain components to autonomously solve complex, goal-driven tasks. Agents encapsulate the logic for interacting with LLMs, managing state and memory, and coordinating multi-step workflows. This allows developers to create intelligent, LLM-powered “actors” that can engage in more natural, contextual conversations and complete intricate assignments.  
Building on the Chains concept, LangChain introduces higher-level abstractions called Agents. Agents are self-contained units that can leverage Chains and other LangChain components to autonomously solve complex, goal-driven tasks. Agents encapsulate the logic for interacting with LLMs, managing state and memory, and coordinating multi-step workflows. This allows developers to create intelligent, LLM-powered “actors” that can engage in more natural, contextual conversations and complete intricate assignments.  
  
Memory  
Memory  
  
A crucial capability provided by LangChain is its memory management system. This allows LLMs to store and retrieve relevant information during the course of a multi-step workflow, enabling context preservation and statefulness across executions. The memory component is essential for building conversational applications and other LLM-powered experiences that require an understanding of previous interactions and intermediate results.  
A crucial capability provided by LangChain is its memory management system. This allows LLMs to store and retrieve relevant information during the course of a multi-step workflow, enabling context preservation and statefulness across executions. The memory component is essential for building conversational applications and other LLM-powered experiences that require an understanding of previous interactions and intermediate results.  
  
By combining these core elements – LLM integrations, Chains, Agents, and Memory – LangChain gives developers a comprehensive toolkit for building sophisticated applications driven by large language models. The framework’s modular, flexible design empowers creators to experiment, iterate, and scale their LLM-powered solutions more efficiently. Rather than getting bogged down in the underlying technical complexities, they can focus on the specific use case and workflow, seamlessly swapping out components as needed to find the optimal configuration.  
By combining these core elements – LLM integrations, Chains, Agents, and Memory – LangChain gives developers a comprehensive toolkit for building sophisticated applications driven by large language models. The framework’s modular, flexible design empowers creators to experiment, iterate, and scale their LLM-powered solutions more efficiently. Rather than getting bogged down in the underlying technical complexities, they can focus on the specific use case and workflow, seamlessly swapping out components as needed to find the optimal configuration.  
  
## Getting Started with LangChain  
## Getting Started with LangChain  
To install LangChain, you can use pip, the package installer for Python. Run the following command:  
To install LangChain, you can use pip, the package installer for Python. Run the following command:  
```
!pip install langchain





```
  
  
  
  
Setting up an LLM provider (e.g., OpenAI, **Anthropic**, Cohere):  
Setting up an LLM provider (e.g., OpenAI, **Anthropic**, Cohere):  
  
LangChain supports integration with various large language model providers. In this example, we’ll set up the OpenAI provider. First, install the necessary dependency:  
LangChain supports integration with various large language model providers. In this example, we’ll set up the OpenAI provider. First, install the necessary dependency:  
```
!pip install qU langchain-openai





```
  
  
  
  
Next, import the required modules and set your OpenAI API key as an environment variable:  
Next, import the required modules and set your OpenAI API key as an environment variable:  
```
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo")





```
  
  
  
  
Hello World example with LangChain  
Hello World example with LangChain  
  
With the LLM provider set up, we can now interact with the language model. Here’s a basic example of using the model for translation:  
With the LLM provider set up, we can now interact with the language model. Here’s a basic example of using the model for translation:  
```
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]
model.invoke(messages)





```
  
  
  
  
  
This will return an ==AIMessage== object containing the model’s response and metadata about the response.  
This will return an ==AIMessage== object containing the model’s response and metadata about the response.  
  
To extract just the string response, we can use an output parser:  
To extract just the string response, we can use an output parser:  
```
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
result = model.invoke(messages)
parser.invoke(result)





```
  
  
  
  
  
In this example, we first create a list of messages representing the conversation context and the input to translate. Using the ‘ invoke ‘ method, we then invoke the language model with these messages. The model returns an ==AIMessage== object containing the translation in Italian (==’Ciao!’==) along with additional metadata.  
In this example, we first create a list of messages representing the conversation context and the input to translate. Using the ‘ invoke ‘ method, we then invoke the language model with these messages. The model returns an ==AIMessage== object containing the translation in Italian (==’Ciao!’==) along with additional metadata.  
  
Using LangChain’s modular components, you can easily set up and interact with various large language models, enabling you to build sophisticated NLP applications with relative ease.  
Using LangChain’s modular components, you can easily set up and interact with various large language models, enabling you to build sophisticated NLP applications with relative ease.  
  
## Ingesting Data from Various Sources  
## Ingesting Data from Various Sources  
  
To read and split a PDF document, you can use the ==PyPDFLoader== class from ==langchain_community.document_loaders==:  
To read and split a PDF document, you can use the ==PyPDFLoader== class from ==langchain_community.document_loaders==:  
  
**Installing dependencies:**  
**Installing dependencies:**  
```
!pip install pypdf
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("2310.06625v4.pdf")
pages = loader.load_and_split()

print(pages[1].page_content)





```
  
  
  
  
  
### Text Splitting and Chunking Techniques:  
### Text Splitting and Chunking Techniques:  
  
Effective text splitting and chunking are essential for handling large documents. The ==CharacterTextSplitter== class can split documents into smaller chunks, which are easier to process and manage.  
Effective text splitting and chunking are essential for handling large documents. The ==CharacterTextSplitter== class can split documents into smaller chunks, which are easier to process and manage.  
  
Split by character  
Split by character  
  
This is the simplest method. This splits based on characters (by default “\n\n”) and measures  
This is the simplest method. This splits based on characters (by default “\n\n”) and measures  
  
chunk length by number of characters.  
chunk length by number of characters.  
```
from langchain.text_splitter import CharacterTextSplitter
# Assuming you have a list of pages loaded
page = pages[0] # Get the first page
# Get the text content of the first page
page_content = page.page_content
# Create a CharacterTextSplitter instance
text_splitter = CharacterTextSplitter(
chunk_size=100, # Adjust the chunk size as needed
chunk_overlap=20, # Adjust the chunk overlap as needed
separator="\n" # Use newline character as the separator
)
# Split the page content into chunks
chunks = text_splitter.split_text(page_content)
chunks





```
  
  
  
  
  
  
  
## Vector Store and Retrieval Mechanisms  
## Vector Store and Retrieval Mechanisms  
  
Vector stores are critical for storing and retrieving document embeddings. This walkthrough showcases basic functionality related to vector stores. A key part of working with vector stores is creating the vector to put in them, usually created via embeddings. Therefore, it is recommended that you familiarize yourself with the text-embedding model interfaces before diving into this. There are many great vector store options; a few are free, open-source, and run entirely on your local machine. Review all integrations for many great hosted offerings.  
Vector stores are critical for storing and retrieving document embeddings. This walkthrough showcases basic functionality related to vector stores. A key part of working with vector stores is creating the vector to put in them, usually created via embeddings. Therefore, it is recommended that you familiarize yourself with the text-embedding model interfaces before diving into this. There are many great vector store options; a few are free, open-source, and run entirely on your local machine. Review all integrations for many great hosted offerings.  
  
Here’s an example using the Chroma vector store:  
Here’s an example using the Chroma vector store:  
```
## this code is if you have latest version of the langchain installed 
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
# Load your documents (assuming 'pages' is already loaded)
text_splitter = CharacterTextSplitter(chunk_size=1000,
chunk_overlap=0)
documents = text_splitter.split_documents(pages)
# Create the embeddings
embeddings = OpenAIEmbeddings()
# Create the Chroma vector store
db = Chroma.from_documents(documents, embeddings)

query = "What is i transformer"
docs = db.similarity_search(query)
print(docs[0].page_content)





```
  
  
  
  
  
This code creates embeddings for the documents and stores them in a Chroma vector store, enabling efficient similarity search queries.  
This code creates embeddings for the documents and stores them in a Chroma vector store, enabling efficient similarity search queries.  
  
## Building Chains  
## Building Chains  
  
Chains refer to sequences of operations, including calls to LLMs, tools, or data preprocessing steps. They are essential for creating complex workflows by linking multiple components together.  
Chains refer to sequences of operations, including calls to LLMs, tools, or data preprocessing steps. They are essential for creating complex workflows by linking multiple components together.  
  
## LCEL (Langchain Expression Language)  
## LCEL (Langchain Expression Language)  
  
LCEL is great for constructing chains, but using chains already on the shelf is also nice.  
LCEL is great for constructing chains, but using chains already on the shelf is also nice.  
  
Chains built with LCEL: LangChain offers a higher-level constructor method in this case. However, all that is being done under the hood is constructing a chain with LCEL. Chains are constructed by subclassing from a legacy Chain class. These chains do not use LCEL under the hood but are the standalone classes. We are working on creating methods that create LCEL versions of all chains. We are doing this for a few reasons.  
Chains built with LCEL: LangChain offers a higher-level constructor method in this case. However, all that is being done under the hood is constructing a chain with LCEL. Chains are constructed by subclassing from a legacy Chain class. These chains do not use LCEL under the hood but are the standalone classes. We are working on creating methods that create LCEL versions of all chains. We are doing this for a few reasons.  
  
Here, we are going to explore only about the LCEL Chains:  
Here, we are going to explore only about the LCEL Chains:  
  
**LLM Chain: Chain to run queries against LLMs**  
**LLM Chain: Chain to run queries against LLMs**  
```

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
prompt_template = "Tell me a {adjective} joke"
prompt = PromptTemplate(
input_variables=["adjective"], template=prompt_template
)
llm = OpenAI()
chain = prompt | llm # chain using prompt and llm
result=chain.invoke("your adjective here")
print(result)





```
  
  
  
  
  
**Combining and Customizing Chains for Complex Tasks**  
**Combining and Customizing Chains for Complex Tasks**  
  
Chains can be combined and customized to handle more complex tasks. By linking multiple chains, you can create sophisticated workflows that leverage various capabilities of LLMs and tools.  
Chains can be combined and customized to handle more complex tasks. By linking multiple chains, you can create sophisticated workflows that leverage various capabilities of LLMs and tools.  
  
## Agents: Elevating LLM Capabilities  
## Agents: Elevating LLM Capabilities  
In LangChain, agents are built to expand the functionality of LLMs by enabling them to interact with diverse tools and data sources. These agents can dynamically make decisions, execute actions, and retrieve information.  
In LangChain, agents are built to expand the functionality of LLMs by enabling them to interact with diverse tools and data sources. These agents can dynamically make decisions, execute actions, and retrieve information.  
  
Agent  
Agent  
  
There are several types of agents, including ZeroShotAgent and ConversationalAgent. Each type is suited for different tasks:  
There are several types of agents, including ZeroShotAgent and ConversationalAgent. Each type is suited for different tasks:  
*  **ZeroShotAgent:** Performs tasks without needing prior context or training.  
*  **ZeroShotAgent:** Performs tasks without needing prior context or training.  
* ** ConversationalAgent:** Maintains context across interactions, suitable for dialog-based applications  
* ** ConversationalAgent:** Maintains context across interactions, suitable for dialog-based applications  
  
* Define Tools  
* Define Tools  
  
* Next, let’s define some tools to use. Let’s write a really simple Python function to calculate the length of a word that is passed in.  
* Next, let’s define some tools to use. Let’s write a really simple Python function to calculate the length of a word that is passed in.  
```
## Loading the model first
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
from langchain.agents import tool
@tool
def get_word_length(word: str) -> int:
"""Returns the length of a word."""
return len(word)
get_word_length.invoke("abc")
#output = 3
tools = [get_word_length]





```
  
  
  
  
Create Prompt Using Agents  
Create Prompt Using Agents  
  
Now, let us create the prompt. Because OpenAI Function Calling is finetuned for tool usage, we hardly need any instructions on how to reason or how to output format. We will just have two input variables: input and agent_scratchpad.  
Now, let us create the prompt. Because OpenAI Function Calling is finetuned for tool usage, we hardly need any instructions on how to reason or how to output format. We will just have two input variables: input and agent_scratchpad.  
  
Input should be a string containing the user objective. agent_scratchpad should be a message sequence containing the previous agent tool invocations and the corresponding tool outputs.  
Input should be a string containing the user objective. agent_scratchpad should be a message sequence containing the previous agent tool invocations and the corresponding tool outputs.  
```
from langchain_core.prompts import ChatPromptTemplate,
MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"You are very powerful assistant, but don't know current
events",
),
("user", "{input}"),
MessagesPlaceholder(variable_name="agent_scratchpad"),
]
)





```
  
  
  
  
## Bind Tools to LLM  
## Bind Tools to LLM  
How does the agent know what tools it can use? In this case, we rely on an OpenAI tool called LLMs, which takes tools as a separate argument. We have been specifically trained to know when to invoke those tools. To pass our tools to the agent, we just need to format them in the OpenAI tool format and pass them to our model. (By binding the functions, we ensure they’re passed each time the model is invoked.)  
How does the agent know what tools it can use? In this case, we rely on an OpenAI tool called LLMs, which takes tools as a separate argument. We have been specifically trained to know when to invoke those tools. To pass our tools to the agent, we just need to format them in the OpenAI tool format and pass them to our model. (By binding the functions, we ensure they’re passed each time the model is invoked.)  
```
llm_with_tools = llm.bind_tools(tools)





```
  
  
  
  
Create the Agent  
Create the Agent  
  
After putting those pieces together, we can now create the agent. We will import two last utility functions: a component for formatting intermediate steps (agent action, tool output pairs) to input messages that can be sent to the model and a component for converting the output message into an agent action/agent finish.  
After putting those pieces together, we can now create the agent. We will import two last utility functions: a component for formatting intermediate steps (agent action, tool output pairs) to input messages that can be sent to the model and a component for converting the output message into an agent action/agent finish.  
```
from langchain.agents.format_scratchpad.openai_tools import (
format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import
OpenAIToolsAgentOutputParser
agent = (
{
"input": lambda x: x["input"],
"agent_scratchpad": lambda x: format_to_openai_tool_messages(
x["intermediate_steps"]
),
}
| prompt
| llm_with_tools
| OpenAIToolsAgentOutputParser()
)
from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
list(agent_executor.stream({"input": "How many letters in the word
eudca"}))





```
  
  
  
  
Adding Memory  
Adding Memory  
  
This is great – we have an agent! However, this agent is stateless – it doesn’t remember anything about previous interactions. This means you can’t ask follow-up questions easily. Let’s fix that by adding in memory. To do this, we need to do two things:  
This is great – we have an agent! However, this agent is stateless – it doesn’t remember anything about previous interactions. This means you can’t ask follow-up questions easily. Let’s fix that by adding in memory. To do this, we need to do two things:  
  
Add a place for memory variables in the prompt. Keep track of the chat history. First, let’s add a place for memory in the prompt. We do this by adding a message placeholder with the key “chat_history.” Notice that we put this above the new user input (to follow the conversation flow).  
Add a place for memory variables in the prompt. Keep track of the chat history. First, let’s add a place for memory in the prompt. We do this by adding a message placeholder with the key “chat_history.” Notice that we put this above the new user input (to follow the conversation flow).  
  
**Code: **  
**Code: **  
```
from langchain_core.prompts import MessagesPlaceholder

MEMORY_KEY = "chat_history"

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are very powerful assistant, but bad at calculating lengths of words.",
    ),
    MessagesPlaceholder(variable_name=MEMORY_KEY),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

from langchain_core.messages import AIMessage, HumanMessage

chat_history = []

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(x["intermediate_steps"]),
        "chat_history": lambda x: x["chat_history"],
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

input1 = "how many letters in the word educa?"

result = agent_executor.invoke({"input": input1, "chat_history": chat_history})
chat_history.extend([HumanMessage(content=input1), AIMessage(content=result["output"])])

agent_executor.invoke({"input": "is that a real word?", "chat_history": chat_history})





```
  
  
  
  
  
## Memory Management in LangChain  
## Memory Management in LangChain  
Memory management is crucial in LangChain applications, especially in multistep workflows, where maintaining context is essential for coherent and accurate interactions. This section delves into the importance of memory and the types of memory used, and it provides examples and use cases to illustrate its application.  
Memory management is crucial in LangChain applications, especially in multistep workflows, where maintaining context is essential for coherent and accurate interactions. This section delves into the importance of memory and the types of memory used, and it provides examples and use cases to illustrate its application.  
  
Importance of Memory in MultiStep Workflows  
Importance of Memory in MultiStep Workflows  
  
Memory ensures that the application can retain information across multiple interactions in multistep workflows. This capability is vital for creating conversational agents that remember previous exchanges and provide relevant, context-aware responses. Each interaction would be independent without memory, leading to disjointed and less useful dialogues.  
Memory ensures that the application can retain information across multiple interactions in multistep workflows. This capability is vital for creating conversational agents that remember previous exchanges and provide relevant, context-aware responses. Each interaction would be independent without memory, leading to disjointed and less useful dialogues.  
  
Types of Memory  
Types of Memory  
  
LangChain supports different types of memory to suit various needs:  
LangChain supports different types of memory to suit various needs:  
* **Conversational Memory:** Keeps track of the entire conversation history, enabling the agent to refer to previous user inputs and responses.  
* **Conversational Memory:** Keeps track of the entire conversation history, enabling the agent to refer to previous user inputs and responses.  
* **Buffer Memory:** Maintains a limited number of recent interactions, balancing context retention and memory efficiency.  
* **Buffer Memory:** Maintains a limited number of recent interactions, balancing context retention and memory efficiency.  
* **Entity Memory:** This technique focuses on tracking specific entities mentioned during the conversation, which is useful for tasks that require detailed information about particular items or concepts.  
* **Entity Memory:** This technique focuses on tracking specific entities mentioned during the conversation, which is useful for tasks that require detailed information about particular items or concepts.  
## ConversationBufferMemory Example and Implementation  
## ConversationBufferMemory Example and Implementation  
ConversationBufferMemory stores the conversation history in a buffer. This type of memory is suitable for scenarios where maintaining a sequential record of interactions is important. It helps the model remember previous interactions and use that context to generate more coherent and contextually relevant responses.  
ConversationBufferMemory stores the conversation history in a buffer. This type of memory is suitable for scenarios where maintaining a sequential record of interactions is important. It helps the model remember previous interactions and use that context to generate more coherent and contextually relevant responses.  
  
**Code**  
**Code**  
```
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnableLambda,RunnablePassthrough

model=ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.0)

prompt= ChatPromptTemplate.from_messages(
        [
            ("system", "Act as a helpful Al Assistant"), 
            MessagesPlaceholder(variable_name="history"), 
            ("human", "(input)"),
        ]
)
memory=ConversationBufferMemory(return_messages=True)

from operator import itemgetter

chain=( 
        RunnablePassthrough.assign
        (
            history=RunnableLambda(memory.load_memory_variables)
            |
            itemgetter("history")
        )
        |
        prompt
        |
        model
        )
#use the conversation chain
user_input={'input':'what are the first four colors of a rainbow'}
response=chain.invoke(user_input)
#saving the context
memory.save_context(user_input,{'output':response.content})
print('First Response: ',response.content)

user_input={'input':'And the last 3 ?'}
response=chain.invoke(user_input)
#also using memory present in the chain 
memory.save_context(user_input,{'output':response.content})
print('Second Response: ',response.content)


user_input = {'input': 'Which color is in the center of a rainbow?'}
response = chain.invoke(user_input)
memory.save_context(user_input, {'output': response.content})
print('Third Response: ', response.content)





```
  
  
  
  
  
**Also Read: ++[How to Build a LangChain Chatbot with Memory?](https://www.analyticsvidhya.com/blog/2024/06/langchain-chatbot-with-memory/)++**  
**Also Read: ++[How to Build a LangChain Chatbot with Memory?](https://www.analyticsvidhya.com/blog/2024/06/langchain-chatbot-with-memory/)++**  
## Real-world Applications and Case Studies  
## Real-world Applications and Case Studies  
Practical Applications of LangChain  
Practical Applications of LangChain  
  
LangChain has found numerous applications across various industries due to its powerful capabilities in handling large language models (LLMs) and maintaining conversational memory. Some practical applications include:  
LangChain has found numerous applications across various industries due to its powerful capabilities in handling large language models (LLMs) and maintaining conversational memory. Some practical applications include:  
* **Customer Support: **Companies use LangChain to create intelligent chatbots that provide personalized and context-aware responses, improving customer service efficiency and satisfaction.  
* **Customer Support: **Companies use LangChain to create intelligent chatbots that provide personalized and context-aware responses, improving customer service efficiency and satisfaction.  
* **Healthcare:** LangChainpowered systems assist healthcare professionals by offering accurate medical information and advice, helping with patient interactions, and maintaining a coherent conversation history for better patient care.  
* **Healthcare:** LangChainpowered systems assist healthcare professionals by offering accurate medical information and advice, helping with patient interactions, and maintaining a coherent conversation history for better patient care.  
* **Education:** Educators leverage LangChain to develop interactive tutoring systems that provide personalized learning experiences, track student progress, and offer continuous support through coherent dialogues.  
* **Education:** Educators leverage LangChain to develop interactive tutoring systems that provide personalized learning experiences, track student progress, and offer continuous support through coherent dialogues.  
* **Content Creation: **LangChain aids content creators by generating ideas, drafting articles, and maintaining consistent narrative flow in long-form content, thereby enhancing productivity.  
* **Content Creation: **LangChain aids content creators by generating ideas, drafting articles, and maintaining consistent narrative flow in long-form content, thereby enhancing productivity.  
  
* Success Stories and Industry Use Cases  
* Success Stories and Industry Use Cases  
* **E-commerce**: An online retailer integrated LangChain into their customer service platform, significantly reducing response times and increasing customer satisfaction by 40%. The system’s ability to remember previous interactions allowed for more personalized and effective support.  
* **E-commerce**: An online retailer integrated LangChain into their customer service platform, significantly reducing response times and increasing customer satisfaction by 40%. The system’s ability to remember previous interactions allowed for more personalized and effective support.  
* **Financial Services**: A financial advisory firm used LangChain to develop a virtual assistant that provides clients with tailored financial advice and tracks their investment histories. This led to a 25% increase in client engagement and satisfaction.  
* **Financial Services**: A financial advisory firm used LangChain to develop a virtual assistant that provides clients with tailored financial advice and tracks their investment histories. This led to a 25% increase in client engagement and satisfaction.  
* **Telecommunications: **A telecommunications company deployed LangChain to streamline technical support. The conversational memory feature enabled the support system to recall past customer issues, leading to faster problem resolution and a 30% reduction in support tickets.  
* **Telecommunications: **A telecommunications company deployed LangChain to streamline technical support. The conversational memory feature enabled the support system to recall past customer issues, leading to faster problem resolution and a 30% reduction in support tickets.  
  
* Potential Challenges and Limitations  
* Potential Challenges and Limitations  
* **Scalability:** As interactions grow, managing and scaling memory efficiently can become challenging, requiring robust infrastructure and optimization techniques.  
* **Scalability:** As interactions grow, managing and scaling memory efficiently can become challenging, requiring robust infrastructure and optimization techniques.  
* **Data Privacy: **Storing conversation histories necessitates stringent data privacy measures to protect sensitive user information and comply with regulations.  
* **Data Privacy: **Storing conversation histories necessitates stringent data privacy measures to protect sensitive user information and comply with regulations.  
* **Model Limitations:** While LLMs are powerful, they may still produce incorrect or biased responses. Ensuring the reliability and accuracy of the information generated remains a critical challenge.  
* **Model Limitations:** While LLMs are powerful, they may still produce incorrect or biased responses. Ensuring the reliability and accuracy of the information generated remains a critical challenge.  
## Future of LangChain and LLMs  
## Future of LangChain and LLMs  
LangChain’s roadmap includes several exciting features aimed at enhancing its capabilities:  
LangChain’s roadmap includes several exciting features aimed at enhancing its capabilities:  
* **Enhanced Memory Management:** Memory handling improves to support larger and more complex conversation histories.  
* **Enhanced Memory Management:** Memory handling improves to support larger and more complex conversation histories.  
* **Integration with External Knowledge Bases: **LangChain can access external databases and APIs for more accurate and comprehensive responses.  
* **Integration with External Knowledge Bases: **LangChain can access external databases and APIs for more accurate and comprehensive responses.  
* **Advanced Personalization:** Leveraging user profiles and preferences to provide more tailored interactions.  
* **Advanced Personalization:** Leveraging user profiles and preferences to provide more tailored interactions.  
* **Multimodal Capabilities**: Expanding support to include visual and auditory inputs, enabling more diverse and rich user interactions.  
* **Multimodal Capabilities**: Expanding support to include visual and auditory inputs, enabling more diverse and rich user interactions.  
## Potential Impact of LLMs on Various Industries  
## Potential Impact of LLMs on Various Industries  
The integration of LLMs into different sectors is poised to revolutionize how businesses operate and interact with their customers:  
The integration of LLMs into different sectors is poised to revolutionize how businesses operate and interact with their customers:  
* **Healthcare:** Enhanced diagnostic tools, virtual health assistants, and personalized patient care.  
* **Healthcare:** Enhanced diagnostic tools, virtual health assistants, and personalized patient care.  
* **Education:** Intelligent tutoring systems, personalized learning pathways, and automated grading.  
* **Education:** Intelligent tutoring systems, personalized learning pathways, and automated grading.  
* **Finance:** Advanced financial advisory systems, fraud detection, and personalized banking experiences.  
* **Finance:** Advanced financial advisory systems, fraud detection, and personalized banking experiences.  
* **Retail:** Improved customer service, personalized shopping experiences, and efficient inventory management.  
* **Retail:** Improved customer service, personalized shopping experiences, and efficient inventory management.  
## Ethical Considerations and Responsible AI Practices  
## Ethical Considerations and Responsible AI Practices  
As LLMs become more prevalent, it is crucial to address ethical concerns and promote responsible AI practices:  
As LLMs become more prevalent, it is crucial to address ethical concerns and promote responsible AI practices:  
* **Bias Mitigation:** Implementing techniques to identify and reduce biases in model outputs.  
* **Bias Mitigation:** Implementing techniques to identify and reduce biases in model outputs.  
* **Transparency:** Ensuring that AI systems are explainable and their decision-making processes are transparent.  
* **Transparency:** Ensuring that AI systems are explainable and their decision-making processes are transparent.  
* **User Privacy:** Protecting user data through robust encryption and compliance with privacy regulations.  
* **User Privacy:** Protecting user data through robust encryption and compliance with privacy regulations.  
* **Accountability:** Establishing clear guidelines for accountability in AI system errors or misuse.  
* **Accountability:** Establishing clear guidelines for accountability in AI system errors or misuse.  
## LangChain Tutorial: Building Innovative LLM Powered Applications End-to-End  
## LangChain Tutorial: Building Innovative LLM Powered Applications End-to-End  
  
  
  
  
Analytics Vidhya  
Analytics Vidhya  
  
138K subscribers  
138K subscribers  
  
[LangChain Tutorial: Building Innovative LLM Powered Applications End-to-End](https://www.youtube.com/watch?v=hLQ8DAkcygI)  
[LangChain Tutorial: Building Innovative LLM Powered Applications End-to-End](https://www.youtube.com/watch?v=hLQ8DAkcygI)  
  
  
Share  
Share  
  
  
  
  
[Watch on](https://www.youtube.com/watch?v=hLQ8DAkcygI&embeds_referring_euri=https%3A%2F%2Fwww.analyticsvidhya.com%2F)  
[Watch on](https://www.youtube.com/watch?v=hLQ8DAkcygI&embeds_referring_euri=https%3A%2F%2Fwww.analyticsvidhya.com%2F)  
  
## Conclusion  
## Conclusion  
LangChain offers a robust framework for building applications with large language models. It provides features like conversational memory that enhance user experience and interaction quality. Its practical applications across various industries demonstrate its potential to revolutionize customer support, healthcare, education, and more.  
LangChain offers a robust framework for building applications with large language models. It provides features like conversational memory that enhance user experience and interaction quality. Its practical applications across various industries demonstrate its potential to revolutionize customer support, healthcare, education, and more.  
  
By democratizing LLM development, LangChain empowers developers and businesses to harness the power of advanced language models. As LangChain continues to evolve, it will play a crucial role in shaping the future of AI-driven applications.  
By democratizing LLM development, LangChain empowers developers and businesses to harness the power of advanced language models. As LangChain continues to evolve, it will play a crucial role in shaping the future of AI-driven applications.  
  
***Ready to master Generative AI? Join our ++[GenAI Pinnacle Program](https://www.analyticsvidhya.com/genaipinnacle?utm_source=blog_page&utm_medium=blog&utm_campaign=SEO)++ today and gain hands-on experience with LangChain and other cutting-edge concepts!***  
