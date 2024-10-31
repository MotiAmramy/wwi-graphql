from graphene import Mutation, InputObjectType, Int, String, Float, Field

from app.db.database import session_maker
from app.gql.types.mission_type import MissionType


class MissionInput(InputObjectType):
    mission_id = Int()
    mission_date = String() 
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()


class AddMission(Mutation):
    class Arguments:
        mission_input = MissionInput(required=True)


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_input):
        with session_maker() as session:
            try:
                # Create the new employee
                new_emp = Employee(
                    name=employee_input.name,
                    email=employee_input.email,
                    industry=employee_input.industry
                )
                session.add(new_emp)
                session.commit()
                session.refresh(new_emp)

                # Create the new job associated with the new employee
                new_job = Job(
                    title=job_input.title,
                    description=job_input.description,
                    employee_id=new_emp.id
                )
                with session_maker() as session:
                    session.add(new_job)
                    session.commit()
                    session.refresh(new_job)

                # Return a serialized employee object
                    return AddEmp(employee=new_emp, job=new_job)
            except Exception as e:
                session.rollback()  # Rollback in case of error
                print(f"An error occurred: {e}")
                raise e  # Reraise or handle the exception as needed
