import json
import random
import os
from swarms import Agent, RoundRobinSwarm
from swarm_models import OpenAIChat

current_dir = os.path.dirname(os.path.realpath(__file__))
personalities_path = os.path.abspath(os.path.join(current_dir, '..', 'personalities.json'))


llm = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="chatgpt-4o-latest", temperature=1
)


def load_agents_from_json(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        agent_data = json.load(file)

    agents = []

    for agent in agent_data:
        agent_instance = Agent(
            agent_name=agent["agent_name"],
            system_prompt=agent["system_prompt"],
            agent_description=agent["agent_description"],
            llm=llm,
            max_loops=agent["max_loops"],
            autosave=agent["autosave"],
            dashboard=agent["dashboard"],
            verbose=agent["verbose"],
            streaming_on=agent["streaming_on"],
            context_length=agent["context_length"]
        )
        agents.append(agent_instance)

    return agents


agents = load_agents_from_json(personalities_path)
swarm = RoundRobinSwarm(agents=agents, verbose=True, max_loops=1)

agent_index = 0

def get_ai_response():
    global agent_index
    agent = agents[agent_index]
    agent_index = (agent_index + 1) % len(agents)
    return swarm._execute_agent(agent, "tweet")