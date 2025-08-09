from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, email=True, nullable=False)
  username = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
