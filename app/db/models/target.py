from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class Target(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'), nullable=True)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'), nullable=True)
    target_priority = Column(Integer, nullable=True)


    mission = relationship("Mission", back_populates="targets")
    city = relationship("City", back_populates="targets")
    target_type = relationship("TargetType", back_populates="targets")

    def __repr__(self):
        return (f"<Target(id={self.target_id}, industry='{self.target_industry}', "
                f"city_id={self.city_id}, mission_id={self.mission_id}, "
                f"type_id={self.target_type_id}, priority={self.target_priority})>")