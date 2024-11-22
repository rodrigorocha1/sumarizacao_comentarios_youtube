from sqlalchemy import String, ForeignKey
from src.model.config_base import Base
from sqlalchemy.orm import mapped_column, Mapped


class Video(Base):
    __tablename__ = 'Videos'

    id_video: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )
    id_canal: Mapped[str] = mapped_column(
        String,
        ForeignKey('Canais.id_canal')

    )
    titulo_video_string: Mapped[String] = mapped_column(String)
    comentario_sumarizado: Mapped[String] = mapped_column(String)

    def __repr__(self):
        return (
            f'Videos[id_video={self.id_video},id_canal={self.id_canal}, titulo_video={self.titulo_video_string}, comentario_sumarizado={self.comentario_sumarizado}]'
        )
