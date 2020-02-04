from flask import Blueprint,render_template
from application import app

route_account = Blueprint('account_page',__name__)

@route_account.route('/index')
def index():
    return render_template('account/index.html')

@route_account.route('/info')
def info():
    return render_template('account/info.html')


@route_account.route('/set')
def set():
    return render_template('account/set.html')