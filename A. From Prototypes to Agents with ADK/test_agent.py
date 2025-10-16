import sys
sys.path.insert(0, '..')

from renovation_agent.agent import root_agent

# Check what methods are available
print("Agent type:", type(root_agent))
print("\nAvailable methods:")
methods = [x for x in dir(root_agent) if not x.startswith('_') and callable(getattr(root_agent, x))]
for method in methods:
    print(f"  - {method}")

# Try to get help
print("\nAgent object:", root_agent)
