from flask import Blueprint
from application.seeds.panels.teacher import courses

teacher_courses_routes = Blueprint('teacher_courses_routes',__name__,static_folder='static')


@teacher_courses_routes.route('/get_teacher_courses',methods=['GET'])
def GetCourses():
    return courses.get_teacher_courses()


@teacher_courses_routes.route('/add_course',methods=['POST'])
def AddCourse():
    return courses.add_course()

@teacher_courses_routes.route('/delete_course',methods=['DELETE'])
def delete_course():
    return courses.delete_course()

@teacher_courses_routes.route('/view_course',methods=['GET'])
def view_course():
    return courses.view_course()



@teacher_courses_routes.route('/update_course',methods=['POST'])
def UpdateCourse():
    return courses.update_course()