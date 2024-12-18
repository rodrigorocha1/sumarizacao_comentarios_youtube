from typing import List, Optional, Tuple

from sqlalchemy import Row
from src.model.canais import Canais
from src.model.video import Video
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session


class CanalModel:

    def __init__(self):
        self.__db = ConexaoBanco()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        return self.__db.obter_sessao()

    def inserir_canal(self, id_canal: str, nome_canal: str):
        """Método para inserir canal

        Args:
            id_canal (str): id canal
            nome_canal (str): nome canal
        """
        sessao = self.obter_sessao()
        canais = Canais(id_canal=id_canal, nome_canal=nome_canal)
        sessao.add(canais)
        sessao.commit()
        sessao.close()

    def selecionar_video_canal_nome(self, nome_canal: str) -> List[Row[Tuple[Canais, Video]]]:
        sessao = self.obter_sessao()

        canal = sessao.query(
            Canais,
            Video
        ).join(
            Video, Canais.id_canal == Video.id_canal
        ).filter(
            Canais.nome_canal == nome_canal
        ).all()

        sessao.close()
        return canal

    def selecionar_canal_id(self, id_canal: str) -> Optional[Tuple[Canais, Video]]:
        sessao = self.obter_sessao()

        canal = sessao.query(
            Canais,
            Video
        ).join(
            Video, Canais.id_canal == Video.id_canal
        ).filter(
            Canais.id_canal == id_canal
        ).first()

        sessao.close()
        if canal:
            return canal[0], canal[1]
        return None

    def listar_todos_os_canais(self) -> List[Canais]:
        sessao = self.obter_sessao()
        canal = sessao.query(
            Canais
        ).all()

        return canal
