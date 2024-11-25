from src.model.youtube_api import YoutubeService
from src.model.video_model import VideoModel
from src.model.canal_model import CanalModel


class Controller:
    def __init__(self):
        self.__youtube_service = YoutubeService()
        self.__video_model = VideoModel()
        self.__canal_model = CanalModel()

    def verificar_video_cadastrado(self, id_video: str) -> bool:
        """Método para verificar vídeo cadastrado

        Args:
            id_video (str): id do vídeo 

        Returns:
            bool: True se o vídeo está cadastrado false caso contrário
        """
        if self.__video_model.selecionar_video(id_video=id_video):
            return True
        return False

    def inserir_dados(self, id_video: str):
        dados_video = self.__youtube_service.obter_detalhes_video(
            id_video=id_video
        )
        # Verificar se o canal existe
        self.__canal_model.inserir_canal()
