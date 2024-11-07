from flask import Flask, session, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/login')
def login():
    session["if_login"] = True
    return "登录成功"

@app.route('/update_user')
def update_user():
    return "更新用户成功"

@app.before_request
def before_request():
    # 获取用户的url，然后根据URL进行判断，哪些拦截，哪些不拦截
    url = request.path
    print(url)
    if url == "/login":
        pass
    else:
        if_login = session.get("if_login")
        if if_login != True:
            return "请先登录"
        
        
if __name__ == "__main__":
    app.run()
