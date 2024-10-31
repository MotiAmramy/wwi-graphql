from graphene import Mutation, InputObjectType, Int, String, Float, Field, Boolean
from app.db.repository.mission_repository import create_mission, update_mission_five_field, delete_mission
from app.gql.types.mission_type import MissionType



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





class UpdateMissionInput(InputObjectType):
    mission_id = Int(required=True)
    aircraft_returned = Float(required=True)
    aircraft_failed = Float(required=True)
    aircraft_damaged = Float(required=True)
    aircraft_lost = Float(required=True)

class UpdateMission(Mutation):
    class Arguments:
        update_mission_input = UpdateMissionInput(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, update_mission_input):
        mission = update_mission_five_field(update_mission_input)
        return UpdateMission(mission=mission)


class DeleteMissionMutation(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    success = Boolean()

    @staticmethod
    def mutate(self, info, mission_id):
        mission = delete_mission(mission_id)
        if mission:
            return DeleteMissionMutation(success=True)