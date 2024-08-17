from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import json
import asyncio
strparser = StrOutputParser()
jsonparser = JsonOutputParser()
llm = ChatOpenAI(model="gpt-4o-mini")
chain = llm | jsonparser

# async def run_chain():
#     async for chunk in chain.astream( "output a list of the countries france, spain and japan and their populations in JSON format. "
#     'Use a dict with an outer key of "countries" which contains a list of countries. '
#     "Each country should have the key `name` and `population`"):
#         print(chunk, flush=True)

# asyncio.run(run_chain())

result = chain.invoke( "output a list of the countries france, spain and japan and their populations in JSON format. "
    'Use a dict with an outer key of "countries" which contains a list of countries. '
    "Each country should have the key `name` and `population`")

print(result)