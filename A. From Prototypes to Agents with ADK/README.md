# Renovation Agent (ADK) — Multi-Tool Demo

## Overview
This project is a small AI agent built with the Google Agent Development Kit (ADK). It answers everyday questions by orchestrating multiple capabilities: a custom crypto price lookup, a real-time web search specialist, and a Wikipedia knowledge tool. The agent uses Gemini 2.0 Flash for fast, tool-centric responses.

**Video walkthrough:** [Add your YouTube link here]

## Features
* **Multi-tool orchestration:** Combines a custom function, a search specialist agent, and a third-party (LangChain) tool.
* **Fast responses:** Uses Gemini 2.0 Flash optimized for tool calling.
* **Streaming UX:** The interactive runner streams replies as they're generated.
* **Clean structure:** Separate files for the root agent, tools, and the simple runner.

## How It Works
1. A root agent receives the user's prompt.
2. Based on intent, the agent selects and invokes the right tool:
   * **Crypto price tool** → fetches a live price from a public API.
   * **Search specialist agent** → retrieves fresh, real-world details (e.g., hours, dates).
   * **Wikipedia tool** → provides concise background knowledge.
3. The agent combines results into one coherent answer and streams the reply to the user.

## Project Structure
* `agent.py` — Defines the root agent and wires in all tools.
* `custom_functions.py` — Contains the crypto price function the agent can call.
* `custom_agents.py` — Defines the search specialist agent (used by the root agent as a tool).
* `third_party_tools.py` — Sets up the Wikipedia tool via LangChain.
* `main.py` — Minimal interactive runner (command-line chat with streamed replies).
* `requirements.txt` — Python dependencies for the project.

## Typical Demo Flow
1. Introduce the goal: a compact multi-tool ADK agent.
2. Show the file layout and briefly explain each piece.
3. Run the interactive chat and try three prompts:
   * "What is the price of bitcoin in USD right now?"
   * "Tell me about the history of Machu Picchu."
   * "What are the opening hours of the Louvre today?"
4. Point out how the agent chooses tools automatically and streams the answer.

## Setup & Installation

### Prerequisites
* Python 3.8+
* Google Cloud Project with Vertex AI enabled
* Google Cloud authentication configured

### Installation Steps
1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd renovation_agent
```

2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Set up environment variables:
```bash
   export PROJECT_ID=$(gcloud config get-value project)
   export LOCATION="us-central1"
```

5. Run the agent:
```bash
   python -m renovation_agent.main
```

## Configuration Notes
* Supports Vertex AI-based Gemini with Google Cloud authentication.
* Project ID and location are configured via environment variables.
* The agent uses `gemini-2.0-flash-exp` model by default.

## Limitations & Next Steps
* Demo-level error handling; consider adding retries, timeouts, and input validation.
* Add more tools (calendar, email, databases) or a small web UI for richer UX.
* Consider persistence, logging, and evaluation for production readiness.
* The crypto price function currently uses CoinGecko API which may have rate limits.

## Acknowledgments
Built with Google Agent Development Kit (ADK) and powered by Gemini models.
