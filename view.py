from operator import is_
from app import app
from flask import render_template,request,redirect,flash,url_for
from Data_Manager import Data_Manager
from users_model import User

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
    #print(persona_dict)
    
    return render_template("personal_page.html",persona = persona_dict)

@app.route("/main/login",methods=("GET","POST"))
def login_page():
    name=""
    gender=""
    name_error=""
    #print("this is request method",request.method)
    if request.method == "POST":
        name = request.form["user_name"]
        gender = request.form["user_gender"]
        print(name)
        #print("parameters:",name,gender)
        is_exist = D_manager.user_exists(name)
        print(is_exist)
        if name and gender and not is_exist:
            D_manager.set_student(User(name,gender))
            flash(f"Thanks for registration {name}")
            return redirect(url_for("main_page"))
        elif is_exist:
            name_error = "name already exists!"     #переделать под почту/уникальный логин
            #return redirect(url_for("sign_up.html",name_error=name_error))
            return render_template("sign_up.html",name_error= name_error)        
        else:
            name_error = "name field is empty!"
            #return redirect(url_for("sign_up.html",name_error=name_error))
            
            return render_template("sign_up.html",name_error= name_error) 

    else:
        #если реквест метод GET, просто возвращаем страницу
        return render_template("sign_up.html",name_error=name_error)
        