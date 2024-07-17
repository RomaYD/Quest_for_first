import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Base import Group, Base, Station, User, Settings


def return_classic_stats(session, roma, gelia):
    with open('db.json', 'r', encoding='UTF-8') as file:
        stations_json = json.load(file)
        for i in stations_json['stations']:
            stations = Station(id=i['id'], name=i['name'], geo=i['geo'], reward=i['reward'], group=i['group'])
            session.add(stations)
            session.commit()
    for i in range(101, 118):
        if i != 110:
            ed_group = Group(id=i, stations='', current_station=0, experience=0, money=0)
            session.add(ed_group)
            session.commit()
    roma_add = User(id=1311111008, username='borxgalki', full_name='Roman', station = roma.station, type=2)
    gelia_add = User(id=1928032533, username='babagelya', full_name='ГАВ', station = gelia.station, type=2)
    session.add(roma_add)
    session.add(gelia_add)
    session.commit()

