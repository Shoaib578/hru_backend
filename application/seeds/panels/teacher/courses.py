from application import db
from application.models.courses import Courses
from flask import Blueprint,jsonify,request
from application.models.courses import Courses
from application.schemas.course_schema import CourseSchema
from application.seeds.utils import save_file,remove_file


def get_teacher_courses():
    teacher_id=request.args.get('teacher_id')
    courses_query = Courses.query.filter_by(teacher_id=teacher_id).all()
    schema = CourseSchema(many=True)
    courses = schema.dump(courses_query)
    return jsonify({
        "data":courses
    })

def add_course():
    course_title = request.form.get('course_title')
    course_description = request.form.get('course_description')
    teacher_id = request.form.get('teacher_id')
    course_thumbnail = request.files.get('course_thumbnail')
    course_price = request.form.get('course_price')
    course_category = request.form.get('course_category')
    is_saved,file_name = save_file(course_thumbnail,'uploads')
    if is_saved:
        new_course = Courses(course_title=course_title,course_description=course_description,teacher_id=teacher_id,course_thumbnail=file_name,course_price=course_price,course_category=course_category)
        db.session.add(new_course)
        db.session.commit()
        return jsonify({
            "is_added": True,
            "status":"Added successfully"
        })
    else:
        return jsonify({
            "is_added": False,
            "status":"Could not save thumbnail"
        })



def delete_course():
    course_id = request.args.get('course_id')
    course = Courses.query.get(course_id)
    is_removed = remove_file(course.course_thumbnail,'uploads')
    if not is_removed:
        pass

    db.session.delete(course)
    db.session.commit()
    return jsonify({
            "is_deleted": True,
            "status":"Deleted successfully"
    })



def update_course():
    course_id = request.form.get('course_id')
    course = Courses.query.filter_by(course_id=course_id).first()
    course_title = request.form.get('course_title')
    
    
    course_description = request.form.get('course_description')
    course_thumbnail = request.files.get('course_thumbnail')
    course_price = request.form.get('course_price')
    course_category = request.form.get('course_category')

    if course_thumbnail:
        is_saved,file_name = save_file(course_thumbnail,'uploads')
        if is_saved:
            is_removed = remove_file(course.course_thumbnail,'uploads')
            if is_removed:
                course.course_title = course_title
                course.course_description = course_description
                course.course_thumbnail = file_name
                course.course_price = course_price
                course.course_category = course_category
                db.session.commit()
                return jsonify({
                    "is_updated": True,
                    "status":"Updated successfully"
                })
            else:
                return jsonify({
                    "is_updated": False,
                    "status":"Could not remove thumbnail"
                })
        else:
            return jsonify({
                "is_updated": False,
                "status":"Could not save thumbnail"
            })
    else:
        course.course_title = course_title
        course.course_description = course_description
        course.course_price = course_price
        course.course_category = course_category
        db.session.commit()
        return jsonify({
            "is_updated": True,
            "status":"Updated successfully"
        })
   




def view_course():
    course_id = request.args.get('course_id')
    course = Courses.query.get(course_id)
    schema = CourseSchema(many=False)
    course = schema.dump(course)
    return jsonify({
        "data":course
    })