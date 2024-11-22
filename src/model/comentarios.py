from sqlalchemy import String, ForeignKey
from src.model.conexao_banco import Base
from sqlalchemy.orm import mapped_column, Mapped


class Comentarios(Base):
    __tablename__ = 'Comentarios'

    id_comentario: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )
    id_video: Mapped[str] = mapped_column(
        String,
        ForeignKey('Videos.id_video')
    )
    usuario: Mapped[str] = mapped_column(
        String
    )
    comentario: Mapped[str] = mapped_column(
        String
    )
    comentario_atualizado: Mapped[str] = mapped_column(
        String
    )
    data_publicacao: Mapped[str] = mapped_column(
        String
    )
    data_atualizacao: Mapped[str] = mapped_column(
        String
    )

    def __repr__(self):
        return (
            f'Comentarios['
            f'id_comentario={self.id_comentario}, '
            f'id_video={self.id_video}, '
            f'usuario={self.usuario}, '
            f'comentario={self.comentario}, '
            f'comentario_atualizado={self.comentario_atualizado}, '
            f'data_publicacao={self.data_publicacao}, '
            f'data_atualizacao={self.data_atualizacao}'
            f']'
        )
