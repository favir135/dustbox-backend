from sqlalchemy.orm import sessionmaker
import sqlalchemy
from typing import Any
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

load_dotenv()
engine = create_engine(
    f"mysql://{getenv('MYSQL_USER')}:{getenv('MYSQL_PASSWORD')}@{getenv('MYSQL_HOST')}/{getenv('DB_NAME')}",
    pool_pre_ping = True)


Base = declarative_base()

class AC_Model(Base):
  __tablename__ = 'access_counter'

  id = Column(Integer, primary_key=True)
  count = Column(Integer, nullable=False, default=0)

Base.metadata.create_all(bind=engine)
session_class = sessionmaker(engine)  # セッションを作るクラスを作成

