from typing import List, Tuple
from src.model.conexao_banco import ConexaoBanco
from sqlalchemy.orm.session import Session
from src.model.resposta_comentarios import RespostaComentarios
from src.model.comentarios import Comentarios
from sqlalchemy import select, union_all
from src.model.video import Video


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

    def selecionar_comentarios_nome_video(self, id_video: str) -> List[Tuple[str, str]]:
        sessao = self.obter_sessao()
        consulta_um = (
            select(Comentarios.comentario_atualizado, Comentarios.usuario)
            .join(Video, Comentarios.id_video == Video.id_video)
            .where(
                Video.id_video == id_video
            )
        )

        consulta_dois = (
            select(RespostaComentarios.resposta_comentario_atualizado,
                   RespostaComentarios.usuario)
            .join(Comentarios, Comentarios.id_comentario == RespostaComentarios.id_comentario)
            .join(Video, Comentarios.id_video == Video.id_video)
            .where(Video.id_video == id_video)
        )

        comentarios_usuarios = union_all(consulta_um, consulta_dois)
        resultado = sessao.execute(comentarios_usuarios).fetchall()
        return resultado
