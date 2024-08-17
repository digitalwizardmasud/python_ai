from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import PydanticToolsParser
from pprint import pprint
from langchain_core.tools import tool
import json
from langchain_core.messages import HumanMessage
class AddTool(BaseModel):
    """Add two Integers."""
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")
    
class MultiplyTool(BaseModel):
    """Multiply two Integers."""
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")
    

llm = ChatOpenAI(model="gpt-4o-mini")
# llm_with_tools = llm.bind_tools([AddTool, MultiplyTool])

# result = llm_with_tools.invoke("what is 3*2 and 3+2")
# result = llm_with_tools.invoke(question).tool_calls

# chain = llm_with_tools | PydanticToolsParser(tools = [AddTool, MultiplyTool])
# result = chain.invoke("what is 3*2 and 3+2")

# pprint(result.tool_calls)


### Another Part 
@tool
def add(a:int, b:int) -> int:
    """Add a and b"""
    return a + b

@tool
def multiply(a:int, b:int) -> int:
    """Multiply a and b"""
    return a * b

query = "What is 3 * 12? Also, what is 11 + 49?"
messages = [HumanMessage(query)]
llm_with_tools = llm.bind_tools([add, multiply])
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)



for tool_call in ai_msg.tool_calls:
    selected_tool = {"add" : add,"multiply" : multiply}[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)
    pprint(tool_msg)

# pprint(messages)