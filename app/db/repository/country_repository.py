
from sqlalchemy.orm import Session

from app.db.database import session_maker
from app.db.models.country import Country


def create_country(country: Country):
    with session_maker() as session:
        session.add(country)
        session.commit()
        session.refresh(country)
        return country

def get_all_countries():
    with session_maker() as session:
        return session.query(Country).all()


def get_country_by_id(country_id):
    with session_maker() as session:
        return session.query(Country).filter(Country.country_id == country_id).first()


def update_country(country_id, country_name=None):
    with session_maker() as session:
        country = session.query(Country).filter(Country.country_id == country_id).first()
        if country:
            if country_name is not None:
                country.country_name = country_name
            session.commit()
        return country


def delete_country(country_id):
    with session_maker() as session:
        country = session.query(Country).filter(Country.country_id == country_id).first()
        if country:
            session.delete(country)
            session.commit()
            return True
        return False