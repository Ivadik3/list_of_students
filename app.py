import imp
from flask import Flask,render_template
from Data_Manager import Data_Manager

#данный класс используется для задания всех возможных страниц сайта
#и методы их формирования
#основной класс приложения, где создаем объект фласки


app = Flask(__name__)


@app.route("/main")
def main_page():
    list_of_posts=[]
    with open("static\data\students.json","a") as file:
        D_manager=Data_Manager()
        list_of_posts = D_manager.get_all_posts()
        
    return render_template("students.html",list_of_posts)




if __name__ == "__main__":
    app.run(debug=True)
