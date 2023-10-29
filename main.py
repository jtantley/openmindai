# Teachable AI
# Version: AXYS
# Module: MAIN
# Filepath: `/main.py`
# Updated: 10-28-2023

from agent import ConversableAgent, TeachableAgent
from ops.chat_manager import ChatManager
from db.database import MemoStore
from ops.config import logger, get_api_key_for_model, get_misc_api_key

# Now you can use logger and get_api_key_for_model in main.py
logger.debug("This is a debug message from main.py")


def main():
    # Initialize a TeachableAgent named "Axys"
    axys_agent = TeachableAgent(name="Axys")

    # Initialize a ChatManager for the TeachableAgent
    axys_chat_manager = ChatManager(teachable_agent=axys_agent)

    # Start the terminal-based chat
    axys_chat_manager.start_chat()


if __name__ == "__main__":
    main()
