from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), unique=True, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    consistency = db.Column(db.String(50), nullable=False)
    core_gpa = db.Column(db.Float, nullable=False)
    local_hackathons = db.Column(db.Integer, nullable=False)
    national_hackathons = db.Column(db.Integer, nullable=False)
    paper_presentations = db.Column(db.Integer, nullable=False)
    peer_assistance = db.Column(db.Integer, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
