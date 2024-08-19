#source: https://python.langchain.com/v0.2/docs/tutorials/chatbot/
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import (BaseChatMessageHistory, InMemoryChatMessageHistory)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.globals import set_verbose, set_debug
from langchain_core.prompts import ChatPromptTemplate

# set_verbose(True)
# set_debug(True)

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

### Normal Message History
# messages = [
#     HumanMessage(content="Hi! I'm Bob"),
#     AIMessage(content="Hello Bob! How can I assist you today?"),
#     HumanMessage(content="What's my name?")
# ]
# chain =  model | parser
# result = chain.invoke(messages)
# print(result)


### Best Message History
store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatprompt = ChatPromptTemplate.from_messages([
    ('system', 'You are helpful assistant. Answer all question to the best of your ability in {language}'),
    ("placeholder", "{messages}")
])
chain = chatprompt | model | parser
with_message_history = RunnableWithMessageHistory( chain, get_session_history, input_messages_key="messages")
config = {"configurable": {"session_id": "abc2"}} # use uuid for session_id

try: 
    def runapp():
        question = input("==> Ask me: ")
        response = with_message_history.invoke({
                'messages' : [HumanMessage(question)],
                'language' : 'spanish'
            }, config=config)
        print(response, 'response')
        runapp()
    runapp()
except Exception as e:
    print(e, 'error')