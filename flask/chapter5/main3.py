from flask import Flask, session, request
import os
from controller.user import user
from controller.article import article

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.register_blueprint(user)
app.register_blueprint(article)
        
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return "页面不存在"

@app.errorhandler(500)
def server_error(e):
    print(e)
    return "服务器内部错误"

if __name__ == "__main__":
    app.run()
