from agent_definition import llm
from state import State


def wattpad_agent(state: State):
    """Write the documentation"""
    result = llm.invoke(state["input"])
    return {"output": result.content}