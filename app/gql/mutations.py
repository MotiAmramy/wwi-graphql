from graphene import ObjectType
from app.gql.mutations_file.mission_mutations import AddMission, AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
