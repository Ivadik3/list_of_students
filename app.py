from flask import Flask
import os
#from view import main_page, student_page


#данный класс используется для задания всех возможных страниц сайта
#и методы их формирования
#основной класс приложения, где создаем объект фласки

app = Flask(__name__)
app.config['SECRET_KEY']="sdfpor23po1rplwekqqewtupeseurst"
app.config["UPLOADED_PHOTOS_DEST"] = "static/uploaded_images"

