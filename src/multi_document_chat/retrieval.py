import sys
import os

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.vectorstores import FAISS
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType



class ConversationalRAG:
    #static method defination
    @staticmethod
    def _format_docs(docs):
        pass

    def __init__(self,session_id:str, retriver=None):
        self.log = CustomLogger().get_logger(__name__)
        pass 
     

    def _load_llm(self):
        pass 

    def _build_lcel_chain(self):
        pass

    def load_retriver_from_faiss(self):
        pass

    def invoke(self):
        pass