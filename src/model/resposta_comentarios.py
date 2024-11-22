from sqlalchemy import String, ForeignKey
from src.model.config_base import Base
from sqlalchemy.orm import mapped_column, Mapped


class RespostaComentarios(Base):
    __tablename__ = 'Resposta_Comentarios'
    id_resposta_comentario: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )
    id_comentario: Mapped[str] = mapped_column(
        String,
        ForeignKey('Comentarios.id_comentario')
    )
    usuario: Mapped[str] = mapped_column(String)
    resposta_comentario: Mapped[str] = mapped_column(String)
    resposta_comentario_atualizado: Mapped[str] = mapped_column(String)
    data_publicacao: Mapped[str] = mapped_column(String)
    data_atualizacao: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return (
            f'Resposta_Comentarios['
            f'id_resposta_comentario={self.id_resposta_comentario}, '
            f'id_comentario={self.id_comentario}, '
            f'usuario={self.usuario}, '
            f'resposta_comentario={self.comentario}, '
            f'resposta_comentario_atualizado={self.comentario_atualizado}, '
            f'data_publicacao={self.data_publicacao}, '
            f'data_atualizacao={self.data_atualizacao}'
            f']'
        )
