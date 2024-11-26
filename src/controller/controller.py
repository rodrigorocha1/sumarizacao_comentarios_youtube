from typing import Union
from src.model.youtube_api import YoutubeService
from src.model.video_model import VideoModel
from src.model.canal_model import CanalModel
from src.model.comentarios_model import ComentariosModel


class Controller:
    def __init__(self):
        self.__youtube_service = YoutubeService()
        self.__video_model = VideoModel()
        self.__canal_model = CanalModel()
        self.__comentarios_model = ComentariosModel()

    def verificar_video_cadastrado(self, id_video: str) -> Union[bool, list]:
        """Método para verificar vídeo cadastrado

        Args:
            id_video (str): id do vídeo

        Returns:
            bool: True se o vídeo está cadastrado false caso contrário
        """
        dados_video_banco = self.__video_model.selecionar_video(
            id_video=id_video
        )

        if dados_video_banco is None:
            dados_video = self.__youtube_service.obter_detalhes_video(
                id_video=id_video
            )
            self.__canal_model.inserir_canal(
                id_canal=dados_video[0],
                nome_canal=dados_video[2]
            )
            return dados_video_banco, dados_video

        else:
            return False

    def inserir_dados_video(self, dados_video: tuple, id_video: str):

        self.__video_model.inserir_video(
            id_canal=dados_video[0],
            id_video=id_video,
            titulo_video=dados_video[2],
            comentario_sumarizado=None
        )

    def tratar_dados_comentarios(self, id_video: str):
        for dados_videos in self.__youtube_service.buscar_comentarios(id_video=id_video):
