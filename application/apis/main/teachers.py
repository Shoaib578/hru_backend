from application.seeds.main import teacher
from flask import Blueprint
main_teacher_routes = Blueprint('main_teacher_routes',__name__)


@main_teacher_routes.route('/get_all_teachers')
def GetAllTeachers():
    return teacher.get_all_teachers()

@main_teacher_routes.route('/get_four_teachers')
def GetFourTeachers():
    return teacher.get_four_teachers()


@main_teacher_routes.route('/get_teacher_details')
def GetTeacherDetails():
    return teacher.get_teacher_details()


@main_teacher_routes.route('/send_application',methods=['POST'])
def SendApplication():
    return teacher.send_application()