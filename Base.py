import sys
# для настройки баз данных
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()


# здесь добавим классы
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    stations = Column(String(1000))
    current_station = Column(Integer)
    experience = Column(Integer)
    money = Column(Integer)


class Station(Base):
    __tablename__ = 'stations'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    geo = Column(String(250))
    reward = Column(Integer)
    group = Column(Integer)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    full_name = Column(String(250))
    type = Column(Integer)
    group = Column(Integer)
    station = Column(Integer)


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    status = Column(Boolean)
    is_started = Column(Boolean)
    is_ended = Column(Boolean)
# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///kvestinfa.db')

Base.metadata.create_all(engine)