from src.controller.controller import Controller


c = Controller()
id_video = 'LCnsyNfaAk4'
# dados = c.verificar_video_cadastrado(id_video=id_video)


# # # Se não existir dados na tabela de vídeos insere os dados na tabela e atualiza os comentários :
# if dados:
#     c.inserir_dados_video(dados_video=dados, id_video=id_video)

# # Se existir dados na tabela de vídeo buscar os dados dos comentários na api
# c.tratar_dados_comentarios(id_video=id_video)

c.tratar_dados_resposta_comentarios(id_video=id_video)

# c.tratar_dados_resposta_comentarios(id_video=id_video)
