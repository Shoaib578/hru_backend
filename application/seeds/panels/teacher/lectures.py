from application import db
from application.models.courses import Courses
from flask import Blueprint,jsonify,request
from application.models.lectures import Lectures
from application.schemas.lecture_schema import LectureSchema
from application.seeds.utils import save_file,remove_file


def get_lectures():
    course_id = request.args.get('course_id')
    lectures = Lectures.query.filter_by(course_id=course_id).all()

    lecture_schema = LectureSchema(many=True)
    data = lecture_schema.dump(lectures)
    return jsonify({
        "data": data
    })


def add_lecture():
    course_id = request.form.get('course_id')
    lecture_title = request.form.get('lecture_title')
    lecture_description = request.form.get('lecture_description')
    lecture_video = request.files.get('lecture_video')
    lecture_duration = request.form.get('lecture_duration')
    lecture_type = request.form.get('lecture_type')
    lecture_number = request.form.get('lecture_number')
    print(lecture_video)
    is_saved,filename = save_file(lecture_video,'uploads')
    if is_saved:
        new_lecture = Lectures(course_id=course_id,lecture_title=lecture_title,lecture_description=lecture_description,lecture_number=lecture_number,lecture_duration=lecture_duration,lecture_video=filename,lecture_type=lecture_type)
        db.session.add(new_lecture)
        db.session.commit()

        return jsonify({
                "status": "Lecture added successfully",
                "is_added": True,
            })
    else:
        return jsonify({
            "status": "could not save video",
            "is_added": False,
        })

    
def delete_lecture():
    lecture_id = request.args.get('lecture_id')

    lecture = Lectures.query.filter_by(lecture_id=lecture_id).first()
    
    is_removed = remove_file(lecture.lecture_video,'uploads')
    if not is_removed:
        pass
    db.session.delete(lecture)
    db.session.commit()
    return jsonify({
        "is_deleted":True,
        "status":"Lecture deleted successfully"
    })



