from app import app
from flask import render_template,request,redirect,flash,url_for,session,g
from Data_Manager import Data_Manager
from users_model import User
from my_forms import LoginForm, SignUpForm, AboutMeForm,LoadPictureForm
from werkzeug.utils import secure_filename
from uuid import uuid1
import os
from my_forms import photos
from flask_uploads import configure_uploads

#класс взаимодействующий с бд
D_manager=Data_Manager()

#конфигурируем куда UploadSet будет выгружать фото
configure_uploads(app,photos)

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
    persona_obj = D_manager.get_student(student_id)
    print(persona_obj.ID,"THIS IS PERS OBJ")
    return render_template("personal_page.html",persona = persona_obj)

@app.route("/main/students/<int:student_id>/redact_page",methods=("GET","POST"))
def redact_student_page(student_id):

    if not g.student or g.student.ID!=session["user_id"]:
        return redirect(url_for("main_page"))
    ab_me_form = AboutMeForm()
    load_pic_form = LoadPictureForm()
    student_obj = D_manager.get_student(id = session["user_id"], name=None)
    if ab_me_form.validate_on_submit():
        for el in [ab_me_form.about_me,ab_me_form.activities]:
            if el.data:
                student_obj.set_attributes({el.label.text: el.data})  
        D_manager.update_student(student_obj)
    
    if load_pic_form.validate_on_submit():
        print("validation made")
        #добавляем картинку, если пользователь прислал таковую
        pic = load_pic_form.profile_pic.data 
        if pic:
            file_name = photos.save(pic,name=f"{uuid1()}.jpg")
            if student_obj.Image:
                try:
                    os.remove(os.path.join(app.config["UPLOADED_PHOTOS_DEST"],student_obj.Image))
                except FileNotFoundError:
                    print("no such file")
            student_obj.Image=file_name
            D_manager.update_student(student_obj)
            return redirect(url_for("redact_student_page",student_id=student_id))
        else:
            if student_obj.Image:
                try:
                    os.remove(os.path.join(app.config["UPLOADED_PHOTOS_DEST"],student_obj.Image))
                except FileNotFoundError:
                    print("no such file")
            student_obj.Image = ""
            D_manager.update_student(student_obj)
            return redirect(url_for("redact_student_page",student_id=student_id))
        
    return render_template("redact_info.html",my_form = ab_me_form,my_pic_form =load_pic_form)


"""
    log-in/out  sign-in/out methods below
"""

@app.route("/main/login",methods=("GET","POST"))
def login_page():
    log_form = LoginForm()
    if log_form.validate_on_submit():
        session.pop("user_id",None)
        name = log_form.user.data
        password = log_form.passwd.data
        student_obj = D_manager.get_student(id=None,name = name)
        if student_obj:
            if student_obj.Password == password:
                session["user_id"] = student_obj.ID
                return redirect(url_for("main_page"))
        else:
            return redirect(url_for("login_page"))
    return render_template("login.html",my_form = log_form)


@app.route("/main/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("login_page"))

@app.route("/main/sign_up",methods=("GET","POST"))
def signup_page():
    name=""
    gender=""
    name_error=""
    s_up_form = SignUpForm()
    if s_up_form.validate_on_submit():
        session.pop("user_id",None)
        name = s_up_form.user.data
        password = s_up_form.passwd.data
        gender = s_up_form.select_gender.data
        is_exist = D_manager.user_exists(name)
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
        return render_template("sign_up.html",name_error=name_error,s_up_form=s_up_form)
        
