from enum import Enum

class ResponseSignal(Enum):
  OPENAI="OPENAI"
  COHERE="COHERE"
  GEMINI="GEMINI"
  GROQ="GROQ"


class OpenAIEnums(Enum):
    SYSTEM="system"
    USER="user"
    ASSISTANT="assistant"

class CohereEnums(Enum):
    SYSTEM="SYSTEM"
    USER="USER"
    ASSISTANT="CHATBOT"
    DOCUMENT="search_document"
    QUERY="search_query"

class DocumentTypeEnums(Enum):
    DOCUMENT="document"
    QUERY="query"


class  GEMINIEnums(Enum):
    SYSTEM="system"
    USER="user"
    ASSISTANT="assistant"


class GROQEnums(Enum):
    SYSTEM="system"
    USER="user"
    ASSISTANT="assistant"
