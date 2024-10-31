from graphene import ObjectType
from app.gql.mutations_file.mission_mutations import AddMission, UpdateMission, DeleteMissionMutation
from app.gql.mutations_file.target_mutations import CreateTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    create_target = CreateTarget.Field()
    update_mission = UpdateMission.Field()
    delete_mission = DeleteMissionMutation.Field()
