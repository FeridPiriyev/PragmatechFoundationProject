from stories import db

# export FLASK_APP=models.py

class Product(db.Model):
    __tablename__="product"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    short_description =db.Column(db.String(120))
    image=db.Column(db.String(20),nullable=False)
    created_at=db.Column(db.String(80))
    

    def __repr__(self):
        return '<Product %r>' % self.title 


class Silde(db.Model):
    __tablename__="slide"
    id = db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(20),nullable=False)
  

    def __repr__(self):
        return '<slide %r>' % self.title 


