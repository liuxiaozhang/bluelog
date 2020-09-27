from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
mail = Mail()
