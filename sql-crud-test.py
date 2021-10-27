from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model with my favorite food
class FavPlaces(base):
    __tablename__ = "FavPlaces"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# to create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an acutal session by calling the Session() subclass defined above
session = Session()

# creating the databse using declarative_base subclass
base.metadata.create_all(db)

# creating records for all the favorite places
catalunya = FavPlaces(
    name="Catalunya",
    capital_city="Barcelona",
    population=7000
)

uk = FavPlaces(
    name="United Kingdom",
    capital_city="London",
    population=23000000
)

france = FavPlaces(
    name="France",
    capital_city="Paris",
    population=4300
)

# session.add(catalunya)
# session.add(uk)
# session.add(france)

# updating a single record



# query database to find all records
places = session.query(FavPlaces)
for place in places:
    print(
        place.id,
        place.name,
        place.capital_city,
        place.population,
        sep="|"
    )
