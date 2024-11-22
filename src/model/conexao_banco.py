from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.config_base import Base
from sqlalchemy.orm.session import Session
import os


class ConexaoBanco:
    def __init__(self):
        self.__CAMINHO_BANCO = os.path.join(
            os.getcwd(),
            'database',
            'youtube_comentarios_db.sqlite'
        )
        self.__DATABASE_URL = 'sqlite:///' + self.__CAMINHO_BANCO
        self.__engine = create_engine(
            self.__DATABASE_URL,
            echo=False,
            isolation_level='AUTOCOMMIT',
            connect_args={'timeout': 30}
        )
        self.__sessao_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.__engine
        )

    def obter_sessao(self) -> Session:
        session = self.__sessao_local()
        try:
            return session
        except Exception:
            session.rollback()
            raise

    def iniciar_banco(self):
        Base.metadata.create_all(bind=self.__engine)
