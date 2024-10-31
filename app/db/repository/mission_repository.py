from app.db.database import session_maker
from app.db.models.mission import Mission



def create_mission(mission_input):
    new_mission = Mission(
        mission_date=mission_input.mission_date,
        airborne_aircraft=mission_input.airborne_aircraft,
        attacking_aircraft=mission_input.attacking_aircraft,
        bombing_aircraft=mission_input.bombing_aircraft,
        aircraft_returned=mission_input.aircraft_returned,
        aircraft_failed=mission_input.aircraft_failed,
        aircraft_damaged=mission_input.aircraft_damaged,
        aircraft_lost=mission_input.aircraft_lost
    )

    with session_maker() as session:
        session.add(new_mission)
        session.commit()
        session.refresh(new_mission)
        return new_mission

def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()

def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

def update_mission(mission_id, mission_date=None, airborne_aircraft=None,
                   attacking_aircraft=None, bombing_aircraft=None,
                   aircraft_returned=None, aircraft_failed=None,
                   aircraft_damaged=None, aircraft_lost=None):
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        if mission:
            if mission_date is not None:
                mission.mission_date = mission_date
            if airborne_aircraft is not None:
                mission.airborne_aircraft = airborne_aircraft
            if attacking_aircraft is not None:
                mission.attacking_aircraft = attacking_aircraft
            if bombing_aircraft is not None:
                mission.bombing_aircraft = bombing_aircraft
            if aircraft_returned is not None:
                mission.aircraft_returned = aircraft_returned
            if aircraft_failed is not None:
                mission.aircraft_failed = aircraft_failed
            if aircraft_damaged is not None:
                mission.aircraft_damaged = aircraft_damaged
            if aircraft_lost is not None:
                mission.aircraft_lost = aircraft_lost
            session.commit()
        return mission

def delete_mission(mission_id):
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        if mission:
            session.delete(mission)
            session.commit()
            return True
        return False