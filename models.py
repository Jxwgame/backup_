from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    description = Column(String, index=True)
    abbre_title = Column(String, index=True)
    category = Column(String, index=True)

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Integer, index=True)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    menu = Column(String, index=True)
    total = Column(Integer, index=True)
    note = Column(String, index=True)

    ##FIXXX