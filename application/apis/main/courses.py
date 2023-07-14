from flask import Blueprint
from application.seeds.main import courses


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


@main_courses_routes.route('/get_all_links')
def GetAllLinks():
    return courses.get_all_links()


@main_courses_routes.route('/add_link',methods=['POST'])
def AddLink():
    return courses.add_link()


@main_courses_routes.route('/delete_link',methods=['DELETE'])
def DeleteLink():
    return courses.delete_link()

    


@main_courses_routes.route('/get_course_by_link_code')
def GetCourseByLinkCode():
    return courses.get_course_by_link_code()