from application import db
from flask import jsonify,request
from application.models.featured_courses import FeaturedCourses
from application.models.courses import Courses
from application.schemas.course_schema import CourseSchema
from application.schemas.featured_course_schema import FeaturedCourseSchema
from werkzeug.security import generate_password_hash,check_password_hash


def GetAllFeaturedCourses():
    courses_query = FeaturedCourses.query.all()
    schema = FeaturedCourseSchema(many=True)
    courses = schema.dump(courses_query)
    return jsonify({
        "data":courses
    })


def GetAllCoursesForDropdown():
    courses_query = Courses.query.all()
    schema = CourseSchema(many=True)
    courses = schema.dump(courses_query)
    return jsonify({
        "data":courses
    })

def DeleteFeaturedCourse():
    featured_id = request.args.get('featured_id')
    print(id)
    featured_course = FeaturedCourses.query.filter_by(featured_id=featured_id).first()
    db.session.delete(featured_course)
    db.session.commit()
    return jsonify({
        "status":"Featured Course Deleted Successfully",
        "is_deleted": True
    })


def AddFeaturedCourse():
    course_id = request.form.get('course_id')
    new_featured_course = FeaturedCourses(course_id=course_id)
    db.session.add(new_featured_course)
    db.session.commit()
    return jsonify({
            "status":"Featured Course Added Successfully",
            "is_added":True
        })
    
