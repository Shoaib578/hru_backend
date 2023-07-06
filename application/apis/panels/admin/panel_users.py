from application.seeds.panels.admin import panel_users
from flask import Blueprint

admin_panel_user = Blueprint('admin_panel_user', __name__,static_folder="static")

@admin_panel_user.route('/add',methods=['POST'])
def AddPanelUser():
    return panel_users.add_panel_user()


@admin_panel_user.route('/delete_panel_user',methods=['DELETE'])
def DeletePanelUser():
    return panel_users.delet_panel_user()

@admin_panel_user.route('/get_all_users')
def GetAllUsers():
    return panel_users.get_all_users()

@admin_panel_user.route('/get_all_teachers',methods=['GET'])
def GetAllTeachers():
    return panel_users.get_all_teachers()

@admin_panel_user.route('/get_teacher_courses')
def AdminGetTeacherCourses():
    return panel_users.admin_get_teacher_courses()

@admin_panel_user.route('/get_all_admin',methods=['GET'])
def GetAllStudents():
    return panel_users.get_all_admins()