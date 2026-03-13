import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from Tools.NetworkConfigration import DeviceInfoTools
import warnings
import logging
from google.adk.models.lite_llm import LiteLlm

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)


class BaseAgent:
    def __init__(self, name: str,
                #   API_KEY: str, 
                  AgentModel: str | LiteLlm,
                 description: str, instruction: str, tools: list,
                 user_id:str, session_id:str,
                 session_service: InMemorySessionService = None):
        self.name = name
        self.AgentModel = AgentModel
        self.description = description
        self.instruction = instruction
        self.tools = tools
        self.session_service = session_service or InMemorySessionService()
        self.GOOGLE_GENAI_USE_VERTEXAI = False
        self.user_id=user_id
        self.session_id=session_id


    def create_agent(self):
        """Creates the ADK Agent instance."""
        agent = Agent(
            name=self.name,
            model=self.AgentModel,
            description=self.description,
            instruction=self.instruction,
            tools=self.tools,
        )
        return agent

    async def create_session(self, app_name: str):
        """Creates a new session for this agent."""
        session = await self.session_service.create_session(
            app_name=app_name,
            user_id=self.user_id,
            session_id=self.session_id
        )
        return session

    async def run_agent(self, app_name: str, user_message: str):
        session = await self.create_session(app_name=app_name)
        
        agent = self.create_agent()
        runner = Runner(
            agent=agent,
            app_name=app_name,
            session_service=self.session_service
        )
        message = types.Content(role="user", parts=[types.Part(text=user_message)])
        
        response_text = "Agent did not produce a final response."
        
        async for event in runner.run_async(user_id=self.user_id, session_id=self.session_id, new_message=message):
            if event.is_final_response():
                if event.content and event.content.parts:
                    response_text = event.content.parts[0].text
                break   
        
        return response_text

