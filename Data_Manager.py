
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

    def get_student(self,id,name=None):
        #из за того что жсон грузится в виде [{json file}] мы должны делать
        #крокозяблу с filter-ом
        with open(Data_Manager.USERS,"r") as file:
            if not name:
                individual_user = list(filter(lambda dict1: dict1["ID"] == str(id),json.load(file)))
            else:
                individual_user = list(filter(lambda dict1: dict1["Name"] == str(name),json.load(file)))
            #print(post)
        if individual_user:
            return individual_user[0]
        return {}
            
    def set_student(self,user_object):
        with open(Data_Manager.USERS,"r") as file:
            posts = json.load(file)
            max_id = 0
            for el in posts:            ###оптимизировать этот цикл какой то крутой функцией
                if int(el["ID"])>max_id:      
                    max_id = int(el["ID"])
            max_id = str(int(max_id)+1)
            user_object.ID= f"{max_id}"
            posts.append(user_object.__dict__)
        with open(Data_Manager.USERS,"w",encoding ='utf8') as file:
            json.dump(posts,file,ensure_ascii = False) 
        return int(max_id)

    def user_exists(self,name):
        with open(Data_Manager.USERS,"r") as file:
            posts = json.load(file)
            name_exists = list(filter(lambda el:el["Name"]==name,posts))
            print(name_exists)
            if len(name_exists)>0:
                return True
            return False
