from application import ma

class SharedLinksSchema(ma.Schema):
    class Meta:
        fields = ('shared_link_id','link','course_id','shared_by')