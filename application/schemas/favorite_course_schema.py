from application import ma

class FavoriteCourseSchema(ma.Schema):
    class Meta:
        fields = ("favorite_id","course_id","user_id")