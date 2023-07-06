from application import ma


class PanelUserSchema(ma.Schema):
    class Meta:
        fields = ('panel_userid','email','phone','password','profile_picture','title','name','title','description','is_admin','is_teacher','created_at')