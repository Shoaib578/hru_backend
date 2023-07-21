from flask import Flask,Blueprint
from application.seeds.main import user

user_routes = Blueprint('user_route', __name__,static_folder='../static')


@user_routes.route('/register', methods=['POST'])
def Register():
    return user.register_user()


@user_routes.route('/login',methods=['POST'])
def Login():
    return user.login_user()


@user_routes.route('/get_user_details')
def GetUserDetails():
    return user.get_user_details()



@user_routes.route('/update_user_details',methods=['POST'])
def UpdateUserDetails():
    return user.update_user_details()


@user_routes.route('/change_password',methods=['POST'])
def ChangePassword():
    return user.change_password()


@user_routes.route('/send_mail',methods=['POST'])
def SendMail():
    return user.send_mail()