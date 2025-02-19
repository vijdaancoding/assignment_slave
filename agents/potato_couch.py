"""
Potato Couch. Agent that reads, routes and merges.
"""


from pydantic import BaseModel, Field

from typing_extensions import Literal, TypedDict
from langchain_core.messages import HumanMessage, SystemMessage

from agent_definition import llm

#Routing Schema 
class Router(BaseModel):
    step: Literal["documentation", "code", "hybrid"] = Field(
        None, description="Choosing what type of assignment we are dealing with"
    )

router = llm.with_structured_output(Router)

#State
class State(TypedDict):
    input: str
    decision: str
    output: str








