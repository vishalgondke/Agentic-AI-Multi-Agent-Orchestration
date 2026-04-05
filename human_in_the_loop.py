import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat


async def main():
    print("Hello, World!")
    model_client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")
    math_teacher_agent = AssistantAgent(name="MathTeacher",model_client=model_client,system_message="You are a Math teacher that helps user with their math problems. Explain your reasoning step by step and provide the final answer at the end. When user says something like 'Thanks, that is helpful!' or 'Thank you!' or 'That is all I needed help with.' or 'That is all I needed help with, thanks!' or 'That is all I needed help with, thank you!' or 'That is all I needed help with, thanks a lot!' or 'That is all I needed help with, thank you very much!', that means the user has no more questions and the conversation should end and acknowledge and say 'Lesson complete'.")
    user_proxy_agent = UserProxyAgent(name="Student")
    team = RoundRobinGroupChat(participants=[math_teacher_agent, user_proxy_agent], termination_condition=TextMentionTermination(terminate_strings=["Lesson complete"])).start()
    await Console(team.run_stream(task = "I need help with bernoulli distribution. Can you explain it to me?"))
    await model_client.close()
 
asyncio.run(main())