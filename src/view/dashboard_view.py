import streamlit as st
from time import sleep
from src.controller.controller import Controller


class DashboardView:
    st.set_page_config(
        layout='wide',
        page_title='Sumarização Comentários youtube',

    )

    def __init__(self):
        self.__controller = Controller()

    def gerar_layout_cadastrar_video(self):
        st.header('Sumarização Comentários youtube')
        with st.container(border=True):
            st.subheader('Espaço para cadastrar vídeo')
            url = st.text_input('Digite a url do vídeo')
            # Validar url
            botao_pesquisar = st.button(
                'Recuperar comentários',
                key=1
            )
            if botao_pesquisar:
                id_video = url.split('=')[1].split('&')[0]

                dados = self.__controller.verificar_video_cadastrado(
                    id_video=id_video)

                if len(dados) > 0 and dados is not None:
                    self.__controller.inserir_dados_video(
                        dados_video=dados, id_video=id_video)
                    st.toast('Vídeo inserido com sucesso')

                    self.__controller.tratar_dados_comentarios(
                        id_video=id_video)
                    self.__controller.tratar_dados_resposta_comentarios(
                        id_video=id_video)
                    st.success(f'Vídeo {dados[2]} cadastrado com sucesso')
                else:
                    st.warning(
                        f'Vídeo {dados[2]} já está cadastrado')

    def gerar_layout_atualizar_video(self):
        canais = self.__controller.listar_inputs_canais_videos()
        st.subheader('Atualizar comentários')
        with st.container(border=True):
            canal = st.selectbox(
                label='Escolha o canal',
                options=canais,
                key=2
            )
            nome_videos = self.__controller.listar_input_video_canal(
                nome_canal=canal)

            videos = st.selectbox(
                label='Escolha o vídeo',
                options=nome_videos,
                key=3
            )
            botao = st.button(
                label=f'Atualizar dados do vídeo {videos}',
                key=4
            )
            if botao:
                return videos

    def rodar_dashboard(self):
        self.gerar_layout_cadastrar_video()
        videos = self.gerar_layout_atualizar_video()
