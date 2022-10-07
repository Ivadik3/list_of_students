from tkinter.tix import Select
from flask_wtf import FlaskForm  
from wtforms import StringField,SubmitField,BooleanField, PasswordField, SelectField,TextAreaField
from wtforms.validators import DataRequired,Email,Length,ValidationError
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_uploads import UploadSet, IMAGES


photos = UploadSet("photos",IMAGES)

#формы на страничке логина и регистрации
class LoginForm(FlaskForm):
	user = StringField("Имя пользователя", validators=[DataRequired(),Length(min=4,max=100)])
	passwd = PasswordField("Введите пароль", validators=[DataRequired(),Length(min=4,max=100)]) 
	submit_btn = SubmitField("Войти")

class SignUpForm(FlaskForm):
	user = StringField("Задайте имя пользователя", validators=[DataRequired(),Length(min=4,max=100)])
	passwd = PasswordField("Задайте пароль", validators=[DataRequired(),Length(min=4,max=100)]) 
	select_gender = SelectField(u"Select your gender", choices=[[0,"female"],[0,"male"]])
	submit_btn = SubmitField("Зарегистрироваться")

#формы на страничке редактирования профиля


#кастомный валидатор для проверки размера файла
def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb*1024*1024

    def file_length_check(form, field):
        if field.data:
            if len(field.data.read()) > max_bytes:
                raise ValidationError(f'File size is too large. Max allowed: {max_size_in_mb} MB')
            field.data.seek(0)
        else:
            pass
    return file_length_check

class LoadPictureForm(FlaskForm):
	profile_pic = FileField(validators=[FileAllowed(photos,"only images are allowed"),
													FileSizeLimit(max_size_in_mb=10)])
	submit_btn = SubmitField("Save")




class AboutMeForm(FlaskForm):
	about_me = TextAreaField("ScheduleAction", validators=[Length(min=0,max=200)])
	activities = TextAreaField("Info", validators=[Length(min=0,max=200)])
	submit_btn = SubmitField("Save")