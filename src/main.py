from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from routes import base,StartDevice,AgentSession
from Helpers import get_settings
from Tools.NetworkConfigration.SimulatedDevice.Device_sim import (
    VirtualCloudProvider, VirtualFirewall, VirtualRouter, 
    VirtualSwitch, PC1, PC2
)
from dotenv import load_dotenv
import os


app=FastAPI()


@app.on_event("startup")
async def startup_span():
        settings = get_settings()
        # Initialize all devices with configuration
        VirtualCloudProvider.initialize(settings)
        VirtualFirewall.initialize(settings)
        VirtualRouter.initialize(settings)
        VirtualSwitch.initialize(settings)
        PC1.initialize(settings)
        PC2.initialize(settings)


        os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
        os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
        os.environ["MODEL_GEMINI_2_5_FLASH"] = settings.MODEL_GEMINI_2_5_FLASH
        os.environ["LAMA_MODEL"] = settings.OLLAMA_MODEL
        os.environ["APP_NAME"] = settings.APP_NAME
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"





@app.on_event("shutdown")
async def shutdown_span():
        pass



app.include_router(base.base_routes)
app.include_router(StartDevice.StartDevice_Routes)
app.include_router(AgentSession.StartAgents)




