from flask import Flask, make_response, request, session
import datetime
import os

app = Flask(__name__)
# 启用session
app.config['SECRET_KEY'] = os.urandom(24) # 生成一个随机密钥

now = datetime.datetime.now()


@app.route('/')
def hello_world():
    return "flask我又来了"

@app.route('/cookie')
def cookie():

    expires_time = now + datetime.timedelta(days=1)

    # 设置cookie
    response = make_response("设置cookie成功")
    response.set_cookie("username", "admin",expires=expires_time)
    response.set_cookie("sex", "男",expires=expires_time)

    return response

@app.route('/get_cookie')
def get_cookie():
    # 获取一个cookie
    name = request.cookies.get("username")
    print(name)

    # 获取所有cookie
    cookies = request.cookies
    cookie_dict = request.cookies.to_dict()
    print(cookies)
    print(cookie_dict)
    for k,v in cookie_dict.items():
        print(f"{k}:{v}")
    return "获取cookie成功"

@app.route('/del_cookie')
def delete_cookie():
    # 删除一个cookie
    response = make_response("删除cookie成功")
    response.delete_cookie("username")

    # 删除所有cookie   
    cookies_dict = request.cookies.to_dict()
    print(cookies_dict) 
    for k,v in cookies_dict.items():
        print(f"{k}:{v}")
        response.delete_cookie(k)
    
    return response

# 操作session

# 启用session
@app.route('/add_session')
def add_session():
    session['username'] = 'xixuer'
    session['nickname'] = 'xzh'
    session['role'] = 'admin'

    return "设置session成功"

# 获取sessionq
@app.route('/get_session')
def get_session():
    print(session)
    username = session.get('username')
    return f"获取session成功，username:{username}"

# 删除session
@app.route('/del_session')
def del_session():
    session.clear()
    return "删除session成功"

if __name__ == "__main__":
    app.run()
