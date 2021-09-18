
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.string(55), nullable=False)
    last_name=db.Column(db.string(55), nullable=False)
    username=db.Column(db.string(100), unique=True)
    email=db.Column(db.string(100), unique=True)



if __name__=="__main__":
    app.run(debug=True)