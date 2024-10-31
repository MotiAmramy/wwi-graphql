from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.orm import sessionmaker

from app.db.models import Base
from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)




# class Test(Base):
#     __tablename__ = "test"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#
# def init_db():
#     Base.metadata.create_all(engine)