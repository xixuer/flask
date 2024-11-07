from flask import Blueprint, render_template, session

index = Blueprint("index",__name__)

@index.route('/index')
def my_index():
    # session参数的传递
    session["username"] = "xixuer"

    article = {
        "title": "论Python语言的学习难度",
        "count": 2000
    }

    return render_template("index.html",article=article)
