from src.model.video import Video
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session


class VideoModel:
    def __init__(self):
        self.__db = ConexaoBanco()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        return self.__db.obter_sessao()

    def inserir_video(self, id_video: str, id_canal: str, titulo_video_string: str, comentario_sumarizado: str):
        """Método para inserir vídeo

        Args:
            id_video (str): id do vídeo
            id_canal (str): id canal
            titulo_video_string (str): título do vídeo
            comentario_sumarizado (str): comentário sumarizado
        """
        sessao = self.obter_sessao()
        video = Video(
            id_video=id_video,
            id_canal=id_canal,
            titulo_video_string=titulo_video_string,
            comentario_sumarizado=comentario_sumarizado
        )
        sessao.add(video)
        sessao.commit()
        sessao.close()

    # def selecionar_canal(self, id_video: str):
    #     sessao = self.obter_sessao()
    #     video = Video()
