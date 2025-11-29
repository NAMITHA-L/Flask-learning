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
            return render_template("form.html", success=success )
        else:
            return render_template("form.html",success=success)
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
