import imp
from flask import Flask

#основной класс приложения, где создаем объект фласки


app = Flask(__name__)

<<<<<<< HEAD

@app.route("/main")
def main_page():
    with open("static\data\students.json","a") as file:
        
        
    return render_template("students.html")




if __name__ == "__main__":
    app.run(debug=True)
=======
>>>>>>> origin/main
