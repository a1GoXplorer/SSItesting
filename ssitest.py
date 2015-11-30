from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home(name=None):
    return render_template("home.html",name=name)

@app.route('/login')
def login(name=None):
    return render_template("login.html",name=name)

if __name__ == '__main__':
     app.debug = True
     app.run()