# from .providers import OpenAIProvider, CoHereProvider ,GeminiProvider
# from . import LLMInterface
# from .LLMEnums.LLMEnums import ResponseSignal
# from flask import config


# class LLMProviderFactory:
#     def __init__(self,config:dict):
#         self.config = config

#     def create(self,provider: str):
#         self.provider = provider
#         if self.provider == ResponseSignal.OPENAI.value:
#             return OpenAIProvider(
#                 api_key=self.config.OPENAI_API_KEY,
#                 api_url=self.config.OPENAI_API_URL,
#                 default_generation_output_max_token=self.config.DEFAULT_GENERATION_MAX_TOKENS,
#                 default_generation_temprature=self.config.DEFAULT_GENERATION_TEMPERATURE,
#                 default_input_max_token=self.config.DEFAULT_INPUT_MAX_TOKENS
#             )






#         elif self.provider == ResponseSignal.COHERE.value:
#             return CoHereProvider(
#                 api_key=self.config.COHERE_API_KEY,
#                 default_generation_output_max_token=self.config.DEFAULT_GENERATION_MAX_TOKENS,
#                 default_generation_temperature=self.config.DEFAULT_GENERATION_TEMPERATURE,
#                 default_input_max_token=self.config.DEFAULT_INPUT_MAX_TOKENS

#             )
 
#         # -------- Gemini --------
#         elif self.provider == ResponseSignal.GEMINI.value:
#             return GeminiProvider(
#                 api_key=self.config.GEMINI_API_KEY,
#                 default_generation_output_max_token=self.config.DEFAULT_GENERATION_MAX_TOKENS,
#                 default_generation_temperature=self.config.DEFAULT_GENERATION_TEMPERATURE,
#                 default_input_max_token=self.config.DEFAULT_INPUT_MAX_TOKENS
#             )

#         # -------- Unknown Provider --------
#         return None
