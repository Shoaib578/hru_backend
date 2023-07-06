from application import db
from flask import jsonify,request
from application.models.panel_users import PanelUsers
from application.schemas.panel_user_schema import PanelUserSchema
from werkzeug.security import generate_password_hash,check_password_hash


def update_admin_account():
    user_id = request.form.get('user_id')
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')

    admin = PanelUsers.query.get(user_id)
    admin.name = name
    admin.email = email
    admin.password = generate_password_hash(password)
    db.session.commit()
    return jsonify({
        "status":"admin account updated",
        "is_updated":True
    })



def get_admin_details():
    user_id = request.args.get('user_id')
    
    admin = PanelUsers.query.get(user_id)
    schema = PanelUserSchema(many=False)
    admin_details = schema.dump(admin)
    print(admin_details)
    return jsonify({
        "data":admin_details
    })
