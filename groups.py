from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Base import Group, Base, Station, User
engine = create_engine('sqlite:///kvestinfa.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

while True:
    group = {
        'id': int(input('Номер: ')),
        'stations': [],
        'current_station': 0,
        'experience': 0,
    }
    for i in range(101, 117):
        ed_group = Group(id=i, stations='', current_station=0, experience=0, money=0)
        session.add(ed_group)
        session.commit()
    session.close()
