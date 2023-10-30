# OpenMindAI
# Version: AXYS
# Module: Chat Manager
# Filepath: `/ops/chat_manager.py`
# Updated: 10-28-2023

from typing import Union, Dict, List, Optional
from main import logger
from agent.agent import AgentManager
import db.database as db


class ChatManager:
    """
    Manages the chat functionalities for AgentManager.
    """

    def __init__(self, agent_manager: AgentManager):
        try:
            logger.info(
                f"CHAT MANAGER: Successfully initialized ChatManager class.")
            self.agent_manager = agent_manager
            self.chat_history = []
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error ininitializing ChatManager class: {e}")

    def handle_user_input(self, user_input: str):
        """
        Handles user input by passing it through the various agents.
        """
        # Analyze the text
        try:
            logger.info(f"CHAT MANAGER: Successfully got text analyzer agent.")
            analyzer = self.agent_manager.get_text_analyzer_agent()
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in getting TextAnalyzerAgent: {e}")
        try:
            logger.info(
                f"CHAT MANAGER: Successfully got analyzer.analyze(user_input): {user_input}")
            analysis = analyzer.analyze(
                user_input, "Analyze the text carefully")
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error executing `analyze` function: {e}")

        # Teachable agent considers memo storage or retrieval based on analysis and user input
        try:
            logger.info(f"CHAT MANAGER: Successfully got teachable agent.")
            teachable = self.agent_manager.get_teachable_agent()
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in getting TeachableAgent: {e}")
        try:
            logger.info(
                f"CHAT MANAGER: Successfully got teachable.consider_memo_retrieval(user_input): {user_input}")
            teachable.consider_memo_storage(user_input)
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in getting teachable.consider_memo_retrieval(user_input)")

        # Conversable agent generates a reply
        try:
            logger.info(f"CHAT MANAGER: Successfully got conversable agent.")
            conversable = self.agent_manager.get_conversable_agent()
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in getting ConversableAgent: {e}")
        try:
            logger.info(
                f"CHAT MANAGER: Successfully got conversable.generate_reply(user_input): {user_input}")
            reply = conversable.generate_reply(
                [{'role': 'user', 'content': user_input}])
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in getting conversable.generate_reply(user_input): {e}")
        try:
            logger.info(f"CHAT MANAGER: Successfully returned reply: {reply}")
            return reply
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Error in returning reply: {e}")

    def start_chat(self):
        """
        Starts a terminal-based chat with the user.
        """
        print("Hello! How can I assist you today?")
        try:
            while True:
                user_input = input("> ")
                if user_input.lower() == "quit":
                    print("Goodbye!")
                    self.agent_manager.get_teachable_agent().close_db()
                    break

                reply = self.handle_user_input(user_input)
                print(reply)
        except Exception as e:
            logger.error(
                f"CHAT MANAGER: Catch-all error in start_chat: {e}")
