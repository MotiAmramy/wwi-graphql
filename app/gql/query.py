from graphene import ObjectType, Field, List, Int, String, Float
from app.db.repository.mission_repository import get_mission_by_id, get_all_missions
from app.db.repository.query_repository import get_missions_by_target_industry, \
    get_missions_by_date_range, get_missions_by_country_name, get_mission_result_by_target_type, \
    get_mission_statistics_by_city_id, get_missions_with_high_lost_aircraft, get_missions_by_target_industry_average
from app.gql.types.mission_type import MissionType



class CityStatisticsType(ObjectType):
    city_id = Int()
    city_name = String()
    mission_count = Int()
    average_priority = Float()


class MissionStatisticsByCountryType(ObjectType):
    country_id = Int()
    country_name = String()
    total_missions = Int()
    total_lost_aircraft = Float()
    average_lost_aircraft = Float()

class MissionIndustryStatsType(ObjectType):
    target_industry = String()
    mission_count = Int()
    total_priority = Float()
    average_priority = Float()




class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int(required=True))
    missions_by_date_range = List(MissionType, start_date=String(required=True), end_date=String(required=True))
    missions_by_target_industry = List(MissionType, target_industry=String(required=True))
    missions_by_country_name = List(MissionType, country_name=String(required=True))
    all_missions = List(MissionType)
    mission_result_by_target_type = List(MissionType, target_type=String(required=True))
    mission_statistics_by_city = Field(
        CityStatisticsType,
        city_id=String(required=True)
    )
    missions_with_high_lost_aircraft = List(
        MissionStatisticsByCountryType,
        min_lost_aircraft=Float(required=True)
    )
    get_all_missions_by_target_industry_average = List(MissionIndustryStatsType)


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
    def resolve_mission_result_by_target_type(root, info, target_type):
        return get_mission_result_by_target_type(target_type)

    @staticmethod
    def resolve_mission_statistics_by_city(root, info, city_id):
        stats = get_mission_statistics_by_city_id(city_id)
        print(stats)
        if stats:
            return {
                'city_id': stats.city_id,
                'city_name': stats.city_name,
                'mission_count': stats.mission_count,
                'average_priority': stats.average_priority
            }
        return None

    @staticmethod
    def resolve_missions_with_high_lost_aircraft(root, info, min_lost_aircraft):
        return get_missions_with_high_lost_aircraft(min_lost_aircraft)



    @staticmethod
    def resolve_get_all_missions_by_target_industry_average(root, info):
        stats = get_missions_by_target_industry_average()
        return [{
            'target_industry': stat.target_industry,
            'mission_count': stat.mission_count,
            'total_priority': stat.total_priority,
            'average_priority': stat.average_priority
        } for stat in stats]