from flask import Flask,render_template
app1 = Flask(__name__)

@app1.route("/")
def home():
    return render_template("home.html")

@app1.route("/about")
def about():
    return render_template("about.html")

@app1.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app1.run(debug = True)
