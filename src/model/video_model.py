from typing import Optional, Tuple

from sqlalchemy import Row
from src.model.canais import Canais
from src.model.video import Video
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session


class VideoModel:
    def __init__(self):
        self.__db = ConexaoBanco()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        return self.__db.obter_sessao()

    def inserir_video(self, id_video: str, id_canal: str, titulo_video: str, comentario_sumarizado: str):
        """Método para inserir vídeo

        Args:
            id_video (str): id do vídeo
            id_canal (str): id canal
            titulo_video_string (str): título do vídeo
            comentario_sumarizado (str): comentário
        """
        sessao = self.obter_sessao()
        video = Video(
            id_video=id_video,
            id_canal=id_canal,
            titulo_video=titulo_video,
            comentario_sumarizado=comentario_sumarizado
        )
        sessao.add(video)
        sessao.commit()
        sessao.close()

    def atualizar_video_transcricao(self, id_video: str, transcricao: str):
        sessao = self.obter_sessao()
        video = sessao.query(
            Video
        ).filter(
            Video.id_video == id_video
        ).first()

        video.comentario_sumarizado = transcricao
        sessao.commit()
        sessao.close()

    def selecionar_video(self, id_video: str) -> Optional[Tuple[Canais, Video]]:
        """Método para selecionar vídeo id

        Args:
            id_video (str): id do vídeo

        Returns:
            str: título do vídeo
        """
        sessao = self.obter_sessao()
        canais_video = sessao.query(
            Canais,
            Video
        ).join(
            Video, Canais.id_canal == Video.id_canal
        ).filter(
            Video.id_video == id_video
        ).first()
        sessao.close()
        if canais_video:

            return canais_video[0], canais_video[1]
        return None

    def selecionar_transcricao(self, nome_video: str) -> Video:
        sessao = self.obter_sessao()
        video = sessao.query(
            Video
        ).filter(
            Video.titulo_video == nome_video
        ).first()
        sessao.close()
        return video
