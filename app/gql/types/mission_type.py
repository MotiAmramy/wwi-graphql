from graphene import ObjectType, Int, String, Float


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = String()  # Adjust as necessary for date formatting
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()
    targets = List(lambda: TargetType)  # Us