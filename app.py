from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from create_db import write

app = Flask(__name__)
app.debug = False
app.config.update({
    "SECRET_KEY": 'H4HG75HF83H67BJ57HFUV5',
    "SQLALCHEMY_DATABASE_URI": 'sqlite:///universities.db',
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})
db = SQLAlchemy(app)


class University(db.Model):
    name = db.Column(db.Text, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    motto = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    telephone = db.Column(db.Text, nullable=False)
    website = db.Column(db.Text, nullable=True)
    faculty = db.relationship('Faculty')


class Faculty(db.Model):
    name = db.Column(db.Text, primary_key=True)
    univ = db.Column(db.Text, db.ForeignKey('university.name'), primary_key=True)
    degrees = db.relationship('Degrees')


class Degrees(db.Model):
    name = db.Column(db.Text, primary_key=True)
    duration = db.Column(db.Text, nullable=False)
    minimum = db.Column(db.Integer, nullable=True)
    entry = db.Column(db.Text, nullable=True)
    faculty = db.Column(db.Text, db.ForeignKey('faculty.name'))
    univ = db.Column(db.Text, primary_key=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/universities')
def univs():
    records = University.query.all()
    return render_template("universities.html", universities=records)


@app.route('/universities/<string:name>')
def univ(name):
    result = University.query.filter_by(image=name).first()
    var_name = result.name
    image = name
    faculties = [fac for fac in result.faculty]
    return render_template('univ.html', var_name=var_name, image=image, faculties=faculties)


@app.route('/guidance')
def guide():
    return render_template("guidance.html")


def create_database():
    if not path.exists("universities.db"):
        db.create_all(app=app)
        write()


create_database()

if __name__ == '__main__':
    app.run('0.0.0.0')
