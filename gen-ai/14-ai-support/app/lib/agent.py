import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent
)

from .tools import tools
from ..constants import SUPPORT_AGENT_PROMPT

load_dotenv(dotenv_path=".env")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

def getAgent():
  prompt = ChatPromptTemplate.from_messages([
    ("system", SUPPORT_AGENT_PROMPT),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
  ])
  
  agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
  )
  
  agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True
  )
  
  return agent_executor