from src.model.youtube_api import YoutubeService


class Controller:
    def __init__(self):
        self.__youtube_service = YoutubeService()

    def buscar_dados_canal(self, url: str):
        id_canal = url.split('=')[1].split('&')[0]
        dados_video = self.__youtube_service.obter_detalhes_video(
            id_video=id_canal)
