from flask import Flask,render_template



#hello world
app = Flask(__name__)


@app.route("/main")
def main_page():
    return render_template("students.html")




if __name__ == "__main__":
    app.run(debug=True)