import json

#модуль для добавления доп полей в базу данных у юзеров

def refactor(field_name):
        with open("static/data/student_db.json","r") as file:
            posts = json.load(file)
            for p in posts:
                print(p)
                p[field_name]=""
        with open("static/data/student_db.json","w",encoding ='utf8') as file:
            json.dump(posts,file,ensure_ascii = False) 

