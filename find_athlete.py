import math
from datetime import datetime, date, time, timedelta

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

# CREATE TABLE athelete("id" integer primary key autoincrement, "age" integer,"birthdate" text,"gender" text,"height" real,"name" text,"weight" integer,"gold_medals" integer,
# "silver_medals" integer,"bronze_medals" integer,"total_medals" integer,"sport" text,"country" text);
# CREATE TABLE sqlite_sequence(name,seq);
# CREATE TABLE user("id" integer primary key autoincrement, "first_name" text, "last_name" text, "gender" text, "email" text, "birthdate" text, "height" real);

class Atheletes(Base):
    __tablename__ = 'athelete'
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.INTEGER, primary_key=True)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    birthdate = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    first_name = sa.Column(sa.TEXT)

def connect_db():
    engine = sa.create_engine(DB)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()
atheletes = connect_db().query(Atheletes)
users = connect_db().query(User)

def finder(user_id):
    for ids in users.filter(User.id):
        if int(user_id) == ids.id:
            return ids
    return None

def find_u_love(height):
    res = 10000000
    for athelete in atheletes.all():
        if athelete.height:
            if abs(athelete.height - height) < res:
                res = abs(athelete.height - height)
                love = athelete
    return love.name + "\nРост: " + str(love.height)

def find_u_twinbrother(birthdate):
    if "-" in birthdate:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    elif "." in birthdate:
        birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
    else:
        print ("Неверный формат даты")
        return None
    res = timedelta(100000)
    for athelete in atheletes.all():
        if athelete.birthdate:
            twindate =  datetime.strptime(athelete.birthdate, "%Y-%m-%d")
            if abs(twindate - birthdate) < res:
                res = abs(twindate - birthdate)
                love = athelete
    return "\n---------\n" + love.name + "\nДата рождения: " + str(love.birthdate)

def main():
    user_id = input("Введите идентификатор пользователя: ")
    user = finder(user_id)
    if user:
        print(find_u_love(user.height), find_u_twinbrother(user.birthdate))
    else:
        print ("Пользователm c таким идентификатором не найден") 
# Оставил включенным ;)
main()
