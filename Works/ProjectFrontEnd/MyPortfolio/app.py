from flask import Flask, render_template, request, redirect, url_for
from flask_SQLAlchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/recipe_images/')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    short_description = db.Column(db.String(120))
    image = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Recipe %r>' % self.title


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('MyPortfolio.html' )

@app.route('/support')
def support():
    return render_template('Support.html')

@app.route('/join')
def join():
    return render_template('JoinNow.html')

@app.route('/sign')
def sign():
    return render_template('Signin.html')

@app.route('/ageless')
def ageless():
    return render_template('ageless.html')


if __name__ == '__main__':
    app.run(debug=True)

# ----------------------------------------ADMIN------------------------------------------------
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

