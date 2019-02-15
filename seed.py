import datetime
from sqlalchemy import func

#from model import User, connect_to_db, db, Neighborhood, Restaurant_reaction, Place, Place_comment
from model import *

from server import app


def load_users():
    """Load sample users into database."""

    liz = User(fname="Liz", lname="Law", email="liz@gmail.com", password="123", status="resident")
    ash = User(fname="Ash", lname="Ma", email="ash@gmail.com", password="abc", status="resident")
    tk = User(fname="Tk", lname="Kombarov", email="tk@gmail.com", password="aaa", status="resident")
    jess = User(fname="Jess", lname="Ho", email="jess@gmail.com", password="bbb", status="resident")
    chad = User(fname="Chad", lname="Bradley", email="chad@gmail.com", password="ccc", status="visitor")
    rachel = User(fname="Rachel", lname="Wang", email="rachel@gmail.com", password="haha", status="visitor")
    jon = User(fname="Jon", lname="Whiteaker", email="jon@gmail.com", password="wow", status="resident")

    db.session.add(liz)
    db.session.add(ash)
    db.session.add(tk)
    db.session.add(jess)
    db.session.add(chad)
    db.session.add(rachel)
    db.session.add(jon)

    db.session.commit()


def load_neighborhoods(neighborhood_filename):
    """Load nighborhoods from u.neighborhoodinto database."""

    for i, row in enumerate(open(neighborhood_filename)):
        row = row.rstrip()

        # unpack the row
        neighborhood_id, name, description = row.split("|")

        neighborhood = Neighborhood(neighborhood_id=neighborhood_id,
                                    name=name,
                                    description=description)


        db.session.add(neighborhood)

    db.session.commit()

def load_places_to_visit(places_filename):
    """Load places from u.place into database."""

    for i, row in enumerate(open(places_filename)):
        row = row.rstrip()

        # unpack the row
        place_id, name, neighborhood_id, description = row.split("|")

        place = Place(place_id=place_id,
                        name=name,
                        neighborhood_id=neighborhood_id,
                        description=description)


        db.session.add(place)

    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all() #prevents dupe seeding
    db.create_all()

    neighborhood_filename = "seed_data/u.neighborhood"
    places_filename = "seed_data/u.place"

    load_neighborhoods(neighborhood_filename)
    load_places_to_visit(places_filename)
    load_users()

