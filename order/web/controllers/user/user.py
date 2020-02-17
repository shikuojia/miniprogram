from flask import Blueprint,request,jsonify,make_response,redirect,g
from common.modules.User import User
from common.libs.user.UserService import UserService
from common.libs.user.helper import g_render_template
import json
from application import app,db
from common.libs.UrlManager import UrlManager

route_user = Blueprint('user_page',__name__)

@route_user.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':

        return g_render_template('user/login.html')
    
    resp = {'code':200,'msg':'登录成功','data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入用户名！'
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入密码！'
        return jsonify(resp)

    user_info = User.query.filter_by(login_name = login_name).first()
    
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码！'
        return jsonify(resp)
    
    if user_info.login_pwd != UserService.genPwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码！'
        return jsonify(resp)
    
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],'{}#{}'.format(UserService.genAuthCode(user_info),user_info.uid))

    return response

@route_user.route('/edit',methods=['GET','POST'])
def edit():
    if request.method == 'GET':
        return g_render_template('user/edit.html',{'current':'edit'})
    
    resp = {'code':200,'msg':'操作成功！','data':{}}
    req  = request.values
    nickname = req['nickname'] if 'nickname' in req else None
    email = req['email'] if 'email' in req else None

    if nickname is None or len(nickname) < 1:
        resp['code'] =-1
        resp['msg'] ='请输入正确的用户名！'
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] =-1
        resp['msg'] ='请输入正确的邮箱地址！'
        return jsonify(resp)
    
    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add(user_info)
    db.session.commit()

    return jsonify(resp)




@route_user.route('/reset-pwd',methods=['GET','POST'])
def resetPwd():
    if request.method == 'GET':
        return g_render_template('user/reset_pwd.html',{'current':'reset-pwd'})
    resp = {'code':200,'msg':'操作成功！','data':{}}
    req = request.values

    old_password = req['old_password'] if 'old_password' in req else None
    new_password = req['new_password'] if 'new_password' in req else None

    if old_password is None :
        resp['code'] = -1
        resp['msg'] ='请输入正确的原始密码！'
        return jsonify(resp)

    if new_password is None or len(new_password)<6:
        resp['code'] = -1
        resp['msg'] = '请输入6位以上的新密码'
        return jsonify(resp)

    if new_password == old_password:
        resp['code'] = -1
        resp['msg'] = '新设置的密码，不能与原密码相同，请更换！'
        return jsonify(resp)

    user_info = g.current_user
    user_info.login_pwd = UserService.genPwd(new_password,user_info.login_salt)
    db.session.add(user_info)
    db.session.commit()
    #修改密码后不用重新登录
    # response = make_response(json.dumps(resp))
    # response.set_cookie(app.config['AUTH_COOKIE_NAME'],'{}#{}'.format(UserService.genAuthCode(user_info),user_info.uid))

    # return response
    return resp
    
    


@route_user.route('/logout')
def logout():
    response = make_response(redirect(UrlManager.buildUrl('/user/login')))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response