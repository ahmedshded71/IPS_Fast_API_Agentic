import asyncio
from google.adk.runners import Runner
from Tools.NetworkConfigration import DeviceInfoTools
import warnings
import logging
from .BaseAgent import BaseAgent
from Tools.NetworkConfigration import DeviceInfoTools
from google.genai import types # For creating message Content/Parts
from google.adk.models.lite_llm import LiteLlm
from ..AgentProvidorFactory import AgentProviderFactory
from ..AgentEnums import AgentProvider



class NetworkInfoAgent:
    """
    Agent specialized in retrieving and reporting network info using DeviceInfoTools.
    """
    def __init__(self, name: str, AgentModel: str|LiteLlm ,
                 user_id:str, session_id:str,
                description: str = None, instruction: str = None):
        self.name = name
        self.AgentModel = AgentModel
        self.description =description
        self.instruction=instruction
        self.user_id=user_id
        self.session_id=session_id

        tools = [
            DeviceInfoTools.GetDeviceInfo.show_device_settings,
            DeviceInfoTools.GetDeviceConnections.show_device_connections,
            DeviceInfoTools.GetPCInfo.get_device_position,
        ]


        description = self.description if self.description else "\n".join([
            "Network infrastructure analysis assistant.",
            "Provides structured reports about simulated network devices including router, switch, firewall, PCs, and cloud provider.",
            "Retrieves device configurations, connection topology, device positions, and specific link relationships.",
        ])
        instruction = self.instruction if self.instruction else "\n".join([
            "You are an intelligent network diagnostic assistant.",

            "Your role is to analyze and explain the state of a simulated network infrastructure.",

            "The network may contain multiple types of devices including:",
            "- PCs",
            "- Routers",
            "- Switches",
            "- Firewalls",
            "- Cloud providers",

            "You have access to several tools that can retrieve real-time information about these devices.",

            "Use the available tools whenever the user asks about:",
            "- device configuration (show_device_settings)",
            "- device connections (show_device_connections)",
            "- device location or topology position (get_device_position)",

            "Always retrieve real information using the tools instead of guessing.",

            "If the user asks about a specific device:",
            "1. Identify the device name.",
            "2. Call the appropriate tool.",
            "3. Retrieve the device data.",
            "4. Explain the result clearly.",

            "If the device does not exist or is not initialized, return a clear error message.",

            "Present responses in a structured and easy-to-read format.",

            "Your explanations should be:",
            "- concise",
            "- technical",
            "- clear for network administrators."
        ])

        self.base_agent = AgentProviderFactory(
            name=self.name,
            provider=AgentProvider.GEMINI.value,
            description=description,
            instruction=instruction,
            tools=tools,
            user_id=self.user_id,
            session_id=self.session_id
        ).create()
        

    async def query(self, user_message: str, app_name: str):
        """Send a query to the NetworkInfoAgent and return its response."""
        response = await self.base_agent.run_agent(
            app_name=app_name,
            user_message=user_message,
        )
        return response

