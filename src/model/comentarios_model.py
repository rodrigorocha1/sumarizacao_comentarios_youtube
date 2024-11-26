from typing import Optional
from src.model.comentarios import Comentarios
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session


class ComentariosModel:
    def __init__(self):
        self.__db = ConexaoBanco()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        return self.__db.obter_sessao()

    def inserir_comentarios(self, id_comentario: str, id_video: str, usuario: str, comentario: str, comentario_atualizado: str, data_publicacao: str, data_atualizacao: str, ):
        """Método para inserir comentários

        Args:
            id_comentario (str): id do comentário
            id_video (str): id video
            usuario (str): usuario comentario
            comentario (str): comentário
            comentario_atualizado (str): comentario atualizado
            data_publicacao (str): data de públicação do comentário
            data_atualizacao (str): data de atualização do comentário
        """
        sessao = self.obter_sessao()
        comentario = Comentarios(
            id_comentario=id_comentario,
            id_video=id_video,
            usuario=usuario,
            comentario=comentario,
            comentario_atualizado=comentario_atualizado,
            data_publicacao=data_publicacao,
            data_atualizacao=data_atualizacao

        )
        sessao.add(comentario)
        sessao.commit()
        sessao.close()

    def selecionar_comentarios(self, id_comentario: str, id_video: str = None, flag: int = 1) -> Comentarios:
        sessao = self.obter_sessao()
        if flag == 1:
            comentarios = sessao.query(
                Comentarios
            ).filter(
                Comentarios.id_comentario == id_comentario
            ).first()
        else:
            comentarios = sessao.query(
                Comentarios
            ).filter(
                Comentarios.id_video == id_video
            ).all()
        sessao.close()
        return comentarios

    def atualizar_comentario(self, id_comentario: str, comentario_atualizado: str, data_atualizacao: str):
        sessao = self.obter_sessao()
        comentario = sessao.query(
            Comentarios
        ).filter(
            Comentarios.id_comentario == id_comentario
        ).first()
        comentario.comentario_atualizado = comentario_atualizado
        comentario.data_atualizacao = data_atualizacao
