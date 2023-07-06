from flask import Blueprint
from application.seeds.main import courses
from flask import request

main_courses_routes = Blueprint('main_courses_routes',__name__)


@main_courses_routes.route('/get_all_courses', methods=['GET'])
def getAllCourses():
    return courses.GetAllCourses()


@main_courses_routes.route('/view_course')
def ViewCourse():
    return courses.view_course()

@main_courses_routes.route('/buy_course',methods=['POST'])
def BuyCourse():
    return courses.buy_course()



@main_courses_routes.route('/get_owned_courses',methods=['GET'])
def GetOwnedCourses():
    return courses.GetOwnedCourses()