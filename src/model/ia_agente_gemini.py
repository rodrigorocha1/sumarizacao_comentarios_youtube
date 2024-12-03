from langchain_google_genai import ChatGoogleGenerativeAI
import os
import time
from dotenv import load_dotenv
load_dotenv()


class IaAgenteGemini:
    def __init__(self):
        self.__key = os.environ['GOOGLE_API_KEY']
        self.__llm = ChatGoogleGenerativeAI(
            api_key=self.__key,
            model='gemini-1.5-pro',
            temperature=1
        )

    def gerar_resumo(self, texto: str) -> str:
        messages = [
            (
                'system',
                f""" 
                    Você tem experiência em criar tópicos dos comentários dos videos do youtube da transcrição dos vídeos do youtube ,  
                    gere tópicos sobre as  reações da comunidade . 
                
                    Formate em markdown com a seguinte estrutura, vai ter um título e depois um resumo com base no título gerado
                """),
            ('human', texto),
        ]
        time.sleep(10)
        response = self.__llm.invoke(messages)
        return response.content
