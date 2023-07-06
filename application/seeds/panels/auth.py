from flask import Blueprint,request,jsonify
from application import db
from application.models.panel_users import PanelUsers
from application.schemas.panel_user_schema import PanelUserSchema
from application.seeds.utils import save_file,remove_file
from werkzeug.security import generate_password_hash,check_password_hash



def panel_login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = PanelUsers.query.filter_by(email=email).first()
    schema = PanelUserSchema(many=False)

    if user and check_password_hash(user.password,password):
        user_data = schema.dump(user)
        return jsonify({
            "status":"logged in successfully",
            "is_logged_in": True,
            "user":user_data
        })

    else:
        return jsonify({
            "status":"invalid email or password",
            "is_logged_in": False
        })


