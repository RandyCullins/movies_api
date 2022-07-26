from flask import Blueprint
from controllers import directors_controllers

director = Blueprint('director', __name__)

@director.route('/directors/add', methods=['POST'])
def add_director():
    return directors_controllers.add_director()

@director.route('/directors/list')
def get_all_directorrs():
    return directors_controllers.get_all_directors()

@director.route('/directors/list/<director_id>')
def get_one_director(director_id):
    return directors_controllers.get_one_director(director_id)

@director.route('/directors/edit/<director_id>', methods=['PUT'])
def edit_director(director_id):
    return directors_controllers.edit_director(director_id)

@director.route('/directors/delete/<director_id>', methods=['DELETE'])
def delete_director(director_id):
    return directors_controllers.delete_director(director_id)

@director.route('/directors/deactivate/<director_id>', methods=['PUT'])
def deactivate_director(director_id):
    return directors_controllers.deactivate_director(director_id)

@director.route('/directors/activate/<director_id>', methods=['PUT'])
def activate_director(director_id):
    return directors_controllers.activate_director(director_id)

@director.route('/director/search/<search_term>')
def directors_get_by_search(search_term):
    return directors_controllers.directors_get_by_search(search_term)