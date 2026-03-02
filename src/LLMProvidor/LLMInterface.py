# from abc import ABC, abstractmethod

# class LLMInterface(ABC):
#     """
#     Abstract base class for any LLM provider.
#     Forces implementation of essential methods.
#     """

#     @abstractmethod
#     def set_generation_model(self, model_id: str):
#         """
#         Set or load the generation model (similar to forward in PyTorch).

#         Parameters
#         ----------
#         model_id : str
#             Identifier or path of the model to be used.
#         """
#         pass


#     @abstractmethod
#     def set_embedding_model(self, model_id: str,embedding_size:int):
#         pass


#     @abstractmethod
#     def generate_text(self,prompt:str,max_output_tokens:str=None,chat_history:list=[],tempreature:float=None):
#         pass


#     @abstractmethod
#     def embed_text(self,text:str,decoment_type:str=None):
#         pass

    
#     @abstractmethod
#     def constract_prompt(self,prompet:str,role:str):
#         pass