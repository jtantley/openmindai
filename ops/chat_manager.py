# Teachable AI
# Version: AXYS
# Module: Chat Manager
# Filepath: `/ops/chat_manager.py`
# Updated: 10-28-2023

import openai
from typing import Union, Dict, List, Optional
from main import logger
import db.database as db


class ChatManager:
    """
    Manages the chat functionalities for a TeachableAgent.
    """

    def __init__(self, teachable_agent):
        """
        Initialize the ChatManager.

        Args:
            teachable_agent (TeachableAgent): The TeachableAgent instance that this ChatManager belongs to.
        """
        self.teachable_agent = teachable_agent
        self.chat_history = []

    def get_human_input(self, prompt: str) -> str:
        """
        Gets human input from the terminal.

        Args:
            prompt (str): The prompt to display.

        Returns:
            str: The user's input.
        """
        return input(prompt)

    def generate_reply(self, messages: Optional[List[Dict]] = None) -> Union[str, Dict, None]:
        """
        Generates a reply using the language model.

        Args:
            messages (Optional[List[Dict]]): The message history.

        Returns:
            Union[str, Dict, None]: The generated reply.
        """
        # Implementation of generating reply using language model
        if self.teachable_agent.llm_config:
            try:
                response = openai.Completion.create(
                    engine="gpt-4",
                    prompt=messages[-1]['content'] if messages else '',
                    max_tokens=150
                )
                return response.choices[0].text.strip()
            except Exception as e:
                logger.error(f"CHAT MANAGER: Error in generating reply: {e}")
                return f"CHAT MANAGER: Sorry, I couldn't generate a response. Error: {e}"
        else:
            return "CHAT MANAGER: I'm not configured to reply."

    def start_chat(self):
        """
        Starts a terminal-based chat with the user.
        """
        print(
            f"{self.teachable_agent.name}: Hello! {self.teachable_agent.system_message}")
        while True:
            user_input = self.get_human_input("You: ")
            if user_input.lower() == "quit":
                print(f"{self.teachable_agent.name}: Goodbye!")
                self.teachable_agent.close_db()
                break

            # Retrieve relevant memos from the database
            relevant_memos = self.teachable_agent.retrieve_relevant_memos(
                user_input)
            memo_texts = self.teachable_agent.concatenate_memo_texts(
                relevant_memos)

            # Generate a response using GPT-4 LLM model
            try:
                response = openai.Completion.create(
                    engine="gpt-4",
                    prompt=f"{user_input}\n{memo_texts}",
                    max_tokens=150
                )
                agent_response = response.choices[0].text.strip()
            except Exception as e:
                logger.error(
                    f"CHAT MANAGER: Error in generating response: {e}")
                agent_response = f"CHAT MANAGER: Sorry, I couldn't generate a response. Error: {e}"

            print(f"{self.teachable_agent.name}: {agent_response}")
