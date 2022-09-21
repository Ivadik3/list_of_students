from operator import is_
import re
from app import app
from flask import render_template,request,redirect,flash,url_for,session,g
from Data_Manager import Data_Manager
from users_model import User

#данный класс используется для задания всех возможных страниц сайта
#и методы их формирования
D_manager=Data_Manager()

@app.before_request
def before_request():
    g.student=None
    if "user_id" in session:
        user = D_manager.get_student(session["user_id"])
        g.student = user


@app.route("/main")
def main_page():
    list_of_posts = sorted(D_manager.get_all_posts(),key = lambda dict1: dict1["BreastSize"],reverse=True)       
    return render_template("student_list.html",posts = list_of_posts)

@app.route("/main/students/<int:student_id>")
def student_page(student_id):
    persona_dict = D_manager.get_student(student_id)
    print(persona_dict)
    return render_template("personal_page.html",persona = persona_dict)

@app.route("/main/login",methods=("GET","POST"))
def login_page():
    if request.method =="POST":
        session.pop("user_id",None)
        name = request.form["user_name"]
        password = request.form["user_password"]
        student_obj = D_manager.get_student(id=None,name = name)
        if student_obj:
            if student_obj["Password"] == password:
                session["user_id"] = student_obj["ID"]
                return redirect(url_for("main_page"))
        else:
            return redirect(url_for("login_page"))
    return render_template("login.html")

@app.route("/main/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("login_page"))

@app.route("/main/sign_up",methods=("GET","POST"))
def signup_page():
    name=""
    gender=""
    name_error=""
    #print("this is request method",request.method)
    if request.method == "POST":
        session.pop("user_id",None)
        name = request.form["user_name"]
        password = request.form["user_password"]
        gender = request.form["user_gender"]
        print(name)
        #print("parameters:",name,gender)
        is_exist = D_manager.user_exists(name)
        print(is_exist)
        if name and gender and not is_exist: 
            session["user_id"] = D_manager.set_student(User(name,gender,password))
            flash(f"Thanks for registration {name}")
            return redirect(url_for("main_page"))
        elif is_exist:
            name_error = "name already exists!"     #переделать под почту/уникальный логин
            #return redirect(url_for("sign_up.html",name_error=name_error))
            return render_template("sign_up.html")        
        else:
            #return redirect(url_for("sign_up.html",name_error=name_error))
            return render_template("sign_up.html") 

    else:
        #если реквест метод GET, просто возвращаем страницу
        return render_template("sign_up.html",name_error=name_error)
        