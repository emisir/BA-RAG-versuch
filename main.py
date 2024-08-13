from dotenv import load_dotenv
load_dotenv()

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent.legacy.react.base import ReActAgent
from llama_index.llms.openai import OpenAI
from bundesliga import bundesliga_query_engine
from thirdLiga import thirdLiga_query_engine
from secondBundesliga import secondBundesliga_query_engine
from prompts import context



tools = [
    QueryEngineTool(
        query_engine=bundesliga_query_engine,
        metadata=ToolMetadata(
            name="bundesliga",
            description="This tool provides information about the Football player statistics in Bundesliga",
        ),
    ),
    QueryEngineTool(
        query_engine=secondBundesliga_query_engine,
        metadata=ToolMetadata(
            name="secondBundesliga",
            description="This tool provides information about the Football player statistics in secondBundesliga",
        ),
    ),
    QueryEngineTool(
        query_engine=thirdLiga_query_engine,
        metadata=ToolMetadata(
            name="thirdLiga",
            description="This tool provides information about the Football player statistics in thirdLiga",
        ),
    ),
]

llm = OpenAI(model="gpt-4o")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)