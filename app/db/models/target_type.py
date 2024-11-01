from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class TargetType(Base):
    __tablename__ = 'targettypes'

    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), nullable=False, unique=True)

    targets = relationship("Target", back_populates="target_type")

    def __repr__(self):
        return f"<TargetType(id={self.target_type_id}, name='{self.target_type_name}')>"