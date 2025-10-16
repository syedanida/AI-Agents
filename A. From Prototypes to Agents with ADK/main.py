"""Main script to run the renovation agent (interactive)."""

import asyncio
from google.adk.agents import InvocationContext
from renovation_agent.agent import root_agent

async def chat_with_agent():
    print("🏗️  Renovation Agent Ready!")
    print("Ask me about crypto prices, search the web, or learn via Wikipedia.")
    print("Type 'quit' or 'exit' to stop.\n")

    loop = asyncio.get_event_loop()
    while True:
        try:
            user_input = await loop.run_in_executor(None, input, "You: ")
            user_input = user_input.strip()
            if user_input.lower() in {"quit", "exit", "q"}:
                print("Goodbye! 👋")
                break
            if not user_input:
                continue

            ctx = InvocationContext(agent=root_agent, user_content=user_input)
            print("Agent: ", end="", flush=True)
            async for event in root_agent.run_live(ctx):
                if hasattr(event, "text") and event.text:
                    print(event.text, end="", flush=True)
                elif hasattr(event, "content") and event.content:
                    print(event.content, end="", flush=True)
            print()

        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

def main():
    asyncio.run(chat_with_agent())

if __name__ == "__main__":
    main()