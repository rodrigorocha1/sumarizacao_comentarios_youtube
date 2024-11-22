from src.model.youtube_api import YoutubeService
ys = YoutubeService()

for dados in ys.buscar_comentarios(id_video='rHOPMt_TCvA'):
    print(dados)
