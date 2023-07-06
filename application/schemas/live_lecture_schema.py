from application import ma

class liveLectureSchema(ma.Schema):
    class Meta:
        fields = ('live_id','course_id','lecture_title','lecture_description','status','starting_title','ending_title')