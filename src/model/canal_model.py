from typing import Optional
from src.model.canais import Canais
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

    def selecionar_canal_id(self, id_canal: str) -> Optional[str]:
        sessao = self.obter_sessao()
        canal = sessao.query(
            Canais
        ).filter(
            Canais.id_canal == id_canal
        ).first()

        if canal:
            return str(canal.id_canal)
        return None
