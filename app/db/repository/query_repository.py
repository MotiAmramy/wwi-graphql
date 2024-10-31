from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Target, City, Country, TargetType
from app.db.models.mission import Mission



def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()


def get_missions_by_date_range(start_date, end_date):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()


def get_missions_by_country_name(country_name):
    with (session_maker() as session):
        return session.query(Mission).join(Mission.targets).join(Target.city).join(City.country).filter(Country.country_name == country_name).all()


def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return session.query(Mission).join(Mission.targets).filter(Target.target_industry == target_industry).all()

def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()


def get_mission_result_by_target_type(target_type_name):
    with session_maker() as session:
        return session.query(Mission).join(Mission.targets).join(Target.target_type).filter(TargetType.target_type_name == target_type_name).all()



def get_mission_statistics_by_city_id(city_id):
    with session_maker() as session:
        result = session.query(
            City.city_id,
            City.city_name,
            func.count(Mission.mission_id).label('mission_count'),
            func.avg(Target.target_priority).label('average_priority')
        ) \
        .join(City.targets) \
        .join(Target.mission) \
        .filter(City.city_id == city_id) \
        .group_by(City.city_id, City.city_name) \
        .first()

        return result

def get_missions_with_high_lost_aircraft(min_lost_aircraft):
    with session_maker() as session:
        return session.query(
            Country.country_id,
            Country.country_name,
            func.count(Mission.mission_id).label('total_missions'),
            func.sum(Mission.aircraft_lost).label('total_lost_aircraft'),
            func.avg(Mission.aircraft_lost).label('average_lost_aircraft')
        ).join(Country.cities).join(City.targets).join(Target.mission) \
            .filter(Mission.aircraft_lost >= min_lost_aircraft) \
            .group_by(Country.country_id, Country.country_name) \
            .all()



def get_missions_by_target_industry_average():
    with session_maker() as session:
        return session.query(
            Target.target_industry,
            func.count(Mission.mission_id).label('mission_count'),
            func.sum(Target.target_priority).label('total_priority'),
            func.avg(Target.target_priority).label('average_priority')
        ) \
        .join(Mission.targets) \
        .group_by(Target.target_industry) \
        .all()