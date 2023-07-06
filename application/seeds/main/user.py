from flask import Blueprint,request,jsonify
from application.models.users import Users
from application.schemas.user_schema import UserSchema
from werkzeug.security import generate_password_hash,check_password_hash
from application import db
from application.seeds.utils import save_file
from application.models.users import Users


def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    
    

    hashed_password = generate_password_hash(password)

    user = Users.query.filter_by(email=email).first()
    if user:
        return jsonify({
            "status":"Email Already Exist",
            "is_registered": False
        })

    else:
      
        new_user = Users(name=name,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
                "status":"User Registered Successfully",
                "is_registered": True
        })
        

def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user_query = Users.query.filter_by(email=email).first()
    if user_query and check_password_hash(user_query.password,password):
        
        users_schema = UserSchema(many=False)
        user = users_schema.dump(user_query)
        
       
        return jsonify({
            "user":user,
            "is_loggedin":True,
            "status":"Logged in successfully"
        })
    else:
        return jsonify({
           "is_loggedin":False,
            "status":"Invalid Email or Password"
        })
    

def get_user_details():
    user_id = request.args.get('user_id')
    user_query = Users.query.get(user_id)
    users_schema = UserSchema(many=False)
    user = users_schema.dump(user_query)

    return jsonify({
        "data":user,
       
    })


def update_user_details():
    user_id = request.form.get('user_id')
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    phone_no = request.form.get('phone_no')
    stripe_id = request.form.get('stripe_id')

    user = Users.query.get(user_id)
    user.name = name
    user.email = email
    user.address = address
    user.phone_no = phone_no
    user.stripe_id = stripe_id
    db.session.commit()
    return jsonify({
        "status":"User Updated Successfully",
        "is_updated":True
    })


def change_password():
    user_id = request.form.get('user_id')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')

    user = Users.query.get(user_id)
    if check_password_hash(user.password,old_password):
        hashed_password = generate_password_hash(new_password)
        user.password = hashed_password
        db.session.commit()
        return jsonify({
            "status":"Password Changed Successfully",
            "is_updated":True
        })
    else:
        return jsonify({
            "status":"Invalid Old Password",
            "is_updated":False
        })