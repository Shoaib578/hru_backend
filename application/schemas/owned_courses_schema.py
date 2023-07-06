from application import ma


class OwnedCourseSchema(ma.Schema):
    class Meta:
        fields = ('owned_id','owned_by','course_id','course_title','course_description','course_price','teacher_id','course_thumbnail','course_category','profile_picture','name','panel_userid','title','students_count')