from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
mail = Mail()
migrate = Migrate(db=db)
moment = Moment()