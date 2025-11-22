from flask import Flask
app = Flask(__name__)

@app.route("/")
def first():
    return "Hello Namitha!"  

@app.route("/<name>/<int:age>")  
def third(name,age):
    return "Welcome {0} and your age is:{1}".format(name,age)       
@app.route("/new")
def second():
    return "2nd page"
if __name__ == "__main__":
    app.run(debug = True)