# OpenMindAI
# Version: AXYS
# Module: Conversable_Agent
# Filepath: `/agent/conversable_agent.py`
# Updated: 10-28-2023

import openai
from autogen.agentchat import ConversableAgent
from typing import List, Dict, Optional, Callable, Union
from db.database import MemoStore
from ..main import logger
from ops.config import get_api_key_for_model, get_misc_api_key

from autogen.agentchat import ConversableAgent
from typing import List, Dict, Optional, Callable, Union
from ..main import logger
from ops.config import get_api_key_for_model, get_misc_api_key


class ConversableAgent(ConversableAgent):
    def __init__(self, name: str = "ConversableAgent",
                 system_message: Optional[str] = "You are a helpful AI Assistant eager to learn and have conversations.",
                 human_input_mode: Optional[str] = "TERMINATE",
                 llm_config: Optional[Union[Dict, bool]] = None):
        super().__init__(name=name, system_message=system_message,
                         human_input_mode=human_input_mode, llm_config=llm_config)
        self.chat_history: List[Dict] = []  # Added type hint

    def get_human_input(self, prompt: str) -> str:
        try:
            logger.info("CONVERSABLE-AGENT: Successfully got human input.")
            return input(prompt)
        except Exception as e:
            logger.error(
                f"CONVERSABLE-AGENT: Error in getting human input: {e}")
            return f"CONVERSABLE-AGENT: Sorry, I couldn't get your input. Error: {e}"

    def generate_reply(self, messages: Optional[List[Dict]] = None) -> Union[str, Dict, None]:
        if self.llm_config:
            try:
                response = openai.Completion.create(
                    engine="gpt-4",
                    prompt=messages[-1]['content'] if messages else '',
                    max_tokens=150
                )
                logger.info("CONVERSABLE-AGENT: Successfully generated reply.")
                return response.choices[0].text.strip()
            except Exception as e:
                logger.error(
                    f"CONVERSABLE-AGENT: Error in generating reply: {e}")
                return f"CONVERSABLE-AGENT: Sorry, I couldn't generate a response. Error: {e}"
        else:
            logger.error("CONVERSABLE-AGENT: I'm not configured to reply.")
            return "CONVERSABLE-AGENT: I'm not configured to reply."
