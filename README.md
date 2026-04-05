# 🚀 AgenticAI - Multi-Tool MCP Framework

AgenticAI is a modular framework for building **multi-agent systems** powered by LLMs.  
It enables intelligent agents to collaborate, reason, and execute tasks using tools like APIs, file systems, and automation workflows.

This project demonstrates how to design **scalable, tool-augmented AI systems** using a Multi-Tool MCP (Modular Control Platform) architecture.

---

## 🧠 What is this project?

Traditional AI apps rely on a single model.  
This project explores a more powerful approach:

👉 **Multiple specialized agents working together**

Each agent has a role:
- 🧑‍🔬 Researcher → gathers information  
- ✍️ Writer → creates structured content  
- 🧪 Critic → reviews and improves output  

These agents collaborate through orchestrated workflows to solve complex tasks.

---

## 🧩 Key Features

- 🔁 **Multi-Agent Collaboration**  
  Agents communicate and iterate to improve results

- 🧠 **LLM Provider Flexibility**  
  Works with OpenAI, Groq, or other OpenAI-compatible APIs

- 🛠️ **Tool Integration (MCP Design)**  
  Extend agents with:
  - Excel automation  
  - Database queries  
  - File system operations  
  - API calls (Postman)  
  - Browser automation (Playwright)

- 🔀 **Multiple Interaction Modes**
  - Selector-based group chat
  - Round-robin conversations
  - Human-in-the-loop workflows
  - Multimodal inputs (text + images)

---

## 🏗️ Architecture Overview

```text
User Task
   ↓
Orchestrator / Selector
   ↓
-------------------------
| Researcher Agent      |
| Writer Agent          |
| Critic Agent          |
-------------------------
   ↓
Final Output
