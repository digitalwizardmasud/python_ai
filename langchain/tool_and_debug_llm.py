from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.globals import set_verbose, set_debug
from langchain.tools import BaseTool
from langchain_core.tools import Tool, StructuredTool
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

set_verbose(True)
set_debug(True)

jsonparser = JsonOutputParser()

chat_history = [HumanMessage("I am Masud. I am 20 years old. What is your name?"), AIMessage("I am RoboAI. I am 2 years old")]
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. and always generate json output",
        ),
       MessagesPlaceholder(variable_name="chat_history"),
        ("placeholder", "{chat_history}"),
        ("placeholder", "{agent_scratchpad}"),
        ("human", "{input}"),
    ]
)
llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )


search = SerpAPIWrapper() 
tools = [
    StructuredTool.from_function(
        name="Search",
        func=search.run,
        description="A search engine. Useful for when you need to answer questions about current events. Input should be a search query.",
    ),
   
]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
result = agent_executor.invoke({
    "input": "Todays date? make it json ",
    "chat_history" : chat_history
})

print(result)