# AI Agents with Google ADK - Complete Implementation Series

## Assignment Overview

This assignment explores building intelligent AI agents using Google's Agent Development Kit (ADK). Through four progressive implementations, we demonstrate the evolution from simple conversational agents to complex, tool-enabled agents that interact with databases and perform real-world tasks.

## Assignment Structure

### Part A: ADK Codelabs Implementation (3 Projects)

**Progressive learning through official Google codelabs, each building on previous concepts.**

### Part B: Custom Agent Application (1 Project)

**Independent implementation of an agent from the awesome-adk-agents hackathon repository.**

---

## Part A: Codelab Implementations

### 1. From Prototypes to Agents with ADK
**Goal:** Build a multi-tool agent demonstrating ADK fundamentals

**What I Built:**
- Renovation Agent with three integrated tools
- Custom function (cryptocurrency price lookup)
- Nested agent (Google Search specialist)
- Third-party integration (Wikipedia via LangChain)

**Key Learnings:**
- Multi-tool orchestration
- FunctionTool, AgentTool, and LangchainTool integration
- Streaming responses and session management
- Async architecture with InvocationContext

**Demo Highlights:**
- "What's the price of bitcoin?" → Custom function call
- "What's the weather in San Francisco?" → Search agent delegation
- "Tell me about the Eiffel Tower" → Wikipedia tool integration

---

### 2. Building AI Agents with ADK: Empowering with Tools
**Goal:** Understand ADK foundation and agent structure

**What I Built:**
- Personal Assistant Agent with core ADK components
- Clean project structure (agent.py, __init__.py, .env)
- Development workflow with both CLI and Web UI

**Key Learnings:**
- Agent anatomy (model, name, description, instruction)
- Vertex AI configuration and authentication
- Development UI vs Terminal interface
- Python packaging for agents

**Demo Highlights:**
- Agent creation with `adk create`
- Terminal interaction with `adk run`
- Web UI interaction with `adk web`
- Proper Markdown formatting and debug panels

---

### 3. Build a Travel Agent using MCP Toolbox and ADK
**Goal:** Connect agents to real databases via MCP Toolbox

**What I Built:**
- Hotel Search Agent with database integration
- Cloud SQL PostgreSQL with hotels data
- MCP Toolbox for Databases server
- Two database tools (search by name, search by location)

**Key Learnings:**
- MCP (Model Context Protocol) server setup
- Database tool configuration via tools.yaml
- Sources, Tools, and Toolsets architecture
- ToolboxSyncClient integration with ADK
- Real-time data queries from agents

**Demo Highlights:**
- "Which hotels are in Basel?" → Database query via MCP Toolbox
- "Tell me about the Hyatt Regency" → Name-based search
- Real data from Cloud SQL PostgreSQL
- Automatic tool selection by agent

---

## Part B: Custom Agent Application

### 4. Job Interview Agent (from awesome-adk-agents)
**Goal:** Build a practical agent application demonstrating learned concepts

**What We're Building:**
- Mock interview conducting agent
- Interactive Q&A flow for job candidates
- Response evaluation and feedback
- Role-specific interview questions

**Key Features:**
- Conducts structured job interviews
- Asks relevant technical/behavioral questions
- Evaluates candidate responses
- Provides constructive feedback
- Maintains conversation context

**Demo Highlights:**
- Agent asks interview questions
- Evaluates responses in real-time
- Provides feedback and scores
- Natural conversation flow

---

## Technology Stack

**Core Framework:**
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash / 2.0 Flash models
- Python 3.12+

**Infrastructure:**
- Google Cloud Platform
- Vertex AI
- Cloud SQL for PostgreSQL
- Cloud Shell / Cloud Shell Editor

**Additional Tools:**
- MCP Toolbox for Databases
- LangChain (for Wikipedia integration)
- CoinGecko API (for crypto prices)

---

## Project Progression
```
A: Basic Agent → Multiple Tools → Tool Orchestration
B: Foundation → Project Structure → Development Workflow
C: Database Integration → MCP Server → Real Data Access
Part B: Independent Application → Custom Implementation → Practical Use Case
```

---
## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [MCP Toolbox GitHub](https://github.com/GoogleCloudPlatform/genai-toolbox)
- [Awesome ADK Agents](https://github.com/Sri-Krishna-V/awesome-adk-agents)
- [Google Cloud Console](https://console.cloud.google.com)

---
