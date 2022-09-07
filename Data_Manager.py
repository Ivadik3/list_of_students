
import json
import time
import random

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
        with open(Data_Manager.USERS,"r") as file:
            post = list(filter(lambda dict1: dict1["ID"] == str(id),json.load(file)))
            #print(post)
        if post:
            return post[0]
        return {}
            

