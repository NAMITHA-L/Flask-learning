from flask import Flask,render_template,request
app1 = Flask(__name__)

@app1.route("/",methods = ['GET'])
def home():
     print(request.args)
     my_name = request.args.get('name')
     print(my_name )
     my_age = request.args.get('age')
     print(my_age )
     return render_template("home.html")

@app1.route("/about")
def about():
    return render_template("about.html",List = marks)

@app1.route("/profile")
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app1.run(debug = True)
