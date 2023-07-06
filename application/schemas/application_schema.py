from application import ma

class ApplicationSchema(ma.Schema):
    class Meta:
        fields = ('application_id','resume','email')