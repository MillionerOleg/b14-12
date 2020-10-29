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

def main():
    session = connect_db()

    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    gender = input('Введите свой пол: ')
    email = input('Введите адрес электорнной почты: ')
    birthdate = input('Введите дату своего рождения в формате \"дд.мм.гггг\" или \"гггг-мм-дд\": ')
    height = input('Введите свой рост: ')

    new_user = User(first_name = name, last_name = last_name, gender = gender, email = email, birthdate = birthdate, height = height)
    session.add(new_user)
    cancel = input('Вы уверены, что данные введены корректно? Да/Нет: ')
    if cancel == "Нет":
        session.rollback()
        print("*Ваши данные не были записаны*")
    else:
        print("*Ваши данные были успешно записаны*")
        session.commit()
# Оставил включенным ;)
main() 
