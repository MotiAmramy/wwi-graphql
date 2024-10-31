from app.db.database import session_maker
from app.db.models.target import Target


def create_target(target: Target):
    with session_maker() as session:
        session.add(target)
        session.commit()
        session.refresh(target)
        return target

def get_all_targets():
    with session_maker() as session:
        return session.query(Target).all()

def get_target_by_id(target_id):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_id == target_id).first()

def update_target(target_id, target_industry=None, mission_id=None,
                  city_id=None, target_type_id=None, target_priority=None):
    with session_maker() as session:
        target = session.query(Target).filter(Target.target_id == target_id).first()
        if target:
            if target_industry is not None:
                target.target_industry = target_industry
            if mission_id is not None:
                target.mission_id = mission_id
            if city_id is not None:
                target.city_id = city_id
            if target_type_id is not None:
                target.target_type_id = target_type_id
            if target_priority is not None:
                target.target_priority = target_priority
            session.commit()
        return target

def delete_target(target_id):
    with session_maker() as session:
        target = session.query(Target).filter(Target.target_id == target_id).first()
        if target:
            session.delete(target)
            session.commit()
            return True
        return False




def get_targets_by_mission_id(mission_id):
    with session_maker() as session:
        return session.query(Target).filter(Target.mission_id == mission_id).all()





def get_targets_by_type_id(target_type_id):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_type_id == target_type_id).all()




