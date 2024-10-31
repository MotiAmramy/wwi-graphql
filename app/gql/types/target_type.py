from graphene import ObjectType, Int, String, Field

import app.gql.types.mission_type
from app.db.repository.city_repository import get_city_by_id
from app.db.repository.mission_repository import get_mission_by_id
from app.db.repository.target_type_repository import get_target_type_by_id


class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()
    mission = Field('app.gql.types.mission_type.MissionType')  # Field to retrieve the related mission
    city = Field('app.gql.types.city_type.CityType')  # Field to retrieve the related city
    target_type = Field('app.gql.types.targetType_type.TargetTypeType')  # Field to retrieve the target type

    @staticmethod
    def resolve_mission(root, info):
        return get_mission_by_id(root.mission_id)

    @staticmethod
    def resolve_city(root, info):
        return get_city_by_id(root.city_id)

    @staticmethod
    def resolve_target_type(root, info):
        return get_target_type_by_id(root.target_type_id)




