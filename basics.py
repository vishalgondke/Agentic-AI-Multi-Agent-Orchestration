import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


async def main():

    print("Hello, World!")
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
    assistant = AssistantAgent(name="assistant",model_client=model_client)
    await Console(assistant.run_stream(task = "What is the capital of France?"))
    await model_client.close()

asyncio.run(main())