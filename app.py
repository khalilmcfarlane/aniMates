from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import models
import settings
from random import randint

app = settings.init_flask_app()
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        User = models.User(username, password)
        User.id = randint(100, 1000000000)
        session['username'] = username


        db.session.add(User)
        db.session.commit()
        return render_template("index.html")

    return render_template("signup.html")

@app.route('/login')
def login():
    if "username" in session:
        pass
    
    username = request.form['username']
    password = request.form['password']

    User = db.session.query(models.User).filter(models.User.username == username, models.User.password == password)
    if User is not None:
        session['username'] = username
        return render_template("login.html")
    return redirect("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()