from sqlalchemy import Column, Integer, String, Float
from src.lib.classes.db import Base

class ItemModel(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_offer = Column(String, nullable=True)