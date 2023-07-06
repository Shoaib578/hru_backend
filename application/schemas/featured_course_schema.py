from application import ma

class FeaturedCourseSchema(ma.Schema):
    class Meta:
        fields = ('featured_id','course_id','course_title','course_description','course_price','course_category','course_thumbnail','name','profile_picture','panel_userid')