from enum import Enum


class AgentEnums(Enum):
    NODATAAVELABEL="NO_DATA_AVELABEL"



class AgentProvider(Enum):
    OPENAI = "OPENAI"
    GEMINI = "GEMINI"
    CLOUD = "CLOUD"
