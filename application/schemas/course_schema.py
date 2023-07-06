from application import ma

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('course_id','course_title','course_description','course_price','teacher_id','course_thumbnail','course_category','created_at','updated_at','profile_picture','name','panel_userid','title','students_count','is_owned')