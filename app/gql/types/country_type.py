from graphene import List, String, Int, ObjectType


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
    cities = List(CityType)