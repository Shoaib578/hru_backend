from application import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id','name','email','password','created_at','updated_at','phone_no','stripe_id','address')