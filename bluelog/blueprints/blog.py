from flask import Blueprint, request, current_app
from bluelog.extensions import db
from bluelog.models import Post, Category, Comment


blog_bp = Blueprint('blog', __name__)

class current_user:
    is_authenticated = False


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    par_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = 





@blog_bp.route('/about')
def about():
    return 'The about page'

@blog_bp.route('/category/<int:category_id>')
def category(category_id):
    return 'The category page'
