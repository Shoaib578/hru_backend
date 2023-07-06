from application import db
from application.models.panel_users import PanelUsers
from application.schemas.panel_user_schema import PanelUserSchema
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

from application.seeds.utils import save_file,remove_file



def get_teacher_details():
    user_id = request.args.get('user_id')
    teacher_query= PanelUsers.query.filter_by(panel_userid=user_id).first()
    schema = PanelUserSchema(many=False)
    teacher = schema.dump(teacher_query)
    return jsonify({
        "data":teacher
    })


def update_teacher_account():
    user_id = request.form.get('user_id')
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    title = request.form.get('title')
    description = request.form.get('description')

    teacher= PanelUsers.query.filter_by(panel_userid=user_id).first()
    teacher.email = email
    teacher.password = generate_password_hash(password)
    teacher.name = name
    teacher.title = title
    teacher.description = description
    db.session.commit()
    return jsonify({
        "is_updated":True,
        "status":"Account Updated successfully",
    })