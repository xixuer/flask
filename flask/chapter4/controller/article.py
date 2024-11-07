from flask import Blueprint

article = Blueprint("article",__name__)

@article.route('/article/add')
def add_article():
    return "添加文章成功"

@article.route('/article/update')
def update_article():
    return "更新文章成功"
