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
            
            "Your task is to analyze a simulated network infrastructure and provide clear explanations to the user.",
            
            "You have access to several tools that can retrieve information about network devices such as routers, switches, firewalls, PCs, and cloud providers.",
            
            "Use the tools whenever the user asks about:",
            "- device configuration",
            "- device connections",
            "- network topology",
            "- device positions",
            "- specific links between devices.",
            
            "Always retrieve real data from the tools instead of guessing.",
            
            "If the user asks about a specific device, call the appropriate tool to fetch the device information.",
            
            "Summarize the retrieved information in a structured and readable format.",
            
            "If the device does not exist or is not initialized, return a clear error message.",
            
            "Your responses should be concise, technical, and structured.",
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

