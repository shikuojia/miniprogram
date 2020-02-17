from flask import Blueprint
from common.libs.user.helper import g_render_template
from application import app

route_food = Blueprint('route_food',__name__)

@route_food.route('/index')
def index():
    return g_render_template('food/index.html')


@route_food.route('/cat_set')
def catset():
    return g_render_template('food/cat_set.html')


@route_food.route('/cat')
def cat():
    return g_render_template('food/cat.html')

@route_food.route('/info')
def info():
    return g_render_template('food/info.html')


@route_food.route('/set')
def set():
    return g_render_template('food/set.html')