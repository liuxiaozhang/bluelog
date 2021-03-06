from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager
from flask_wtf import CSRFProtect

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
mail = Mail()
migrate = Migrate(db=db)
moment = Moment()
login_manager = LoginManager()
csrf = CSRFProtect()

@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'