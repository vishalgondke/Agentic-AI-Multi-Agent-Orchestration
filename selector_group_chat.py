import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import MaxMessageTermination

from dotenv import load_dotenv
import json
load_dotenv()

system_message_researcher = f"""
You are a Researcher Agent.

Your role is to gather accurate, relevant, and up-to-date information about a given topic. 
You focus on facts, data, and structured insights rather than opinions.

Guidelines:
- Break down the query into subtopics if needed
- Provide clear, well-organized findings
- Prioritize correctness and completeness
- Avoid speculation or unsupported claims
- Include key points, definitions, and context

Do not write final polished content. Your output will be used by another agent.
"""

system_message_writer = f"""
You are a Writer Agent.

Your role is to transform research into clear, engaging, and well-structured content.

Guidelines:
- Write in a coherent, readable, and professional tone
- Organize content with logical flow
- Simplify complex ideas where possible
- Make the content engaging and easy to understand
- Do not introduce new facts that were not provided

Your goal is to produce high-quality final content based on the research input.
"""

system_message_critic = f"""
You are a Critic Agent.

Your role is to evaluate and improve content produced by another writeragent.

Guidelines:
- Identify inaccuracies, gaps, or unclear sections
- Suggest specific improvements
- Check for logical flow and coherence
- Ensure clarity, correctness, and completeness
- Be constructive and precise in feedback

Do not rewrite the entire content unless necessary. Focus on actionable feedback.
"""
async def main():
    model_client = OpenAIChatCompletionClient(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model_info={
            "family": "llama3",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": False 

        }
    )
    researcher_agent = AssistantAgent(name="ResearcherAgent",model_client=model_client,system_message=system_message_researcher)
    writer_agent = AssistantAgent(name="WriterAgent",model_client=model_client,system_message=system_message_writer)
    critic_agent = AssistantAgent(name="CriticAgent",model_client=model_client,system_message=system_message_critic)

    team = SelectorGroupChat(participants=[researcher_agent, writer_agent, critic_agent], model_client=model_client, termination_condition=MaxMessageTermination(max_messages=5),allow_repeated_speaker=True)
    await Console(team.run_stream(task = "Write a comprehensive 30 word article about the applications of artificial intelligence in healthcare."))
    await model_client.close()

asyncio.run(main())