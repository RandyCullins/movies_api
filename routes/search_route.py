from flask import Blueprint
from controllers import search_all_controller

search = Blueprint('search', __name__)

@search.route('/search/<search_term>')
def get_all_by_search(search_term):
    return search_all_controller.get_all_by_search(search_term)