from graphene import ObjectType, Int, String, List


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()
    targets = List(TargetType)