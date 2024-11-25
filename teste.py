from src.model.youtube_api import YoutubeService
ys = YoutubeService()

# for dados in ys.buscar_comentarios(id_video='lsvDcr8Gvbc'):
#     print(dados)

for dado in ys.buscar_resposta_comentarios(id_comentario_parente='UgwfRT1bmZWxrA8cfnJ4AaABAg'):
    print(dado)
