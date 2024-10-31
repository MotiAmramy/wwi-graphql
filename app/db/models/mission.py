from sqlalchemy import Column, Integer, Numeric, Date, Float

from app.db.models import Base


class Mission(Base):
    __tablename__ = 'missions'

    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=True)
    airborne_aircraft = Column(Float, nullable=True)
    attacking_aircraft = Column(Float, nullable=True)
    bombing_aircraft = Column(Float, nullable=True)
    aircraft_returned = Column(Float, nullable=True)
    aircraft_failed = Column(Float, nullable=True)
    aircraft_damaged = Column(Float, nullable=True)
    aircraft_lost = Column(Float, nullable=True)

    def __repr__(self):
        return (f"<Mission(id={self.mission_id}, date={self.mission_date}, "
                f"airborne={self.airborne_aircraft}, attacking={self.attacking_aircraft}, "
                f"bombing={self.bombing_aircraft}, returned={self.aircraft_returned}, "
                f"failed={self.aircraft_failed}, damaged={self.aircraft_damaged}, "
                f"lost={self.aircraft_lost})>")