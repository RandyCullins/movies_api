from flask import Flask
from flask_marshmallow import Marshmallow
from db import db, init_db
from models.actors_model import Actors
from models.directors_model import Directors
from models.movies_model import Movies

import controllers

app = Flask(__name__)

database_host = "127.0.01:5432"
database_name = "movies"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
    with app.app_context():
        db.create_all()

        print("Querying for Movie...")
        movie_data = db.session.query(Movies).filter(Movies.movie_name == "Top Gun").first()
        if movie_data == None:
            print("Movie not found! Creating Top Gun...")
            actor_data = db.session.query(Actors).filter(Actors.actor_first_name == "Tom").first()
            director_data = db.session.query(Directors).filter(Directors.director_first_name == "Tony").first()
            if actor_data == None:
                print("Adding Actor: Tom Cruise...")
                actor_first_name = "Tom"
                actor_last_name = "Cruise"
                new_actor = Actors(actor_first_name, actor_last_name)

                db.session.add(new_actor)
                db.session.commit()
                
            if director_data == None:
                print("Adding Director: Tony Scott...")
                director_first_name = "Tony"
                director_last_name = "Scott"
                new_director = Directors(director_first_name, director_last_name)

                db.session.add(new_director)
                db.session.commit()
                
                print("Adding Movie: Top Gun...")
                new_movie = Movies("Top Gun", new_actor.actor_id, actor_first_name, actor_last_name, new_director.director_id, director_first_name, director_last_name)
                db.session.add(new_movie)
                db.session.commit()
                print("Movie Added! Starting Application...")

        else:
            print("Top Gun found! Starting Application...")

@app.route('/actors/add', methods=['POST'])
def add_actor():
    return controllers.add_actor()

@app.route('/actors/list')
def get_all_actors():
    return controllers.get_all_actors()

@app.route('/actors/list/<actor_id>')
def get_one_actor(actor_id):
    return controllers.get_one_actor(actor_id)

@app.route('/actors/edit/<actor_id>', methods=['PUT'])
def edit_actor(actor_id):
    return controllers.edit_actor(actor_id)

@app.route('/actors/delete/<actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    return controllers.delete_actor(actor_id)

@app.route('/actors/deactivate/<actor_id>', methods=['PUT'])
def deactivate_actor(actor_id):
    return controllers.deactivate_actor(actor_id)

@app.route('/actors/activate/<actor_id>', methods=['PUT'])
def activate_actor(actor_id):
    return controllers.activate_actor(actor_id)

@app.route('/actor/search/<search_term>')
def actors_get_by_search(search_term):
    return controllers.actors_get_by_search(search_term)

@app.route('/directors/add', methods=['POST'])
def add_director():
    return controllers.add_director()

@app.route('/directors/list')
def get_all_directorrs():
    return controllers.get_all_directors()

@app.route('/directors/list/<director_id>')
def get_one_director(director_id):
    return controllers.get_one_director(director_id)

@app.route('/directors/edit/<director_id>', methods=['PUT'])
def edit_director(director_id):
    return controllers.edit_director(director_id)

@app.route('/directors/delete/<director_id>', methods=['DELETE'])
def delete_director(director_id):
    return controllers.delete_director(director_id)

@app.route('/directors/deactivate/<director_id>', methods=['PUT'])
def deactivate_director(director_id):
    return controllers.deactivate_director(director_id)

@app.route('/directors/activate/<director_id>', methods=['PUT'])
def activate_director(director_id):
    return controllers.activate_director(director_id)

@app.route('/director/search/<search_term>')
def directors_get_by_search(search_term):
    return controllers.directors_get_by_search(search_term)

@app.route('/movies/add', methods=['POST'])
def movie_add():
    return controllers.movie_add()

@app.route('/movies/list')
def get_all_movies():
    return controllers.get_all_movies()

@app.route('/movies/list/<movie_id>')
def get_one_movie(movie_id):
    return controllers.get_one_movie(movie_id)

@app.route('/movies/edit/<movie_id>', methods=['PUT'])
def edit_movie(movie_id):
    return controllers.edit_movie(movie_id)

@app.route('/movies/delete/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    return controllers.delete_movie(movie_id)

@app.route('/movies/deactivate/<movie_id>', methods=['PUT'])
def deactivate_movie(movie_id):
    return controllers.deactivate_movie(movie_id)

@app.route('/movies/activate/<movie_id>', methods=['PUT'])
def activate_movie(movie_id):
    return controllers.activate_movie(movie_id)

@app.route('/movie/search/<search_term>')
def movies_get_by_search(search_term):
    return controllers.movies_get_by_search(search_term)

@app.route('/search/<search_term>')
def get_all_by_search(search_term):
    return controllers.get_all_by_search(search_term)

if __name__ == "__main__":
    create_all()
    app.run()