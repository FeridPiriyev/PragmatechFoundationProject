from flask import render_template,request,redirect,url_for
from . models import Product,Silde
from werkzeug.utils import secure_filename
from stories import app,db,os


@app.route("/")
def index():
    produc=Product().query.all()
    slid=Silde().query.all()
    return render_template('myportfolio.html',produc=produc,slid=slid)



@app.route('/ageless') 
def ageless():
    return render_template('ageless.html')


@app.route('/nv') 
def nv():
    return render_template('nv.html')


@app.route('/luminesce') 
def luminesce():
    return render_template('luminesce.html')



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

# ------------------------------ ADMIN -----------------------------------
@app.route('/products' , methods=["GET" , "POST"])
def admin():
    
    if request.method=="POST":
        file=request.files["file"]
        print(file)
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product= Product(
            title=request.form.get("title"),
            short_description=request.form.get("short-desc"),
            image=filename,
            created_at=request.form.get("time")
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('admin/add-recipe.html')



@app.route('/slide' , methods=["GET" , "POST"])
def slides():
    
    if request.method=="POST":
        file=request.files["file"]
        print(file)
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product= Silde(
            image=filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('admin/addslide.html')



@app.route('/update/<int:id>', methods=['GET','POST'])
def edit(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
       file = request.files.get('file')
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       product.title = request.form.get('title')
       product.short_description = request.form.get('short-desc')
       product.image = filename
       product.created_at=request.form.get('time')
       db.session.add(product)
       db.session.commit()
       return redirect(url_for("adminpanel"))
    return render_template('admin/product-edit.html', product=product)


@app.route('/admin-delete') 
def adminpanel():
    products = Product.query.all()
    return render_template('admin/product-list.html',products=products)

@app.route('/admin/product-delete/<int:id>', methods=['GET','POST'])
def admin_product_delete(id):
    product = Product.query.get_or_404(id)
    print(product,'-----------------------------------')
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("adminpanel"))

