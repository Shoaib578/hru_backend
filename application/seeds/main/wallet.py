from application import db
from sqlalchemy import text
from flask import jsonify,request
from application.models.courses import Courses
from application.models.links import Links
from application.models.wallets import Wallets
from application.schemas.wallet_schema import WalletSchema
from application.models.users import Users
import stripe
stripe.api_key = "sk_test_51Li9vSLrpfnp4zWJmdpNm8vuzpLLpwbbVGzfytQbeVWeYDE9wXSH48h1Rsufx08gqTyqefTlYhSop6AZJh3vprXJ00xTEddr3r"

def add_money_to_wallet():
    code = request.form.get('code')
    course_id = request.form.get('course_id')
    link = Links.query.filter_by(code=code).first()
    course = Courses.query.get(course_id)
    course_price = course.course_price
    user_id = link.shared_by
    twenty_percent = course_price*0.2

    wallet = Wallets.query.filter_by(user_id=user_id).first()

    if wallet:
        wallet.amount = wallet.amount + twenty_percent
        db.session.commit()
    else:
        new_wallet = Wallets(user_id=user_id, amount=twenty_percent)
        db.session.add(new_wallet)
        db.session.commit()
    
    return jsonify({
        "is_added":True,
        "status":"Money Added Sucececely",
    })

def get_money_from_wallet():
    user_id = request.args.get("user_id")
    wallet = Wallets.query.filter_by(user_id=user_id).first()
    wallet_schema = WalletSchema(many=False)
    data= wallet_schema.dump(wallet)
    
    return jsonify({
        "data":data
    })




def create_transfer():
    user_id = request.form.get('user_id')
    user = Users.query.get(user_id)
    wallet = Wallets.query.filter_by(user_id=user_id).first()
    stripe_id = user.stripe_id
    status = ""
    is_tranfered=False
    
    try:

        
        stripe.Transfer.create(
        amount=2000,
        currency="usd",
        destination=stripe_id,
        
        
        )
       

        wallet.amount =0
        db.session.commit()
        status = "Successfully Tranfered"
        is_tranfered = True
    except stripe.error.CardError as e:
        status = e.user_message
        is_tranfered = False
       
    except stripe.error.RateLimitError as e:
         status = e.user_message
         is_tranfered = False
   
    except stripe.error.InvalidRequestError as e:
        status = e.user_message
        is_tranfered = False
   
    except stripe.error.AuthenticationError as e:
        status = e.user_message
        is_tranfered = False
        
    except stripe.error.APIConnectionError as e:
        status = e.user_message
        is_tranfered = False
        
    except stripe.error.StripeError as e:
        status = e.user_message
        is_tranfered = False
   
    except Exception as e:
        status = e
        is_tranfered = False
   
  
    return jsonify({
        "is_tranfered":is_tranfered,
        "status":status
       
    })
