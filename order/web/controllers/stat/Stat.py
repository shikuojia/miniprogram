from flask import Blueprint
from common.libs.user.helper import g_render_template
from application import app

route_stat = Blueprint('stat_page',__name__)

@route_stat.route('/index')
def index():
    return g_render_template('stat/index.html')

@route_stat.route('/food')
def food():
    return g_render_template('stat/food.html')

@route_stat.route('/member')
def member():
    return g_render_template('stat/member.html')


@route_stat.route('/share')
def share():
    return g_render_template('stat/share.html')