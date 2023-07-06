from flask import Blueprint
from application.seeds.main import featured_courses

main_featured_courses_routes = Blueprint('main_featured_courses_routes',__name__)


@main_featured_courses_routes.route('/get_all_featured_courses')
def getFeaturedCourses():
    return featured_courses.GetAllFeaturedCourses()