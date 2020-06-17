from . import index_blu
from flask import flash
from flask import render_template
@index_blu.route("/index")
def index():
    flash("对不起，您尚未登录，请登录！")
    return "hello_word"