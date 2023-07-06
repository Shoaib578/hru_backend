from application.seeds.panels.admin import teaching_applications
from flask import Blueprint


admin_teaching_application_routes = Blueprint('admin_teaching_application_routes',__name__)

@admin_teaching_application_routes.route('/add_application',methods=['POST'])
def AddApplication():
    return teaching_applications.AddApplication()


@admin_teaching_application_routes.route('/get_teaching_applications')
def GetApplication():
    return teaching_applications.GetAllApplications()


@admin_teaching_application_routes.route('/accept_or_reject_application')
def accept_or_reject_application():
    return teaching_applications.AcceptorRejectApplication()