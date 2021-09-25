from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/recipe_images/')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prodactdata.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fulname = db.Column(db.String(80), nullable=False)
    usersname = db.Column(db.String(80),unique=True, nullable=False)
    email = db.Column(db.String(80),unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Recipe %r>' % self.title

db.create_all()



@app.route('/') 
def index():
    return render_template('MyPortfolio.html')


@app.route('/recipes') 
def recipes():
    recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes)

@app.route('/sign') 
def about():
    return render_template('Signup.html')

@app.route('/stories') 
def stories():
    return render_template('stories.html')

@app.route('/login') 
def login():
    return render_template('Signin.html')


@app.route('/contact') 
def contact():
    return render_template('Support.html')



# -------------------------------- ADMIN PANEL ----------------------------------------------------
@app.route('/admin/recipes', methods=['GET', 'POST']) # localhost:5000 #127.0.0.1:5000
def admin():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        recipe = Recipe(
            title=request.form.get('title'),
            category=request.form.get('category'),
            short_description = request.form.get('short-info'),
            image = filename
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('recipes'))
    return render_template('admin/admin.html')








if __name__ == '__main__':
    app.run(debug=True)