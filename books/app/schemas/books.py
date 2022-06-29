from datetime import datetime

from sqlalchemy import Column, Integer, String, Date

from app.database_connection import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Date, default=datetime.today())


class AudioBooks(Base):
    __tablename__ = "audiobooks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Date, default=datetime.today())