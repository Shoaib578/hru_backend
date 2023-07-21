from application import db
from application.models.courses import Courses
from application.schemas.course_schema import CourseSchema
from application.models.lectures import Lectures
from application.schemas.lecture_schema import LectureSchema
from application.models.owned_courses import OwnedCourses
from application.schemas.owned_courses_schema import OwnedCourseSchema
from application.models.links import Links
from application.schemas.links_schema import LinkSchema
from sqlalchemy import text
from flask import jsonify,request

def GetAllCourses():
    courses_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM courses LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id")
    course_engine = None
    with db.engine.connect() as conn:
        course_engine = conn.execute(courses_query)
    schema = CourseSchema(many=True)
    courses = schema.dump(course_engine)
    return jsonify({
        "data":courses
    })

def view_course():
    course_id = request.args.get('course_id')
    is_loggedin = request.args.get('is_loggedin')
    course_query = None
    if is_loggedin:
        user_id = request.args.get('user_id')
        course_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count,(SELECT count(*) FROM owned_courses WHERE course_id="+str(course_id)+" AND owned_courses.owned_by="+str(user_id)+") as is_owned FROM courses LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id WHERE course_id ="+str(course_id))
    else:
        course_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM courses LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id WHERE course_id ="+str(course_id))

    course_engine = None
    with db.engine.connect() as conn:
        course_engine = conn.execute(course_query)
        
    schema = CourseSchema(many=True)
    course = schema.dump(course_engine)




    lectures_query = Lectures.query.filter_by(course_id=course_id).all()
    lecture_schema = LectureSchema(many=True)
    lectures = lecture_schema.dump(lectures_query)


    return jsonify({
        "course":course,
        "lectures":lectures
    })



def GetOwnedCourses():
    user_id = request.args.get('user_id')
    course_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM owned_courses LEFT JOIN courses on courses.course_id=owned_courses.course_id LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id WHERE owned_courses.owned_by="+str(user_id))
    course_engine = None
    with db.engine.connect() as conn:
        course_engine = conn.execute(course_query)
    schema = OwnedCourseSchema(many=True)
    courses = schema.dump(course_engine)
    return jsonify({
        "data":courses
    })


def buy_course():
    course_id = request.form.get('course_id')
    user_id = request.form.get('user_id')
    filter_owned_courses = OwnedCourses.query.filter_by(course_id=course_id, owned_by=user_id).first() 
    if filter_owned_courses:
        pass
    else:
        new_own_course = OwnedCourses(owned_by=user_id,course_id=course_id)
        db.session.add(new_own_course)
        db.session.commit()

    return jsonify({
            "is_owned": True,
            "status":"Bought Successfully",
            "course_id": course_id,
        })



def add_link():
    link = request.form.get("link")
    user_id = request.form.get("user_id")
    course_id = request.form.get("course_id")
    code = request.form.get("code")
    new_link = Links(link=link,shared_by=user_id,course_id=course_id,code=code)
    db.session.add(new_link)
    db.session.commit()
    return jsonify({
        "status":"Link Added",
        "is_added": True
    })

def delete_link():
    link_id = request.args.get("link_id")
    link = Links.query.get(link_id)
    db.session.delete(link)
    db.session.commit()
    return jsonify({
        "status":"Link Deleted",
        "is_deleted": True
    })


def get_all_links():
    user_id = request.args.get('user_id')
    links_query = Links.query.filter_by(shared_by=user_id).all()
    schema = LinkSchema(many=True)
    links = schema.dump(links_query)
    print(links)
    return jsonify({
        "data":links
    })




def get_course_by_link_code():
    code = request.args.get('code')
    is_loggedin = request.args.get('is_loggedin')
    query = None
    
    if is_loggedin:
        user_id = request.args.get('user_id')

        query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count,(SELECT count(*) FROM owned_courses WHERE course_id=courses.course_id AND owned_courses.owned_by="+str(user_id)+") as is_owned FROM links LEFT JOIN courses on courses.course_id=links.course_id  LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id WHERE links.code="+str(code))
    else:
        query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM links LEFT JOIN courses on courses.course_id=links.course_id  LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id  WHERE links.code="+str(code))
        
    engine = None
    with db.engine.connect() as conn:

        engine = conn.execute(query)
    schema = LinkSchema(many=True)
    data= schema.dump(engine)
   
    lectures = []
    if data:
        lectures_query = Lectures.query.filter_by(course_id=data[0]['course_id']).all()
        lecture_schema = LectureSchema(many=True)
        lectures = lecture_schema.dump(lectures_query)
    
    return jsonify({
        "course":data,
        "lectures":lectures
    })


