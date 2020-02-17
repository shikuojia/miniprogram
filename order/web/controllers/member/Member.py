from flask import Blueprint
from common.libs.user.helper import g_render_template
from application import app

route_member = Blueprint('member_page',__name__)

@route_member.route('/index')
def index():
    return g_render_template('member/index.html')



@route_member.route('/comment')
def comment():
    return g_render_template('member/comment.html')



@route_member.route('/info')
def info():
    return g_render_template('member/info.html')



@route_member.route('/set')
def set():
    return g_render_template('member/set.html')
    