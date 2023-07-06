from application.models.panel_users import PanelUsers
from application.schemas.panel_user_schema import PanelUserSchema
from application.models.courses import Courses
from application.schemas.course_schema import CourseSchema
from application.models.applications import Applications
from application import db
from sqlalchemy import text
from flask import Flask,jsonify,request
from application.seeds.utils import save_file


def get_all_teachers():
    teachers = PanelUsers.query.filter_by(is_teacher=1).all()
    schema = PanelUserSchema(many=True)
    data = schema.dump(teachers)
    return jsonify({
        "data":data
    })

def get_four_teachers():
    teachers = PanelUsers.query.filter_by(is_teacher=1).limit(4).all()
    schema = PanelUserSchema(many=True)
    data = schema.dump(teachers)
    return jsonify({
        "data":data
    })

def get_teacher_details():
    teacher_id = request.args.get('teacher_id')
    teacher = PanelUsers.query.filter_by(panel_userid=teacher_id).first()
    schema = PanelUserSchema(many=False)
    teacher = schema.dump(teacher)

    courses_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM courses LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id WHERE teacher_id="+str(teacher_id))
    course_engine = None
    with db.engine.connect() as conn:
        course_engine = conn.execute(courses_query)

    course_schema = CourseSchema(many=True)
    courses = course_schema.dump(course_engine)
    return jsonify({
        "teacher":teacher,
        "courses":courses
    })


def send_application():
    email = request.form.get('email')
    resume = request.files.get('resume')

    is_saved,filename = save_file(resume,'uploads')

    if is_saved:
        new_application = Applications(email=email,resume=filename)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({
            "is_added":True,
            "status":"Application Send Successful"
        })
    else:
        return jsonify({
            "is_added":False,
            "status":"Application Send Failed"
        })
