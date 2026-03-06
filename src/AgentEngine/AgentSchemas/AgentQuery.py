from pydantic import BaseModel
from typing import Optional

class AgentQuery(BaseModel):
    user_message: str
    description: Optional[str] = None
    instruction: Optional[str] = None