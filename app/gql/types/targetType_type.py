from graphene import ObjectType, Int, String, List

import app.gql.types.target_type
from app.db.repository.target_repository import get_targets_by_type_id


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()
    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_targets(root, info):
        return get_targets_by_type_id(root.target_type_id)