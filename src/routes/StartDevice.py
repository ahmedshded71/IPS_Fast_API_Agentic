from sys import prefix
from webbrowser import get
from fastapi import FastAPI, APIRouter, Depends, UploadFile, status, Request
from fastapi.responses import JSONResponse
from Helpers import get_settings, Settings
from Tools.NetworkConfigration.SimulatedDevice.Device_sim import VirtualCloudProvider, VirtualFirewall, VirtualSwitch, VirtualRouter,PC1 ,PC2
from Tools.NetworkConfigration.NetworkEnums.NetworkEnums import NetworkConfigrationToolsEnums

# from models.enums import ResponseSignal,AssetTypeEnums
import logging

# Create a logger for error messages
logger = logging.getLogger("uvicorn.error")

# Create an APIRouter for data endpoints
StartDevice_Routes = APIRouter(
    prefix="/API/V1/StartDevice",
    tags=["IPS_Fast_API_Agentic_StartDevice", "START_DEVICE"],
)

# start device endpoint
@StartDevice_Routes.post("/StartDevice", status_code=status.HTTP_201_CREATED)
async def StartDevice( request: Request,settings: Settings =  Depends(get_settings)):

    VirtualCloudProvider.initialize(settings)
    VirtualFirewall.initialize(settings)
    VirtualRouter.initialize(settings)
    VirtualSwitch.initialize(settings)
    PC1.initialize(settings)
    PC2.initialize(settings)

    return JSONResponse(
        content={"message": NetworkConfigrationToolsEnums.DEVICE_CONFIGRATION_RESPONSE.value},
        status_code=status.HTTP_201_CREATED)

@StartDevice_Routes.post("/ShowDeviceConfig", status_code=status.HTTP_201_CREATED)
async def ShowDeviceConfig( request: Request,settings: Settings = Depends(get_settings)):
    virtual_Firewall=VirtualFirewall()
    virtual_Router=VirtualRouter()
    virtual_Switch=VirtualSwitch()
    virtual_CloudProvider=VirtualCloudProvider()
    PC1_device=PC1()
    PC2_device=PC2()
    if virtual_Firewall and virtual_Router and virtual_Switch:
        return JSONResponse(
        content={"message":[ NetworkConfigrationToolsEnums.DEVICE_CONFIGRATION_RESPONSE.value,
                            NetworkConfigrationToolsEnums.VIRTUAL_CLOUD_PROVIDER_CONFIGRATION.value,
                            VirtualCloudProvider().show_settings().dict(),
                            NetworkConfigrationToolsEnums.VIRTUAL_FIREWALL_CONFiGRATION.value,
                            VirtualFirewall().show_settings().dict(),
                            NetworkConfigrationToolsEnums.VIRTUAL_ROUTER_CONFIGRATION.value,
                            VirtualRouter().show_settings().dict(),
                            NetworkConfigrationToolsEnums.VIRTUAL_SWITCH_CONFIGRATION.value,
                            VirtualSwitch().show_settings().dict(),
                            NetworkConfigrationToolsEnums.VIRTUAL_PC1_CONFIGRATION.value,
                            PC1().show_settings().dict(),
                            NetworkConfigrationToolsEnums.VIRTUAL_PC2_CONFIGRATION.value,
                            PC2().show_settings().dict()]},
                        status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(
            content={"message": NetworkConfigrationToolsEnums.DEVICE_CONFIGRATION_FAILED.value }, 
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
