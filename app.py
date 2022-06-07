from email import message
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from random import randint
from werkzeug.utils import secure_filename
from datetime import datetime
from pytz import timezone

import models
import settings

app = settings.init_flask_app()
db = SQLAlchemy(app)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    posts = db.session.query(models.Post).all()
    return render_template("index.html", posts=posts)


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
        redirect('/profiles/%s' % session['username'])
        # send to profile page
    # else login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        User = db.session.query(models.User).filter(
            models.User.username == username, models.User.password == password)
        if User is not None:
            session['username'] = username
            flash('login succesful', 'success')
            return redirect('/profiles/%s' % username)
        else:
            error = 'wrong username/password'
            render_template("login.html", error)

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    flash("you've been logged out", 'success')
    return redirect(url_for('login'))


@app.route('/profiles/<username>')
def profile(username):
    return render_template("profile.html")


@app.route('/anime')
def anime():
    anime_list = db.session.query(models.Anime).all()
    return render_template("allAnime.html", anime_list=anime_list)


@app.route('/anime/<id>')
def anime_detail(id):
    anime = db.session.query(models.Anime).filter(models.Anime.id == id)
    return render_template("animeDetail.hmtl", anime=anime)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        if 'username' in session:
            username = session['username']
            title = request.form['title']
            text = request.form['text']
            image = request.files['image']

            if not image:
                flash("Image Not Uploaded!", "message")
                return render_template("createPost.html")
            if allowed_file(image.filename):
                image.save(secure_filename(image.filename))
                img = image.filename
                id = randint(100, 1000000000)
                user = db.session.query(models.User).filter(
                    models.User.username == username)
                user_id = user.id
                post = models.Post(id, user_id, title, text, img)
                post.time_sent = datetime.now(timezone('US/Eastern'))
                db.session.add(post)
                db.session.commit()

                flash("Post Created!")
                return redirect('/')
            elif not allowed_file(image.filename):
                flash("Incorrect file format: Please upload jpg, png, or gif", "message")
        else:
            flash('Please login first!', 'error')
            return redirect('/login')

    return render_template("createPost.html")


if __name__ == '__main__':

    db.create_all()
    app.run()
