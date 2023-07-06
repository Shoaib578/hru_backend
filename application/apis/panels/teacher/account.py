from flask import Blueprint
from application.seeds.panels.teacher import account
teacher_account_routes = Blueprint('teacher_account_routes',__name__)



@teacher_account_routes.route('/get_teacher_details')
def GetTeacherDetails():
    return account.get_teacher_details()


@teacher_account_routes.route('/update_teacher_account',methods=['POST'])
def GetTeacherSubjects():
    return account.update_teacher_account()