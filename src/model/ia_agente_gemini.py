from langchain_google_genai import ChatGoogleGenerativeAI
import os
import time


class IaAgenteGemini:
    def __init__(self):
        self.__key = os.environ['GOOGLE_API_KEY']
        self.__llm = ChatGoogleGenerativeAI(
            api_key=self.__key,
            model='gemini-1.5-pro',
            temperature=1
        )

    def gerar_resumo(self, texto: str, nome_canal: str, titulo_video: str) -> str:
        messages = [
            (
                'system',
                f""" 
                    Você tem experiência em criar tópicos dos comentários dos videos do youtube da transcrição dos vídeos do youtube n
                
                    Formate em markdown para exibição em metade da página do navegador
                """),
            ('human', texto),
        ]
        time.sleep(10)
        response = self.__llm.invoke(messages)
        return response.content
