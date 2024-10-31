from graphene import List, String, Int, ObjectType

import app.gql.types.city_type
from app.db.database import session_maker
from app.db.models.city import City
from app.db.repository.city_repository import get_cities_by_country_id


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
    cities = List('app.gql.types.city_type.CityType')

    @staticmethod
    def resolve_cities(root, info):
        return get_cities_by_country_id(root.country_id)