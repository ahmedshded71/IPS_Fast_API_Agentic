import os
from typing import Optional, List, Any
from AgentEnums import AgentProvider
from .BaseAgent import BaseAgent
from google.adk.models.lite_llm import LiteLlm

MODEL_GPT_4O = os.getenv("MODEL_GPT_4O", "openai/gpt-4o")
LAMA_MODEL = os.getenv("LAMA_MODEL", "gemma2:9b-instruct-q5_0")

class AgentProviderFactory:
    def __init__(self, name: str, provider: str, tools: List[Any],
                 user_id: str, session_id: str,
                 description: Optional[str] = None, 
                 instruction: Optional[str] = None):

        self.name = name
        self.provider = provider
        self.description = description or ""
        self.instruction = instruction or ""
        self.tools = tools
        self.user_id = user_id
        self.session_id = session_id

    def create(self) -> Optional[BaseAgent]:
        if self.provider == AgentProvider.OPENAI.value:
            return BaseAgent(
                name=self.name,
                AgentModel=LiteLlm(model=MODEL_GPT_4O), 
                description=self.description,
                instruction=self.instruction,
                tools=self.tools,
                user_id=self.user_id,
                session_id=self.session_id
            )

        elif self.provider == AgentProvider.GEMINI.value:
            return BaseAgent(
                name=self.name,
                AgentModel=LAMA_MODEL, 
                description=self.description,
                instruction=self.instruction,
                tools=self.tools,
                user_id=self.user_id,
                session_id=self.session_id
            )

        elif self.provider == AgentProvider.CLOUD.value:
            MODEL_CLAUDE = os.getenv("MODEL_CLAUDE_SONNET", "anthropic/claude-3-5-sonnet")
            return BaseAgent(
                name=self.name,
                AgentModel=LiteLlm(model=MODEL_CLAUDE),
                description=self.description,
                instruction=self.instruction,
                tools=self.tools,
                user_id=self.user_id,
                session_id=self.session_id
            )

        else:
            print(f"Provider '{self.provider}' not supported.")
            return None