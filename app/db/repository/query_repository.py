from app.db.database import session_maker
from app.db.models.mission import Mission


@staticmethod
def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

@staticmethod
def get_missions_by_date_range(start_date, end_date):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()

@staticmethod
def get_missions_by_country_id(country_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.country_id == country_id).all()

@staticmethod
def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.target_industry == target_industry).all()

@staticmethod
def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()

@staticmethod
def get_attack_results_by_type(attack_type):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.attack_type == attack_type).all()