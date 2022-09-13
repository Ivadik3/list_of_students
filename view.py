from app import app
from flask import render_template
from Data_Manager import Data_Manager

#данный класс используется для задания всех возможных страниц сайта
#и методы их формирования
D_manager=Data_Manager()

@app.route("/main")
def main_page():

    list_of_posts = sorted(D_manager.get_all_posts(),key = lambda dict1: dict1["BreastSize"],reverse=True)
        
    return render_template("student_list.html",posts = list_of_posts)

@app.route("/main/students/<int:student_id>")
def student_page(student_id):
    persona_dict = D_manager.get_student(student_id)
    print(persona_dict)
    
    return render_template("personal_page.html",persona = persona_dict)
