from flask import Blueprint, session, request

user = Blueprint("user", __name__)

@user.before_request
def before_request():
    if request.path.startswith("/v"):
        pass
    else:
        if_login = session.get("if_login")
        if if_login != True:
            return "请先登录"

@user.route('/user/add')
def add_user():
    return "添加用户成功"

@user.route('/user/update')
def update_user():
    return "更新用户成功"

@user.route('/v/user/info')
def user_info():
    return "获取用户信息成功"
