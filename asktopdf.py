from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from pprint import pprint
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import chromadb
from langchain_openai import OpenAIEmbeddings
from uuid import uuid4
from dotenv import load_dotenv
from uuid import uuid4
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
try:
    # LOAD PDF 
    loader = PyPDFLoader(
    file_path = "./data/history.pdf",
    extract_images = False,
    )
    docs = loader.lazy_load()
    
    # loader = DirectoryLoader("./data", glob="**/*.txt", loader_cls=TextLoader)
    # docs = loader.load()
    
    # SPLIT DOCUMENT 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    
    # text_splitter = CharacterTextSplitter(
    #     separator="\n\n",
    #     chunk_size=100,
    #     chunk_overlap=20,
    #     length_function=len,
    #     is_separator_regex=False,
    # )

    splitted_docs = text_splitter.split_documents(docs)
    
    # EMBEDDING 
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    # Vector DB 
    persistent_client = chromadb.PersistentClient()
    collection = persistent_client.get_or_create_collection("historycollection")
    
    vector_store = Chroma(
        client=persistent_client,
        collection_name="historycollection",
        embedding_function=embeddings,
    )
    # uuids = [str(uuid4()) for _ in range(len(splitted_docs))]
    # vector_store.add_documents(documents=splitted_docs, ids=uuids)
    
    
    # Retrival Data
    # results = vector_store.similarity_search("write a summary for A Land of Water", k=2)
    # for x in results:
    #     pprint(x)
    
    
    llm = ChatOllama(
        model="llama3",
        temperature=0,
    )
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "You are RoboAI, an AI Assistant"),
    #     ("human", "{input}")
    # ])
    # chain = prompt | llm
    # output = chain.invoke({
    #     "input" : "write a summary within 200 character"
    # })
    # pprint(output)
    
    query_prompt = PromptTemplate(
        input_variables = ["question"],
        template = """
        You are AI language model assistant. your task is to generate five different versions of the given user question to retrieve relevant documents from a vector database. Original Question is {question}
        """
    )
    retriever = MultiQueryRetriever.from_llm(
        vector_store.as_retriever(),
        llm,
        prompt=query_prompt
    )
    
    template = """
    Answer the question based ONLY on the following context: {context}
    Question: {question}
    """
    chatPrompt = ChatPromptTemplate.from_template(template)
    chain = (
        {"context": retriever, "question":RunnablePassthrough()}
        | chatPrompt
        | llm
        | StrOutputParser()
    )
    result = chain.invoke("who is the prime minister of bangladesh")
    print(result)
except Exception as e:
    pprint(e)
