from fastapi import FastAPI
from routes import base
from Helpers import get_settings


app=FastAPI()


@app.on_event("startup")
async def startup_span():
        Settings=get_settings()





@app.on_event("shutdown")
async def shutdown_span():
        pass



app.include_router(base.base_routes)





