from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), nullable=True)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(Numeric, nullable=True)
    longitude = Column(Numeric, nullable=True)

    # Relationship to the Country model (if you have one)
    country = relationship("Country", back_populates="cities")

    def __repr__(self):
        return f"<City(id={self.city_id}, name='{self.city_name}', country_id={self.country_id})>"