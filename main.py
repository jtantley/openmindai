# Teachable AI
# Version: AXYS
# Module: MAIN
# Filepath: `/main.py`
# Updated: 10-28-2023

from agent.agent import AgentManager
from ops.chat_manager import ChatManager
from ops.config import logger

# Now you can use logger in main.py
logger.debug("MAIN FILE: This is a debug message from main.py.")


def main():
    # Initialize an AgentManager
    axys_agent_manager = AgentManager()

    # Initialize a ChatManager for the AgentManager
    axys_chat_manager = ChatManager(agent_manager=axys_agent_manager)

    # Start the terminal-based chat
    axys_chat_manager.start_chat()


if __name__ == "__main__":
    main()
