import asyncio
from google.adk.runners import Runner
from Tools.NetworkConfigration import DeviceInfoTools
import warnings
import logging
from AgentEngine.BaseAgent import BaseAgent
from Tools.NetworkConfigration import DeviceInfoTools
from google.genai import types # For creating message Content/Parts

class NetworkInfoAgent:
    """
    Agent specialized in retrieving and reporting network info using DeviceInfoTools.
    """
    def __init__(self, name: str, AgentModel: str,
                 user_id:str, session_id:str,
                description: str = None, instruction: str = None):
        self.name = name
        self.AgentModel = AgentModel
        self.description =description
        self.instruction=instruction
        self.user_id=user_id
        self.session_id=session_id

        tools = [
            DeviceInfoTools.GetDeviceInfo.show_Device_settings,
            DeviceInfoTools.GetDeviceConnections.show_Device_connections,
            DeviceInfoTools.GetPCInfo.get_conection_device,
        ]


        description =self.description  if self.description else "\n".join([
            "Provides structured network reports for all devices.",
            ])
        instruction =self.instruction  if self.instruction else "\n".join([
            "You are a network diagnostic assistant. ",
            "Use the available tools to inspect device connection states, ",
            "generate structured reports, and respond clearly to the user.",
        ])

        self.base_agent = BaseAgent(
            name=self.name,
            AgentModel=self.AgentModel,
            description=description,
            instruction=instruction,
            tools=tools,
            user_id=self.user_id,
            session_id=self.session_id
        )

    async def query(self, user_message: str, app_name: str):
        """Send a query to the NetworkInfoAgent and return its response."""
        response = await self.base_agent.run_agent(
            app_name=app_name,
            user_message=user_message,
        )
        return response

