import streamlit as st
from time import sleep
from src.controller.controller import Controller


class DashboardView:
    st.set_page_config(
        layout='wide',
        page_title='Sumarização Comentários youtube'
    )

    def __init__(self):
        self.__controller = Controller()

    def gerar_layout_titulo(self):
        st.header('Sumarização Comentários youtube')

        url = st.text_input('Digite a url do vídeo')
        botao_pesquisar = st.button('Recuperar comentários')
        if botao_pesquisar:
            id_video = url.split('=')[1].split('&')[0]
            # Verificar se o vídeo existe
            with st.status('Pesquisando URL') as status:
                st.write('Pesquisando url')
                sleep(2)
                status.update(
                    label='Pesquisa terminada',
                    state='complete'
                )

                st.write(url)

    def rodar_dashboard(self):
        self.gerar_layout_titulo()
