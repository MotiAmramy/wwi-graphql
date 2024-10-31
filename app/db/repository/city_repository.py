from app.db.database import session_maker
from app.db.models.city import City





def create_city(city: City):
    with session_maker() as session:

        session.add(city)
        session.commit()
        session.refresh(city)
        return city



def get_all_cities():
    with session_maker() as session:
        return session.query(City).all()



def get_city_by_id(city_id):
    with session_maker() as session:
        return session.query(City).filter(City.city_id == city_id).first()



# Update a city
def update_city(city_id, city_name=None, country_id=None, latitude=None, longitude=None):
    with session_maker() as session:
        city = session.query(City).filter(City.city_id == city_id).first()
        if city:
            if city_name is not None:
                city.city_name = city_name
            if country_id is not None:
                city.country_id = country_id
            if latitude is not None:
                city.latitude = latitude
            if longitude is not None:
                city.longitude = longitude
            session.commit()
        return city


def delete_city(city_id):
    with session_maker() as session:
        city = session.query(City).filter(City.city_id == city_id).first()
        if city:
            session.delete(city)
            session.commit()
            return True
        return False






def get_cities_by_country_id(country_id):
    with session_maker() as session:
        return session.query(City).filter(City.country_id == country_id).all()