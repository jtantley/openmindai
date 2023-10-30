# OpenMindAI
# Version: AXYS
# Module: Text_Analyzer_Agent
# Filepath: `/agent/text_analyzer_agent.py`
# Updated: 10-28-2023

from autogen.agentchat.contrib import TextAnalyzerAgent
from typing import List, Dict, Optional, Callable, Union
from ..main import logger
from ops.config import get_api_key_for_model, get_misc_api_key


class TextAnalyzerAgent(TextAnalyzerAgent):
    def __init__(self,
                 name="analyzer",
                 system_message: Optional[str] = None,
                 human_input_mode: Optional[str] = "NEVER",
                 llm_config: Optional[Union[Dict, bool]] = None,
                 teach_config: Optional[Dict] = None,
                 **kwargs):
        super().__init__(name=name, system_message=system_message, human_input_mode=human_input_mode, llm_config=llm_config,
                         teach_config=teach_config, **kwargs)

    def analyze(self, text_to_analyze, analysis_instructions):
        """
        Asks TextAnalyzerAgent to analyze the given text according to specific instructions.

        Args:
            text_to_analyze (str): The text to be analyzed.
            analysis_instructions (str): Instructions for analysis.
        """
        # TextAnalyzerAgent must be initialized elsewhere
        analysis_result = TextAnalyzerAgent.analyze(
            text_to_analyze, analysis_instructions)
        return analysis_result
