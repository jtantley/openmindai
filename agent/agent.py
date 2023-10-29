# OpenMindAI
# Version: AXYS
# Module: Agent
# Filepath: `/agent/agent.py`
# Updated: 10-28-2023

import openai
from autogen.agentchat import ConversableAgent
from autogen.agentchat.contrib import TeachableAgent, TextAnalyzerAgent
from typing import List, Dict, Optional, Union
import db.database as db
from db.database import MemoStore  # Import MemoStore from db file
from ..main import logger, get_api_key_from_model, get_misc_api_key


class ConversableAgent:
    def __init__(self, name: str,
                 system_message: Optional[str] = "You are a helpful AI Assistant eager to learn.",
                 human_input_mode: Optional[str] = "TERMINATE",
                 llm_config: Optional[Union[Dict, bool]] = None):
        self.name = name
        self.system_message = system_message
        self.human_input_mode = human_input_mode
        self.llm_config = llm_config
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


class TeachableAgent:
    """
    Teachable Agent, a subclass of ConversableAgent using a vector database to remember user teachings.
    """

    def __init__(self,
                 name="teachableagent",
                 system_message: Optional[str] = "You are a helpful AI assistant that remembers user teachings from prior chats.",
                 human_input_mode: Optional[str] = "NEVER",
                 llm_config: Optional[Union[Dict, bool]] = None,
                 analyzer_llm_config: Optional[Union[Dict, bool]] = None,
                 teach_config: Optional[Dict] = None,
                 **kwargs):
        """
        Initialize the TeachableAgent.

        Args:
            name (str): Name of the agent.
            system_message (Optional[str]): System message for the ChatCompletion inference.
            human_input_mode (Optional[str]): This agent should NEVER prompt the human for input.
            llm_config (Optional[Union[Dict, bool]]): LLM inference configuration.
            analyzer_llm_config (Optional[Union[Dict, bool]]): LLM inference configuration passed to TextAnalyzerAgent.
            teach_config (Optional[Dict]): Additional parameters used by TeachableAgent.
            **kwargs: Other keyword arguments.
        """
        self.name = name
        self.system_message = system_message
        self.human_input_mode = human_input_mode
        self.llm_config = llm_config
        self.analyzer_llm_config = analyzer_llm_config
        self.teach_config = teach_config if teach_config else {}

        # Initialize MemoStore for this TeachableAgent
        try:
            self.memo_store = MemoStore(
                verbosity=self.teach_config.get("verbosity", 0),
                reset=self.teach_config.get("reset_db", False),
                db_filename=self.teach_config.get(
                    "db_filename", "/db/axys.db")
            )
            logger.info("TEACHABLE-AGENT: Successfully initialized MemoStore.")
        except Exception as e:
            logger.error(
                f"TEACHABLE-AGENT: Error in initializing MemoStore: {e}")
            raise RuntimeError(
                f"TEACHABLE-AGENT: Error in initializing MemoStore: {e}")

        if self.teach_config.get("prepopulate", True):
            try:
                self.memo_store.prepopulate()
                logger.info(
                    "TEACHABLE-AGENT: Successfully prepoulated MemoStore.")
            except Exception as e:
                logger.error(
                    f"TEACHABLE-AGENT: Error in prepopulating MemoStore: {e}")
                raise RuntimeError(
                    f"TEACHABLE-AGENT: Error in prepopulating MemoStore: {e}")

    def close_db(self):
        """
        Cleanly closes the memo store.
        """
        try:
            self.memo_store.close()
            logger.info("TEACHABLE-AGENT: Successfully closed MemoStore.")
        except Exception as e:
            logger.error(f"TEACHABLE-AGENT: Error in closing MemoStore: {e}")
            raise RuntimeError(
                f"TEACHABLE-AGENT: Error in closing MemoStore: {e}")

    def prepopulate_db(self):
        """
        Adds a few arbitrary memos to the DB.
        """
        try:
            self.memo_store.prepopulate()
            logger.info("TEACHABLE-AGENT: Successfully prepoulated MemoStore.")
        except Exception as e:
            logger.error(
                f"TEACHABLE-AGENT: Error in prepopulating MemoStore: {e}")
            raise RuntimeError(
                f"TEACHABLE-AGENT: Error in prepopulating MemoStore: {e}")

    def learn_from_user_feedback(self):
        """
        Reviews the user comments from the last chat, 
        and decides what teachings to store as memos.
        """
    for message in self.chat_history:
        if message['role'] == 'user':
            comment = message['content']
            # Analyzing user comment to decide what to store
            if self.should_store(comment):
                self.memo_store.add_memo(comment)
            # ... further analysis and action

    def should_store(self, comment):
        """
        A helper method to determine whether a comment should be stored.
        This is a simplistic example and should be replaced with your actual logic.
        """
        # Replace with your actual logic
        return True if len(comment.split()) > 3 else False

    def consider_memo_storage(self, comment):
        """
        Decides whether to store something from one user comment in the DB.

        Args:
            comment (str): The user comment.
        """
        # Placeholder for now, the actual implementation would depend on certain conditions for memo storage.
        pass

    def consider_memo_storage(self, comment):
        """
        Decides whether to store something from one user comment in the DB.

        Args:
            comment (str): The user comment.
        """
    # Example logic to decide whether to store the comment
    if self.should_store(comment):
        self.memo_store.add_memo(comment)

    def concatenate_memo_texts(self, memo_list):
        """
        Concatenates the memo texts into a single string for inclusion in the chat context.

        Args:
            memo_list (list): A list of memos.
        """
        concatenated_text = ' '.join([memo['text'] for memo in memo_list])
        return concatenated_text

    def retrieve_relevant_memos(self, input_text):
        """
        Returns semantically related memos from the DB.

        Args:
            input_text (str): The input text.

        Returns:
            list: A list of relevant memos.
        """
        try:
            return self.memo_store.get_related_memos(
                input_text,
                n_results=self.teach_config.get("max_num_retrievals", 10),
                threshold=self.teach_config.get("recall_threshold", 1.5)
            )
        except Exception as e:
            logger.error(
                f"TEACHABLE-AGENT: Error in retrieving relevant memos: {e}")
            raise RuntimeError(
                f"TEACHABLE-AGENT: Error in retrieving relevant memos: {e}")

    def analyze(self, text_to_analyze, analysis_instructions):
        """
        Asks TextAnalyzerAgent to analyze the given text according to specific instructions.

        Args:
            text_to_analyze (str): The text to be analyzed.
            analysis_instructions (str): Instructions for analysis.
        """
        # Assuming TextAnalyzerAgent is initialized elsewhere
        analysis_result = TextAnalyzerAgent.analyze(
            text_to_analyze, analysis_instructions)
        return analysis_result
