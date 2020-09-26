from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
