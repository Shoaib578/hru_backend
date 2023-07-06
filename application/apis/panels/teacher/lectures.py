from application.seeds.panels.teacher import lectures
from flask import Blueprint
teacher_lecture_routes = Blueprint('teacher_lecture_routes',__name__,static_folder='static')



@teacher_lecture_routes.route('/get_teacher_courses',methods=['GET'])
def GetTeacherCourseLectures():
    return lectures.get_lectures()


@teacher_lecture_routes.route('/add_lecture',methods=['POST'])
def AddLecture():
    return lectures.add_lecture()


@teacher_lecture_routes.route('/delete_lecture',methods=['DELETE'])
def DeleteLecture():
    return lectures.delete_lecture()


    
@teacher_lecture_routes.route('/get_lectures')
def GetLectures():
    return lectures.get_lectures()