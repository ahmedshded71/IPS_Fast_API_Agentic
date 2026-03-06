from pydantic import BaseModel

class ConnectionSchema(BaseModel):
    device: str
    status: str