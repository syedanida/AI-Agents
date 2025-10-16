from google.adk.agents import Agent
from google.adk.tools import google_search

# Search specialist agent using the built-in google_search tool
google_search_agent = Agent(
    model="gemini-2.5-flash",
    name="google_search_agent",
    description="A search agent that uses Google Search to get latest information about current events, weather, or business hours.",
    instruction="Use Google Search to answer user questions about real-time, logistical information.",
    tools=[google_search],
)