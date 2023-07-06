from application.seeds.panels.admin import featured_courses
from flask import Blueprint

admin_featured_course_routes = Blueprint('admin_featured_course_routes', __name__,static_folder="static")


@admin_featured_course_routes.route('/get_featured_courses')
def GetFeaturedcourse():
    return featured_courses.GetAllFeaturedCourses()


@admin_featured_course_routes.route('/get_courses_for_dropdown')
def GetAllCoursesForDropdown():
    return featured_courses.GetAllCoursesForDropdown()


@admin_featured_course_routes.route('/delete_featured_course',methods=['DELETE'])
def Deletefeaturedcourse():
    return featured_courses.DeleteFeaturedCourse()



@admin_featured_course_routes.route('/add_featured_course',methods=['POST'])
def AddFeaturedCourse():
    return featured_courses.AddFeaturedCourse()