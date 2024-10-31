from graphene import ObjectType, Int, String, Float, List
from app.db.repository.target_repository import get_targets_by_mission_id


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = String()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()
    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_targets(root, info):
        return get_targets_by_mission_id(root.mission_id)





