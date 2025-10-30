from strands import Agent, tool
from strands_tools import calculator  # Import the calculator tool
import argparse
import json
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel


@tool
def weather():
    """Get weather"""  # Dummy implementation
    return "sunny"


model_id = "au.anthropic.claude-haiku-4-5-20251001-v1:0"

model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather.",
)


def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    response = agent(user_input)
    return response.message["content"][0]["text"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=str)
    args = parser.parse_args()
    response = strands_agent_bedrock(json.loads(args.payload))
