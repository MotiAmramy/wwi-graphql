from app.db.database import session_maker
from app.db.models import Target, City, Country
from app.db.models.mission import Mission



def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()


def get_missions_by_date_range(start_date, end_date):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()


def get_missions_by_country_name(country_name):
    with session_maker() as session:
        return session.query(Mission).join(Mission.targets).join(Target.city).join(City.country).filter(Country.country_name == country_name).all()


def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return session.query(Mission).join(Mission.targets).filter(Target.target_industry == target_industry).all()

def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()


def get_attack_results_by_type(attack_type):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.attack_type == attack_type).all()