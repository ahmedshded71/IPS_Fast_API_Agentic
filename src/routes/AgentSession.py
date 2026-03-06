from sys import prefix
from webbrowser import get
from Tools.NetworkConfigration.SimulatedDevice.Device_sim import VirtualCloudProvider
from fastapi import FastAPI, APIRouter, Depends, UploadFile, status, Request
from fastapi.responses import JSONResponse
from Helpers import get_settings, Settings
from AgentEngine import NetworkInfoAgent
from dotenv import load_dotenv
import os
from AgentEngine import AgentEnums
from AgentEngine.AgentSchemas import AgentQuery

# from models.enums import ResponseSignal,AssetTypeEnums
import logging

# Create a logger for error messages
logger = logging.getLogger("uvicorn.error")

# Create an APIRouter for data endpoints
StartAgents = APIRouter(
    prefix="/API/V1/AgentSession",
    tags=["IPS_Fast_API_Agentic_StartDevice", "Agent_Session"],
)

# start device endpoint
@StartAgents.post("/NetworkInfoAgentRoutes/{session_id}/{user_id}", status_code=status.HTTP_201_CREATED)
async def NetworkInfoAgentRoutes( request: Request ,session_id:str ,user_id:str,query: AgentQuery,
                                 settings: Settings =  Depends(get_settings),
                                 ):

    load_dotenv()  
    os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
    os.environ["MODEL_GEMINI_2_5_FLASH"] = settings.MODEL_GEMINI_2_5_FLASH
    os.environ["APP_NAME"] = settings.APP_NAME
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"
    MODEL_NAME = os.getenv("MODEL_GEMINI_2_5_FLASH")
    APP_NAME = os.getenv("APP_NAME")


    network_agent_info = NetworkInfoAgent(
        name="network_agent_info",
        AgentModel=MODEL_NAME,
        description=query.description,
        instruction=query.instruction,
        session_id=session_id,
        user_id=user_id
    )
    response= await network_agent_info.query(app_name=APP_NAME,
                                      user_message= query.user_message)
    
    if response:
        return JSONResponse(
        content={"Responce": response},
        status_code=status.HTTP_201_CREATED)

    else:
        return JSONResponse(
        content={"Responce": AgentEnums.NODATAAVELABEL.value },
        status_code=status.HTTP_201_CREATED)

