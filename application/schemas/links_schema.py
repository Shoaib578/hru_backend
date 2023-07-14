from application import ma

class LinkSchema(ma.Schema):
    class Meta:
        fields = ('shared_link_id','link','shared_by','course_id','code','course_title','course_description','course_price','teacher_id','course_thumbnail','course_category','created_at','updated_at','profile_picture','name','panel_userid','title','students_count','is_owned')