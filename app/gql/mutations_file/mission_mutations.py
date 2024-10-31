from graphene import Mutation, InputObjectType, Int, String, Float, Field
from app.db.repository.mission_repository import create_mission
from app.db.repository.target_repository import create_target
from app.gql.types.mission_type import MissionType
from app.gql.types.target_type import TargetType


class MissionInput(InputObjectType):
    mission_date = String(required=True)
    airborne_aircraft = Float(required=True)
    attacking_aircraft = Float(required=True)
    bombing_aircraft = Float(required=True)
    aircraft_returned = Float(required=True)
    aircraft_failed = Float(required=True)
    aircraft_damaged = Float(required=True)
    aircraft_lost = Float(required=True)


class AddMission(Mutation):
    class Arguments:
        mission_input = MissionInput(required=True)


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_input):
        new_mission = create_mission(mission_input)
        return AddMission(mission=new_mission)









class AddTarget(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        target_industry = String(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=False)
        target_priority = Int(required=False)

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, mission_id, target_industry, city_id, target_type_id=None, target_priority=None):
        new_target = Target(
            mission_id=mission_id,
            target_industry=target_industry,
            city_id=city_id,
            target_type_id=target_type_id,
            target_priority=target_priority
        )

        # Use the create_target function to handle the database operations
        created_target = create_target(new_target)

        return AddTarget(target=created_target)