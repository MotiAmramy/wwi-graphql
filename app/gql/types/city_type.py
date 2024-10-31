from graphene import ObjectType, Int, String, Float




class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()