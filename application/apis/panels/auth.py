from flask import Blueprint
from application.seeds.panels.auth import panel_login
panel_auth = Blueprint("panel_auth",__name__)

@panel_auth.route('/panel/login',methods=['POST'])
def PanelLogin():
    return panel_login()