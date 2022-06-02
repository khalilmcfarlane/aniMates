from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import settings

app = settings.init_flask_app()


@app.route("/")
def index():
    return "Hello World!"

if __name__ == '__main__':
   app.run()