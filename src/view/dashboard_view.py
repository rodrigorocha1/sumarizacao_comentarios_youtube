import streamlit as st
from time import sleep


class DashboardView:
    st.set_page_config(
        layout='wide',
        page_title='Sumarização Comentários youtube'
    )

    def __init__(self):
        pass

    def gerar_layout_titulo(self):
        st.header('Sumarização Comentários youtube')

        url = st.text_input('Digite a url do vídeo')
        botao_pesquisar = st.button('Recuperar comentários')
        if botao_pesquisar:
            if len(url) > 0:
                with st.status('Pesquisando URL') as status:
                    st.write('Pesquisando url')
                    sleep(2)
                    status.update(
                        label='Pesquisa terminada',
                        state='complete'
                    )
                    url = url.split('=')[1].split('&')[0]
                    st.write(url)
            else:
                st.warning('Formato da url Invalida')

    def rodar_dashboard(self):
        self.gerar_layout_titulo()
