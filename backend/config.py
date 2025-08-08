import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.environ.get("DATABASE_URL")

class Config:
  SQLALCHEMY_DATABASE_URI = DATABASE_URI
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True
  SECRET_KEY = os.environ.get("SECRET_KEY")
