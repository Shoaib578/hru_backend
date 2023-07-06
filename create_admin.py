from application import db,app
from application.models.panel_users import PanelUsers

from werkzeug.security import generate_password_hash,check_password_hash

def create_admin():
    admin = PanelUsers.query.filter_by(is_admin=1).first()
    if admin:
        print("Admin Already Exist")
    else:
        new_admin = PanelUsers(name="Admin(By Default)",email='theadmin@gmail.com',password=generate_password_hash("Games"),is_admin=1,is_teacher=0)
        db.session.add(new_admin)
        db.session.commit()
        print("Admin created successfully")

app.app_context().push()
create_admin()