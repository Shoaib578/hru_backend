from application import ma

class CummunityPostSchema(ma.Schema):
    class Meta:
        fields = ('community_post_id','title','description','media','posted_by')