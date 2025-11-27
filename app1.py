from flask import Flask,render_template,request
app1 = Flask(__name__)

@app1.route("/",methods = ['GET'])
def home():
    try:
     print(request.args)
     data = request.args
     print(data)
     print(type(data))
     my_name = request.args.get('name')
     print(my_name )
     my_age = request.args.get('age')
     print(my_age+"hi") 
     print(my_age+90)
     return render_template("home.html")
    except Exception as e:
       return "Provide valid data"
       #raise

@app1.route("/about")
def about():
    return render_template("about.html",List = marks)

@app1.route("/profile")
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app1.run(debug = True)
