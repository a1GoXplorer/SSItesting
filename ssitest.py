from flask import Flask, url_for, render_template, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
from sqlalchemy import  create_engine

# engine = create_engine('postgresql+psycopg2://MasterControl@localhost:5000/SSItesting')




# login_manager = LoginManager()

app = Flask(__name__)

# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials.  Please Try Again.'
        else:
          return redirect(url_for('home.html'))
    return render_template("login.html", error=error)



@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")





if __name__ == '__main__':
     app.debug = True
     app.run()