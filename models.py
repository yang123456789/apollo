from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from conf.config import MYSQL
from datetime import datetime
import pytz

engine = create_engine('mysql://{username}:{password}@{host}:{port}/{db}?charset={charset}'.format(**MYSQL),
                       encoding="utf8", echo=False)

DB = declarative_base()

Session = sessionmaker(bind=engine)
# create a Session
session = Session()

_datetime = datetime.now(tz=pytz.timezone('Asia/Shanghai'))


class Users(DB):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    create_at = Column(DateTime, default=_datetime)
    username = Column(String(40), nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(12), nullable=False)
    email = Column(String(120), nullable=False)

    # def __init__(self, username, pwd, phone, email):
    #     self.username = username
    #     self.password = pwd
    #     self.phone = phone
    #     self.email = email

    def __repr__(self):
        return '<User %s>' % self.username

    @classmethod
    def get_by_username(cls, username):
        result = session.query(Users).filter(Users.username == username).all()
        session.close()
        if result:
            return result[0]
        return None

    @classmethod
    def get_by_phone(cls, phone):
        result = session.query(Users).filter(Users.phone == phone).all()
        session.close()
        if result:
            return result[0]
        return None

    @classmethod
    def get_by_email(cls, email):
        result = session.query(Users).filter(Users.email == email).all()
        session.close()
        if result:
            return result[0]
        return None


def initdb():
    DB.metadata.create_all(engine)
