from typing import Optional, Tuple, Union
from src.model.canais import Canais
from src.model.video import Video
from src.model.youtube_api import YoutubeService
from src.model.video_model import VideoModel
from src.model.canal_model import CanalModel
from src.model.comentarios_model import ComentariosModel
from src.model.resposta_comentarios_model import RespostaComentariosModel


class Controller:
    def __init__(self):
        self.__youtube_service = YoutubeService()
        self.__video_model = VideoModel()
        self.__canal_model = CanalModel()
        self.__comentarios_model = ComentariosModel()
        self.__resposta_comentarios = RespostaComentariosModel()

    def verificar_video_cadastrado(self, id_video: str) -> Optional[Tuple[str, str, str]]:
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

            canal_dados = self.__canal_model.selecionar_canal_id(
                id_canal=dados_video[0])
            if canal_dados is None:
                self.__canal_model.inserir_canal(
                    id_canal=dados_video[0],
                    nome_canal=dados_video[1]
                )
            return dados_video

    def inserir_dados_video(self, dados_video: tuple, id_video: str):

        self.__video_model.inserir_video(
            id_canal=dados_video[0],
            id_video=id_video,
            titulo_video=dados_video[2],
            comentario_sumarizado=None
        )

    def tratar_dados_comentarios(self, id_video: str):
        for dados_videos_comentarios in self.__youtube_service.buscar_comentarios(id_video=id_video):
            dados_comentarios = self.__comentarios_model.selecionar_comentario_por_id(
                id_comentario=dados_videos_comentarios[0]
            )
            if dados_comentarios is None:
                self.__comentarios_model.inserir_comentarios(
                    id_comentario=dados_videos_comentarios[0],
                    id_video=id_video,
                    usuario=dados_videos_comentarios[2],
                    comentario=dados_videos_comentarios[1],
                    comentario_atualizado=None,
                    data_atualizacao=dados_videos_comentarios[4],
                    data_publicacao=dados_videos_comentarios[3]
                )
            else:
                self.__comentarios_model.atualizar_comentario(
                    id_comentario=dados_comentarios[0],
                    comentario_atualizado=dados_comentarios[1],
                    data_atualizacao=dados_comentarios[4]
                )

    def tratar_dados_resposta_comentarios(self, id_video: str):
        comentarios = self.__comentarios_model.selecionar_comentarios_por_video(
            id_video=id_video
        )
        for comentario in comentarios:

            for dado in self.__youtube_service.buscar_resposta_comentarios(
                id_comentario_parente=comentario.id_comentario
            ):

                resultado_consulta_resposta = self.__resposta_comentarios.selecionar_resposta_comentarios(
                    id_resposta_comentarios=dado[0]
                )
                if resultado_consulta_resposta is not None:
                    self.__resposta_comentarios.inserir_resposta_comentarios(
                        id_resposta_comentario=dado[0],
                        data_atualizacao=dado[3],
                        data_publicacao=dado[4],
                        id_comentario=comentario.id_comentario,
                        resposta_comentario=dado[1],
                        resposta_comentario_atualizado=None,
                        usuario=dado[2]
                    )
                else:
                    self.__resposta_comentarios.atualizar_resposta_comentarios(
                        id_resposta_comentario=dado[0],
                        resposta_comentario_atualizado=dado[1],
                        data_atualizacao=dado[3]
                    )

    def listar_inputs_canais_videos(self) -> Tuple[Canais]:

        lista_canais = self.__canal_model.listar_todos_os_canais()
        nome_canais = tuple(canal.nome_canal for canal in lista_canais)
        return nome_canais

    def listar_input_video_canal(self, nome_canal: str):
        id_canal = self.__canal_model.selecionar_can
