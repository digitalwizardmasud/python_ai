from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

import os



model = OllamaLLM(model="llama3")
chat_history = []

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system", "You are AI Chatbot"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
)

chain = prompt_template | model

def start_app():
    while True:
        question = input("You: ")
        if(question=="done"):
            return
        response = chain.invoke({"input":question, "chat_history":chat_history})
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=response))
        print("AI: "+ response)

if __name__ ==  "__main__":
    start_app()