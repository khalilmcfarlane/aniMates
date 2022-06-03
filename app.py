from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import models
import settings
from random import randint
from jikanpy import Jikan

app = settings.init_flask_app()
db = SQLAlchemy(app)
jikan = Jikan()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = models.User(username, password)
        user.id = randint(100, 1000000000)
        session['username'] = username

        db.session.add(user)
        db.session.commit()
        return render_template("index.html")

    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "username" in session:
        redirect(url_for('profile'))
        # send to profile page
    # else login 
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        User = db.session.query(models.User).filter(models.User.username == username, models.User.password == password)
        if User is not None:
            session['username'] = username
            flash('login succesful', 'success')
            return render_template("login.html")
        else:
            error = 'wrong username/password'
            render_template("login.html", error)

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    flash("you've been logged out",'success')
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    return render_template("profile.html")
if __name__ == '__main__':
   

    db.create_all()
    app.run()
