import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination


async def main():
    print("Hello, World!")
    model_client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")
    math_teacher_agent = AssistantAgent(name="MathTeacher",model_client=model_client,system_message="You are a Math teacher that helps students with their math problems. Explain your reasoning step by step and provide the final answer at the end.")
    student_agent = AssistantAgent(name="Student",model_client=model_client,system_message="You are a student who needs help with math problems. Ask questions and seek clarification.")

    team = RoundRobinGroupChat(participants=[math_teacher_agent, student_agent], termination_condition=MaxMessageTermination(max_messages=5)).start()
    await Console(team.run_stream(task = "The student has a math problem: What is the area of an ellipse? The math teacher will help the student solve the problem step by step."))
    await model_client.close()
 
asyncio.run(main())