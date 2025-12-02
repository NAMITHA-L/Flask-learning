from flask import Flask,render_template,request
app1 = Flask(__name__)
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Namitha@1008",
    database = "mydb"
)
cursor = db.cursor()



@app1.route("/",methods = ['GET'])
def home():
    myargs = request.args
    success = ""
    try:
        if request.args.get('reg') == "Register":
            name = request.args.get('name')
            email = request.args.get('email')
            pwd = request.args.get('pwd')
            print(name, email,pwd)
            sql = "insert into users(name,email,pwd) values('{0}','{1}','{2}')".format(name,email,pwd)
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount >= 1:
                           success = "success"
            return render_template("register.html", success=success )
        elif request.args.get('login') == "Login":
            email = request.args.get('email')
            pwd = request.args.get('pwd')
            sql = "select * from users where email = '{0}' and pwd = '{1}';".format(email,pwd)
            cursor.execute(sql)
            db_data = cursor.fetchall()
            print("DATA FROM DB:", db_data)
            return render_template("profile.html", profile_data = db_data )

        else:
            return render_template("home.html",myargs = myargs)
    except Exception as e:
       return "Provide valid data"
       #raise`

@app1.route("/about")
def about():
    return render_template("about.html",List = marks)

@app1.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app1.run(debug = True)
