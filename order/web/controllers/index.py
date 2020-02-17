from flask import Blueprint,g
from common.libs.user.helper import g_render_template

route_index = Blueprint('index_page',__name__)

@route_index.route('/')
def index():
    
    return g_render_template('index/index.html')

