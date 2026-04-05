import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    print("Hello, World!")
    model_client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")
    assistant = AssistantAgent(name="MultiModalAssistant",model_client=model_client)
    image = Image.from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Iconic_image_of_Earth_from_space.jpg/2560px-Iconic_image_of_Earth_from_space.jpg").save("earth.jpg")
    multimodal_message = MultiModalMessage(content=["What is in this image?", image],source="user")

    await Console(assistant.run_stream(task = multimodal_message))
    await model_client.close()

asyncio.run(main())