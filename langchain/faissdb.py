from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
import chromadb
from langchain_community.document_loaders import PyPDFLoader, PDFPlumberLoader
from pprint import pprint
from langchain_community.utilities import SerpAPIWrapper


embeddings = OllamaEmbeddings(model="nomic-embed-text")
# embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


loader = PyPDFLoader("../data/resume.pdf")

# loader = PyPDFLoader(
#     file_path = "../data/resume.pdf",
#     extract_images = False,
# )
docs = loader.load()
pages = [x.page_content for x in docs]


###### Faiss DB
vectorstore = FAISS.from_texts(
    pages,
    embedding=embeddings,
)

##### Chroma DB
# persistent_client = chromadb.PersistentClient(path = "../chroma")
# collection = persistent_client.get_or_create_collection("resumeopenai")
    
# vectorstore = Chroma(
#     client=persistent_client,
#     collection_name="resumeopenai",
#     embedding_function=embeddings,
# )
    

llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

retriever = vectorstore.as_retriever()
retriever_chain = (
    {
        # "context" : SerpAPIWrapper().run,
        "context" : retriever.with_config(run_name="Docs"),
        "question" : RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

# for chunk in retriever_chain.stream("who is masud?"):
#     print(chunk, end="")

def start():
    question = input("=> Ask me: ")
    print(retriever_chain.invoke(question), 'with chain')
    start()
start()

