from application import db
from flask import jsonify,request
from application.models.featured_courses import FeaturedCourses

from application.schemas.featured_course_schema import FeaturedCourseSchema
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import text,engine


def GetAllFeaturedCourses():
    courses_query = text("SELECT *,(SELECT count(*) from owned_courses WHERE course_id=courses.course_id) as students_count FROM featured_courses LEFT JOIN courses on courses.course_id=featured_courses.course_id LEFT JOIN panel_users on panel_users.panel_userid=courses.teacher_id")
    course_engine = None

    with db.engine.connect() as conn:
        course_engine= conn.execute(courses_query)
    
   
    schema = FeaturedCourseSchema(many=True)
    courses = schema.dump(course_engine)
    return jsonify({
        "data":courses
    })