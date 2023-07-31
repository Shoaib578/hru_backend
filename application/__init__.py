from flask import Flask,jsonify,request
from config import DATABASE_URI,SECRET_KEY
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import stripe

app = Flask(__name__)


app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
stripe.api_key = "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"
ma= Marshmallow(app)
db = SQLAlchemy(app)
Migrate(app,db)
CORS(app)





@app.route('/create-payment-intent',methods=['POST'])
def create_payment_intent():
    price = request.form.get('amount')
    print(price)
    intent = stripe.PaymentIntent.create(
        amount=price,
        currency='usd',
        automatic_payment_methods={"enabled": True},

       
    )

    

    return jsonify({
        "client_secret":intent.client_secret
    })




from application.apis.main.user import user_routes
app.register_blueprint(user_routes,url_prefix='/apis/main/user')


from application.apis.main.featured_courses import main_featured_courses_routes
app.register_blueprint(main_featured_courses_routes,url_prefix='/apis/main/featured_courses')




from application.apis.main.courses import main_courses_routes
app.register_blueprint(main_courses_routes,url_prefix='/apis/main/courses')

from application.apis.main.teachers import main_teacher_routes
app.register_blueprint(main_teacher_routes,url_prefix='/apis/main/teachers')

from application.apis.main.coupons import main_coupon_routes
app.register_blueprint(main_coupon_routes,url_prefix='/apis/main/coupons')




from application.apis.main.wallet import wallet_routes
app.register_blueprint(wallet_routes,url_prefix='/apis/main/wallet')








from application.apis.panels.auth import panel_auth
app.register_blueprint(panel_auth,url_prefix='/apis')


from application.apis.panels.admin.panel_users import admin_panel_user
app.register_blueprint(admin_panel_user,url_prefix='/apis/admin')


from application.apis.panels.admin.pending_withdrawals import admin_pending_withdrawals_routes
app.register_blueprint(admin_pending_withdrawals_routes,url_prefix='/apis/admin')



from application.apis.panels.admin.account import admin_account_routes
app.register_blueprint(admin_account_routes,url_prefix='/apis/admin')


from application.apis.panels.admin.featured_courses import admin_featured_course_routes
app.register_blueprint(admin_featured_course_routes,url_prefix='/apis/admin/featured_courses')

from application.apis.panels.admin.applications import admin_teaching_application_routes
app.register_blueprint(admin_teaching_application_routes,url_prefix='/apis/admin/teaching_applications')

from application.apis.panels.admin.coupons import admin_coupon_routes
app.register_blueprint(admin_coupon_routes,url_prefix='/apis/admin/coupons')


from application.apis.panels.teacher.course import teacher_courses_routes
app.register_blueprint(teacher_courses_routes,url_prefix='/apis/teacher/courses')


from application.apis.panels.teacher.lectures import teacher_lecture_routes
app.register_blueprint(teacher_lecture_routes,url_prefix='/apis/teacher/lectures')


from application.apis.panels.teacher.account import teacher_account_routes
app.register_blueprint(teacher_account_routes,url_prefix='/apis/teacher/account')



