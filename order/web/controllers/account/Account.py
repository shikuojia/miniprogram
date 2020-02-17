from flask import Blueprint
from common.libs.user.helper import g_render_template
from application import app

route_account = Blueprint('account_page',__name__)

@route_account.route('/index')
def index():
    return g_render_template('account/index.html')

@route_account.route('/info')
def info():
    return g_render_template('account/info.html')


@route_account.route('/set')
def set():
    return g_render_template('account/set.html')