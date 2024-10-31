from app.db.database import session_maker
from app.db.models.target_type import TargetType


def create_target_type(target_type: TargetType):
    with session_maker() as session:
        session.add(target_type)
        session.commit()
        session.refresh(target_type)
        return target_type

def get_all_target_types():
    with session_maker() as session:
        return session.query(TargetType).all()

def get_target_type_by_id(target_type_id):
    with session_maker() as session:
        return session.query(TargetType).filter(TargetType.target_type_id == target_type_id).first()

def update_target_type(target_type_id, target_type_name=None):
    with session_maker() as session:
        target_type = session.query(TargetType).filter(TargetType.target_type_id == target_type_id).first()
        if target_type:
            if target_type_name is not None:
                target_type.target_type_name = target_type_name
            session.commit()
        return target_type

def delete_target_type(target_type_id):
    with session_maker() as session:
        target_type = session.query(TargetType.filter(TargetType.target_type_id == target_type_id).first())
        if target_type:
            session.delete(target_type)
            session.commit()
            return True
        return False