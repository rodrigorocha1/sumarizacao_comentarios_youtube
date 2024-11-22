from typing import Generator, Optional, Tuple, Union
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build  # type: ignore


load_dotenv()


class YoutubeService():

    def __init__(self):
        self.__api_key = os.environ['YOUTUBE_API_KEY']
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def buscar_comentarios(self, id_video: str) -> Generator[Tuple[str, str, str, str]]:

        flag_token = True
        token = ''
        while flag_token:
            request = self.__youtube.commentThreads().list(
                part='snippet',
                videoId=id_video,
                textFormat='plainText',
                pageToken=token,
            )
            response = request.execute()
            for item in response['items']:
                id_comentario = item['id']
                texto_comentario = item['snippet']['topLevelComment']['snippet']['textOriginal']
                autor_comentario = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                data_publicacao = item['snippet']['topLevelComment']['snippet']['publishedAt']
                data_atualizacao = item['snippet']['topLevelComment']['snippet']['updatedAt']

                yield id_comentario, texto_comentario, autor_comentario, data_publicacao, data_atualizacao
            try:
                token = response['nextPageToken']
                flag_token = True
            except KeyError:
                flag_token = False

    def buscar_resposta_comentarios(self, id_comentario_parente: str):
        flag_token = True
        token = ''
        while flag_token:
            request = self.__youtube.comments().list(
                part='snippet',
                parentId=id_comentario_parente,
                textFormat='plainText',
                pageToken=token
            )
            response = request.execute()
            for item in response['items']:
                id_resposta_comentario = item['id'].split('.')[-1]
                texto_resposta_comentario = item['snippet']['textOriginal']
                autor_resposta_comentario = item['snippet']['authorDisplayName']
                data_publicacao = item['snippet']['publishedAt']
                data_atualizacao = item['snippet']['updatedAt']
                yield (id_resposta_comentario, texto_resposta_comentario, autor_resposta_comentario, data_atualizacao, data_publicacao)
            try:
                token = response['nextPageToken']
                flag_token = True
            except KeyError:
                flag_token = False
