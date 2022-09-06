from app import app
from flask import render_template
from Data_Manager import Data_Manager

#данный класс используется для задания всех возможных страниц сайта
#и методы их формирования

@app.route("/main")
def main_page():
    D_manager=Data_Manager()
    list_of_posts = D_manager.get_all_posts()
    return render_template("students.html",posts = list_of_posts)

