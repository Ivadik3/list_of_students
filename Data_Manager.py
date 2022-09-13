
import json
import time
import random
import users_model

#этот класс импортируем в view.py, чтобы получать данные о студентах

class Data_Manager:
    USERS= "static/data/student_db.json"
    def __init__(self):
        try: 
            with open(self.USERS,"r",encoding="utf-8"):
                pass
        except FileNotFoundError:
            with open(self.USERS,"w",encoding="utf-8") as f:
                json.dump({},f)
        
    def get_all_posts(self):
        with open(Data_Manager.USERS,"r") as file:
            posts = json.load(file)
        return posts

    def get_student(self,id):
        #из за того что жсон грузится в виде [{json file}] мы должны делать
        #крокозяблу с filter-ом
        with open(Data_Manager.USERS,"r") as file:
            post = list(filter(lambda dict1: dict1["ID"] == str(id),json.load(file)))
            #print(post)
        if post:
            return post[0]
        return {}
            
    def set_student(self,user_object):
        with open(Data_Manager.USERS,"r") as file:
            posts = json.load(file)
            max_id = 0
            for el in posts:            ###оптимизировать этот цикл какой то крутой функцией
                if int(el["ID"])>max_id:      
                    max_id = int(el["ID"])
            posts.append(
            {
                "ID": f"{max_id}",
                "Name": f"{user_object.Name}",
                "Gender": f"{user_object.Gender}",
                "Class": user_object.NOT_DEFINED,
                "Seat": user_object.NOT_DEFINED,
                "Club": user_object.NOT_DEFINED,
                "Persona": user_object.NOT_DEFINED,
                "Crush": user_object.NOT_DEFINED,
                "BreastSize": user_object.NOT_DEFINED,
                "Strength": user_object.NOT_DEFINED,
                "Hairstyle": user_object.NOT_DEFINED,
                "Color": user_object.NOT_DEFINED,
                "Eyes": user_object.NOT_DEFINED,
                "EyeType": user_object.NOT_DEFINED,
                "Stockings": user_object.NOT_DEFINED,
                "Accessory": user_object.NOT_DEFINED,
                "ScheduleTime": user_object.NOT_DEFINED,
                "ScheduleDestination": user_object.NOT_DEFINED,
                "ScheduleAction": user_object.NOT_DEFINED,
                "Info": user_object.NOT_DEFINED
             }
            )
        with open(Data_Manager.USERS,"w",encoding ='utf8') as file:
            json.dump(posts,file,ensure_ascii = False) 

