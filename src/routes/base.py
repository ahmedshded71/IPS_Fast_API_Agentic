from sys import prefix
from webbrowser import get
from fastapi import FastAPI ,APIRouter, Depends
from Helpers import get_settings,Settings
base_routes=APIRouter(
    prefix="/API/V1",
    tags=["IPS_Fast_API_Agentic"]
)
@base_routes.get("/health")
async def welcom(settings:Settings=Depends(get_settings)):
    app_name=settings.APP_NAME
    app_version=settings.APP_VERSION
    return {
        "APP_NAME": app_name,
        "APP_VERSION":app_version,
        "message":"Welcome to IPS Fast API Agentic"}    