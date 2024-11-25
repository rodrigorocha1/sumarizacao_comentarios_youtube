from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from src.model.config_base import Base


class Canais(Base):
    __tablename__ = 'Canais'
    id_canal: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )
    nome_canal: Mapped[str] = mapped_column(
        String
    )

    def __repr_(self):
        return (
            f'Canais[id_canal={self.id_canal}, nome_canal={self.nome_canal}]'
        )
