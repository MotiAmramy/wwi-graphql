from graphene import ObjectType, Int, String, Float, Field
from app.db.repository.country_repository import get_country_by_id


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()
    country = Field('app.gql.types.country_type.CountryType')

    @staticmethod
    def resolve_country(root, info):
        return get_country_by_id(root.country_id)