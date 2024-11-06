from flask import Flask, make_response, request, session
import datetime
import os
from controller.user import user
from controller.article import article

app = Flask(__name__)
# 启用session
app.config['SECRET_KEY'] = os.urandom(24) # 生成一个随机密钥

app.register_blueprint(user)
app.register_blueprint(article)

if __name__ == "__main__":
    app.run()
