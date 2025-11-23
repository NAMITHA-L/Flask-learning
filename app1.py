from flask import Flask,render_template
app1 = Flask(__name__)

@app1.route("/")
def home():
    marks = [23,12,34,45,56,67,78,89,90]
    return render_template("home.html",List = marks)

@app1.route("/about")
def about():
    return render_template("about.html")

@app1.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app1.run(debug = True)
