from application import ma

class LectureSchema(ma.Schema):
    class Meta:
        fields = ('lecture_id','lecture_number','lecture_title','lecture_duration','lecture_description','course_id','lecture_video','lecture_type','created_at','panel_userid')