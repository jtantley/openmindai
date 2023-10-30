# OpenMindAI
# Version: AXYS
# Module: Agent
# Filepath: `/agent/agent.py`
# Updated: 10-28-2023

# Import necessary modules and packages
from .conversable_agent import ConversableAgent
from .teachable_agent import TeachableAgent
from .text_analyzer_agent import TextAnalyzerAgent


class AgentManager:
    def __init__(self):
        self.conversable_agent = ConversableAgent(name="conversable")
        self.teachable_agent = TeachableAgent(name="teachable")
        self.text_analyzer_agent = TextAnalyzerAgent(name="analyzer")

    def get_conversable_agent(self):
        return self.conversable_agent

    def get_teachable_agent(self):
        return self.teachable_agent

    def get_text_analyzer_agent(self):
        return self.text_analyzer_agent

    def get_conversable_agent(self):
        return self.conversable_agent

    def get_teachable_agent(self):
        return self.teachable_agent

    def get_text_analyzer_agent(self):
        return self.text_analyzer_agent
