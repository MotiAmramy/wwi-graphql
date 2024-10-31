from graphene import ObjectType, Field, List, Int, String
from app.db.database import session_maker
from app.db.models import City
from app.db.repository.mission_repository import get_mission_by_id, get_all_missions
from app.db.repository.query_repository import get_missions_by_target_industry, \
    get_missions_by_date_range, get_attack_results_by_type, get_missions_by_country_name
from app.gql.types.city_type import CityType
from app.gql.types.mission_type import MissionType



class Query(ObjectType):
    all_cities = List(CityType)
    mission_by_id = Field(MissionType, mission_id=Int(required=True))
    missions_by_date_range = List(MissionType, start_date=String(required=True), end_date=String(required=True))
    missions_by_target_industry = List(MissionType, target_industry=String(required=True))
    missions_by_country_name = List(MissionType, country_name=String(required=True))
    all_missions = List(MissionType)
    attack_results_by_type = List(MissionType, attack_type=String(required=True))


    @staticmethod
    def resolve_all_cities(root, info):
        with session_maker() as session:
            return session.query(City).all()



    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id)

    @staticmethod
    def resolve_missions_by_date_range(root, info, start_date, end_date):
        return get_missions_by_date_range(start_date, end_date)

    @staticmethod
    def resolve_missions_by_country_name(root, info, country_name):
        return get_missions_by_country_name(country_name)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return get_missions_by_target_industry(target_industry)

    @staticmethod
    def resolve_all_missions(root, info):
        return get_all_missions()

    @staticmethod
    def resolve_attack_results_by_type(root, info, attack_type):
        return get_attack_results_by_type(attack_type)