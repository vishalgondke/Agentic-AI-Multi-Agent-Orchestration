import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import json
load_dotenv()

async def main():
    print("Hello, World!")
    # model_client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")
    model_client = OpenAIChatCompletionClient(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model_info={
            "family": "llama3",
            "vision": False,
            "function_calling": True,
            "json_output": True
        }
    )
    primary_agent = AssistantAgent(name="Helper",model_client=model_client)
    backup_agent = AssistantAgent(name="BackupHelper",model_client=model_client)
    
    await Console(primary_agent.run_stream(task = "My favourite song is Blue moon."))
    state = await primary_agent.save_state()
    with open("model_state.json", "w") as f:
        json.dump(state, f) 

    with open("model_state.json", "r") as f:
        saved_state = json.load(f)
    await backup_agent.load_state(saved_state)
    await Console(backup_agent.run_stream(task = "What is my favourite song?"))
    await model_client.close()

asyncio.run(main())