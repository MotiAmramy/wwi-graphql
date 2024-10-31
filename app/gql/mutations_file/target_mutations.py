from graphene import Mutation, Int, String, Field
from app.db.models import  Target
from app.gql.types.target_type import TargetType
from app.db.repository.target_repository import create_target





class CreateTarget(Mutation):
    class Arguments:
        target_industry = String(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=False)
        target_priority = Int(required=False)

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, target_industry, city_id, target_type_id=None, target_priority=None):
        new_target = Target(
            target_industry=target_industry,
            city_id=city_id,
            target_type_id=target_type_id,
            target_priority=target_priority
        )

        created_target = create_target(new_target)

        return CreateTarget(target=created_target)
