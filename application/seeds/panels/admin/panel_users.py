from flask import Blueprint,jsonify,request
from application import db
from application.models.panel_users import PanelUsers
from application.models.users import Users
from application.schemas.panel_user_schema import PanelUserSchema
from application.schemas.user_schema import UserSchema
from application.seeds.utils import save_file,remove_file
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import text
from application.schemas.course_schema import CourseSchema

def add_panel_user():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')

    is_admin = request.form.get('is_admin')
    is_teacher = request.form.get('is_teacher')
    check_email = PanelUsers.query.filter_by(email=email).first()
    if not check_email:
        if is_admin == 1:
            new_panel_user = PanelUsers(name=name,email=email,password=generate_password_hash(password),is_admin=is_admin,is_teacher=is_teacher)
            db.session.add(new_panel_user)
            db.session.commit()
            return jsonify({
                "status":"Admin Added successfully",
                "is_added": True
            })
        else:
            profile_picture = request.files.get('profile_picture')
            print(profile_picture)
            phone = request.form.get('phone')
            title =request.form.get('title')
            print(title)
            description = request.form.get('description')

            is_saved,file_name = save_file(profile_picture,'uploads')

            if is_saved:
                new_panel_user = PanelUsers(name=name,email=email,password=generate_password_hash(password),phone=phone,title=title,description=description,profile_picture=file_name,is_admin=is_admin,is_teacher=is_teacher)
                db.session.add(new_panel_user)
                db.session.commit()
                return jsonify({
                    "status":"Teacher Added successfully",
                    "is_added": True
                })
            else:
                return jsonify({
                    "status":"Could not save profile picture",
                    "is_added": False
                })
    else:
        return jsonify({
                     "status":"Email Already Exists.Please try another email",
                    "is_added": False
                    
                    })




def delet_panel_user():
    user_id = request.args.get('user_id')
    user = PanelUsers.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        "status":"Teacher Deleted successfully",
        "is_deleted": True
    })
   
def get_all_users():
    users_query = Users.query.all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(users_query)
    return jsonify({
        "data":users
    })

def get_all_teachers():
    teachers_query = PanelUsers.query.filter_by(is_teacher=1).all()
    schema = PanelUserSchema(many=True)
    teachers = schema.dump(teachers_query)
    return jsonify({
        "status":"Teachers Fetched successfully",
        "data":teachers
    })

def admin_get_teacher_courses():
    teacher_id = request.args.get('teacher_id')
    courses_query = text("SELECT * FROM courses LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id  WHERE teacher_id="+str(teacher_id))
    courses_engine = None

    with db.engine.connect() as conn:
        courses_engine = conn.execute(courses_query)

    courses_schema = CourseSchema(many=True)
    courses = courses_schema.dump(courses_engine)

    print(courses)
    return jsonify({
            "status":"Courses Fetched successfully",
            "data":courses
        })

def get_all_admins():
    admins_query = PanelUsers.query.filter_by(is_admin=1).all()
    schema = PanelUserSchema(many=True)
    admins = schema.dump(admins_query)
    return jsonify({
        "status":"Admins Fetched successfully",
        "data":admins
    })