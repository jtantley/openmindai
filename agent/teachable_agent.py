# OpenMindAI
# Version: AXYS
# Module: Teachable_Agent
# Filepath: `/agent/teachable_agent.py`
# Updated: 10-28-2023

from autogen.agentchat.contrib import TeachableAgent as AutoGenTeachableAgent
from typing import List, Dict, Optional, Callable, Union
from db.database import MemoStore
from ..main import logger
from ops.config import get_api_key_for_model, get_misc_api_key


class TeachableAgent(AutoGenTeachableAgent):
    def __init__(self,
                 name="TeachableAgent",
                 system_message: Optional[str] = "You are a helpful AI assistant that remembers user teachings from prior chats.",
                 human_input_mode: Optional[str] = "NEVER",
                 llm_config: Optional[Union[Dict, bool]] = None,
                 analyzer_llm_config: Optional[Union[Dict, bool]] = None,
                 teach_config: Optional[Dict] = None,
                 **kwargs):
        super().__init__(name=name, system_message=system_message, human_input_mode=human_input_mode, llm_config=llm_config,
                         teach_config=teach_config, **kwargs)
        self.analyzer_llm_config = analyzer_llm_config
        self.initialize_memostore(teach_config)

    def initialize_memostore(self, teach_config):
        try:
            self.memo_store = MemoStore(
                verbosity=teach_config.get("verbosity", 0),
                reset=teach_config.get("reset_db", False),
                path_to_db_dir=teach_config.get("path_to_db_dir", "/db/app.db")
            )
            logger.info("TEACHABLE-AGENT: Successfully initialized MemoStore.")
        except Exception as e:
            logger.error(
                f"TEACHABLE-AGENT: Error in initializing MemoStore: {e}")
            raise RuntimeError(
                f"TEACHABLE-AGENT: Error in initializing MemoStore: {e}")

        if teach_config.get("prepopulate", True):
            try:
                self.memo_store.prepopulate()
                logger.info(
                    "TEACHABLE-AGENT: Successfully prepopulated MemoStore.")
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
                self.consider_memo_storage(comment)

    def consider_memo_storage(self, comment):
        """
        Decides whether to store something from one user comment in the DB.

        Args:
            comment (str): The user comment.
        """
        # Example logic to decide whether to store the comment
        if len(comment.split()) > 3:
            self.memo_store.add_input_output_pair(comment, "Sample Output")

    def consider_memo_retrieval(self, comment):
        """
        Decides whether to retrieve memos from the DB, 
        and add them to the chat context.
        """
        # Placeholder logic to decide whether to retrieve memos
        if "recall" in comment.lower():
            relevant_memos = self.retrieve_relevant_memos(comment)
            concatenated_memos = self.concatenate_memo_texts(relevant_memos)
            self.chat_context += concatenated_memos

    def retrieve_relevant_memos(self, input_text):
        """
        Returns semantically related memos from the DB.

        Args:
            input_text (str): The input text.

        Returns:
            list: A list of relevant memos.
        """
        return self.memo_store.get_related_memos(
            input_text,
            n_results=self.teach_config.get("max_num_retrievals", 10),
            threshold=self.teach_config.get("recall_threshold", 1.5)
        )

    def concatenate_memo_texts(self, memo_list):
        """
        Concatenates the memo texts into a single string for inclusion in the chat context.

        Args:
            memo_list (list): A list of memos.
        """
        return ' '.join([memo['input_text'] for memo in memo_list])

    def start_chat(self):
        """
        Integrates with chat_manager.py to start a chat session.
        """
        from ops.chat_manager import ChatManager  # Importing here to avoid circular imports
        chat_manager = ChatManager(self)
        chat_manager.start_chat()
