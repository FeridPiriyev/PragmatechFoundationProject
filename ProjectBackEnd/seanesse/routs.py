from flask import Flask,redirect,url_for,render_template,request
from . models import Card,Prodact
from seanesse import app,db,os
from werkzeug.utils import secure_filename

@app.route('/') 
def index():
    return render_template('myportfolio.html')



@app.route('/sign') 
def about():
    return render_template('Signin.html')

@app.route('/ageless') 
def ageless():
    return render_template('ageless.html')


@app.route('/login') 
def login():
    return render_template('Signin.html')


@app.route('/support') 
def support():
    return render_template('support.html')

@app.route('/building') 
def building():
    return render_template('blog1.html')

@app.route('/helping') 
def helping():
    return render_template('blog2.html')


@app.route('/uplifting') 
def uplifting():
    return render_template('blog3.html')


@app.route('/term') 
def term():
    return render_template('kullanim.html')

@app.route('/privacy') 
def privacy():
    return render_template('gizlilik.html')





# -------------------------------- ADMIN PANEL ----------------------------------------------------
@app.route('/admin/card', methods=['GET', 'POST']) # localhost:5000 #127.0.0.1:5000
def admincard():
    if request.method == 'POST':
        file = request.files.get('file')
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cart = Card(
            title=request.form.get('title'),
            datet=request.form.get('datet'),
            descrip = request.form.get('descrip'),
            image = request.form.get('image')
        )
        db.session.add(cart)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('admin/admin.html')


