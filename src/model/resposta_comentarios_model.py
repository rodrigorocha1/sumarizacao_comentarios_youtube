from typing import List
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session
from src.model.resposta_comentarios import RespostaComentarios


class RespostaComentariosModel:
    def __init__(self):
        self.__db = ConexaoBanco()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        return self.__db.obter_sessao()

    def inserir_resposta_comentarios(self, id_resposta_comentario: str, id_comentario: str, usuario: str, resposta_comentario: str, resposta_comentario_atualizado: str, data_publicacao: str, data_atualizacao: str):
        sessao = self.obter_sessao()
        d_resposta_comentario = RespostaComentarios(
            id_resposta_comentario=id_resposta_comentario,
            id_comentario=id_comentario,
            usuario=usuario,
            resposta_comentario=resposta_comentario,
            resposta_comentario_atualizado=resposta_comentario_atualizado,
            data_publicacao=data_publicacao,
            data_atualizacao=data_publicacao
        )
        sessao.add(d_resposta_comentario)
        sessao.commit()
        sessao.close()

    def selecionar_resposta_comentarios(self, id_resposta_comentarios: str) -> List[RespostaComentarios]:
        sessao = self.obter_sessao()
        resultado_resposta_comentarios = sessao.query(
            RespostaComentarios
        ).filter(
            RespostaComentarios.id_resposta_comentario == id_resposta_comentarios
        ).all()
        sessao.close()
        return resultado_resposta_comentarios

    def atualizar_resposta_comentarios(self, id_resposta_comentario: str, resposta_comentario_atualizado: str, data_atualizacao: str):
        sessao = self.obter_sessao()
        resposta_comentarios = sessao.query(
            RespostaComentarios
        ).filter(
            RespostaComentarios.id_resposta_comentario == id_resposta_comentario
        ).first()

        if resposta_comentarios is not None:
            resposta_comentarios.resposta_comentario_atualizado = resposta_comentario_atualizado
            resposta_comentarios.data_atualizacao = data_atualizacao
            sessao.commit()

        sessao.close()
